from selenium import webdriver


class WebdriverFactory:

    @staticmethod
    def getWebdriver(browserName):
        if browserName == "firefox":
            return webdriver.Firefox()
        elif browserName == "chrome":
            return webdriver.Chrome()
        else:
            raise ValueError(f"{browserName} не поддерживается.\nПоддерживаемое окружение:firefox, chrome")