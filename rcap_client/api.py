import io
import base64
import requests
from PIL import Image

SERVER_URL = "http://localhost:8000"


def get_models():
    res = requests.get(f"{SERVER_URL}/models")
    res.raise_for_status()
    return res.json()["models"]


def detect_cells(image_array, grid, target_text):
    image = Image.fromarray(image_array)
    buffer = io.BytesIO()
    image.save(buffer, format="PNG")

    image_b64 = base64.b64encode(buffer.getvalue()).decode()

    res = requests.post(
        f"{SERVER_URL}/detect",
        json={
            "image": image_b64,
            "grid": grid,           # "3x3" or "4x4"
            "target": target_text,
        },
        timeout=60,
    )
    res.raise_for_status()
    return res.json()["cells"]
