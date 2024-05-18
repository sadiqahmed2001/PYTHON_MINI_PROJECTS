from PIL import Image

# ASCII characters to represent different shades of gray
ASCII_CHARS = '@%#*+=-:. '

def scale_image(image, new_width=100):
    """Scale the image while preserving the aspect ratio."""
    (original_width, original_height) = image.size
    aspect_ratio = original_height / float(original_width)
    new_height = int(aspect_ratio * new_width)
    return image.resize((new_width, new_height))

def convert_to_grayscale(image):
    """Convert the image to grayscale."""
    return image.convert('L')

def map_pixels_to_ascii(image, range_width=25):
    """Map each pixel to an ASCII character based on its intensity."""
    pixels = image.getdata()
    ascii_str = ''
    for pixel_value in pixels:
        ascii_str += ASCII_CHARS[pixel_value // range_width]
    return ascii_str

def generate_ascii_art(image_path, new_width=100):
    """Generate ASCII art from an image."""
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(e)
        return

    image = scale_image(image, new_width)
    image = convert_to_grayscale(image)

    ascii_str = map_pixels_to_ascii(image)

    # Format the ASCII string into lines
    pixel_count = len(ascii_str)
    ascii_art = ''
    for i in range(0, pixel_count, new_width):
        ascii_art += ascii_str[i:i + new_width] + '\n'

    return ascii_art

def main():
    image_path = 'path/to/your/image.jpg'  # Path to your image file
    ascii_art = generate_ascii_art(image_path)
    print(ascii_art)

if __name__ == "__main__":
    main()
