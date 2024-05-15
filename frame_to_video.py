import cv2
import os
import re
def sorted_nicely(lst):
    """Sort the given list in the way that humans expect."""
    convert = lambda text: int(text) if text.isdigit() else text
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
    return sorted(lst, key=alphanum_key)

def create_video(frames_folder, output_video_path, fps):
    # Get the list of frame filenames
    frame_filenames = sorted(os.listdir(frames_folder))
    frame_filenames = sorted_nicely(frame_filenames)

    # Get the frame size from the first frame
    first_frame = cv2.imread(os.path.join(frames_folder, frame_filenames[0]))
    height, width, _ = first_frame.shape

    # Initialize video writer
    # fourcc = cv2.VideoWriter_fourcc(*'XVID')
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video_writer = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

    # Write each frame to the video
    for frame_filename in frame_filenames:
        frame_path = os.path.join(frames_folder, frame_filename)
        frame = cv2.imread(frame_path)
        # Check if the dimensions of the current frame are different from those of the video writer
        if frame.shape[:2] != (height, width):
            # If dimensions are different, resize the frame to match the dimensions of the video writer
            frame = cv2.resize(frame, (width, height))
        video_writer.write(frame)

    # Release video writer
    video_writer.release()


# Example usage
frames_folder = "D:/Start Ups/Dabana/Code/Sample/Sample Frames"
output_video_path = "D:/Start Ups/Dabana/Code/Sample/image_remade.mp4"
fps = 30  # Adjust as needed

create_video(frames_folder, output_video_path, fps)
