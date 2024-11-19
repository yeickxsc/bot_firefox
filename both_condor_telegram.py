import asyncio
from telegram import Bot

# Reemplaza 'YOUR_BOT_TOKEN' con el token que te proporcionó BotFather
bot_token = '7147297940:AAEkw7gdsUxEaBEJF_PYTbjyoU7rtTQwO3g'

# Crear una instancia del bot
bot = Bot(token=bot_token)

# ID de chat donde quieres enviar el mensaje (puede ser tu propio ID o el de un grupo)
chat_id = -4201948973  # Puedes obtener este ID usando el bot @userinfobot en Telegram



def notification_proc(message_text):
    async def main():
        try:
            # Enviar el mensaje usando await para esperar la respuesta
            await bot.send_message(chat_id=chat_id, text=message_text)
            print(f'Mensaje enviado a {chat_id}: {message_text}')
        except Exception as e:
            print(f'Error al enviar mensaje: {e}')

    # Ejecutar el bucle de eventos de asyncio para iniciar el script
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

