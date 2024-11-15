def send_email(message, recipient, sender="university.help@gmail.com"):
    domen_mail = (".com ", ".ru ",".net")
    if "@" not in recipient or not recipient.endswith(domen_mail):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}.")
        return
    if sender == recipient:
        print(f"Нельзя отправить письмо самому себе!")
        return
    if sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}")

    else:
        print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено"
              " с адреса <sender> на адрес <recipient>.")

send_email("Проверка связи", "gr.natasha.2003@gmail.ru")
send_email("Проверка связи", "gr.natasha.2003gmail.com")
send_email("Проверка связи", "university.help@gmail.com")
send_email("Проверка связи", "university.help@gmail.com", "university.help@gmail.com" )