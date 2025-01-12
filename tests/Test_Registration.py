import random
import time
from conftest import driver
from tests_locators import Test_Locators

user_name = f'Алексей{random.randint(0, 999)}'
user_email = f'AlexTat_17_{random.randint(100, 999)}@yandex.ru'
incorrect_password = random.randint(0, 99999)
correct_password = random.randint(100000, 999999)

class Test_Registration_False:
    def test_avtorization_non_valid(self, driver):

        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*Test_Locators.SEARCH_PERSONAL_ACCOUNT).click()
        driver.find_element(*Test_Locators.SEARCH_REGISTRATION).click()

        driver.find_element(*Test_Locators.INPUT_NAME).send_keys(user_name)
        driver.find_element(*Test_Locators.INPUT_EMAIL).send_keys(user_email)
        driver.find_element(*Test_Locators.INPUT_PASSWORD).send_keys(incorrect_password)
        driver.find_element(*Test_Locators.BUTTON_REGISTRATION).click()
        assert driver.find_element(*Test_Locators.MISTAKE_INCORRECT_PASSWORD).text == "Некорректный пароль" #ассерт на некорректный пароль

class Test_Registration_True:
    def test_avtorization_valid(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*Test_Locators.SEARCH_PERSONAL_ACCOUNT).click()
        driver.find_element(*Test_Locators.SEARCH_REGISTRATION).click()

        driver.find_element(*Test_Locators.INPUT_NAME).send_keys(user_name)
        driver.find_element(*Test_Locators.INPUT_EMAIL).send_keys(user_email)
        driver.find_element(*Test_Locators.INPUT_PASSWORD).send_keys(correct_password)

        driver.find_element(*Test_Locators.BUTTON_REGISTRATION).click()
        time.sleep(0.5) #топорная задержка, без которой не успеет отработать
        assert driver.find_element(*Test_Locators.SEARCH_INPUT_ELEMENT_TEXT).text == "Вход" #ассерт на переход к странице с заголовком "Вход"

        #print(f'Имя:{user_name}; Логин: {user_email}; Пароль: {correct_password}') #вывод имени,логина,пароля (опционально)