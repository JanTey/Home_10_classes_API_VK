# у меня проблема с аккаунтом VK. Когда-то очень давно я с ними сильно поругался, еще на заре становления этого VK
import requests

class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def get_friends(self, access_token):
        """
        Получает список друзей пользователя
        :param access_token: токен доступа VK API
        :return: список друзей пользователя в виде списка идентификаторов
        """
        url = 'https://api.vk.com/method/friends.get'
        params = {
            'user_id': self.user_id,
            'access_token': access_token,
            'v': '5.131'
        }
        response = requests.get(url, params=params)
        friends = response.json()['response']['items']
        return friends

    def get_common_friends(self, other_user, access_token):
        """
        Получает список общих друзей с другим пользователем
        :param other_user: другой пользователь, объект класса User
        :param access_token: токен доступа VK API
        :return: список общих друзей с другим пользователем в виде списка идентификаторов
        """
        my_friends = set(self.get_friends(access_token))
        other_friends = set(other_user.get_friends(access_token))
        common_friends = list(my_friends.intersection(other_friends))
        return common_friends
    
""" user1 = User('12345678')
user2 = User('87654321')
common_friends = user1.get_common_friends(user2, '10b2e6b1a90a01875cfaa0d2dd307b7a73a15ceb1acf0c0f2a9e9c586f3b597815652e5c28ed8a1baf13c')
print(common_friends) """    

#Пользователя нужно описать с помощью класса и реализовать метод поиска общих друзей, используя API VK. Ссылка на документацию VK/dev. Токен для запросов: 10b2e6b1a90a01875cfaa0d2dd307b7a73a15ceb1acf0c0f2a9e9c586f3b597815652e5c28ed8a1baf13c
#Поиск общих друзей должен происходить с помощью оператора &, т.е. user1 & user2 должен выдать список общих друзей пользователей user1 и user2, в этом списке должны быть экземпляры классов.