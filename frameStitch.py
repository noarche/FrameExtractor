import os
import random
from math import ceil, sqrt
from PIL import Image, ImageOps
from tqdm import tqdm
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def get_images_from_directory(directory):
    """
    Collect all image file paths from a single directory (non-recursive).
    """
    supported_formats = ('.jpg', '.jpeg', '.png', '.webp')
    image_paths = []

    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path) and file.lower().endswith(supported_formats):
            image_paths.append(file_path)
    return image_paths

def select_random_images(image_paths, count=9):
    """
    Select a fixed number of random images from the list.
    """
    return random.sample(image_paths, min(len(image_paths), count))

def resize_to_fit(image, max_size):
    """
    Resize the image to fit within max_size while maintaining aspect ratio.
    """
    return ImageOps.contain(image, max_size, Image.Resampling.LANCZOS)

def calculate_grid_dimensions(image_count):
    """
    Dynamically calculate the grid layout (rows and columns) based on image count.
    """
    columns = ceil(sqrt(image_count))
    rows = ceil(image_count / columns)
    return rows, columns

def combine_images(images, canvas_color=(30, 30, 30)):
    """
    Combine images into a single image with a professional grid layout.
    """
    rows, cols = calculate_grid_dimensions(len(images))
    print(f"{Fore.CYAN}Creating a grid with {rows} rows and {cols} columns...{Style.RESET_ALL}")

    # Resize all images to the smallest width and height of the group
    min_width = min(img.width for img in images)
    min_height = min(img.height for img in images)
    target_size = (min_width, min_height)

    resized_images = [resize_to_fit(img, target_size) for img in tqdm(images, desc=f"{Fore.YELLOW}Resizing images{Style.RESET_ALL}")]

    # Create canvas
    grid_width = cols * target_size[0]
    grid_height = rows * target_size[1]
    canvas = Image.new("RGBA", (grid_width, grid_height), canvas_color)

    # Place images on the canvas
    for idx, img in enumerate(resized_images):
        x = (idx % cols) * target_size[0]
        y = (idx // cols) * target_size[1]
        canvas.paste(img, (x, y), mask=img)

    return canvas

def resize_final_image(image, max_edge=1024):
    """
    Resize the final image so the longest edge is 1024 pixels.
    """
    return resize_to_fit(image, (max_edge, max_edge))

def save_image(image, output_path):
    """
    Save the image as a WebP file with compression.
    """
    image.save(output_path, "WEBP", quality=80)
    print(f"{Fore.GREEN}Image saved to: {output_path}{Style.RESET_ALL}")

def process_directory(input_dir):
    """
    Process a single directory to create a summary image of images only in that directory.
    """
    print(f"{Fore.MAGENTA}Scanning directory: {input_dir} for images...{Style.RESET_ALL}")
    image_paths = get_images_from_directory(input_dir)

    if not image_paths:
        print(f"{Fore.RED}No images found in {input_dir}.{Style.RESET_ALL}")
        return

    print(f"{Fore.CYAN}Found {len(image_paths)} images. Selecting 9 random images...{Style.RESET_ALL}")
    selected_images_paths = select_random_images(image_paths, count=9)

    # Load images
    images = [Image.open(img).convert("RGBA") for img in selected_images_paths]

    # Combine images into a professional layout
    combined_image = combine_images(images)

    # Resize final image
    final_image = resize_final_image(combined_image)

    # Prepare output path
    dir_name = os.path.basename(os.path.abspath(input_dir))
    output_file = os.path.join(input_dir, f"{dir_name}.Thumbnail.preview.webp")

    # Save output
    save_image(final_image, output_file)

def process_subdirectories(root_dir):
    """
    Process each subdirectory of the given root directory.
    """
    print(f"{Fore.BLUE}Scanning for subdirectories in: {root_dir}\n{Style.RESET_ALL}")
    for item in os.listdir(root_dir):
        subdirectory = os.path.join(root_dir, item)
        if os.path.isdir(subdirectory):
            print(f"{Fore.YELLOW}Processing directory: {subdirectory}{Style.RESET_ALL}")
            process_directory(subdirectory)

def main():
    print(f"{Fore.MAGENTA}### Professional Image Combiner ###{Style.RESET_ALL}")
    # Prompt for input directory
    input_dir = input(f"{Fore.CYAN}Enter the root directory to scan for subdirectories: {Style.RESET_ALL}").strip().strip('"').strip("'")
    if not input_dir:
        input_dir = os.getcwd()

    # Validate and process directories
    if os.path.isdir(input_dir):
        process_subdirectories(input_dir)
        print(f"{Fore.GREEN}Processing complete for all subdirectories!{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}Error: {input_dir} is not a valid directory.{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
