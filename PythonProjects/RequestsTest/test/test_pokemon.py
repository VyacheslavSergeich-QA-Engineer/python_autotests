import requests
import pytest

host = 'https://api.pokemonbattle.me:9104'
id = '1934'

def test_status_code():
    response = requests.get('host/trainers')
    assert response.status_code == 200


def test_status_code():
    response = requests.get(f'{ host }/trainers' , params = {'trainer_name' : 'asdasdasd'})
    assert response.status_code == 200