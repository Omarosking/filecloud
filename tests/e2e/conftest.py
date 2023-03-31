import json
import pytest
import selenium.webdriver
import os


from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

@pytest.fixture
def config(scope = 'session'):

    #Read the config.json file
    with open('config.json') as config_file:
        config = json.load(config_file)
    
    #Assert values from config.json are valid
    assert config['browser'] in ['Firefox', 'Chrome', 'Headless Chrome']
    assert isinstance(config['implicit_wait'], int)
    assert config['implicit_wait'] > 0

    return config

@pytest.fixture
def browser(config):

    #Let's start the webdriver instance 

    if config['browser'] == 'Firefox':
        init = selenium.webdriver.Firefox()
        init.maximize_window() 
    elif config['browser'] == 'Chrome':
       init = selenium.webdriver.Chrome()
       
       init.maximize_window() 
    elif config['browser'] == 'Headless Chrome':
        chrome_options = selenium.webdriver.ChromeOptions()
        chrome_options.add_argument('headless')
        init = selenium.webdriver.Chrome(options=chrome_options)
    else:
        raise Exception(f'Selected browser: "{config["browser"]}" is invalid.')

    #Let's set the implicit wait for tests

    init.implicitly_wait(config['implicit_wait'])

    #Return the webdriver instance for the setup

    yield init

    #Quit webdriver for cleanup
    init.quit()