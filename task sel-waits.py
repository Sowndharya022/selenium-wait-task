# Using Python Selenium, Explicit Wait, Expected Conditions and Chrome Webdriver kindly do the following task mentioned below :-
# 1) Go to https://www.imdb.com/search/name/
# 2) Fill the data given in the Input Boxes, Select Boxes and Drop Down menu on the webpage and do a search.
# 3) Do not use the sleep() method for the task.



from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.maximize_window()

try:
    # Navigate to the IMDB search page
    driver.get("https://www.imdb.com/search/name/")

    # Initialize WebDriverWait
    wait = WebDriverWait(driver, 30)

    # Locate and interact with the "Name" input field
    try:
        name_input = wait.until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='nameTextAccordion']//input"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", name_input)
        print("Name input field located and scrolled into view.")
    except TimeoutException:
        print("Timeout: Unable to locate the name input field.")



    # Locate and click on the "Expand All" button if necessary
    try:
        expand_all_button = wait.until(
            EC.element_to_be_clickable((By.XPATH,
                                        '//*[@id="__next"]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[1]/div/button'))
        )
        driver.execute_script("arguments[0].click();", expand_all_button)  # Use JavaScript click

        driver.implicitly_wait(5)
        print("Clicked on the expand all button.")
        driver.implicitly_wait(4)
    except TimeoutException:
        print("Timeout: Unable to locate or click the expand all button.")
    except Exception as e:
        print(f"Exception occurred: {e}")

    # Locate and interact with the "Name" search bar
    try:
        name_searchbar = wait.until(
            EC.element_to_be_clickable((By.XPATH, '//input[@data-testid="test-nametext"]'))
        )
        name_searchbar.send_keys("Sowndharya M")
        driver.execute_script("arguments[0].click();", name_searchbar)  # Click the search bar if needed

        print("Entered text into name search bar.")

    except TimeoutException:
        print("Timeout: Unable to interact with the name search bar.")



    # Locate and click on the "See results" button
    try:
        see_results_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='See results']"))
        )
        actions = ActionChains(driver)
        actions.double_click(see_results_button).perform()  # Perform double-click action

        print("Double-clicked on the see results button.")
    except TimeoutException:
        print("Timeout: Unable to locate the see results button.")
    except Exception as e:
        print(f"Exception occurred: {e}")

finally:

    driver.quit()
