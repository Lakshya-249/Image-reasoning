from pytesseract import image_to_string
from PIL import Image


def extract_text(image_path: str):
    img = Image.open(image_path)

    text = image_to_string(img)

    return [t for t in text.split("\n") if t.strip()]
