import pytesseract
from PIL import Image
import cv2

# ADD THIS HERE
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\tesseract\tesseract.exe"

def extract_text(processed_image):

    custom_config = r'--oem 3 --psm 6'

    text = pytesseract.image_to_string(
        processed_image,
        config=custom_config,
        lang='eng'
    )

    return text