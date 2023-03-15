# у меня проблема с аккаунтом VK. Когда-то очень давно я с ними сильно поругался, еще на заре становления этого VK
import requests

class User:
    def __init__(self, user_id, token):
        self.user_id = user_id
        self.token = token
        self.name = ''
        self.surname = ''
        self.friends = []
        self.get_user_info()
        self.get_friends()
        
    def get_user_info(self):
        url = f'https://api.vk.com/method/users.get?user_ids={self.user_id}&fields=first_name,last_name&access_token={self.token}&v=5.131'
        response = requests.get(url)
        user_info = response.json()['response'][0]
        self.name = user_info['first_name']
        self.surname = user_info['last_name']
        
    def get_friends(self):
        url = f'https://api.vk.com/method/friends.get?user_id={self.user_id}&access_token={self.token}&v=5.131'
        response = requests.get(url)
        self.friends = [User(user_id, self.token) for user_id in response.json()['response']['items']]
        
    def __and__(self, other):
        common_friends = [friend for friend in self.friends if friend in other.friends]
        return common_friends
    
# установка токена
token = '10b2e6b1a90a01875cfaa0d2dd307b7a73a15ceb1acf0c0f2a9e9c586f3b597815652e5c28ed8a1baf13c'

# создание экземпляров класса для двух пользователей
user1 = User('1', token)
user2 = User('2', token)

# поиск общих друзей
common_friends = user1 & user2

# вывод общих друзей
if common_friends:
    print(f'Общие друзья пользователей {user1.name} {user1.surname} и {user2.name} {user2.surname}:')
    for friend in common_friends:
        print(friend.name, friend.surname)
else:
    print('У пользователей нет общих друзей.')