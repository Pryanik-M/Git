import requests
from distance import lonlat_distance


# Севастопольская улица, 4, Арзамас, Нижегородская область
# улица Пушкина, 138/1, Арзамас, Нижегородская область
geocoder_api_server = 'http://geocode-maps.yandex.ru/1.x/'
search_api_server = 'https://search-maps.yandex.ru/v1/'
static_api_server = 'https://static-maps.yandex.ru/v1'

geocoder_apikey = '8013b162-6b42-4997-9691-77b7074026e0'
search_apikey = 'dda3ddba-c9ea-4ead-9010-f43fbc15c6e3'
static_apikey = 'f3a0fe3a-b07e-4840-a1da-06f18b2ddf13'

geocoder_params_home = {
    'apikey': geocoder_apikey,
    'geocode': input('Введите адрес места проживания: '),
    'format': 'json'
}

geocode_response_home = requests.get(geocoder_api_server, params=geocoder_params_home)
if not geocode_response_home:
    print('Ошибка geocode')

json_geocode = geocode_response_home.json()
print(json_geocode)

coord_geocode = json_geocode['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
long_home, lat_home = coord_geocode.split()

geocoder_params_school = {
    'apikey': geocoder_apikey,
    'geocode': input('Введите адрес учебного заведения: '),
    'format': 'json'
}

geocode_response_school = requests.get(geocoder_api_server, params=geocoder_params_school)
if not geocode_response_school:
    print('Ошибка geocode')

json_geocode = geocode_response_school.json()
print(json_geocode)

coord_geocode = json_geocode['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
long_school, lat_school = coord_geocode.split()

print(lonlat_distance((float(long_home), float(lat_home)), (float(long_school), float(lat_school))))