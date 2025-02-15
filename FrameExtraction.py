import cv2
import os

# Video path
video_path = r"videos_path"

# Output directory for extracted frames
output_dir = r"storing_path"
os.makedirs(output_dir, exist_ok=True)  # Create the directory if it doesn't exist

# Open the video file
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Could not open video file.")
    exit()

# Get video properties
fps = int(cap.get(cv2.CAP_PROP_FPS))  # Frames per second
frame_interval = max(1, fps // 30)  # Interval to extract 30 frames per second

frame_count = 0
saved_frame_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Save frame if it matches the frame_interval condition
    if frame_count % frame_interval == 0:
        frame_filename = os.path.join(output_dir, f"frame_{saved_frame_count:04d}.jpg")
        cv2.imwrite(frame_filename, frame)
        saved_frame_count += 1

    frame_count += 1

# Release resources
cap.release()
print(f"Extracted {saved_frame_count} frames and saved to {output_dir}")