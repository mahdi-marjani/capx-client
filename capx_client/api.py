import io
import base64
import requests
from PIL import Image

SERVER_URL = "http://localhost:8000/detect"

AVAILABLE_MODELS = [
    "bicycle",
    "bus",
    "tractor",
    "boat",
    "car",
    "hydrant",
    "motorcycle",
    "traffic",
    "crosswalk",
    "stair",
    "taxi",
]

def is_model_available(target_text):
    for model in AVAILABLE_MODELS:
        if model in target_text:
            return True
    return False

def detect(image_array, grid, target_text):
    """
    Detect cells in the image based on the grid and target text.
    
    :param image_array: Numpy array of the image.
    :param grid: Grid size, either "3x3" or "4x4".
    :param target_text: Text to detect or target in the image.
    :return: List of detected cells from the server response.
    """
    image = Image.fromarray(image_array)
    
    buffered = io.BytesIO()
    image.save(buffered, format="PNG")
    
    image_b64 = base64.b64encode(buffered.getvalue()).decode()
    
    res = requests.post(
        SERVER_URL,
        json={
            "image": image_b64,
            "grid": grid,
            "target": target_text
        },
        timeout=30
    )
    res.raise_for_status()
    return res.json()["cells"]