from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




def cookie():
    driver = webdriver.Chrome()
    driver.get("https://orteil.dashnet.org/cookieclicker/")
    cookie_id = "bigCookie"
    cookies_id = "cookies"
    product_price_prefix = "productPrice"
    product_prefix = "product"

    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'English')]"))
    )

    language = driver.find_element(By.XPATH, "//*[contains(text(),'English')]")
    language.click()

    WebDriverWait(driver, 5).until(
         EC.presence_of_element_located((By.ID, cookie_id))
    )

    cookie = driver.find_element(By.ID, cookie_id)
    cookie.click()

    while True:
        cookie.click()
        cookies_count = int(driver.find_element(By.ID, cookies_id).text.split(" ")[0].replace(",", ""))
   
        for i in range(4):
            product_price = driver.find_element(By.ID, product_price_prefix + str(i)).text.replace(",", "")
            if not product_price.isdigit():
                continue

            product_price = int(product_price)

            if cookies_count >= product_price:
                product = driver.find_element(By.ID, product_prefix + str(i))
                product.click()
                break

    # Add a delay to avoid overwhelming the server
        time.sleep(1)

    # Add a condition to break out of the loop
        if cookies_count > 1000000:
            break

    time.sleep(10)
    driver.quit()

