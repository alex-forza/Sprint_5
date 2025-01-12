from conftest import driver
from tests_locators import Test_Locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

user_email = "AlexTat_17_742@yandex.ru"
correct_password = 129510

class Test_Transition_To_Pers_Acc:
    def test_transition_to_acc(self,driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*Test_Locators.SEARCH_SIGN_IN_MAIN).click()
        driver.find_element(*Test_Locators.INPUT_EMAIL).send_keys(user_email)
        driver.find_element(*Test_Locators.INPUT_PASSWORD).send_keys(correct_password)
        driver.find_element(*Test_Locators.BUTTON_INPUT).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")))

        driver.find_element(*Test_Locators.SEARCH_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, ".//button[text()='Выход']")))