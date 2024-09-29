import time
import math
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

answer = str(math.log(int(time.time())))


@pytest.mark.parametrize('link',
                         ['https://stepik.org/lesson/236895/step/1','https://stepik.org/lesson/236896/step/1',
'https://stepik.org/lesson/236897/step/1',
'https://stepik.org/lesson/236898/step/1',
'https://stepik.org/lesson/236899/step/1',
'https://stepik.org/lesson/236903/step/1',
'https://stepik.org/lesson/236904/step/1',
'https://stepik.org/lesson/236905/step/1'])
def test_autorize_stepic(browser, link):
    browser.implicitly_wait(10)
    wait = WebDriverWait(browser, 30, poll_frequency=1)
    browser.get(link)
    button = browser.find_element(By.ID,'ember458')
    button.click()
    login = browser.find_element(By.ID, "id_login_email")
    password = browser.find_element(By.ID, "id_login_password")
    wait.until(EC.element_to_be_clickable(login))
    login.send_keys("shibaiy1991@gmail.com")
    wait.until(EC.element_to_be_clickable(password))
    password.send_keys("c755pk57RUS")
    entry = browser.find_element(By.XPATH, '//button[@class="sign-form__btn button_with-loader "]')
    wait.until(EC.element_to_be_clickable(entry))
    entry.click()
    wait.until(EC.invisibility_of_element_located((By.XPATH, '//*[@class="modal-dialog-block"]')))
    textarea = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@class="ember-text-area ember-view textarea string-quiz__textarea"]')))
    textarea.clear()
    textarea.send_keys(str(math.log(int(time.time()))))
    post = browser.find_element(By.XPATH, '//button[@class="submit-submission"]')
    wait.until((EC.element_to_be_clickable(post)))
    post.click()
    result = browser.find_element(By.XPATH, '//*[@class="smart-hints__hint"]')
    wait.until((EC.element_to_be_clickable(result)))
    assert result.text == 'Correct!'
