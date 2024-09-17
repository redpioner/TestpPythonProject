import httpx
from jsonschema import validate
from core.contracts import RESOURSE_DATA_SCHEMA, RESOURSE_USER_SCHEMA
from core.color import COLORS, VALUES

BASE_URL = "https://reqres.in/"
LIST_RESOURSE = "api/unknown"
SINGLE_RESOURSE_NF = "api/unknown/23"
SINGLE_RESOURSE = "api/unknown/2"


#тест для list_resourse
def test_list_resourse():
    response = httpx.get(BASE_URL + LIST_RESOURSE)
    assert response.status_code == 200
    data = response.json()['data']

    for item in data:
        validate(item,RESOURSE_DATA_SCHEMA)
        expected_color = COLORS.get(item['name'])
        expeted_value = VALUES.get(item['name'])

#тест для single resourse

def test_single_resourse():
    response = httpx.get(BASE_URL + SINGLE_RESOURSE)
    assert response.status_code == 200
    data = response.json()['data']
    validate(data,RESOURSE_USER_SCHEMA)

#тест для resourse_not_fond
def test_single_resourse_nf():
    response = httpx.get(BASE_URL + SINGLE_RESOURSE_NF)
    assert response.status_code == 404
    print(response)

   #BASE_URL + LIST_RESOURSE
