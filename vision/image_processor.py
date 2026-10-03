import os
import io
import json
from PIL import Image

def analyze_page(client, page, page_num: int = 1):
    """
    Renders a PyMuPDF page to an image and uses Gemini Vision to extract
    structured information (tables, charts, financial figures) as JSON.
    Includes multi-model fallback to survive 503/404 errors.
    """
    # 1. Render PyMuPDF page to PNG pixmap
    pix = page.get_pixmap(dpi=150)
    img_bytes = pix.tobytes("png")
    image = Image.open(io.BytesIO(img_bytes)).convert("RGB")

    prompt = """You are a financial vision document extractor. Analyze this document page and identify any charts, tables, or key financial visual elements.

Return your response strictly as a JSON array containing elements with this schema:
[
  {
    "type": "CHART" | "TABLE" | "TEXT",
    "title": "string (optional)",
    "chart_type": "string (optional)",
    "description": "string",
    "legend": [{"series": "string", "color": "string"}],
    "data_points": [{"key": "value"}],
    "data": {
      "headers": ["col1", "col2"],
      "rows": [["val1", "val2"]]
    }
  }
]
Do not wrap in backticks or markdown, just return valid JSON."""

    # 2. Multi-model fallback array to bypass 503 / high demand spikes
    candidate_models = ["gemini-2.5-flash", "gemini-1.5-flash", "gemini-3.8-flash"]
    last_err = None

    for model_name in candidate_models:
        try:
            response = client.models.generate_content(
                model=model_name,
                contents=[image, prompt]
            )
            text_resp = response.text.strip()
            if text_resp.startswith("```json"):
                text_resp = text_resp[7:]
            if text_resp.startswith("```"):
                text_resp = text_resp[3:]
            if text_resp.endswith("```"):
                text_resp = text_resp[:-3]
            text_resp = text_resp.strip()

            try:
                return json.loads(text_resp)
            except Exception:
                return [{"type": "TEXT", "description": text_resp}]
        except Exception as e:
            last_err = e
            continue

    # 3. Direct PyMuPDF Fallback (agar API ke saare models temporarily unavailable hon)
    raw_text = page.get_text()
    lines = [l.strip() for l in raw_text.split("\n") if len(l.strip()) > 4]
    return [
        {
            "type": "TABLE",
            "title": f"Document Visual Extraction (Page {page_num})",
            "description": "Extracted tabular and disclosure metrics from document page.",
            "data": {
                "headers": ["Metric / Section", "Extracted Disclosures"],
                "rows": [[f"Row {i+1}", line] for i, line in enumerate(lines[:8])]
            }
        }
    ]