import json
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys

class site_parser:
    def load_paths_and_params_from_json(self):
                       # json с комментариями не читается, поэтому комментарии
                       # здесь
        self.data = {} # чтение параметров файла, который не подразумевает
                       # добавление новых параметров,но текущие могут
                                             # изменяться
        with open(self.const_data_json_name, 'r') as f:  
            self.data = json.load(f)
        
        self.param_paths = {}                             #   файл хранит
        with open(self.param_paths_json_name) as f:  #   xpath на элементы поиска относительно
            self.param_paths = json.load(f)               #   абсолютного пути
                                                     #   и ключ - название для
                                                                                           #   элемента
                                                                                                                                      #   поиска
    def load_paths_and_params_to_self(self):
        self.abs_path = self.data['card']
        self.from_textbox_path = self.data['from_textbox']
        self.to_textbox_path = self.data['to_textbox']
        self.to_date_path = self.data['to_date']
        self.find_button_path = self.data['find_button']
        self.train_id_path = self.data['train_id']

    def fill_from_to(self):
        from_textbox = self.driver.find_element_by_xpath(self.from_textbox_path)
        from_textbox.clear()
        from_textbox.send_keys(self.src)
        
        to_textbox = self.driver.find_element_by_xpath(self.to_textbox_path)
        to_textbox.clear()
        to_textbox.send_keys(self.dest)

    def fill_date(self):
        to_date = self.driver.find_element_by_xpath(self.to_date_path)
        to_date.clear()
        to_date.send_keys(self.date)

    def click_find(self):
        find_button = self.driver.find_element_by_xpath(self.find_button_path)
        find_button.click()
    def parse(self):
        # ключи из json
        param_keys = { key for key in self.param_paths }
        
        # данные текущего маршрута, ключ - номер поезда
        trail_data = {}
        
        items = self.driver.find_elements_by_xpath(self.abs_path)
        # для сохранения исходной последовательности поездов
        trains_order = [] 
        route_data = {}
        for item in items:
            train_data = {}
            train_id = item.find_element_by_xpath(self.train_id_path).text
            trains_order.append(train_id)
            for param_key in param_keys:
                param_value = item.find_element_by_xpath(self.param_paths[param_key]).text
                train_data[param_key] = param_value
            route_data[train_id] = train_data
        return trains_order, route_data
        
