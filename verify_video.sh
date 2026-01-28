#!/bin/bash
# Extract key frames from a manim video for AI verification
# Usage: ./verify_video.sh <video_path> [num_frames]

VIDEO_PATH="$1"
NUM_FRAMES="${2:-5}"  # Default 5 frames
OUTPUT_DIR="media/verification_frames"

mkdir -p "$OUTPUT_DIR"

# Get video duration
DURATION=$(ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "$VIDEO_PATH")

# Extract evenly spaced frames
for i in $(seq 0 $((NUM_FRAMES - 1))); do
    TIMESTAMP=$(echo "scale=2; $DURATION * $i / ($NUM_FRAMES - 1)" | bc)
    OUTPUT_FILE="$OUTPUT_DIR/frame_$(printf '%02d' $i)_at_${TIMESTAMP}s.png"
    ffmpeg -y -ss "$TIMESTAMP" -i "$VIDEO_PATH" -vframes 1 -q:v 2 "$OUTPUT_FILE" 2>/dev/null
    echo "Extracted: $OUTPUT_FILE"
done

echo "Done! Frames saved to $OUTPUT_DIR"
ls -la "$OUTPUT_DIR"
