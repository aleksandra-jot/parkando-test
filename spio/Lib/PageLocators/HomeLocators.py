class HomeLocators(object):
    cardid_input = "//input[@id='number']"
    name_input = "//input[@id='name']"
    surname_input = "//input[@id='surname']"
    button_submit = "//button[contains(@class, 'form__login')]"
    alert_error = "//label[@for='surname']/span[@class='simple-label__error']"
    alert_id_error = "//label[@for='number']/span[@class='simple-label__error']"


class WelcomeLocators(object):
    welcome_username = "//section/div[contains(@class, 'user-name')]"
    welcome_button = "//button[contains(@class, 'welcome')]"


