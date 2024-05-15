from rembg import remove
from PIL import Image
import os


def rem_bag(input_path, output_path):
    # Processing the image
    input = Image.open(input_path)
    # Removing the background from the given Image
    output = remove(input)
    # Saving the image in the given path
    output.save(output_path)


lst = os.listdir("D:/Start Ups/Dabana/Code/Sample/Sample Frames")
number_files = len(lst)

for i in range(0, number_files):
    input_path = "D:/Start Ups/Dabana/Code/Sample/Sample Frames/" + str(i) + ".jpg"
    output_path = "D:/Start Ups/Dabana/Code/Sample/Sample Frames/" + str(i) + "_removed.png"
    rem_bag(input_path, output_path)

