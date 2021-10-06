import json

import requests

# Task_1

user = 'IgoryanM'
user_repos = requests.get(f'https://api.github.com/users/{user}/repos')

with open('task_1.json', 'w') as f:
    json.dump(json.loads(user_repos.text), f, indent=5)

# Task_2
# https://openweathermap.org/current

appid = '6ee88d9139454843550e7c8fa1f335f8'
city_name = 'Saint Petersburg'

weather = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={appid}&units=metric')
print(weather.text)
with open('task_2.json', 'w') as f:
    json.dump(json.loads(weather.text), f, indent=5)
