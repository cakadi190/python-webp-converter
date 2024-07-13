from PIL import Image
import os
import shutil
from tqdm import tqdm

def compress_image(image_path, quality):
    image = Image.open(image_path)
    image.save(image_path, optimize=True, quality=quality)

def convert_to_webp(image_path, output_path):
    image = Image.open(image_path)
    rgb_image = image.convert('RGB')
    rgb_image.save(output_path, 'webp')

def truncate_output_folder(output_dir):
    for filename in os.listdir(output_dir):
        file_path = os.path.join(output_dir, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f"Error deleting file: {e}")

def convert_all_images(input_dir, output_dir, quality):
    truncate_output_folder(output_dir)  # truncate the output folder
    files = [f for f in os.listdir(input_dir) if f.endswith(('.png', '.jpg', '.JPG', '.JPEG', '.HEIC', '.heic', '.jpeg', '.gif'))]
    print(f"Converting progress\n")
    for _ in tqdm(range(len(files)), desc="Converting images", unit="files"):
        pass
    for filename in files:
        image_path = os.path.join(input_dir, filename)
        original_size = os.path.getsize(image_path)
        compress_image(image_path, quality)
        output_path = os.path.join(output_dir, filename.split('.')[0] + '.webp')
        convert_to_webp(image_path, output_path)
        converted_size = os.path.getsize(output_path)
        print(f"Successfully converted \"{filename}\" (from {original_size/1024:.2f} KB to {converted_size/1024:.2f} KB, saved {(original_size - converted_size) / original_size * 100:.2f}%)")
    print(f"Converted {len(files)} files successfully!")

# Example usage:
input_dir = './images'
output_dir = './output'
quality = 80  # adjust the quality value to your liking (1-100)

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

convert_all_images(input_dir, output_dir, quality)