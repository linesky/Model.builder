
from PIL import Image, ImageDraw
import sys
#pip install pillow
def draw_cube(image, draw, x, y, size):
    # Define the coordinates for the cube faces
    faces = [
        (x + size, y),            # Top face
        (x, y + size),            # Left face
        (x + size, y + size),     # Front face
        (x + 2 * size, y + size), # Right face
        (x + size, y + 2 * size), # Bottom face
        (x + size, y + 3 * size)  # Back face
    ]

    for fx, fy in faces:
        draw.rectangle([fx, fy, fx + size, fy + size], outline="black", width=2)
    
    # Draw tabs
    tab_size = 15
    tabs = [
        (x + size , y - tab_size, x + size+size , y), # Top face tab
        (x + size - tab_size, y , x + size , y + size),# Top left face tab
        (x + size * 2 , y , x + size * 2 + tab_size, y + size),# Top rigth face tab
        (x - tab_size, y + size, x, y + size + size), # Left face tab
        (x + 3 * size, y + size, x + 3 * size + tab_size, y + size + size), # Right face tab
        (x + size - tab_size  , y + 2 * size, x + size , y + 3 * size ), # Bottom face tab
        (x + size - tab_size  , y + 3 * size, x + size , y + 4 * size ), # Bottom face tab
        (x + size * 2 , y + 2 * size, x + size*2 + tab_size, y + 3 * size ), # Back face tab
        (x + size * 2 , y + 3 * size, x + size*2 + tab_size, y + 4 * size ) # Back face tab
    ]

    for tx1, ty1, tx2, ty2 in tabs:
        draw.rectangle([tx1, ty1, tx2, ty2], outline="black", width=2)

def main():
    # Ask user for dimensions in pixels
    try:
        height = int(input("Enter the height of the cube in pixels: "))
        width = int(input("Enter the width of the cube in pixels: "))
        depth = int(input("Enter the depth of the cube in pixels: "))
    except ValueError:
        print("Please enter valid integer dimensions.")
        sys.exit(1)

    if height <= 0 or width <= 0 or depth <= 0:
        print("Dimensions must be positive integers.")
        sys.exit(1)

    # Create a blank image
    img_width = width * 6 + 30
    img_height = height * 8 + 30
    image = Image.new("RGB", (img_width, img_height), "white")
    draw = ImageDraw.Draw(image)

    # Draw the cube with tabs
    draw_cube(image, draw, width, height, width)

    # Save the image
    image.save("out.png")
    print("Cube layout saved to out.png")

print("\x1bc\x1b[47;30m")
if __name__ == "__main__":
    main()
