import json
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from site_parser import site_parser


class new_site_parser(site_parser):
    def __init__(self):
        self.const_data_json_name = 'rzd.ru.const.json'
        self.param_paths_json_name = 'rzd.ru.json'

    def getTrains(self, driver, src, dest, date):
        self.driver, self.src, self.dest, self.date = driver, src, dest, date

        self.load_paths_and_params_from_json()
        self.load_paths_and_params_to_self()

        self.driver.get('https://www.rzd.ru/')

        self.fill_from_to()
        self.fill_date()
        self.click_find()

        return self.parse()


