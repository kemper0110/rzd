import json
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from site_parser import site_parser


class old_site_parser(site_parser):
    def __init__(self):
        self.const_data_json_name = 'pass.rzd.ru.const.json'
        self.param_paths_json_name = 'pass.rzd.ru.json'

    def fill_date(self):
        to_date = self.driver.find_element_by_xpath(self.to_date_path)
        # to_date.clear() # бессилен в данном случае, поэтому использую это
        to_date.send_keys(Keys.CONTROL + Keys.BACKSPACE)
        to_date.send_keys(self.date)

    def click_find(self):
        checkbox = self.driver.find_element_by_xpath(self.checkbox_path)
        checkbox.click()
        find_button = self.driver.find_element_by_xpath(self.find_button_path)
        find_button.click()

    def getTrains(self, driver, src, dest, date):
        self.driver, self.src, self.dest, self.date = driver, src, dest, date

        self.load_paths_and_params_from_json()
        self.load_paths_and_params_to_self()
        self.checkbox_path = self.data['checkbox']

        self.driver.get('https://pass.rzd.ru/')

        self.fill_from_to()
        self.fill_date()
        self.click_find()

        return self.parse()

