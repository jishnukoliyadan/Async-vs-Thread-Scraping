import os
from ast import literal_eval
from PIL import Image, ImageDraw, ImageFont
from config.scraper_config import TOTAL_REQUESTS_COUNT

# Directory to save images
os.makedirs("./static", exist_ok=True)


def create_number_image(number: float, image_num: int) -> None:
    filename = f"./static/timer_{image_num}.png"
    width, height = 150, 50

    image = Image.new("RGB", (width, height), color=(255, 255, 255))

    draw = ImageDraw.Draw(image)

    try:
        font = ImageFont.truetype("arial.ttf", 40)
    except IOError:
        print('errore')
        font = ImageFont.load_default()

    text = str(number)

    bbox = draw.textbbox((0, 0), text, font=font)

    text_width = bbox[2] - bbox[0]

    position = ((width - text_width) / 2, 4)

    draw.text(position, text, fill="black", font=font)

    # Save the image with the specified filename
    image.save(filename)


# Function to extract time from a line in the 'results.txt' file
def get_time(line: str) -> float:
    time = line.split(" : ")[-1].strip()
    return literal_eval(time)


# Open the 'results.txt' file and process lines that contain 'Average time'
with open("benchmark_result.txt", "r") as file:
    lines = [get_time(line) for line in file.readlines() if "Average time" in line]

# For each extracted time value, create a corresponding image
for idx, line in enumerate(lines):
    create_number_image(round(line, 4), idx)

create_number_image(round(TOTAL_REQUESTS_COUNT, 4), idx + 1)

print("Image files updated\n")
