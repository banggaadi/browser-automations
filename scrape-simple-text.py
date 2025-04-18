from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Run in headless mode (no GUI)
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')  # Overcome limited resource problems
    options.add_argument('disable-infobars')
    options.add_argument('start-maximized')  # Start maximized
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_argument('disable-blink-features=AutomationControlled')

    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(options=options, service=service)
    driver.get('https://automated.pythonanywhere.com/')  # Replace with your target URL
    return driver

def main():
    driver = get_driver()
    try:
        # Wait for the page to load and find the element containing the text
        time.sleep(3)  # Optional: wait for a few seconds to ensure the page is fully loaded
        element = driver.find_element(by='xpath',value='/html/body/div[1]/div/h1[2]')  # Replace with your target element's XPath
        print(element.text)  # Print the text content of the element
    finally:
        driver.quit()  # Close the browser

print(main())