from selenium import webdriver 
from new_site_parser import new_site_parser
from old_site_parser import old_site_parser
import json
import time
import datetime
from excel_writer import excel_writer

routes = []
with open("routes.json") as f:
    routes = json.load(f)



driver = webdriver.Chrome(r'webdrivers\chromedriver.exe')
driver.implicitly_wait(4)   # при медленном соединении следует увеличить

new_data = {}
new_parser = new_site_parser()
for src, dest, date in routes:
    trains_order, route_data = new_parser.getTrains(driver, src, dest, date)
    new_data[src + ' ' + dest + ' ' + date] = {"trains_order" : trains_order, "route_data" : route_data}

with open('new_data.json', 'w') as f:
    json.dump(new_data, f, indent = 4)


old_data = {}
old_parser = old_site_parser()
for src, dest, date in routes:
    trains_order, route_data = old_parser.getTrains(driver, src, dest, date)
    old_data[src + ' ' + dest + ' ' + date] = {"trains_order" : trains_order, "route_data" : route_data}

with open('old_data.json', 'w') as f:
    json.dump(old_data, f, indent = 4)


param_keys = []
with open("rzd.ru.json") as f:
    param_keys = [key for key in json.load(f)]
param_keys.sort()   # лишь вариант порядка вывода параметров

with open('new_data.json', 'r') as f:
    new_data = json.load(f)
with open('old_data.json', 'r') as f:
    old_data = json.load(f)

excel_writer().write(routes, param_keys, old_data, new_data).save()


#input()
driver.quit()
