from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then

@when('I go to Google Page')
def go_to_google_page(context):
    context.driver.get("https://www.google.lk/")
    assert True


@when('I Click on "{search_text}" site')
def google_search_for_text(context,search_text):
    wait = WebDriverWait(context.driver, 10)
    google_search_text_area = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id=\"APjFqb\"]")))
    google_search_text_area.send_keys(search_text)
    google_search_text_area.send_keys(Keys.RETURN)
    context.driver.implicitly_wait(5)
    googled_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id=\"rso\"]/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a")))
    googled_link.click()
    assert True
  

    
