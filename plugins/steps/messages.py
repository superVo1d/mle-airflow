from airflow.providers.telegram.hooks.telegram import TelegramHook # импортируем хук телеграма
from airflow.models import Variable

TELEGRAM_TOKEN = Variable.get('TELEGRAM_TOKEN')
TELEGRAM_CHAT_ID = Variable.get('TELEGRAM_TOKEN')

def send_telegram_success_message(context): # на вход принимаем словарь со контекстными переменными
    hook = TelegramHook(telegram_conn_id='test',
                        token=TELEGRAM_TOKEN,
                        chat_id=TELEGRAM_CHAT_ID)
    dag = context['dag']
    run_id = context['run_id']
    
    message = f'Исполнение DAG {dag} с id={run_id} прошло успешно!' # определение текста сообщения
    hook.send_message({
        'chat_id': TELEGRAM_CHAT_ID,
        'text': message
    }) # отправка сообщения 

def send_telegram_failure_message(context):
    hook = TelegramHook(telegram_conn_id='test',
                        token=TELEGRAM_TOKEN,
                        chat_id=TELEGRAM_CHAT_ID)

    run_id = context['run_id']
    task_instance_key_str = context['task_instance_key_str']
    
    message = f'Исполнение DAG {task_instance_key_str} с id={run_id} завершилось с ошибкой!'
    hook.send_message({
        'chat_id': TELEGRAM_CHAT_ID,
        'text': message
    })    