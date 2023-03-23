"""
Використовуючи код домашнього завдання 1 лекции 11, додайте до
серверу чату систему логування рівня INFO, WARNING і ERROR.
"""
import socket
import logging

def server_program():
    # отримати ім'я хоста
    host = socket.gethostname()
    port = 5000  # ініціювати порт вище 1024
    logging.info("initialize the port")

    server_socket = socket.socket()  # створити TCP-сокет
    server_socket.bind((host, port))  # прив’язати сокет до вказаної нами адреси

    # налаштуйте, скільки клієнтів сервер може слухати одночасно
    server_socket.listen(2)
    conn, address = server_socket.accept()  # прийняти нове підключення
    print("Connection from: " + str(address))
    while True:
        # отримати потік даних. Він не приймає пакети даних, більші за 1024 байти
        data = conn.recv(1024).decode()
        if not data:
            # якщо дані не отримані, розрив
            logging.warning("no data received")
            break
        print("from connected user: " + str(data))
        data = input(' -> ')
        conn.send(data.encode())  # відправити дані клієнту
        logging.error("data has not been sent to the client")

    conn.close()  # закрийте з'єднання

def log():

    fmtstr = "%(asctime)s: %(levelname)s: %(funcName)s line: %(lineno)d %(message)s"
    # встановлюємо рівень логування
    logging.basicConfig(level=logging.INFO,
                        filename="log_output.log",
                        filemode="w",
                        format=fmtstr)

if __name__ == '__main__':
    log()
    server_program()
