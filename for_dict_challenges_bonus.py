"""
Пожалуйста, приступайте к этой задаче после того, как вы сделали и получили ревью ко всем остальным задачам
в этом репозитории. Она значительно сложнее.


Есть набор сообщений из чата в следующем формате:

```
messages = [
    {
        "id": "efadb781-9b04-4aad-9afe-e79faef8cffb",
        "sent_at": datetime.datetime(2022, 10, 11, 23, 11, 11, 721),
        "sent_by": 46,  # id пользователя-отправителя
        "reply_for": "7b22ae19-6c58-443e-b138-e22784878581",  # id сообщение, на которое это сообщение является ответом (может быть None)
        "seen_by": [26, 91, 71], # идентификаторы пользователей, которые видели это сообщение
        "text": "А когда ревью будет?",
    }
]
```

Так же есть функция `generate_chat_history`, которая вернёт список из большого количества таких сообщений.
Установите библиотеку lorem, чтобы она работала.

Нужно:
1. Вывести айди пользователя, который написал больше всех сообщений.
2. Вывести айди пользователя, на сообщения которого больше всего отвечали.
3. Вывести айди пользователей, сообщения которых видело больше всего уникальных пользователей.
4. Определить, когда в чате больше всего сообщений: утром (до 12 часов), днём (12-18 часов) или вечером (после 18 часов).
5. Вывести идентификаторы сообщений, который стали началом для самых длинных тредов (цепочек ответов).

Весь код стоит разбить на логические части с помощью функций.
"""
from collections import defaultdict, Counter

import random
import uuid
import datetime

import lorem




class ChatHistory:
    def __init__(self):
        self.chat_history = self.generate_chat_history()

    def __repr__(self):
        return f"<Format x {self.chat_history}"
    
    def generate_chat_history(self):
        messages_amount = random.randint(200, 1000)
        users_ids = list(
            {random.randint(1, 10000) for _ in range(random.randint(5, 20))}
        )
        sent_at = datetime.datetime.now() - datetime.timedelta(days=100)
        messages = []
        for _ in range(messages_amount):
            sent_at += datetime.timedelta(minutes=random.randint(0, 240))
            messages.append({
                "id": uuid.uuid4(),
                "sent_at": sent_at,
                "sent_by": random.choice(users_ids),
                "reply_for": random.choice(
                    [
                        None,
                        (
                            random.choice([m["id"] for m in messages])
                            if messages else None
                        ),
                    ],
                ),
                "seen_by": random.sample(users_ids,
                                         random.randint(1, len(users_ids))),
                "text": lorem.sentence(),
            })
        return messages
    
    def get_reply_to_message(self):
        reply_to_message = defaultdict(list)
        for message in self.chat_history:
            if message["reply_for"] is not None:
                reply_to_message[message["reply_for"]].append(message["id"])
        return reply_to_message
    
    def get_first_messages(self):
        return [message["id"] for message in self.chat_history if message["reply_for"] is None]
    
    def find_message_for_reply(self, reply_id, dict_reply_message, num_message): 
        count_message = int()
        if dict_reply_message.get(reply_id) is not None:
            for message in dict_reply_message.get(reply_id):
                count_message += self.find_message_for_reply(message, dict_reply_message, num_message+1) 
            return count_message + 1
        return 1

    def find_longest_conversation(self):
        reply_to_message = self.get_reply_to_message()
        first_messages = self.get_first_messages()

        max_len = 0
        max_messages_id = []
        for first_message in first_messages:
            len_conversation = self.find_message_for_reply(first_message, reply_to_message, 0)
            if (len_conversation > max_len):
                max_len = len_conversation
                max_messages_id = [first_message]
            elif len_conversation == max_len:
                max_messages_id.append(first_message)
        return max_messages_id
    
    def find_popular_daypart(self):
        popular_hours = defaultdict(int)
        for message in self.chat_history:
            hour = int(message["sent_at"].strftime("%-H"))
            if hour < 12:
                part_day = "утром"
            elif hour <18:
                part_day = "днём"
            else:
                part_day = "вечером"
            popular_hours[part_day] +=1
        return popular_hours
    
    def find_user_id(self, message_id):
        for message in self.chat_history:
            if message["id"] == message_id:
                return message["sent_by"] 
        return None
    
    def find_statistic_user_id(self):
        statistic_user = defaultdict(list) # user_id: [count_message, count_seen_by, count_answer] 
        for message in self.chat_history:
            user_id = message["sent_by"]
            if statistic_user.get(user_id) is not None:
                statistic_user[user_id][0] += 1
                statistic_user[user_id][1] = max(statistic_user[user_id][1], len(set(message["seen_by"])))
            else:
                statistic_user[user_id] = [0, 0, 0]
                statistic_user[user_id][0] = 1
                statistic_user[user_id][1] = len(set(message["seen_by"]))
            if message["reply_for"] is not None:
                user_from_reply_for = self.find_user_id(message["reply_for"])
                if user_from_reply_for is not None:
                    if statistic_user.get(user_from_reply_for) is not None:
                        statistic_user[user_from_reply_for][2] += 1
                    else:
                        statistic_user[user_from_reply_for] = [0, 0, 0] 
                        statistic_user[user_from_reply_for][2] = 1
        return statistic_user




def most_often_object_in_dict(objects, place = None):
    often_object = list()
    often_id = 0
    for key, val in objects.items():
        if place is not None:
            val = val[place]
        if often_id == 0 or often_id<val:
            often_object = [key]
            often_id = val
        elif often_id == val:
            often_object.append(key)
    return often_object


if __name__ == "__main__":
    history = ChatHistory()

    statistic = history.find_statistic_user_id()

    max_count_user_message = most_often_object_in_dict(statistic, 0)
    max_response_user_message = most_often_object_in_dict(statistic, 2)
    more_seen_by = most_often_object_in_dict(statistic, 1)
    popular_part_day = most_often_object_in_dict(history.find_popular_daypart())
    longest_conversation = history.find_longest_conversation()
    
    
    print(f"1. id пользователя, который написал больше всех сообщений - {max_count_user_message}")
    print(f"2. id пользователя, на сообщения которого больше всего отвечали - {max_response_user_message}" )
    print(f"3. id пользователей, сообщения которых видело больше всего уникальных пользователей - {more_seen_by}")
    print(f"4. Больше всего сообщений в чате - {popular_part_day[0]}")
    print(f"5. Идентификаторы первых сообщений с самыми длинными цепочками {longest_conversation}")

