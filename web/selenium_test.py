import time

from selenium import webdriver
#webdriver is what actually links to the browser

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

path = "C:/Users/bruno/OneDrive - The University of Auckland/Documents/code/python/web"
driver_path = "C:/Users/bruno/OneDrive - The University of Auckland/Documents/code/python/web/chromedriver.exe"

#first step is to specify what driver we want to use with selenium
driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))

#driver.get("https://www.google.com")
driver.get("http://localhost:8000/html_test.html")


#driver.close() #closes current tab
#driver.quit() #closes entire browser

output = driver.find_element(By.ID, "test_output")
output = output.get_attribute("innerHTML")
print(output)
    