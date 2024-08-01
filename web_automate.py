from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

data =["Bilawal","Imtiaz","Memon","Artificial intelligence","Morning","Male"]
print(len(data))
try: 
    driver =  webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    
    path = r"file:///C:/Users/DELL%207500/Desktop/SQA/Course.html"
    driver.get(path)
    driver.maximize_window()

    name = driver.find_element(By.ID,"name")
    name.send_keys(data[0])
    f_name = driver.find_element(By.ID,"f_name")
    f_name.send_keys(data[1])
    cast = driver.find_element(By.ID,"cast")
    cast.send_keys(data[2])
    #shift = driver.find_element(By.ID,data[4])
    #shift.click()
    Course = driver.find_element(By.ID,"Course")
    #Course.send_keys("we")
    if data[3] == "Artificial Intelleigence":
        Ai = driver.find_element(By.id,"Ai")
        Ai.click()
    elif data[3] == "Web Development":
        we = driver.find_element(By.ID,"we")
        we.click()
    elif data[3] == "SQA":
        sqa = driver.find_element(By.ID,"sqa")
        sqa.click()
    elif data[3] == "Game Development":
        game = driver.find_element(By.ID,"game")
        game.click()

    if data[4] == "Morning":
        morning = driver.find_element(By.ID,"morning")
        morning.click()
    elif data[4] == "Evening":
        evening = driver.find_element(By.ID,"evening")
        evening.click()

    if data[5] == "Male":
        male = driver.find_element(By.ID,"male")
        male.click()
    elif data[5] == "Female":
        female = driver.find_element(By.ID,"female")
        female.click()
    elif data[5] == "Other":
        other = driver.find_element(By.ID,"other")
        other.click()
    Submit = driver.find_element(By.ID,"Submit")
    Submit.click()


except Exception as e:
    print("Error in Opening Chrome",e)
finally:
    time.sleep(10)
    print(driver.title)
    print(driver.current_url)
    driver.quit()