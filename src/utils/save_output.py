import json
import os
from datetime import datetime


def save_result(result: dict, image_path: str, output_dir: str = "outputs"):
    os.makedirs(output_dir, exist_ok=True)

    image_name = os.path.splitext(os.path.basename(image_path))[0]
    filename = f"{image_name}.json"
    output_path = os.path.join(output_dir, filename)

    payload = {
        "image": image_path,
        "timestamp": datetime.utcnow().isoformat(),
        "result": result,
    }

    with open(output_path, "w") as f:
        json.dump(payload, f, indent=2)

    return output_path
