from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
try: 
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    
    path = r"https://www.facebook.com/"
    driver.get(path)
    driver.maximize_window()

    email_input = driver.find_element(By.ID,"email")
    email_input.send_keys("bilawal_memon@live.com")
    password_input = driver.find_element(By.ID,"pass")
    password_input.send_keys("test@12")
    
    time.sleep(2)
    login_button = driver.find_element(By.NAME,"login")
    login_button.click()

    
except Exception as e:
    print("Error in Opening Chrome",e)
finally:
    time.sleep(20)
    print(driver.title)
    print(driver.current_url)
    driver.quit()