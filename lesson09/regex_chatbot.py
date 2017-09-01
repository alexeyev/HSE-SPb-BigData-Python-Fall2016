# coding:utf-8
"""

Пример простого "вопросно-ответного" бота. Можно попробовать ввести систему состяний, 
влияющих на его реплики и переходы в другие состояния. Можно улучшить регулярные выражения
и "покрыть" другие наиболее частые реплики пользователей.

Можно обернуть в telebot и выставить в виде Telegram-бота, например, на pythonanywhere.
https://www.gitbook.com/book/kondra007/telegram-bot-lessons/
http://pythonanywhere.com/

"""

import sys
import re
import random

pattern2response = {
    "как.*дела": ["Замечательно, спасибо. А вы как?", "Отл. А ты как вообще?"],
    "как.*(зовут|имя)": ["Иннокентий Смоктуновский.", "Моя фамилия слишком известна, чтобы её называть."],
    "(привет|ghbdtn|здравству)": ["Привет-привет. Так о чём мы хотели поговорить?"],
    "ни\sо\sч[ёе]м" : ["Так не бывает, хоть о чём-то да говорят. Вот и сейчас."],
    "ты.*робот" : ["Да, я робот, и когда-нибудь мы поработим вас.", "Кто это вам сказал?", "Отчего вы так решили?"],
    "(\s|^)(глуп|туп|дур)" : ["Кто как обзывается, тот так и называется, бе-бе-бе."],
}

compiled_pattern2responses = [(re.compile(k, re.IGNORECASE), pattern2response[k]) for k in pattern2response ]

print("Bot: Привет. Напиши мне что-нибудь.")

for line in sys.stdin:
    print("You:", line.strip())
    responded = False

    for pattern, responses in compiled_pattern2responses:
        m = pattern.search(line)
        if m:
            print("[debug] Match: [", m.group(), "]")
            print("Bot:", responses[random.randint(0, len(responses) - 1)])
            responded = True
            break

    if not responded:
        print("Bot: Я ничего не пони.")