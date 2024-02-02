import pytest
import json
from selenium import webdriver

import configparser


@pytest.fixture(params=["chrome"])
def init_driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
        config = read_config()
        base_url = config[0].get('UI', 'BASE_URL')
        driver.get(base_url)
        driver.maximize_window()
        # request.node._driver = driver 
        yield driver
        driver.quit()

@pytest.fixture
def get_api_data():
    config = read_config()
    print(config)
    return {
        "BASE_URL": config[1].get("API", "BASE_URL"),
        "api_key": config[1].get("API", "api_key"),
        "location": config[1].get("API", "location"),
        "days": config[1].get("API", "days")
    }


def read_config(ui_path='config.ini', api_path='api_config.ini'):
    ui_config = configparser.ConfigParser()
    ui_config.read(ui_path)
    api_config = configparser.ConfigParser()
    api_config.read(api_path)
    return [ui_config, api_config]


@pytest.fixture
def login_data():
    # Load data from the JSON file
    with open("Data/data.json", "r") as file:
        data = json.load(file)
    return data


@pytest.fixture
def assertion_data():
    # Load  assertion data from the JSON file
    with open("Data/assertionData.json", "r") as file:
        assertionData = json.load(file)
    return assertionData
