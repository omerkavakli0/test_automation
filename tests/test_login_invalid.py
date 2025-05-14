from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
import time

def test_invalid_login():
    # WebDriver servisini GeckoDriverManager ile başlat
    service = Service(executable_path=GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    driver.get("https://the-internet.herokuapp.com/login")

    wait = WebDriverWait(driver, 10)

    username_input = wait.until(EC.presence_of_element_located((By.ID, "username")))
    password_input = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.CSS_SELECTOR, "button.radius")

    username_input.send_keys("wronguser")
    password_input.send_keys("wrongpass")
    time.sleep(2)

    login_button.click()

    error = wait.until(EC.presence_of_element_located((By.ID, "flash")))
    print("Hata mesajı:", error.text)

    time.sleep(2)
    driver.quit()

if __name__ == "__main__":
    test_invalid_login()
