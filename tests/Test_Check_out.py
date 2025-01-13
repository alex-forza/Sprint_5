from conftest import driver
from data import Urls, Variables
from locators import TestLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestCheckOut:
    def test_check_out(self,driver):
        driver.get(Urls.url)
        driver.find_element(*TestLocators.search_sign_in_main).click()
        driver.find_element(*TestLocators.input_email).send_keys(Variables.user_email_static)
        driver.find_element(*TestLocators.input_password).send_keys(Variables.correct_password_static)
        driver.find_element(*TestLocators.button_input).click()

        driver.find_element(*TestLocators.search_personal_account).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.search_exit_acc))
        driver.find_element(*TestLocators.search_exit_acc).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.search_input_element_text))
        assert driver.find_element(*TestLocators.search_input_element_text).text == "Вход"