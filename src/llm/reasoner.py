import json
import os
import re
from dotenv import load_dotenv
from groq import Groq

load_dotenv()


openai_api_key = os.environ.get("GROQ_API_KEY")
client = Groq(api_key=openai_api_key)


def reason_about_image(features: dict):
    prompt = f"""
You are an ML quality evaluator for e-commerce images.

Analyze the following extracted image features:
{json.dumps(features, indent=2)}

Return STRICT JSON with:
- image_quality_score (0-1)
- issues_detected
- final_verdict
- reasoning_summary
- confidence
"""
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        response_format={"type": "json_object"},
    )

    output_text = response.choices[0].message.content
    if output_text.startswith("```"):
        output_text = re.sub(
            r"^```json\s*|```$", "", output_text, flags=re.MULTILINE
        ).strip()

    try:
        return json.loads(output_text)
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")
        return {"raw_output": output_text, "error": "failed_to_parse"}
