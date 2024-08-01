from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
try: 
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    
    path = r"https://www.zameen.com/tools/area-unit-converter/"
    driver.get(path)
    driver.maximize_window()

    input_field = driver.find_element(By.XPATH,"/html/body/div[1]/main/div[2]/div[1]/div[2]")
    input_field.send_keys("100")
    from_unit_dropdown = driver.find_element(By.ID,"from_unit")
    from_unit_dropdown.send_keys("Square")
    to_unit_dropdown = driver.find_element(By.ID,"to_unit")
    to_unit_dropdown.send_keys("Square Feet")

    time.sleep(2)
    convert_button = driver.find_element(By.ID,"convert_button")
    convert_button.click()

    converted_value = driver.find_element(By.ID,"convert_output").text
    print("Converted value:", converted_value)



    
except Exception as e:
    print("Error in Opening Chrome",e)
finally:
    time.sleep(20)
    print(driver.title)
    print(driver.current_url)
    driver.quit()