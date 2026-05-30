# AI-Powered OCR Pipeline for Historical Document Digitization

## Overview

This project is an end-to-end OCR (Optical Character Recognition) system designed for digitizing degraded historical documents, archival records, and scanned manuscripts. The pipeline uses computer vision techniques and Tesseract OCR to improve text extraction accuracy from noisy, skewed, and low-quality document images.

## Features

* Historical document digitization
* Image preprocessing and enhancement
* Noise reduction and denoising
* Adaptive thresholding (binarization)
* Deskewing and alignment correction
* Morphological image processing
* OCR text extraction using Tesseract
* Automated text cleaning and correction
* Batch image processing support

## Tech Stack

* Python
* OpenCV
* Tesseract OCR
* NumPy
* Pillow
* TextBlob

## Project Workflow

Input Image
→ Grayscale Conversion
→ Noise Reduction
→ Contrast Enhancement
→ Binarization
→ Deskewing
→ Morphological Processing
→ OCR Extraction
→ Text Cleaning
→ Export Final Text

## Installation

```bash
git clone <repository-url>
cd historical-ocr

pip install -r requirements.txt
```

Install Tesseract OCR and configure the executable path if required.

## Run Project

```bash
python main.py
```

## Output

* Processed document images
* Extracted text files
* OCR-ready digitized archives

## Future Enhancements

* Transformer-based OCR models
* Handwritten text recognition
* Layout analysis
* PDF generation
* Cloud deployment
* Searchable digital archives

## Author

Developed as a Computer Vision and OCR Digitization Project.
