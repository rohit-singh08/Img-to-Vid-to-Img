from PIL import Image
import os


def compress_image(input_image_path, output_image_path, quality=85):
    # Open an image file
    with Image.open(input_image_path) as img:
        # Resize the image while maintaining the aspect ratio
        img.thumbnail((1600, 1600))

        # Save it with JPEG compression and without EXIF data
        # We do this by creating a new Image object to discard EXIF data
        img_no_exif = Image.new(img.mode, img.size)
        img_no_exif.putdata(list(img.getdata()))
        img_no_exif.save(output_image_path, 'JPEG', quality=quality, optimize=True)


# Example usage
input_image_path = 'path/to/original/image.jpg'
output_image_path = 'path/to/compressed/image.jpg'
compress_image(input_image_path, output_image_path)

# Check the sizes
original_size = os.path.getsize(input_image_path)
compressed_size = os.path.getsize(output_image_path)
print(f"Original size: {original_size / 1024:.2f} KB")
print(f"Compressed size: {compressed_size / 1024:.2f} KB")
