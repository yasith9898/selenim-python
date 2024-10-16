from features.steps.broswer_init import get_chrome_instance
from features.steps.google_page import google_search_for_text
from features.steps.python_home import downlaod_python_latest_release



def test_scenario1():
    search_text = "python.org"
    get_chrome_instance()
    driver.get("https://www.google.lk/")
    driver = google_search_for_text(driver,search_text)
    driver = downlaod_python_latest_release(driver)


test_scenario1()

