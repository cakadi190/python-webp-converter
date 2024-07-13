import os
import argparse
from PIL import Image

def crop_images_to_169(directory, output_directory, crop_position):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for filename in os.listdir(directory):
        if filename.endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.heic', '.JPEG', '.JPG', '.HEIC')):
            img_path = os.path.join(directory, filename)
            img = Image.open(img_path)
            width, height = img.size
            aspect_ratio = width / height

            # Check if the image ratio is not 19:6
            if aspect_ratio!= 19/6:
                new_width = width
                new_height = int(new_width * 9 / 16)

                if crop_position == 'top':
                    y_offset = 0
                elif crop_position == 'center':
                    y_offset = (height - new_height) // 2
                elif crop_position == 'bottom':
                    y_offset = height - new_height
                else:
                    raise ValueError("Invalid crop position. Must be 'top', 'center', or 'bottom'.")

                cropped_img = img.crop((0, y_offset, width, y_offset + new_height))
                cropped_img.save(os.path.join(output_directory, filename))
            else:
                print(f"Image {filename} already has a 19:6 aspect ratio, skipping...")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Crop images to 19:6 aspect ratio')
    parser.add_argument('input_directory', help='Input directory containing images')
    parser.add_argument('output_directory', help='Output directory for cropped images')
    parser.add_argument('-P', '--position', choices=['top', 'center', 'bottom'], default='center', help='Crop position (top, center, or bottom)')
    args = parser.parse_args()

    crop_images_to_169(args.input_directory, args.output_directory, args.position)