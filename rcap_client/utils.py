import io
import requests
import numpy as np
from PIL import Image


def get_image_array(url):
    """Download an image from URL and return it as a numpy array."""
    response = requests.get(url)
    if response.status_code == 200:
        image = Image.open(io.BytesIO(response.content))
        return np.array(image)
    else:
        raise ValueError(f"Failed to download image from {url}")


def paste_image_on_main(main_img, new_img, position):
    """Paste a new image onto the main one at a position.

    Positions map to a 3x3 grid like this:
    +---+---+---+
    | 1 | 2 | 3 |
    +---+---+---+
    | 4 | 5 | 6 |
    +---+---+---+
    | 7 | 8 | 9 |
    +---+---+---+
    """
    main = np.copy(main_img)

    section_map = {
        1: (0, 0),
        2: (0, 1),
        3: (0, 2),
        4: (1, 0),
        5: (1, 1),
        6: (1, 2),
        7: (2, 0),
        8: (2, 1),
        9: (2, 2),
    }
    
    row, col = section_map[position]
    height, width = main.shape[0] // 3, main.shape[1] // 3
    
    start_row = row * height
    start_col = col * width
    
    main[start_row : start_row + height, start_col : start_col + width] = new_img
    
    return main
