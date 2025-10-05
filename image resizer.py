import os
from PIL import Image

def resize_images(input_folder, output_folder, width, height, output_format="JPEG"):
    # Create output folder if not exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Loop through all files in input folder
    for filename in os.listdir(input_folder):
        if filename.lower().endswith((".png", ".jpg", ".jpeg", ".bmp", ".gif")):
            img_path = os.path.join(input_folder, filename)
            try:
                img = Image.open(img_path)
                
                # Resize image
                img_resized = img.resize((width, height))
                
                # Convert extension
                base_name, _ = os.path.splitext(filename)
                new_filename = f"{base_name}.{output_format.lower()}"
                output_path = os.path.join(output_folder, new_filename)

                # Save image
                img_resized.save(output_path, output_format)
                print(f"✅ Saved {output_path}")

            except Exception as e:
                print(f"❌ Error processing {filename}: {e}")

if __name__ == "__main__":
    input_dir = "input_images"     # folder with original images
    output_dir = "resized_images"  # folder for resized images
    new_width, new_height = 300, 300  # resize dimensions
    format_convert = "JPEG"        # e.g., "JPEG", "PNG", "BMP"

    resize_images(input_dir, output_dir, new_width, new_height, format_convert)