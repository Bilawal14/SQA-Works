from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

data =["Bilawal","Imtiaz","Memon","41306-0167840-1","Hyderabad","Python","Male","Morning"]
print(len(data))
try: 
    driver =  webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    
    path = r"file:///C:/Users/DELL%207500/Downloads/Q2.html"
    driver.get(path)
    driver.maximize_window()

    name = driver.find_element(By.ID,"name")
    name.send_keys(data[0])

    f_name = driver.find_element(By.ID,"f_name")
    f_name.send_keys(data[1])

    caste = driver.find_element(By.ID,"caste")
    caste.send_keys(data[2])

    cnic = driver.find_element(By.ID,"cnic")
    cnic.send_keys(data[3])

    city = driver.find_element(By.ID,"course")
    if data[4] == "Karachi":
        khi = driver.find_element(By.ID,"khi")
        khi.click()
    elif data[4] == "Hyderabad":
        hyd = driver.find_element(By.ID,"hyd")
        hyd.click()
    elif data[4] == "Jacobabad":
        jcb = driver.find_element(By.ID,"jcb")
        jcb.click()

    if data[5] == "Python":
        python = driver.find_element(By.ID,"python")
        python.click()
    elif data[4] == "Jaavascript":
        Javascript = driver.find_element(By.ID,"Javascript")
        Javascript.click()

    if data[6] == "Male":
        male = driver.find_element(By.ID,"male")
        male.click()
    elif data[6] == "Female":
        female = driver.find_element(By.ID,"female")
        female.click()
    elif data[6] == "Other":
        other = driver.find_element(By.ID,"other")
        other.click()

    if data[7] == "Morning":
        morning = driver.find_element(By.ID,"morning")
        morning.click()
    elif data[7] == "Afternoon":
        noon = driver.find_element(By.ID,"noon")
        noon.click()
    elif data[7] == "Evening":
        evening = driver.find_element(By.ID,"evening")
        evening.click()


    Submit = driver.find_element(By.ID,"submit")
    Submit.click()

    Clear = driver.find_element(By.ID,"clear")
    Clear.click()

except Exception as e:
    print("Error in Opening Chrome",e)
finally:
    time.sleep(10)
    print(driver.title)
    print(driver.current_url)
    driver.quit()