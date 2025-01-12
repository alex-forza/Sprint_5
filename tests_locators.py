import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from conftest import driver
import random

class Test_Locators:
    SEARCH_PERSONAL_ACCOUNT = By.LINK_TEXT, "Личный Кабинет"
    SEARCH_REGISTRATION = By.LINK_TEXT, "Зарегистрироваться"
    INPUT_NAME = By.XPATH, "//label[text()='Имя']/following-sibling::input[@name='name']"
    INPUT_EMAIL = By.XPATH, "//label[text()='Email']/following-sibling::input[@name='name']"
    INPUT_PASSWORD = By.NAME,"Пароль"
    BUTTON_REGISTRATION = By.XPATH, ".//button[text()='Зарегистрироваться']"
    MISTAKE_INCORRECT_PASSWORD = By.XPATH, "//p[contains(text(), 'Некорректный пароль')]"
    SEARCH_INPUT_ELEMENT_TEXT = By.XPATH, ".//h2"
    BUTTON_INPUT = By.XPATH, ".//button[text()='Войти']"
    SEARCH_SIGN_IN_MAIN = By.XPATH, ".//button[text()='Войти в аккаунт']"
    SEARCH_SIGN_IN_THROW_REGISTRATION_AND_RECOVERY = By.XPATH, "//a[@class='Auth_link__1fOlj' and @href='/login']"
    SEARCH_FORGOT_PASSWORD = By.XPATH, "//a[@class='Auth_link__1fOlj' and @href='/forgot-password']"
    SEARCH_EXIT_ACC = By.XPATH, ".//button[text()='Выход']"
    BUTTON_CONSTRUCTOR = By.XPATH, ".//p[text()='Конструктор']"
    LOGO_STELLAR_BURGERS = By.CSS_SELECTOR, ".AppHeader_header__logo__2D0X2"
    BUTTON_MAIN_BREADS = By.XPATH, "//span[text()='Булки']"
    BUTTON_MAIN_SAUCES = By.XPATH, "//span[text()='Соусы']"
    BUTTON_MAIN_FILLINGS = By.XPATH, "//span[text()='Начинки']"