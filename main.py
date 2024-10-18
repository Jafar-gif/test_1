

def send_email(message,recipient,sender = 'ortukov97@inbox.ru'):
    if '@' not in recipient or not recipient.endswith(('.com', '.ru', '.net')):
        if'@' not in sender or not sender.endswith(('.com', '.ru', '.net')):
            print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}.')
        elif sender == recipient:
            print('Нельзя отправить письмо самому себе!')
        elif sender == 'ortukov97@inbox.ru':
            print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
        elif sender != 'ortukov97@inbox.ru':
            print (f'Нестандартный отправитель! Письмо отправлено с адреса {sender} на адрес {recipient}.')

send_email('message','stiw.box@mail.ru')
send_email('message','recipient',)

send_email('mesaage',{'stiw.box@mail.ru'},{'stiw.xod@mail.ru'})
send_email('message','recipient','sender')

send_email('message',{'ortukov97@inbox.ru'},{'ortukov97@inbox.ru'})
send_email('message',{'sender'},{'sender'})





