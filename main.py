from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

# Pinterest credentials
PINTEREST_EMAIL = "YOUR_PINTEREST_EMAIL@gmail.com"
PINTEREST_PASSWORD = "YOUR_PASSWORD_PINTERES"

# Redbubble product links
PRODUCT_LINKS = [
    "https://www.redbubble.com/i/t-shirt/Rise-Sip-Shine-Colorful-Coffee-Chalkboard-Art-by-LifeUpDown/161102768.1YYVU",
    "https://www.redbubble.com/i/iphone-skin/Stay-Wild-Moon-Child-Retro-Text-Design-by-LifeUpDown/161096311.62NBT",
]

# Pinterest board name
BOARD_NAME = "Unique Designs & Gifts on Redbubble"

def setup_driver():
    """Set up the WebDriver using webdriver_manager."""
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    wait = WebDriverWait(driver, 20)
    return driver, wait

def human_wait(min_seconds=2, max_seconds=5):
    """Wait for a random amount of time to simulate human interaction."""
    time.sleep(random.uniform(min_seconds, max_seconds))

def login_to_pinterest(driver, wait):
    """Log in to Pinterest using email and password."""
    driver.get("https://www.pinterest.com/login/")
    human_wait(4, 7)
    email_field = wait.until(EC.presence_of_element_located((By.NAME, 'id')))
    email_field.send_keys(PINTEREST_EMAIL)
    human_wait(3, 6)
    password_field = driver.find_element(By.NAME, 'password')
    password_field.send_keys(PINTEREST_PASSWORD)
    human_wait(2, 5)
    password_field.send_keys(Keys.RETURN)

def extract_product_info(url):
    """Extract product title and description from the URL."""
    product_name = url.split('/')[-2].replace('-', ' ').title()
    product_title = product_name
    product_description = f"Check out this amazing product: {product_name}. Available now on Redbubble!"
    return product_title, product_description

def create_pin_from_url(driver, wait, product_link):
    """Create a new pin from a URL."""
    driver.get("https://www.pinterest.com/pin-builder/?tab=save_from_url")
    human_wait(4, 8)

    # Input the product link
    url_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="scrape-view-website-link"]')))
    url_field.send_keys(product_link)
    human_wait(3, 6)

    # Click the "Add" button to proceed
    add_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div/div[1]/div/div[3]/div/div/button')
    add_button.click()
    human_wait(5, 9)  # Wait for the page to process the URL and show pin options

    # Wait for the grid of images to load and randomly select one
    image_containers = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[@data-test-id="image-from-search-container"]')))
    random_image = random.choice(image_containers)
    random_image.click()
    human_wait(3, 6)

    # Extract product information
    product_title, product_description = extract_product_info(product_link)
    
    # Wait for the "Add 1 Pin" button to become clickable and click it
    add_pin_button = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div/div[2]/div/div[2]/div[2]/button')))
    add_pin_button.click()
    human_wait(6, 10)  # Longer wait after saving the pin

    # Input title and description
    title_field = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[1]/div[1]/div/div/div[1]/textarea')))
    title_field.send_keys(product_title)
    human_wait(2, 5)

    # description_field = driver.find_element(By.XPATH, '//*[@data-test-id="pin-description"]')
    # description_field.send_keys(product_description)
    # human_wait(2, 5)

    # Click the "Save" button
    save_button = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div/div/button[2]')))
    save_button.click()
    human_wait(6, 10)  # Longer wait after saving the pin

def main():
    driver, wait = setup_driver()
    try:
        login_to_pinterest(driver, wait)
        human_wait(6, 10)  # Wait for the login process to complete
        for link in PRODUCT_LINKS:
            create_pin_from_url(driver, wait, link)
            human_wait(6, 10)  # Wait between creating pins to avoid being flagged as spam
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
