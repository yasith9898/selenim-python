from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


def get_chrome_instance():
    chrome_driver_path = 'C:\Code\e-learning\Batch2\Lesson3\driver\chromedriver.exe'  
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized") 
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

