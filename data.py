from helpers import *


class UsersData:
    email = 'lubitelburgerov@yandex.ru'
    password = 'plokij'
    username = 'Donald'

    credentials_with_empty_field = [
        {'email': '',
         'password': create_random_password(),
         'name': create_random_username()
         },
        {'email': create_random_email(),
         'password': '',
         'name': create_random_username()
         },
        {'email': create_random_email(),
         'password': create_random_password(),
         'name': ''
         }
    ]

class IngredientData:
    #correct_ingredients_hash_data = {  # Корректные хеши ингредиентов
        #"ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]
    #}
   # incorrect_ingredients_hash_data = {  # Несуществующие хеши ингредиентов
       # "ingredients": ["69d5b44abracadabaraf6a76", "609646e4daboradabara2870"]
   # }
   #empty_ingredients_data = {  # Null ингредиенты
       # "ingredients": []
   #}


    burger_1 = ['60d3b41abdacab0026a733c6', '609646e4dc916e00276b2870',
                '61c0c5a71d1f82001bdaaa76', '61c0c5a71d1f82001bdaaa79']

    burger_2 = ['61c0c5a71d1f82001bdaaa74', '61c0c5a71d1f82001bdaaa6d',
                '61c0c5a71d1f82001bdaaa7a', '61c0c5a71d1f82001bdaaa6f']

    invalid_hash_ingredient = '609646e4daboradabara2870'