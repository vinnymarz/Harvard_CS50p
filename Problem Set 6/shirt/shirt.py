import sys
import os
from PIL import Image, ImageOps

def main():
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    in_path, out_path = sys.argv[1], sys.argv[2]
    valid_extensions = [".jpg", ".jpeg", ".png"]

    if os.path.splitext(in_path)[1] not in valid_extensions:
        sys.exit("Invalid input")

    if os.path.splitext(out_path)[1] not in valid_extensions:
        sys.exit("Invalid output")

    if os.path.splitext(in_path)[1] != os.path.splitext(out_path)[1]:
        sys.exit("Input and output have different file extensions")


    try:
        first_image = Image.open(in_path)
        shirt = Image.open("shirt.png")
        size = shirt.size
        second_image = ImageOps.fit(first_image, size)
        second_image.paste(shirt, shirt)
        second_image.save(out_path)
        print(f"Image saved as {out_path}")
    except FileNotFoundError:
        sys.exit("Input does not exist")


if __name__ == "__main__":
    main()
