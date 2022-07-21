import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
token="токен" # token
bh = vk_api.VkApi(token = token)
give = bh.get_api()
longpoll = VkLongPoll(bh)
def blasthack(id, text):
    bh.method('messages.send', {'user_id' : id, 'message' : text, 'random_id': 0})
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
      # Чтобы наш бот не слышал и не отвечал на самого себя
       if event.to_me:

        # Для того чтобы бот читал все с маленьких букв 
          message = event.text.lower()
          # Получаем id пользователя
          id = event.user_id

          if message == 'привет':
            blasthack(id, 'Привет!')

          elif message == 'как дела?':
              blasthack(id, 'Хорошо, а твои как?' )

          else:
             blasthack(id, 'Команда не найдена!')
