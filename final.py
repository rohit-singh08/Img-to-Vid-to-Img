import cv2
import os
import re

print("Hello User", '\n')
print("Do you want to:", '\n')

Choice = 'y'
while Choice == 'y' or Choice == 'Y':
    print("1: Compress Your Image Folder", '\n')
    print("2: Decompress Your Image Folder", '\n')
    try:
        f = int(input("Enter you Choice: "))
        if f == 1:
            path_of_folder = input("Enter Your Image Folder Path to Compress: ")
        elif f == 2:
            path_of_folder = input("Enter Your Image Folder Path to Decompress: ")
        else:
            print("Invalid Input. Redirecting Now.")
    except:
        print("Invalid Input. Redirecting Now.")

    if f == 1:
        frames_folder = path_of_folder
        output_folder = os.path.dirname(frames_folder)
        Image_folder_Storage = os.path.basename(frames_folder)
        Image_folder_Storage = Image_folder_Storage + '_Compressed'
        Image_folder_Storage = os.path.join(Image_folder_Storage, '')
        output_folder = os.path.join(output_folder, Image_folder_Storage)

        try:
            os.mkdir(output_folder)
            Image_folder_name = os.path.join(output_folder, 'Image Names')
            os.mkdir(Image_folder_name)
        except:
            print("Folder already exist with the same name.")

        fps = 30


        def sorted_nicely(lst):
            """Sort the given list in the way that humans expect."""
            convert = lambda text: int(text) if text.isdigit() else text
            alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
            return sorted(lst, key=alphanum_key)
        def create_videos(frames_folder, output_folder, fps):
            # Get the list of frame filenames
            frame_filenames = sorted(os.listdir(frames_folder))
            frame_filenames = sorted_nicely(frame_filenames)

            # Initialize dictionary to store video writers for each dimension
            video_writers = {}

            # Write each frame to the appropriate video file based on its dimensions
            for frame_filename in frame_filenames:
                frame_path = os.path.join(frames_folder, frame_filename)
                frame = cv2.imread(frame_path)
                height, width, _ = frame.shape

                # Create a video writer for frames with this dimension if not already created
                if (height, width) not in video_writers:
                    # Initialize video writer for this dimension
                    output_video_path = os.path.join(output_folder, f"video_{height}x{width}.mp4")
                    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
                    video_writers[(height, width)] = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))
                output_file_name_txt = os.path.join(output_folder, f"Image Names/video_{height}x{width}.txt")
                with open(output_file_name_txt, "a") as f:
                    f.write(frame_filename + "\n")
                # Write frame to the appropriate video writer
                video_writers[(height, width)].write(frame)

            # Release video writers
            for video_writer in video_writers.values():
                video_writer.release()
        print("Image Compression Under Progress...")
        create_videos(frames_folder, output_folder, fps)
        
    if f == 2:

        input_folder = path_of_folder
        output_folder = os.path.dirname(input_folder)
        Image_folder_Storage = os.path.basename(input_folder)
        Image_folder_Storage = Image_folder_Storage + '_Deompressed'
        output_folder = os.path.join(output_folder, Image_folder_Storage)

        try:
            os.mkdir(output_folder)
        except:
            print("Folder already exist with the same name.")

        def split_videos(input_folder, output_folder, quality):
            # Get the list of video filenames
            # video_filenames = sorted(os.listdir(input_folder))
            video_filenames = sorted([f for f in os.listdir(input_folder) if
                                      os.path.isfile(os.path.join(input_folder, f))])  # read only files not folders

            # Iterate through each video file
            for video_filename in video_filenames:
                video_path = os.path.join(input_folder, video_filename)
                txt_file = input_folder + "/Image Names"
                txt_file = os.path.join(txt_file, video_filename)
                txt_file = txt_file.replace(".mp4", ".txt")
                with open(txt_file) as inp:
                    data = list(inp)
                # Initialize video capture object
                video_capture = cv2.VideoCapture(video_path)
                # video_capture.set(cv2.CAP_PROP_FPS, 30)

                # Get video dimensions
                width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
                height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

                # Create output folder for this video based on its dimensions
                video_output_folder = os.path.join(output_folder)
                os.makedirs(video_output_folder, exist_ok=True)

                # Read and save each frame
                frame_count = 0
                while True:
                    ret, frame = video_capture.read()
                    if not ret:
                        break
                    count = data[frame_count].strip()
                    frame_filename = os.path.join(video_output_folder, f"{count}")
                    cv2.imwrite(frame_filename, frame, [int(cv2.IMWRITE_JPEG_QUALITY), quality])
                    frame_count += 1

                # Release video capture object
                video_capture.release()
        quality = int(input("What should be your photo quality?(0-100): "))
        print("Image Decompression Under Progress...")
        split_videos(input_folder, output_folder, quality)


    Choice = input("Do you wish to continue?(y/n): ")
    print('\n')
    if not (Choice == 'y' or Choice == 'Y'):
        print('Exiting now')