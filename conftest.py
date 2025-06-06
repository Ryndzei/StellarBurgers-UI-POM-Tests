import time
import allure
import pytest
import requests
from driver_factory import WebdriverFactory
from page_objects.forgot_password_page import ForgotPasswordPage
from page_objects.home_page import HomePage
from page_objects.login_page import LoginPage
from page_objects.orders_list_page import OrdersListPage
from page_objects.personal_account_page import PersonalAccountPage
from page_objects.reset_password_page import ResetPasswordPage
from random_data import generate_user_register_body
from urls import URL


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    browser_name = request.param
    driver = WebdriverFactory.getWebdriver(browser_name)
    yield driver
    driver.quit()

@pytest.fixture(scope="function", name="home_page")
def home_page(driver):
    return HomePage(driver)

@pytest.fixture(scope="function", name="login_page")
def login_page(driver):
    return LoginPage(driver)

@pytest.fixture(scope="function", name="forgot_password_page")
def forgot_password_page(driver):
    return ForgotPasswordPage(driver)

@pytest.fixture(scope="function", name="reset_password_page")
def reset_password_page(driver):
    return ResetPasswordPage(driver)

@pytest.fixture(scope="function", name="personal_account_page")
def personal_account_page(driver):
    return PersonalAccountPage(driver)

@pytest.fixture(scope="function", name="orders_list_page")
def orders_list_page(driver):
    return OrdersListPage(driver)

@pytest.fixture(scope="function", name="user_create_and_cleanup")
def user_create_and_cleanup():
    time.sleep(1)
    with allure.step("POST /auth/register — создаем пользователя"):
        payload = generate_user_register_body()
        response_register = requests.post(URL.REGISTER_USER_URL, json=payload)
        assert response_register.status_code == 200 and response_register.json()['success'] == True

    yield payload

    with allure.step("POST /auth/login — получаем token для удаления"):
        login_response = requests.post(URL.LOGIN_USER_URL, json=payload)
        assert login_response.status_code == 200
        token = login_response.json().get('accessToken')

    with allure.step("DELETE /auth/user — удаляем пользователя по полученному token"):
        delete_response = requests.delete(URL.DELETE_USER_URL, headers={'Authorization': token})

        assert delete_response.status_code == 202
        assert delete_response.json().get('message') == 'User successfully removed'
