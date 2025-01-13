from data import Urls, Variables
import time
from conftest import driver
from locators import TestLocators

class TestRegistrationFalse:
    def test_avtorization_non_valid(self, driver):

        driver.get(Urls.url)
        driver.find_element(*TestLocators.search_personal_account).click()
        driver.find_element(*TestLocators.search_registration).click()

        driver.find_element(*TestLocators.input_name).send_keys(Variables.user_name)
        driver.find_element(*TestLocators.input_email).send_keys(Variables.user_email)
        driver.find_element(*TestLocators.input_password).send_keys(Variables.incorrect_password)
        driver.find_element(*TestLocators.button_registration).click()
        assert driver.find_element(*TestLocators.mistake_incorrect_password).text == "Некорректный пароль" #ассерт на некорректный пароль

class TestRegistrationTrue:
    def test_avtorization_valid(self, driver):
        driver.get(Urls.url)
        driver.find_element(*TestLocators.search_personal_account).click()
        driver.find_element(*TestLocators.search_registration).click()

        driver.find_element(*TestLocators.input_name).send_keys(Variables.user_name)
        driver.find_element(*TestLocators.input_email).send_keys(Variables.user_email)
        driver.find_element(*TestLocators.input_password).send_keys(Variables.correct_password)

        driver.find_element(*TestLocators.button_registration).click()
        time.sleep(0.5) #топорная задержка, без которой не успеет отработать
        assert driver.find_element(*TestLocators.search_input_element_text).text == "Вход" #ассерт на переход к странице с заголовком "Вход"