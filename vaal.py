import  requests

valcode = input('Введіть валюту:')


respource = requests.get("https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?date=20120302&json")


data = respource.json()


print(data)

print(data[0]['rate'])