# Image-Aware Reasoning Assistant

A mini multimodal intelligence system that analyzes images using classical computer vision and ML models, then applies LLM-based reasoning to produce structured, explainable decisions.

This project was built as part of a Machine Learning Engineer evaluation task.  
The focus is on **thinking, trade-offs, and system design**, not UI or deployment polish.

---

## 🚀 What This System Does

Given an image as input, the system:

1. **Extracts visual signals (pre-LLM intelligence)**

   - Object detection (YOLOv8)
   - Image quality analysis (blur, brightness)
   - OCR text extraction (Tesseract)

2. **Aggregates features into a structured representation**

3. **Applies an LLM reasoning layer**

   - Uses extracted signals (not raw images)
   - Produces a structured, explainable decision

4. **Persists results as JSON files** for offline analysis and auditing

---

## 🧠 Example Use Case

> _“Is this image suitable for use as a professional e-commerce product image?”_

Example output:

```json
{
  "features": {
    "objects": ["vase", "bowl", "potted plant", "clock"],
    "text": [],
    "quality": {
      "blur_score": 1185.84,
      "brightness": 134.65,
      "issues": []
    }
  },
  "decision": {
    "image_quality_score": 0.87,
    "issues_detected": false,
    "final_verdict": "Acceptable",
    "reasoning_summary": "The image quality is generally good with a high resolution (implied) and no detectable issues. However, there's a slight blur effect which affects the overall quality score.",
    "confidence": 0.9
  }
}
```

---

## 🛠️ Installation & Setup

The project is designed to be easy to run locally with minimal setup.  
It uses **uv** for dependency management and a small number of system-level tools.

---

### 1️⃣ Prerequisites

Ensure the following are installed on your system:

- **Python 3.10+**
- **Linux or macOS** (tested on Ubuntu)
- Internet access (for model downloads and LLM API calls)

---

### 2️⃣ Install `uv` (Python Package Manager)

`uv` is used to manage the virtual environment and dependencies.

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh

```

Restart your terminal, then verify:

```
uv --version
```

### 3️⃣ Clone the Repository

```bash
git clone https://github.com/Lakshya-249/Image-reasoning.git
cd image_reasoning_assistant
```

### 4️⃣ Install Python Dependencies

Install all required Python packages:

```bash
uv sync
```

If dependencies need to be added manually, they include:

```bash
python3 install -r requirements.txt
```

### 5️⃣ Install System Dependencies

#### Tesseract OCR

Tesseract is required for OCR-based text extraction.

```bash
sudo apt update
sudo apt install -y tesseract-ocr
```

Verify installation:

```
tesseract --version
```

### 6️⃣ Environment Variables

Create a .env file in the project root:

```
GROQ_API_KEY=gsk_xxxxxxxxxxxxxxxxxxxxxxxxx
```

- The system uses Groq for LLM-based reasoning (LLaMA 3.1).
- Environment variables are loaded locally using python-dotenv.
- In production, secrets should be injected via environment configuration or a secret manager.

### 7️⃣ Run the System

To analyze an image:

```
uv run src/main.py
```

On successful execution:

- The image will be analyzed
- Extracted features and reasoning output will be printed to the console
- A structured JSON output will be saved to src/utils/output/

### 📦 Output Artifacts

Each run produces a JSON file:

```
src/utils/output/<image_name>.json
```

Each output contains:

- Source image path
- Timestamp
- Extracted visual features
- Final decision and confidence score

This makes results reproducible and suitable for offline inspection or evaluation.
