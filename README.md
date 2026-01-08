# capx-client

capx client for solving reCAPTCHA using Selenium and capx server. 

## Installation

Install via pip:

```
pip install capx-client
```

## Usage

Here's an example of how to use it:

```python
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from capx_client.solver import RecaptchaSolver

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.get("https://www.google.com/recaptcha/api2/demo")

solver = RecaptchaSolver(driver)
solver.solve()  # Done!

print("reCAPTCHA solved!")
input("Press Enter to quit...")
driver.quit()
```

## Details

- Uses Selenium for browser interaction.
- Relies on a local API (localhost:8000) for image detection.
