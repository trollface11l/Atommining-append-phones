import logging
import time

import telebot
from telebot import types

import grpc
import access_code_pb2
import access_code_pb2_grpc


bot = telebot.TeleBot("5726093491:AAFzxIarjJxdMmTX1SO8zt3guVASFQMeMLQ")


def run(message):
    phone_numbers = message.text.split('\n')
    phone_numbers = [int(phone_number) for phone_number in phone_numbers]

    with grpc.insecure_channel('localhost:500511') as channel:
        stub = access_code_pb2_grpc.AccessCodeServiceStub(channel)

        for phone_number in phone_numbers:
            response = stub.AppendPhoneNumber(access_code_pb2.AppendPhoneNumberRequest(phone_number=phone_number))
        return response


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Добавить номера телефонов📲")
    markup.add(btn1)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}!".format(message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    if (message.text == "Добавить номера телефонов📲"):
        bot.send_message(message.chat.id, "Отправьте список номеров")
        time.sleep(10)
    if (message.text != "Добавить номера телефонов📲"):
        if __name__ == "__main__":
            logging.basicConfig()
            run(message)
        bot.send_message(message.chat.id, "Вы успешно добавили номера")


bot.polling(none_stop=True)
