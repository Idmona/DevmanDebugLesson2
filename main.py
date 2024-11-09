import os

from dotenv import load_dotenv
from weather_sdk import get_new_event, SMSServer

load_dotenv()

forecast_token = os.getenv('FORECAST_TOKEN')
sms_token = os.getenv('SMS_TOKEN')
town_title = 'Курск'

server = SMSServer(sms_token)
new_event = get_new_event(forecast_token, town_title)
event_date = new_event.get_date()
event_time = new_event.get_time()
event_area = new_event.get_area()
phenomenon_description = new_event.get_phenomenon()

sms_template = '''{town_title}: {event_time} {event_date} {event_area} ожидается {phenomenon_description}. Будьте внимательны и осторожны.'''

sms_message = sms_template.format(
    phenomenon_description=phenomenon_description,
    town_title=town_title,
    event_time=event_time,
    event_date=event_date,
    event_area=event_area)

server.send(sms_message)






# Гипотеза 1: В переменной нет прогноза погоды для Курска
# Способ проверки: Вывела переменную new_event
# Код для проверки: print(new_event)
# Установленный факт:выводится Регион:  Погода:
# Вывод: причина не в этом

# Гипотеза 2.1: town_title на самом деле пуста
# Способ проверки: вывести переменную town_title
# Код для проверки: print('town_title:',town_title)
# Установленный факт: Выводится Курск
# Вывод:причина не в этом 

# Гипотеза 2.2: В town_title не название города
# Способ проверки: вывести переменную town_title
# Код для проверки: print('town_title:',town_title)
# Установленный факт: Курск это город
# Вывод: причина не в этом

# Гипотеза 3: Переменная token на самом деле пуста
# Способ проверки: проверим на значение None 
# Код для проверки: if not FORECAST_TOKEN: 
# Установленный факт: выводит ошибку
# Вывод: переменная token пуста

# Гипотеза 4.1: Может, `token` всё ещё пуст?
# Способ проверки: вывести значение token 
# Код для проверки: print("FORECAST_TOKEN:", token)
# Установленный факт: значение выводится
# Вывод: гипотеза не подтвердилась

# Гипотеза 4.2: Может, в токене не то значение, не `85b98d96709fd49a69ba8165676e4592`?
# Способ проверки: вывести и сравнить значение token 
# Код для проверки: print("FORECAST_TOKEN:", token)
# Установленный факт: значение  не совподает
# Вывод: Гипотеза подтвердилась

# Гипотеза 4.3: Может, значение `85b98d96709fd49a69ba8165676e4592` успевает измениться до строчки `new_event = ...`?
# Способ проверки: вывести значения FORECAST_TOKEN перед вызовом SMS_TOKEN 
# Код для проверки: print("FORECAST_TOKEN:", token)
# Установленный факт:значение совпало 
# Вывод: проблема в переменной token

# Гипотеза 5.1: Переменная `event_time` пуста/в ней не время
# Способ проверки: проверить содержимое event_time 
# Код для проверки: print("event_time:", event_time)
# Установленный факт: выводит время вечером
# Вывод: переменная не пуста

# Гипотеза 5.2: Переменная `event_date` пуста/в ней не дата
# Способ проверки: проверить содержимое event_date
# Код для проверки: print("event_date:", event_date)
# Установленный факт: выводит дату
# Вывод: переменная не пуста

# Гипотеза 5.3: Переменная `event_area` пуста/в ней не место
# Способ проверки: проверить содержимое event_area
# Код для проверки: print("event_area:", event_area)
# Установленный факт: выводит информацию о месте
# Вывод: переменная не пуста

# Гипотеза 5.4: Переменная `phenomenon_description` пуста/в ней не описание погодного явления
# Способ проверки: проверить соднржимое phenomenon_description
# Код для проверки: print("phenomenon_description:", phenomenon_description)
# Установленный факт: выводятся данные о погодном явлении
# Вывод: переменная не пуста

# Гипотеза 6: проверить метод на наличие опечаток
# Способ проверки: VS Code подсвечивает возможные ошибки
# Код для проверки: Ctrl + Shift + F
# Установленный факт: ошибок нет
# Вывод: гипотеза не подтвердилась

# Гипотеза 7: в шаблоне строки sms_template не передана переменная в метод .format()
# Способ проверки: передать все переменные 
# Код для проверки: sms_message = sms_template.format(phenomenon_description=phenomenon_description,town_title=town_title, event_time=event_time, event_date=event_date, event_area=event_area)
# Установленный факт: не были переданы переменные в метод
# Вывод: гипотеза подтвердилась