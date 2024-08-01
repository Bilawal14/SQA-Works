from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
try:
    path = r"https://honda.com.pk/"

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    search_bar = driver.find_element(By.ID)
    driver.get(path)
    driver.maximize_window()
except:
    print("Error in Opening Chrome")
finally:
    time.sleep(20)
    print(driver.title)
    print(driver.current_url)
    driver.quit()