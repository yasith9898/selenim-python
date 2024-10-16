from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

def downlaod_python_latest_realse(driver):
    driver.implicitly_wait(10)
    wait = WebDriverWait(driver, 10)
    actions = ActionChains(driver)
    download_menu_link = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/header/div/nav/ul/li[2]/a")))
    actions.move_to_element(download_menu_link).perform()
    driver.implicitly_wait(10)
    download_menu_link_all_releases = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/header/div/nav/ul/li[2]/ul/li[1]/a")))
    actions.move_to_element(download_menu_link_all_releases).click().perform()
    print("~~~~~")
    for x in range(1, 30):
        try:
            print("~~~~~")
            xpath_string = "/html/body/div/div[3]/div/section/div[2]/ol/li["+str(x)+"]/span[1]/a"
            version_link = wait.until(EC.visibility_of_element_located((By.XPATH, xpath_string)))
            if version_link.text == "Python 3.10.13":
                print("version found")
                download_link_xpath = "/html/body/div/div[3]/div/section/div[2]/ol/li["+str(x)+"]/span[3]/a"
                download_link = wait.until(EC.visibility_of_element_located((By.XPATH, download_link_xpath)))
                download_link.click() 
                break            
        except Exception as e:
            print("Index not found")
    driver.implicitly_wait(10)
    download_link_win64 = wait.until(EC.visibility_of_element_located((By.XPATH,"/html/body/div/div[3]/div/section/article/table/tbody/tr[1]/td[1]/a")))
    download_link_win64.click()
    time.sleep(20)
    driver.close()
    
    
    



