from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
try: 
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    
    path = r"https://www.google.com/"
    driver.get(path)
    driver.maximize_window()

    search_box = driver.find_element(By.ID,"APjFqb")

    search_box.send_keys("python")

    time.sleep(2)

    search_box.send_keys(Keys.ENTER)
except Exception as e:
    print("Error in Opening Chrome",e)
finally:
    time.sleep(20)
    print(driver.title)
    print(driver.current_url)
    driver.quit()