from vision.objects import detect_objects
from vision.ocr import extract_text
from vision.quality import image_quality
from llm.reasoner import reason_about_image
from pathlib import Path
from utils.save_output import save_result


def extract_features(image_path: str):
    return {
        "objects": detect_objects(image_path),
        "text": extract_text(image_path),
        "quality": image_quality(image_path),
    }


def analyze_image(image_path: str):
    features = extract_features(image_path)
    decision = reason_about_image(features)

    return {"features": features, "decision": decision}


def main():
    BASEDIR = Path(__file__).parent
    result = analyze_image(f"{BASEDIR}/utils/temp/test2.webp")
    output_path = save_result(
        result, f"{BASEDIR}/utils/temp/test2.webp", f"{BASEDIR}/utils/output"
    )

    print(f"\nSaved output to: {output_path}\n")
    print(result)


if __name__ == "__main__":
    main()
