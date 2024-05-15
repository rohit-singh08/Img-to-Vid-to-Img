import os

lst = os.listdir("D:/Start Ups/Dabana/Code/Sample/Sample Frames")
number_files = int((len(lst))/2)

for i in range(0, number_files):
    os.remove("D:/Start Ups/Dabana/Code/Sample/Sample Frames/" + str(i) + ".jpg")

print("Original Files Deleted")