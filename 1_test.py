from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    button = browser.find_element(By.XPATH,"//button[@id='book']")
    WebDriverWait(browser,12).until(EC.text_to_be_present_in_element((By.XPATH,"//h5[@id='price']"),"100"))
    button.click()
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    y = browser.find_element(By.XPATH, "//*[@id='input_value']").text
    browser.find_element(By.XPATH, "//*[@id='answer']").send_keys(calc(y))
    butSubmit = browser.find_element(By.XPATH, "//*[@id='solve']")
    butSubmit.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()