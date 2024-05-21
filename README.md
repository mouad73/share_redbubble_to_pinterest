# Pinterest Product Promotion Automation

This repository contains a Python script that automates the process of promoting Redbubble products on Pinterest. Using Selenium WebDriver, the script logs into Pinterest, creates pins for given product links, and fills in the pin details such as title and description based on the product URL.

## Features

- **Automated Login:** Logs into Pinterest using provided credentials.
- **Pin Creation:** Creates new pins from specified product URLs.
- **Title and Description Generation:** Extracts and generates pin titles and descriptions based on the product URL.
- **Human-like Interaction:** Includes random delays to simulate human actions and avoid detection.

## Requirements

- Python 3.6+
- Selenium
- WebDriver Manager

## Setup

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/yourusername/pinterest-product-promotion-automation.git
    cd pinterest-product-promotion-automation
    ```

2. **Install Dependencies:**
    ```bash
    pip install selenium webdriver_manager
    ```

3. **Update Credentials:**
   - Open the script file and update the `PINTEREST_EMAIL` and `PINTEREST_PASSWORD` variables with your Pinterest login details.
   - Add your Redbubble product links to the `PRODUCT_LINKS` list.

## Usage

1. **Run the Script:**
    ```bash
    python pinterest_automation.py
    ```

2. The script will:
   - Log into Pinterest.
   - Navigate to the pin builder page.
   - Input each product link.
   - Randomly select an image.
   - Set the pin title and description.
   - Save the pin to the specified board.

## Example

Here's an example of how the product links and board name are configured:

```python
# Pinterest credentials
PINTEREST_EMAIL = "your_email@example.com"
PINTEREST_PASSWORD = "your_password"

# Redbubble product links
PRODUCT_LINKS = [
    "https://www.redbubble.com/i/t-shirt/Rise-Sip-Shine-Colorful-Coffee-Chalkboard-Art-by-LifeUpDown/161102768.1YYVU",
    "https://www.redbubble.com/i/iphone-skin/Stay-Wild-Moon-Child-Retro-Text-Design-by-LifeUpDown/161096311.62NBT",
    # Add more product links
]

# Pinterest board name
BOARD_NAME = "Unique Designs & Gifts on Redbubble"
