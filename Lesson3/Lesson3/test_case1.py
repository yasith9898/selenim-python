from broswer_init import get_chrome_instance
from google_page import google_search_for_text
from python_home import downlaod_python_latest_realse



def test_scenario1():
    search_text = "python.org"
    driver = get_chrome_instance()
    driver.get("https://www.google.lk/")
    driver = google_search_for_text(driver,search_text)
    driver = downlaod_python_latest_realse(driver)


test_scenario1()

