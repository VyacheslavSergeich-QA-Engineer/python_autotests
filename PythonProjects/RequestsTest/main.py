import requests #{"id":"6175","message":"Покемон создан"}

token = '421fa56e7007559add279f9c798f4675'

'''responce = requests.post('https://api.pokemonbattle.me:9104/pokemons', json = {
    "name": "sdfhdfgjdhj",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}, headers = {'Content-Type' : 'application/json' , 'trainer_token' : 
              token } )

print(responce.text)''' # создать покемона

'''responce_change = requests.put('https://api.pokemonbattle.me:9104/pokemons', json = {
    "pokemon_id": "6175",
    "name": "asdasdasd",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}, headers = {'Content-Type' : 'application/json' , 'trainer_token' : 
              token } )

print(responce_change.text)''' # переименовать покемона

'''responce_gacha = requests.post('https://api.pokemonbattle.me:9104//trainers/add_pokeball', json = {
    "pokemon_id": "6175"
}, headers = {'Content-Type' : 'application/json' , 'trainer_token' : 
              token } )

print(responce_gacha.text)''' # поймать покемона