from aiogram import Bot, Dispatcher, executor, types



api_token = '5954391664:AAHiV2wHRekH4j8Cbw5L-pqs9dbflTwH6N4'
bot = Bot(token=api_token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])


async def welcome_str(message: types.Message):
    await message.reply('Привет!\n'
                        'Сюда ты можешь анонимно отправить музыку, которую хочешь услышать 7.11\n'
                        'Напиши сообщение в формате "Name of artist - Track"')

@dp.message_handler()
async def wrtln(message: types.Message):
    with open('USERSANSWERS.txt', 'a', encoding='utf-8') as out:
        print(message.text, file=out)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)