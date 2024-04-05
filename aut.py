    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    # Create a new instance of the Firefox driver
    driver = webdriver.Firefox()

    # Go to the Google search page
    driver.get("https://www.example.com    # Find the search box and enter a search term
    search_box = driver.find_element_by_name("q")
    search_box.send_keys("Selenium")

    # Find the search button and click it
    search_button = driver.find_element_by_name("btnK")
    search_button.click()

    # Wait for the search results to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "search"))
    )

    # Find the first search result and click it
    first_result = driver.find_element_by_css_selector("div.rc")
    first_result.click()

    # Wait for the page to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))
    )

    # Find the close button and click it
    close_button = driver.find_element_by_css_selector("button.close-button")
    close_button.click()

    # Close the browser
    driver.close()  
