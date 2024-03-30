import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
smtp_server.starttls()
smtp_server.login("clashmakerr@gmail.com", "fMo3Yu9Qqh6S")

# Создание объекта сообщения
msg = MIMEMultipart()

# Настройка параметров сообщения
msg["From"] = "clashmakerr@gmail.com"
msg["To"] = "vzukov623@gmail.com"
msg["Subject"] = "Тестовое письмо"

# Добавление текста в сообщение
text = "Привет! Это тестовое письмо, отправленное с помощью Python"
msg.attach(MIMEText(text, "plain"))

# Отправка письма
smtp_server.sendmail("clashmakerr@gmail.com", "vzukov623@gmail.com", msg.as_string())

# Закрытие соединения
smtp_server.quit()