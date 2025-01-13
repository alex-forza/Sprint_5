from conftest import driver
from data import Urls, Variables
from locators import TestLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestCheckIn:
    def test_check_in_main(self,driver):
        driver.get(Urls.url)

        driver.find_element(*TestLocators.search_sign_in_main).click()

        driver.find_element(*TestLocators.input_email).send_keys(Variables.user_email_static)
        driver.find_element(*TestLocators.input_password).send_keys(Variables.correct_password_static)
        driver.find_element(*TestLocators.button_input).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.button_order))
        assert driver.find_element(*TestLocators.button_order).text == 'Оформить заказ'

    def test_check_in_personal_acc(self,driver):
        driver.get(Urls.url)

        driver.find_element(*TestLocators.search_personal_account).click()

        driver.find_element(*TestLocators.input_email).send_keys(Variables.user_email_static)
        driver.find_element(*TestLocators.input_password).send_keys(Variables.correct_password_static)
        driver.find_element(*TestLocators.button_input).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.button_order))
        assert driver.find_element(*TestLocators.button_order).text == 'Оформить заказ'

    def test_check_in_throw_registration(self, driver):
        driver.get(Urls.url)

        driver.find_element(*TestLocators.search_personal_account).click()
        driver.find_element(*TestLocators.search_registration).click()
        driver.find_element(*TestLocators.search_sign_in_throw_registration_and_recovery).click()

        driver.find_element(*TestLocators.input_email).send_keys(Variables.user_email_static)
        driver.find_element(*TestLocators.input_password).send_keys(Variables.correct_password_static)
        driver.find_element(*TestLocators.button_input).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.button_order))
        assert driver.find_element(*TestLocators.button_order).text == 'Оформить заказ'

    def test_check_in_throw_forgot(self, driver):
        driver.get(Urls.url)

        driver.find_element(*TestLocators.search_personal_account).click()
        driver.find_element(*TestLocators.search_forgot_password).click()
        driver.find_element(*TestLocators.search_sign_in_throw_registration_and_recovery).click()

        driver.find_element(*TestLocators.input_email).send_keys(Variables.user_email_static)
        driver.find_element(*TestLocators.input_password).send_keys(Variables.correct_password_static)
        driver.find_element(*TestLocators.button_input).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.button_order))
        assert driver.find_element(*TestLocators.button_order).text == 'Оформить заказ'