
import cv2
import numpy as np
import pytesseract
import streamlit as st
from pathlib import Path
from PIL import Image, UnidentifiedImageError

# Configure the Streamlit page
st.set_page_config(
    page_title="AI Image-to-Text Recognition",
    page_icon="📝",
    layout="wide"
)

# Locate Tesseract OCR on Windows
possible_paths = [
    r"C:\Program Files\Tesseract-OCR\tesseract.exe",
    r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe",
]

for path in possible_paths:
    if Path(path).exists():
        pytesseract.pytesseract.tesseract_cmd = path
        break

# Application heading
st.title("AI Image-to-Text Recognition 📝")
st.write(
    "Upload an image containing printed text and "
    "extract its contents using Optical Character Recognition."
)

st.info("Built with Python, OpenCV, pytesseract and Tesseract OCR.")

# Sidebar
with st.sidebar:
    st.header("About")
    st.write("DecodeLabs — Week 4 AI Project")
    st.write("Technology: Computer Vision and OCR")
    st.write("Language: English")

# Image uploader
uploaded_file = st.file_uploader(
    "Upload an image containing text",
    type=["png", "jpg", "jpeg", "bmp", "tif", "tiff"]
)

if uploaded_file is not None:
    try:
        image = Image.open(uploaded_file).convert("RGB")
        image_array = np.array(image)
        image_bgr = cv2.cvtColor(image_array, cv2.COLOR_RGB2BGR)

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Uploaded Image")
            st.image(image, use_container_width=True)

        with col2:
            st.subheader("Image Details")
            st.write(f"Width: {image.width} pixels")
            st.write(f"Height: {image.height} pixels")
            st.write(f"Filename: {uploaded_file.name}")

        st.divider()

        preprocessing = st.selectbox(
            "Choose image preprocessing",
            [
                "Grayscale",
                "Black and white thresholding",
                "Original image"
            ]
        )

        if st.button("Extract Text", type="primary"):
            try:
                if preprocessing == "Grayscale":
                    processed = cv2.cvtColor(
                        image_bgr, cv2.COLOR_BGR2GRAY
                    )

                elif preprocessing == "Black and white thresholding":
                    gray = cv2.cvtColor(
                        image_bgr, cv2.COLOR_BGR2GRAY
                    )
                    processed = cv2.threshold(
                        gray,
                        0,
                        255,
                        cv2.THRESH_BINARY + cv2.THRESH_OTSU
                    )[1]

                else:
                    processed = image_bgr

                with st.spinner("Recognizing text..."):
                    extracted_text = pytesseract.image_to_string(
                        processed,
                        lang="eng"
                    ).strip()

                st.subheader("Extracted Text")

                if extracted_text:
                    st.success("Text recognition completed!")
                    st.text_area(
                        "Recognized content",
                        extracted_text,
                        height=250
                    )

                    st.download_button(
                        "Download Extracted Text",
                        data=extracted_text,
                        file_name="recognized_text.txt",
                        mime="text/plain"
                    )
                else:
                    st.warning(
                        "No readable text found. Try a clearer image "
                        "or another preprocessing option."
                    )

            except pytesseract.TesseractNotFoundError:
                st.error(
                    "Tesseract OCR is not installed or could not be "
                    "found. Please check its Windows installation path."
                )

            except Exception as error:
                st.error(f"OCR failed: {error}")

    except (UnidentifiedImageError, OSError, ValueError):
        st.error("Unable to open this image. Please try another file.")

else:
    st.write("Upload an image to begin text recognition.")

st.divider()
st.caption("DecodeLabs | Week 4 | Basic OCR Application")