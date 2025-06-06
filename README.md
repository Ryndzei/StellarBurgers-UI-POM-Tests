# Дипломный проект. Яндекс Практикум. Задание 3: UI Tests

Тестирование сервиса [Stellar Burgers](https://stellarburgers.nomoreparties.site/) по Page Object Model

Были выполнены проверки по следующим сценариям:

#### [Восстановление пароля](tests/test_password_recovery.py)

* Переход на страницу восстановления пароля по кнопке «Восстановить пароль»
* Переход на страницу сброса пароля после ввода почты и нажатия «Восстановить»
* Клик по кнопке «показать/скрыть пароль» делает поле активным (подсвечивает его)

#### [Личный кабинет](tests/test_personal_account.py)

* Переход по клику на «Личный кабинет»
* Переход в раздел «История заказов»
* Выход из аккаунта по кнопке «Выход»

#### [Основной функционал](tests/test_basic_functionality.py)

* Переход по клику на «Конструктор» на странице логина (редирект на базовую страницу)
* Переход по клику на «Лента заказов» на главной странице
* При клике на ингредиент открывается всплывающее окно с деталями
* Всплывающее окно закрывается кликом по крестику
* При добавлении ингредиента счётчик ингредиента увеличивается
* Залогиненный пользователь может оформить заказ

#### [Лента заказов](tests/test_orders_list.py)

* При клике на заказ открывается всплывающее окно с деталями
* Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»
* При создании нового заказа счётчик «Выполнено за всё время» увеличивается
* При создании нового заказа счётчик «Выполнено сегодня» увеличивается
* После оформления заказа его номер появляется в разделе «В работе»

---

## Структура репозитория

#### В корне проекта находятся:

* `conftest.py` – фикстуры и логика создания/удаления тестового пользователя через API
* `driver_factory.py` – фабрика, возвращающая WebDriver для Chrome и Firefox
* `random_data.py` – генератор случайных email/паролей через Faker
* `requirements.txt` – список зависимостей
* `urls.py` – константы с URL страниц и API-эндпоинтов
* Папка `allure_results` – директория для хранения результатов Allure-отчёта

#### В папке `locators` находятся описания локаторов для элементов страниц:

* `base_page_locators.py`
* `forgot_password_locators.py`
* `home_page_locators.py`
* `login_account_locators.py`
* `orders_list_locators.py`
* `personal_account_locators.py`
* `reset_password_page_locators.py`

#### В папке `page_objects` находятся POM-классы:

* `base_page.py`
* `forgot_password_page.py`
* `home_page.py`
* `login_page.py`
* `orders_list_page.py`
* `personal_account_page.py`
* `reset_password_page.py`

#### В папке `tests` находятся тесты:

* `test_password_recovery.py`
* `test_personal_account.py`
* `test_basic_functionality.py`
* `test_orders_list.py`

---

## Библиотеки

* pytest
* selenium
* allure-python-commons
* Faker
* requests

---

## Команды

Установить зависимости:

```shell
pip3 install -r requirements.txt
```

Запустить все тесты:

```shell
pytest tests/
```

Посмотреть отчёт в формате веб-страницы:

```shell
allure serve allure_results
```