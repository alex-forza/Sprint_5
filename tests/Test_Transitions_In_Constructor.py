from conftest import driver
from data import Urls, Variables
from locators import TestLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestTransitionInConstructor:
    def test_transition_sauces(self,driver):
        driver.get(Urls.url)
        driver.find_element(*TestLocators.search_sign_in_main).click()
        driver.find_element(*TestLocators.input_email).send_keys(Variables.user_email_static)
        driver.find_element(*TestLocators.input_password).send_keys(Variables.correct_password_static)
        driver.find_element(*TestLocators.button_input).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.button_order))

        driver.find_element(*TestLocators.button_main_sauces).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.condition_sauces))
        assert driver.find_element(*TestLocators.search_sauces).text == 'Соус Spicy-X'

    def test_transition_breads(self, driver):
        driver.get(Urls.url)
        driver.find_element(*TestLocators.search_sign_in_main).click()
        driver.find_element(*TestLocators.input_email).send_keys(Variables.user_email_static)
        driver.find_element(*TestLocators.input_password).send_keys(Variables.correct_password_static)
        driver.find_element(*TestLocators.button_input).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.button_order))

        driver.find_element(*TestLocators.button_main_sauces).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.button_main_sauces))
        driver.find_element(*TestLocators.button_main_breads).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.condition_breads))
        assert driver.find_element(*TestLocators.search_breads).text == 'Флюоресцентная булка R2-D3'

    def test_transition_fillings(self, driver):
        driver.get(Urls.url)
        driver.find_element(*TestLocators.search_sign_in_main).click()
        driver.find_element(*TestLocators.input_email).send_keys(Variables.user_email_static)
        driver.find_element(*TestLocators.input_password).send_keys(Variables.correct_password_static)
        driver.find_element(*TestLocators.button_input).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.button_order))

        driver.find_element(*TestLocators.button_main_fillings).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.condition_fillings))
        assert driver.find_element(*TestLocators.search_fillings).text == 'Биокотлета из марсианской Магнолии'