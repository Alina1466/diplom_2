# diplom_2
Тест для проверки API приложения "Stellar Burgers" с помощью библиотеки Pytest, Requests и allure-pytest
Структура проекта:

tests/ - папка с файлами тестов:

tests/test_create_user.py - тесты создания пользователя
tests/test_login_user.py - тесты авторизации пользователя
tests/test_changing_data_user.py - тесты обновления данных пользователя
tests/test_create_order.py - тесты создания заказа
tests/test_take_order_user.py - тесты получения заказов пользователя

Файл "methods.py" - файл, в котором лежат генераторы данных для пользователя

Файл "conftest.py" - Файл, в котором лежит фикстура, в которую передается сгенерированные данные для создание пользователя.
Также после окончания работы теста, созданный пользователь удаляется. 

Файл "data.py" - константы, URL-адреса и данные для тестов

Файл ".gitignore" - файл для проекта в Git/GinHub

Файл "requirements.txt" - файл с внешними зависимостями

README.md - файл с описанием проекта 

Папка "allure_results/" - папка с отчетами Allure

Для запуска тестов должны быть установлены пакеты:
Pytest
Requests
Allure-pytest
Allure-python-commons
Для генерации отчетов необходимо дополнительно установить:
пакет Allure
фреймворк JDK
Запуск всех тестов выполняется командой:

$ pytest -v ./tests

Запуск тестов с генерацией отчета Allure выполняется командой:

$ pytest -v ./tests  --alluredir=allure_results

Генерация отчета выполняется командой:

$ allure serve allure_results

Генерация файла внешних зависимостей requirements.txt выполняется командой:

$  pip freeze > requirements.txt

Установка зависимостей из файла requirements.txt выполняется командой:

$ pip install -r requirements.txt
