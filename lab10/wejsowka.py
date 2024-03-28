import requests


def load_from_link():
    link = "https://api.edamam.com/search?q=Z&app_id=X&app_key=Y"
    data = requests.get(link).json()
    return data


komentarze: 
#fix me - jest bug i trzeba naprawić 
#to do - 