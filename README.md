#qa_python_sprint_5
1. Class TestRegistrationFalse (файл Test_Registration.py). Проверяет отработку при попытке зарегистрировать некорректной пароль. 
Критерий корректности пароля: >5 символов.

2. Class TestRegistrationTrue (файл Test_Registration.py). Проверяет отработку при попытке регистрации с корректными введенными данными.
Формат "Имени": Имя_Рандом(0,999).
Формат "Email": Имя_Фамилия(сокращ.)_№когорты_Рандом(100,999)_@yandex.ru.
Формат "Пароля": >5 символов.

3. Class CheckIn. Проверяет возможность входа из четырех мест: 
- По кнопке "Войти в аккаунт" на главной странице;
- По кнопке "Личный кабинет";
- По кнопке "Вход" из формы регистрации;
- По кнопке "Вход" из формы восстановления пароля.

4. Class TestTransitionToPersAcc. Проверка перехода в личный кабинет по соответствующей кнопке.

5. TestTransitionFromAccToConstructor. Проверка перехода в конструктор по:
- Клику на "Конструктор" (def test_transition_from_acc_to_constructor_button);
- Клику на логотип (def test_transition_from_acc_to_constructor_logo).

6. Class CheckOut. Проверяет отработку выхода из аккаунта по кнопке "Выход" из личного кабинета.

7. Class TestTransitionInConstructor. Проверка перехода к разделам:
- Булки (def test_transition_breads);
- Соусы (def test_transition_sauces);
- Начинки (def test_transition_fillings).