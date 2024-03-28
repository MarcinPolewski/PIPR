import requests

result = requests.get("https://api.gios.gov.pl/pjp-api/rest/station/findAll")
print(result)
print(result.text)  # zwraca dane jako test
result.json()  # dostajemy dane bezpośrednio jako dane pythonowe
result = requests.get("asdfasdfasdf")
print("test")
