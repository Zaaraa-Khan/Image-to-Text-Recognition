
# AI Image-to-Text Recognition System

**DecodeLabs Week 4 — Artificial Intelligence Project**

## Overview
A basic Optical Character Recognition (OCR) application that extracts
printed text from uploaded images.

## Features
- Upload and preview images
- Extract printed English text
- Preprocess images using OpenCV
- Compare grayscale, thresholding, and original image methods
- Display recognized text
- Download results as a text file
- Handle empty results and common OCR errors

## Technologies
- Python
- Streamlit
- OpenCV
- pytesseract
- Tesseract OCR
- Pillow
- NumPy

## Setup
Install Python and the Tesseract OCR engine first.

Create a virtual environment:

```powershell
py -3.12 -m venv .venv
```

Install the dependencies:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Run the app:

```powershell
.\.venv\Scripts\python.exe -m streamlit run app.py
```

## Usage
1. Start the application.
2. Upload a supported image.
3. Choose a preprocessing method.
4. Click Extract Text.
5. Review or download the recognized text.

## Limitations
Results may contain errors when images are blurry, handwritten,
rotated, poorly lit, or have complex layouts. The default OCR
language is English.

## Learning Outcomes
- Basic computer vision
- Image preprocessing with OpenCV
- OCR integration in Python
- Interactive application development with Streamlit
- Error handling and text export