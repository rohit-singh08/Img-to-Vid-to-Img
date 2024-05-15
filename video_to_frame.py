import cv2


def extract_frames(video_path, output_folder):
    # Open the video file
    video_capture = cv2.VideoCapture(video_path)
    #video_capture.set(cv2.CAP_PROP_FPS, 30)  # Set frame rate to 24 fps. Default is 30

    # Check if the video file is opened successfully
    if not video_capture.isOpened():
        print("Error: Could not open video file.")
        return

    # Initialize frame count
    frame_count = 0

    # Loop through each frame in the video
    while True:
        # Read the next frame
        ret, frame = video_capture.read()
        # 'ret' is a boolean variable that indicates whether the frame was read successfully or not
        # Check if the frame is read successfully
        if not ret:
            break

        # Write the frame to a file
        frame_filename = f"{output_folder}/{frame_count}.jpg"
        cv2.imwrite(frame_filename, frame)

        # Increment frame count
        frame_count += 1

    # Release the video capture object
    video_capture.release()


# Example usage
video_path = "D:/Start Ups/Dabana/Code/Sample/image_remade.mp4"
output_folder = "D:/Start Ups/Dabana/Code/Sample/Frames"
extract_frames(video_path, output_folder)
