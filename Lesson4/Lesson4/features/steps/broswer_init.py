from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from behave import given, when, then

@given('Open A Chrome Browser')
def get_chrome_instance(context):
    chrome_driver_path = 'C:\\Users\\Hi\\Desktop\\Lesson4\\Lesson4\\driver\\chromedriver.exe'  
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized") 
    service = Service(chrome_driver_path)
    context.driver = webdriver.Chrome(service=service, options=chrome_options)


