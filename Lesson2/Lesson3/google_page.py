from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def google_search_for_text(driver,search_text):
    wait = WebDriverWait(driver, 10)
    google_search_text_area = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id=\"APjFqb\"]")))
    google_search_text_area.send_keys(search_text)
    google_search_text_area.send_keys(Keys.RETURN)
    driver.implicitly_wait(5)
    googled_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id=\"rso\"]/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a")))
    googled_link.click()
    return driver

    
