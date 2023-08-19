import requests


class WeatherAssistant:
    def __init__(self, city):
        self.city = city
        self.api_key = '25a3a8fd4f83c1c60d47c15bd604a594'

    def today(self):
        url = f"https://api.openweathermap.org/data/2.5/weather?q={self.city}&appid={self.api_key}&units=metric"

        response = requests.get(url)
        data = response.json()

        # pprint(data)
        if data['cod'] != '404':
            message = f"Обу ҳаво дар шаҳри *{self.city}*:\n" + \
                      f'Температура: _{data["main"]["temp"]} C_\n' + \
                      f'Намнокии ҳаво: _{data["main"]["humidity"]}%_\n' + \
                      f'Суръати шамол: _{data["wind"]["speed"]} м/с_'
            return message
        else:
            return '_Шаҳри нодурустро навиштед. Номи шаҳрро аз назар гузаронида аз нав санҷед._'

    def print_weather_5days(self):
        url = f'https://api.openweathermap.org/data/2.5/forecast?q={self.city}&appid={self.api_key}&units=metric'

        response = requests.get(url)
        data = response.json()
        message = ''
        if data['cod'] != '404':
            forecasts = data['list']
            prev_date = 0
            message += f"Обу ҳаво дар шаҳри *{self.city}*:\n\n"
            for i in forecasts:
                date = i['dt_txt'].split()[0]
                if date != prev_date:
                    message += f'_{date}_\n'
                    message += f'_Температура:_ *{i["main"]["temp"]} C*\n'
                    message += f'_Намнокии ҳаво:_ *{i["main"]["humidity"]}%*\n'
                    message += f'_Суръати шамол:_ *{i["wind"]["speed"]} м/с*\n'
                    message += '\n\n'
                    prev_date = date

        else:
            message = '_Шаҳри нодурустро навиштед. Номи шаҳрро аз назар гузаронида аз нав санҷед._'


        return message


# city_name = input('Номи шаҳри худро нависед: ')
# obj = WeatherAssistant(city_name, api_key)
# obj.days()
# # print(obj.city)
