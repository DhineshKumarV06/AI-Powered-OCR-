import cv2
import numpy as np


def load_image(image_path):
    image = cv2.imread(image_path)

    if image is None:
        raise ValueError(f"Unable to load image: {image_path}")

    return image


# -------------------------------------------------
# Convert to grayscale
# -------------------------------------------------

def to_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# -------------------------------------------------
# Noise reduction
# -------------------------------------------------

def remove_noise(image):
    return cv2.fastNlMeansDenoising(image, None, 30, 7, 21)


# -------------------------------------------------
# Adaptive thresholding / binarization
# -------------------------------------------------

def binarize(image):
    return cv2.adaptiveThreshold(
        image,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        11,
        2
    )


# -------------------------------------------------
# Deskewing
# -------------------------------------------------

def deskew(image):
    coords = np.column_stack(np.where(image > 0))

    angle = cv2.minAreaRect(coords)[-1]

    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle

    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)

    M = cv2.getRotationMatrix2D(center, angle, 1.0)

    rotated = cv2.warpAffine(
        image,
        M,
        (w, h),
        flags=cv2.INTER_CUBIC,
        borderMode=cv2.BORDER_REPLICATE
    )

    return rotated


# -------------------------------------------------
# Morphological enhancement
# -------------------------------------------------

def morphological_processing(image):
    kernel = np.ones((1, 1), np.uint8)

    image = cv2.dilate(image, kernel, iterations=1)
    image = cv2.erode(image, kernel, iterations=1)

    return image


# -------------------------------------------------
# Full preprocessing pipeline
# -------------------------------------------------

def preprocess_document(image_path):
    image = load_image(image_path)

    gray = to_grayscale(image)

    denoised = remove_noise(gray)

    binary = binarize(denoised)

    deskewed = deskew(binary)

    processed = morphological_processing(deskewed)

    return processed