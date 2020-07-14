from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.upload import VkUpload
import vk_api
from datetime import datetime
import requests
import random
import time
import get_pictures


token = "ea962f6ba831d72090552f917e3e263e44db759542cd3f91b441a789967b1b14ce1908d3318b011337c8c"
#token = "fa38c3e92052318b45b35f66933d19519d2ba01f6cd128e6458b3f00500fb9bed041fd05d18f6790c9753"
vk_session = vk_api.VkApi(token=token)

session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

def create_keyboard(response):
    keyboard = VkKeyboard(one_time=False)

    if response == 'начать':
        keyboard.add_button('Поступающим', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('Расписание звонков', color=VkKeyboardColor.DEFAULT)
        keyboard.add_button('Схема корпусов', color=VkKeyboardColor.DEFAULT)
        keyboard.add_line()
        keyboard.add_button('Общежития', color=VkKeyboardColor.DEFAULT)
        keyboard.add_button('Стипендии', color=VkKeyboardColor.DEFAULT)
        keyboard.add_line()
        keyboard.add_button('Задать вопрос специалисту', color=VkKeyboardColor.DEFAULT)


    elif response == 'поступающим':

        keyboard.add_button('Прием документов', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Необходимые документы', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()  # Переход на вторую строку
        keyboard.add_button('Сроки приема', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Вступительные испытания', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()
        keyboard.add_button('Бюджетные места', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Индивидуальные достижения', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()
        keyboard.add_button('Рейтинг поступающих', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Минимальные баллы', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()
        keyboard.add_button('Проходные баллы', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Калькулятор ЕГЭ', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()
        keyboard.add_button('Платное обучение', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Иностранным гражданам', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()
        keyboard.add_button('Вернуться в основное меню', color=VkKeyboardColor.NEGATIVE)


    elif response == 'прием документов':
        keyboard.add_button('Прием документов', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Необходимые документы', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()  # Переход на вторую строку
        keyboard.add_button('Сроки приема', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Вступительные испытания', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()
        keyboard.add_button('Бюджетные места', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Индивидуальные достижения', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()
        keyboard.add_button('Рейтинг поступающих', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Минимальные баллы', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()
        keyboard.add_button('Проходные баллы', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Калькулятор ЕГЭ', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()
        keyboard.add_button('Платное обучение', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Иностранным гражданам', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()
        keyboard.add_button('Вернуться в основное меню', color=VkKeyboardColor.NEGATIVE)

    elif response == 'необходимые документы':
        keyboard.add_button('Прием документов', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Необходимые документы', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()  # Переход на вторую строку
        keyboard.add_button('Сроки приема', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Вступительные испытания', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()
        keyboard.add_button('Бюджетные места', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Индивидуальные достижения', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()
        keyboard.add_button('Рейтинг поступающих', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Минимальные баллы', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()
        keyboard.add_button('Проходные баллы', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Калькулятор ЕГЭ', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()
        keyboard.add_button('Платное обучение', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Иностранным гражданам', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()
        keyboard.add_button('Вернуться в основное меню', color=VkKeyboardColor.NEGATIVE)

    elif response == 'сроки приема':
        keyboard.add_button('Бакалавриат, специалитет', color=VkKeyboardColor.DEFAULT)
        keyboard.add_button('Магистратура', color=VkKeyboardColor.DEFAULT)
        keyboard.add_line()
        keyboard.add_button('Вернуться в основное меню', color=VkKeyboardColor.NEGATIVE)


    elif response == 'вступительные испытания':
        keyboard.add_button('Прием документов', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Необходимые документы', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()  # Переход на вторую строку
        keyboard.add_button('Сроки приема', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Вступительные испытания', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()
        keyboard.add_button('Бюджетные места', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Индивидуальные достижения', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()
        keyboard.add_button('Рейтинг поступающих', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Минимальные баллы', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()
        keyboard.add_button('Проходные баллы', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Калькулятор ЕГЭ', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()
        keyboard.add_button('Платное обучение', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Иностранным гражданам', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()
        keyboard.add_button('Вернуться в основное меню', color=VkKeyboardColor.NEGATIVE)

    elif response == 'бюджетные места':
        keyboard.add_button('Прием документов', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Необходимые документы', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()  # Переход на вторую строку
        keyboard.add_button('Сроки приема', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Вступительные испытания', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()
        keyboard.add_button('Бюджетные места', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Индивидуальные достижения', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()
        keyboard.add_button('Рейтинг поступающих', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Минимальные баллы', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()
        keyboard.add_button('Проходные баллы', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Калькулятор ЕГЭ', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()
        keyboard.add_button('Платное обучение', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Иностранным гражданам', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()
        keyboard.add_button('Вернуться в основное меню', color=VkKeyboardColor.NEGATIVE)

    elif response == 'индивидуальные достижения':
        keyboard.add_button('Прием документов', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Необходимые документы', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()  # Переход на вторую строку
        keyboard.add_button('Сроки приема', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Вступительные испытания', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()
        keyboard.add_button('Бюджетные места', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Индивидуальные достижения', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()
        keyboard.add_button('Рейтинг поступающих', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Минимальные баллы', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()
        keyboard.add_button('Проходные баллы', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Калькулятор ЕГЭ', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()
        keyboard.add_button('Платное обучение', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Иностранным гражданам', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()
        keyboard.add_button('Вернуться в основное меню', color=VkKeyboardColor.NEGATIVE)

    elif response == 'рейтинг поступающих':
        keyboard.add_button('Прием документов', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Необходимые документы', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()  # Переход на вторую строку
        keyboard.add_button('Сроки приема', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Вступительные испытания', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()
        keyboard.add_button('Бюджетные места', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Индивидуальные достижения', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()
        keyboard.add_button('Рейтинг поступающих', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Минимальные баллы', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()
        keyboard.add_button('Проходные баллы', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Калькулятор ЕГЭ', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()
        keyboard.add_button('Платное обучение', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Иностранным гражданам', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()
        keyboard.add_button('Вернуться в основное меню', color=VkKeyboardColor.NEGATIVE)

    elif response == 'минимальные баллы':
        keyboard.add_button('Прием документов', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Необходимые документы', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()  # Переход на вторую строку
        keyboard.add_button('Сроки приема', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Вступительные испытания', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()
        keyboard.add_button('Бюджетные места', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Индивидуальные достижения', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()
        keyboard.add_button('Рейтинг поступающих', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Минимальные баллы', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()
        keyboard.add_button('Проходные баллы', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Калькулятор ЕГЭ', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()
        keyboard.add_button('Платное обучение', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Иностранным гражданам', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()
        keyboard.add_button('Вернуться в основное меню', color=VkKeyboardColor.NEGATIVE)

    elif response == 'проходные баллы':
        keyboard.add_button('Прием документов', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Необходимые документы', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()  # Переход на вторую строку
        keyboard.add_button('Сроки приема', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Вступительные испытания', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()
        keyboard.add_button('Бюджетные места', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Индивидуальные достижения', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()
        keyboard.add_button('Рейтинг поступающих', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Минимальные баллы', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()
        keyboard.add_button('Проходные баллы', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Калькулятор ЕГЭ', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()
        keyboard.add_button('Платное обучение', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Иностранным гражданам', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()
        keyboard.add_button('Вернуться в основное меню', color=VkKeyboardColor.NEGATIVE)

    elif response == 'калькулятор егэ':
        keyboard.add_button('Прием документов', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Необходимые документы', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()  # Переход на вторую строку
        keyboard.add_button('Сроки приема', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Вступительные испытания', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()
        keyboard.add_button('Бюджетные места', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Индивидуальные достижения', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()
        keyboard.add_button('Рейтинг поступающих', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Минимальные баллы', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()
        keyboard.add_button('Проходные баллы', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Калькулятор ЕГЭ', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()
        keyboard.add_button('Платное обучение', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Иностранным гражданам', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()
        keyboard.add_button('Вернуться в основное меню', color=VkKeyboardColor.NEGATIVE)

    elif response == 'платное обучение':
        keyboard.add_button('Прием документов', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Необходимые документы', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()  # Переход на вторую строку
        keyboard.add_button('Сроки приема', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Вступительные испытания', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()
        keyboard.add_button('Бюджетные места', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Индивидуальные достижения', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()
        keyboard.add_button('Рейтинг поступающих', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Минимальные баллы', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()
        keyboard.add_button('Проходные баллы', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Калькулятор ЕГЭ', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()
        keyboard.add_button('Платное обучение', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Иностранным гражданам', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()
        keyboard.add_button('Вернуться в основное меню', color=VkKeyboardColor.NEGATIVE)

    elif response == 'иностранным гражданам':
        keyboard.add_button('Прием документов', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Необходимые документы', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()  # Переход на вторую строку
        keyboard.add_button('Сроки приема', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Вступительные испытания', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()
        keyboard.add_button('Бюджетные места', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Индивидуальные достижения', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()
        keyboard.add_button('Рейтинг поступающих', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Минимальные баллы', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()
        keyboard.add_button('Проходные баллы', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Калькулятор ЕГЭ', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()
        keyboard.add_button('Платное обучение', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Иностранным гражданам', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()
        keyboard.add_button('Вернуться в основное меню', color=VkKeyboardColor.NEGATIVE)

    elif response == 'бакалавриат, специалитет':
        keyboard.add_button('Прием документов', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Необходимые документы', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()  # Переход на вторую строку
        keyboard.add_button('Сроки приема', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Вступительные испытания', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()
        keyboard.add_button('Бюджетные места', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Индивидуальные достижения', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()
        keyboard.add_button('Рейтинг поступающих', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Минимальные баллы', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()
        keyboard.add_button('Проходные баллы', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Калькулятор ЕГЭ', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()
        keyboard.add_button('Платное обучение', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Иностранным гражданам', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()
        keyboard.add_button('Вернуться в основное меню', color=VkKeyboardColor.NEGATIVE)
    elif response == 'магистратура':
        keyboard.add_button('Прием документов', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Необходимые документы', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()  # Переход на вторую строку
        keyboard.add_button('Сроки приема', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Вступительные испытания', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()
        keyboard.add_button('Бюджетные места', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Индивидуальные достижения', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()
        keyboard.add_button('Рейтинг поступающих', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Минимальные баллы', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()
        keyboard.add_button('Проходные баллы', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Калькулятор ЕГЭ', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()
        keyboard.add_button('Платное обучение', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Иностранным гражданам', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()
        keyboard.add_button('Вернуться в основное меню', color=VkKeyboardColor.NEGATIVE)

    elif response == 'вернуться в основное меню':
        keyboard.add_button('Поступающим', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('Расписание звонков', color=VkKeyboardColor.DEFAULT)
        keyboard.add_button('Схема корпусов', color=VkKeyboardColor.DEFAULT)
        keyboard.add_line()
        keyboard.add_button('Общежития', color=VkKeyboardColor.DEFAULT)
        keyboard.add_button('Стипендии', color=VkKeyboardColor.DEFAULT)
        keyboard.add_line()
        keyboard.add_button('Задать вопросы специалисту', color=VkKeyboardColor.DEFAULT)

    elif response == 'задать вопросы специалисту':
        keyboard.add_button('Начать', color=VkKeyboardColor.DEFAULT)

    elif response == "расписание звонков":
        keyboard.add_button('Поступающим', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('Расписание звонков', color=VkKeyboardColor.DEFAULT)
        keyboard.add_button('Схема корпусов', color=VkKeyboardColor.DEFAULT)
        keyboard.add_line()
        keyboard.add_button('Общежития', color=VkKeyboardColor.DEFAULT)
        keyboard.add_button('Стипендии', color=VkKeyboardColor.DEFAULT)
        keyboard.add_line()
        keyboard.add_button('Задать вопросы специалисту', color=VkKeyboardColor.DEFAULT)

    elif response == "схема корпусов":
        keyboard.add_button('Поступающим', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('Расписание звонков', color=VkKeyboardColor.DEFAULT)
        keyboard.add_button('Схема корпусов', color=VkKeyboardColor.DEFAULT)
        keyboard.add_line()
        keyboard.add_button('Общежития', color=VkKeyboardColor.DEFAULT)
        keyboard.add_button('Стипендии', color=VkKeyboardColor.DEFAULT)
        keyboard.add_line()
        keyboard.add_button('Задать вопросы специалисту', color=VkKeyboardColor.DEFAULT)

    elif response == "общежития":
        keyboard.add_button('Поступающим', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('Расписание звонков', color=VkKeyboardColor.DEFAULT)
        keyboard.add_button('Схема корпусов', color=VkKeyboardColor.DEFAULT)
        keyboard.add_line()
        keyboard.add_button('Общежития', color=VkKeyboardColor.DEFAULT)
        keyboard.add_button('Стипендии', color=VkKeyboardColor.DEFAULT)
        keyboard.add_line()
        keyboard.add_button('Задать вопросы специалисту', color=VkKeyboardColor.DEFAULT)

    elif response == "стипендии":
        keyboard.add_button('Поступающим', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('Расписание звонков', color=VkKeyboardColor.DEFAULT)
        keyboard.add_button('Схема корпусов', color=VkKeyboardColor.DEFAULT)
        keyboard.add_line()
        keyboard.add_button('Общежития', color=VkKeyboardColor.DEFAULT)
        keyboard.add_button('Стипендии', color=VkKeyboardColor.DEFAULT)
        keyboard.add_line()
        keyboard.add_button('Задать вопросы специалисту', color=VkKeyboardColor.DEFAULT)

    keyboard = keyboard.get_keyboard()
    return keyboard


def send_message(vk_session, id_type, id, message=None, attachment=None, keyboard=None):
    vk_session.method('messages.send', {id_type: id, 'message': message, 'random_id': random.randint(-2147483648, +2147483648), "attachment": attachment, 'keyboard': keyboard})


upload = vk_api.VkUpload(vk_session)

photo = upload.photo_messages('JZIHitK5yJM.jpg')
owner_id = photo[0]['owner_id']
photo_id = photo[0]['id']
access_key = photo[0]['access_key']
attachment1 = f'photo{owner_id}_{photo_id}_{access_key}'





for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        print('Сообщение пришло в: ' + str(datetime.strftime(datetime.now(), "%H:%M:%S")))
        print('Текст сообщения: ' + str(event.text))
        print(event.user_id)
        response = event.text.lower()
        keyboard = create_keyboard(response)

        if event.from_user and not event.from_me:
            if response == "начать":
                send_message(vk_session, 'user_id', event.user_id, message='Нажми на кнопку, чтобы получить список команд',keyboard=keyboard)
            elif response == "поступающим":
                send_message(vk_session, 'user_id', event.user_id, message= 'Приемная комиссия ЧГУ \n \n abiturient.chuvsu.ru \n vk.com/priemkomchgu ',keyboard=keyboard)
            elif response == "прием документов":
                send_message(vk_session, 'user_id', event.user_id, message= 'Прием документов от поступающих осуществляется: \n 💻 в электронном виде, через Личный кабинет абитуриента на сайте приемной комиссии https://priem.chuvsu.ru/ \n ✉ в бумажном виде через операторов почтовой связи общего пользования на адрес: 428015, Чувашская Республика, г. Чебоксары, Московский проспект, 15, Приемная комиссия. \n Рекомендуем воспользоваться Личным кабинетом, в котором вы можете внести свои данные, загрузить необходимые документы, выбрать интересующие направления подготовки, специальности. \n  ❗ Напоминаем, что абитуриент может подать документы не более чем в 5 вузов и в каждом участвовать в конкурсе на бюджетные места не более чем по 3 специальностям, направлениям подготовки.',keyboard=keyboard)
            elif response == "необходимые документы":
                send_message(vk_session, 'user_id', event.user_id, message= 'Документы загружаются в Личный кабинет в формате pdf или jpg, размером не более 3 Мб каждый: \n 1. Фото или скан паспорта (стр. 2-3 + стр. с регистрацией + стр. с данными предыдущего паспорта). \n 2. Фото или скан аттестата о среднем общем образовании с приложением или диплома о среднем профессиональном (высшем, высшем профессиональном) образовании с приложением. \n 3. Фото или сканы документов, подтверждающих индивидуальные достижения (при наличии). 4. Фото или сканы документов, подтверждающих право на поступление в пределах особой квоты (при наличии). \n 5. Фото или скан документа, подтверждающего право на поступление в пределах целевой квоты (при наличии). \n 6. Фото или скан документа, подтверждающего право на поступление без испытаний (при наличии). \n 7.Медицинская справка (для поступающих на направления подготовки: «Теплоэнергетика и теплотехника», «Электроэнергетика и электротехника», «Теплоэнергетика и теплотехника», «Электроэнергетика и электротехника», «Наземные транспортно-технологические комплексы», «Сестринское дело», «Психолого-педагогическое образование», специальности: «Радиоэлектронные системы и комплексы», «Лечебное дело», «Педиатрия», «Стоматология», «Фармация»). \n ❗ Оригинал документа об образовании (аттестата, диплома) и медицинская справка предоставляются в университет в течение первого года обучения.',keyboard=keyboard)
            elif response == "сроки приема":
                send_message(vk_session, 'user_id', event.user_id, message= 'Сроки начала и завершения приема документов, проведения вступительных испытаний и зачисления зависят от интересующего вас уровня образования. Выберите нужный уровень.', keyboard=keyboard)
            elif response == "вступительные испытания":
                send_message(vk_session, 'user_id', event.user_id, message='🔹 Бакалавриат, специалитет – прием по результатам ЕГЭ 2016-2020 гг. (для выпускников школ) или по результатам внутренних вступительных испытаний в вузе (для выпускников ссузов, вузов). \n На направлениях «Дизайн», «Журналистика» и всех направлениях факультета искусств предусмотрены дополнительные внутренние испытания творческой (профессиональной) направленности. Полный перечень на сайте приемной комиссии vk.cc/aw2HU0 \n 🔹 Магистратура – прием по результатам междисциплинарного экзамена по выбранному профилю. \n 🔹 Ординатура – прием по результатам тестирования. \n 🔹 Аспирантура – прием по результатам экзамена по специальной дисциплине.', keyboard=keyboard)
            elif response == "бюджетные места":
                send_message(vk_session, 'user_id', event.user_id, message='В 2020 году в ЧувГУ всего выделено 1669 бюджетных мест. Из них: \n 🔹 бакалавриат, специалитет – 1360 мест, \n 🔹 магистратура – 185 мест, \n 🔹 ординатура – 99 мест, \n 🔹 аспирантура – 25 мест. \n  Для уточнения бюджетных мест по направлениям, специальностям напишите нам 👇', keyboard=keyboard)
            elif response == "индивидуальные достижения":
                send_message(vk_session, 'user_id', event.user_id, message='Максимальная сумма баллов за результаты индивидуальных достижений – 10 баллов. \n Перечень индивидуальных достижений определен вузом, в него входят: академические успехи, олимпиады и конкурсы, спортивные достижения, волонтерская деятельность, дополнительное образование.', keyboard=keyboard)
            elif response == "рейтинг поступающих":
                send_message(vk_session, 'user_id', event.user_id, message='📝 На основании поданных абитуриентами документов формируется список поступающих (рейтинг). Список формируется отдельно на каждое направление, специальность с учетом формы обучения (очная, очно-заочная, заочная). Обновление происходит в режиме онлайн. \n ⬇ Поступающие располагаются в порядке убывания баллов - от высшего до самого маленького. \n При этом они сгруппированы по категориям: \n - без испытаний, \n - особые права, \n - целевой прием, \n - на общих основаниях, \n - по контракту. \n ❗ Напоминаем, что в конкурсе на бюджетные места участвуют только те абитуриенты, которые оформили заявление о согласии на зачисление в установленные сроки. \n Ссылка на рейтинг поступающих vk.cc/9z1t5I', keyboard=keyboard)
            elif response == "минимальные баллы":
                send_message(vk_session, 'user_id', event.user_id, message='Минимальные баллы – это пороговые значения вступительных испытаний, позволяющие претендовать на поступление в вуз. С результатами ниже минимальных баллов поступающий не может быть принят в вуз, даже на платное обучение. \n 🔷 Бакалавриат, специалитет: \n Русский язык, Физика, География, История, Биология, Химия, Литература, Иностранный язык – 40 баллов \n Математика – 39 баллов \n Обществознание – 45 баллов \n Русский язык, Биология, Химия (на специальности «Лечебное дело», «Педиатрия», «Стоматология», «Сестринское дело», «Фармация») – 43 балла \n Рисунок, Живопись, Сочинение, Теория музыки, Музыкальная специальность – 50 баллов \n 🔶 Магистратура, ординатура, аспирантура: \n Междисциплинарный экзамен, тестирование, экзамен по специальности – 50 баллов', keyboard=keyboard)
            elif response == "проходные баллы":
                send_message(vk_session, 'user_id', event.user_id, message='Проходные баллы представляют собой итоги прошлогоднего приема на бюджет, они не являются гарантией зачисления в текущем году. Проходной балл определяется отдельно по каждому направлению подготовки, специальности. \n Чтобы узнать проходные баллы 2019 года напишите нам 👇', keyboard=keyboard)
            elif response == "калькулятор егэ":
                send_message(vk_session, 'user_id', event.user_id, message='Специально для абитуриентов в ЧувГУ создан онлайн-сервис «Калькулятор ЕГЭ». Введите свои реальные или предполагаемые баллы ЕГЭ по предметам и сервис подберет подходящие направления, специальности. По каждому приводится описание, проходные баллы и бюджетные места за несколько лет, что поможет оценить шансы на поступление и принять верное решение. \n Ссылка на ресурс https://profchgu.ru/kalkulyator-ege', keyboard=keyboard)
            elif response == "платное обучение":
                send_message(vk_session, 'user_id', event.user_id, message='📄 Основанием для платного обучения является договор об образовании. Заказчиком, оплачивающим обучение, может быть сам обучающийся (в случае достижения совершеннолетия) или его законный представитель (родитель или доверенное лицо). Договор оформляется через Личный кабинет абитуриента в электронном виде. \n Для зачисления необходимо произвести оплату в размере не менее 10% от годовой стоимости обучения.  \n ❗ Исходя из среднего балла результатов ЕГЭ или внутренних экзаменов (без учета индивидуальных достижений) предоставляется скидка: \n 60-70 баллов – 7% \n 71-80 баллов – 10% \n 81 балл и выше – 20% \n \n Контакты Отдела по работе со студентами, обучающимися на договорной основе:  \n тел. +7 (8352) 58-11-46, 45-26-91 (доб. 2067), e-mail: market120@chuvsu.ru ', keyboard=keyboard)
            elif response == "иностранным гражданам":
                send_message(vk_session, 'user_id', event.user_id, message='Организационно-визовый сектор (оформление визовых документов): \n Тел. +7(8352) 58-05-56 \n e-mail: decinstud@chuvsu.ru \n Адрес: г. Чебоксары Московский пр., 15, каб. К-404 \n \n Отдел международного образования (поступление) \n Тел. +7(8352) 45-26-85, +79030633606 \n e-mail: mezhotd301@mail.ru \n Адрес: г. Чебоксары Московский пр., 15, каб. К-403 \n \n Organization and Visa Sector: \n K-404 \n Phone number: +7(8352) 58-05-56 \n e-mail: decinstud@chuvsu.ru \n Address: Moskovsky Prospect, 15, К-404 \n \n International Education Office: \n K-404 \n Phone number: +7(8352) 45-26-85, +79030633606 \n e-mail: mezhotd301@mail.ru \n Address: Moskovsky Prospect, 15, К-403', keyboard=keyboard)
            elif response == "бакалавриат, специалитет":
                send_message(vk_session, 'user_id', event.user_id, message= '🔵 ОЧНАЯ И ОЧНО-ЗАОЧНАЯ ФОРМА: \n 20 июня – начало приема документов. \n ❗ 3 августа – завершение приема документов от поступающих по результатам внутренних вступительных испытаний (на бюджет и платно). \n 4-18 августа – проведение внутренних вступительных испытаний. \n ❗ 18 августа – завершение приема документов от поступающих по результатам ЕГЭ. \n 19 августа – размещение рейтинга (списка поступающих) на сайте. \n 🔶 Приоритетное зачисление (без вступительных испытаний, в пределах особой квоты, целевой квоты): \n 20-21 августа – прием заявлений о согласии на зачисление. \n 22 августа – издание приказа о зачислении. \n Зачисление по общему конкурсу проходит в два этапа: \n 🔶 Первый этап – заполнение 80% основных конкурсных мест: \n22-23 августа – прием заявлений о согласии на зачисление, \n24 августа – издание приказа о зачислении. \n 🔶 Второй этап – заполнение до 100% основных конкурсных мест: \n 24-25 августа – прием заявлений о согласии на зачисление, \n 26 августа – издание приказа о зачислении. \n 29 августа – завершение приема документов от поступающих на платное обучение по результатам ЕГЭ. \n 🔵 ЗАОЧНАЯ ФОРМА: \n 20 июня – начало приема документов. \n 27 августа – завершение приема документов на бюджетные места. \n 28-29 августа – проведение вступительных испытаний. \n 27 октября – завершение приема документов на платное обучение.', keyboard=keyboard)
            elif response == "магистратура":
                send_message(vk_session, 'user_id', event.user_id, message= '20 июня – начало приема документов. \n 10 августа – завершение приема документов на бюджетные места. \n 11-13 августа – вступительные испытания (междисциплинарный экзамен). \n 14 августа – размещение рейтинга (списка поступающих) на сайте. \n 17 августа – завершение приема заявлений о согласии на зачисление. \n 18 августа – издание приказа о зачислении. \n 27 августа – завершение приема документов на платное обучение. \n 28-29 августа – вступительные испытания на платное обучение. \n 27 октября – завершение приема документов на платное обучение.', keyboard=keyboard)
            elif response == "расписание звонков":
                send_message(vk_session, 'user_id', event.user_id, message= 'Расписание звонков 🔔 \n \n 1 пара 08.20 – 09.40 \n 2 пара 09.55 – 11.15 \n 3 пара 11.30 – 12.50 \n Большой перерыв \n 4 пара 13.20 – 14.40 \n 5 пара 14.55 – 16.15 \n 6 пара 16.30 – 17.50 \n 7 пара 18.05 – 19.25 \n 8 пара 19.40 – 21.00', keyboard=keyboard)
            elif response == "схема корпусов":
                send_message(vk_session, 'user_id', event.user_id, message= '📚 "Новый корпус" (ул. Университетская, 38) — Научная библиотека, Дворец культуры, Учебно-спортивный комплекс, факультеты: юридический; иностранных языков; искусств; историко-географический; прикладной математики, физики и информационных технологий; русской и чувашской филологии и журналистики. \n 💺 "Главный корпус" (Московский проспект, 15) — Факультеты: информатики и вычислительной техники; энергетики и электротехники; радиоэлектроники и автоматики. \n 💵 Корпус "Е" (Московский проспект, 29) — Экономический факультет. \n 💉 Корпус "М" (Московский проспект, 45), корпус "Л" (ул. Пирогова, 5), корпус "П" (ул. Пирогова, 7), корпус "С" (ул. Пирогова, 3) — Медицинский факультет. \n 👷‍♀ Корпус "Н" (проспект Ленина, 6) — Строительный факультет (студенты направления "Дизайн" — Московский проспект, 17, строение 1). \n 🔬 Корпус "О" (Московский проспект, 19) — Химико-фармацевтический факультет, факультет управления и социальных технологий. \n 🔧 Корпус "Т" (ул. Спиридона Михайлова, 3) — Машиностроительный факультет. \n \n Более подробную информацию можете найти тут: vk.cc/agDHkD', keyboard=keyboard)
            elif response == "общежития":
                send_message(vk_session, 'user_id', event.user_id, message= 'Иногородним поступающим предоставляются благоустроенные общежития. Всего у ЧувГУ 9 общежитий, из них 8 - в г. Чебоксары (коридорного и секционного типа) и 1 – в г. Новочебоксарск (квартирного типа). Стоимость проживания составляет 600-700 руб. в месяц. \n Контакты Администрации студенческого городка: 8 (8352) 45-48-35, hostel@chuvsu.ru.', keyboard=keyboard)
            elif response == "стипендии":
                send_message(vk_session, 'user_id', event.user_id, message= '👉🏻Для назначения государственной академической стипендии должны соблюдаться всего два требованияна момент официального завершения экзаменационной сессии: \n — отсутствие оценок «удовлетворительно», \n — отсутствие академической задолженности, то есть не сданных зачетов, курсовых работ, экзаменов, отчетов по практик по итогам прошлых и текущей сессии. \n \n 👉🏻Социальная стипендия, в отличие от академической, не зависит от оценок и может быть оформлена в любой момент в течение учебного года теми, кто относится к льготным категориям получателей. \n \n Больше информации об этих и других стипендиях Вы можете найти тут: vk.cc/akcElO', keyboard=keyboard, attachment=attachment1)
            elif response == "задать вопросы специалисту":
                send_message(vk_session, 'user_id', event.user_id, message= 'Напишите ваш вопрос, мы постараемся на него ответить. \n \n Если передумали и хотите вернуться к боту, напишите "Начать"', keyboard=keyboard)


            elif response == 'вернуться в основное меню':
                send_message(vk_session, 'user_id', event.user_id, message='Вернуться в основное меню', keyboard=keyboard)

        print('-' * 30)