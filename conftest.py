import random
import pytest
from selenium import webdriver

import helper
from data import User


@pytest.fixture(scope='function')
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--window-size=1024,768')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    drv = webdriver.Chrome(options=chrome_options)
    try:
        yield drv
    finally:
        drv.quit()


@pytest.fixture
def user():
    user = User(name='Nikitaa03')
    user.email = f'nikskras03{random.randint(1000, 9999)}@mail.ru'
    user.password = helper.gen_password()
    return user