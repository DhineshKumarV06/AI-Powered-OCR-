import os
import cv2

from preprocess import preprocess_document
from ocr_engine import extract_text
from postprocess import clean_text, correct_spelling


INPUT_FOLDER = "input"
OUTPUT_IMAGE_FOLDER = "output/processed_images"
OUTPUT_TEXT_FOLDER = "output/extracted_text"


os.makedirs(OUTPUT_IMAGE_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_TEXT_FOLDER, exist_ok=True)


SUPPORTED_FORMATS = ('.png', '.jpg', '.jpeg', '.tif', '.tiff')


for filename in os.listdir(INPUT_FOLDER):

    if filename.lower().endswith(SUPPORTED_FORMATS):

        image_path = os.path.join(INPUT_FOLDER, filename)

        print(f"Processing: {filename}")

        # ---------------------------------------------
        # Preprocessing
        # ---------------------------------------------
        processed_image = preprocess_document(image_path)

        # Save processed image
        processed_image_path = os.path.join(
            OUTPUT_IMAGE_FOLDER,
            f"processed_{filename}"
        )

        cv2.imwrite(processed_image_path, processed_image)

        # ---------------------------------------------
        # OCR Extraction
        # ---------------------------------------------
        extracted_text = extract_text(processed_image)

        # ---------------------------------------------
        # Post Processing
        # ---------------------------------------------
        cleaned_text = clean_text(extracted_text)

        corrected_text = correct_spelling(cleaned_text)

        # ---------------------------------------------
        # Save text
        # ---------------------------------------------
        text_filename = os.path.splitext(filename)[0] + '.txt'

  
        output_text_path = os.path.join(
            OUTPUT_TEXT_FOLDER,
            text_filename
        )

        with open(output_text_path, 'w', encoding='utf-8') as f:
            f.write(corrected_text)

        print(f"Saved text to: {output_text_path}")

print("OCR Pipeline Completed Successfully")