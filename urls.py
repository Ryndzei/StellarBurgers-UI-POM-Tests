
class URL:

    BASE_URL = "https://stellarburgers.nomoreparties.site/"
    REGISTER_URL = f"{BASE_URL}register"
    LOGIN_URL = f"{BASE_URL}login"
    FORGOT_PASS_URL = f"{BASE_URL}forgot-password"
    RESET_PASS_URL = f"{BASE_URL}reset-password"
    PERSONAL_ACCOUNT_URL = f"{BASE_URL}account/profile"
    ORDER_HISTORY_URL = f"{BASE_URL}account/order-history"
    ORDERS_LIST_URL = f"{BASE_URL}feed"

    REGISTER_USER_URL = f'{BASE_URL}api/auth/register'
    LOGIN_USER_URL = f'{BASE_URL}api/auth/login'
    DELETE_USER_URL = f'{BASE_URL}api/auth/user'