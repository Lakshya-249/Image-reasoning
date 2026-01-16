import cv2
import numpy as np


def image_quality(image_path: str):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    blur_score = cv2.Laplacian(gray, cv2.CV_64F).var()
    brightness = np.mean(img)

    issues = []
    if blur_score < 100:
        issues.append("blurry")
    if brightness < 60:
        issues.append("low_lighting")

    return {
        "blur_score": round(float(blur_score), 2),
        "brightness": round(float(brightness), 2),
        "issues": issues,
    }
