# -*- coding: utf-8 -*-
import socket
import os

def load_request_dict(request):
    request_dict = {}

    split_request = request.split('\r\n')
    split_first_line = split_request[0].split(' ')

    request_dict['Method'] = split_first_line[0]
    request_dict['URI'] = split_first_line[1]
    request_dict['HTTP-Version'] = split_first_line[2]

    for now_line in split_request[1:]:
        if now_line != '':
            now_split_string = now_line.split(': ')
            request_dict[now_split_string[0]] = now_split_string[1]
    return  request_dict

def dump_responce(http_version, state_code, state_code_describe, html_page):
    responce =  "%s %d %s\r\n" \
                "Content-Language: ru\r\n" \
                "Content-Type: text/html; charset=utf-8\r\n" \
                "Content-Length: %d\r\n" \
                "Connection: %s\r\n" \
                "\r\n" \
                "%s" % (http_version, state_code, state_code_describe, len(html_page), "keep-alive", html_page)
    return responce

def get_response(request):
    request_dict = load_request_dict(request)

    if request_dict['URI'] == "/" :
        return  dump_responce(request_dict['HTTP-Version'], 200, "OK", "Hello mister!\r\nYou are: " + request_dict['User-Agent'])

    elif request_dict['URI'][:7] == "/media/" :
        file_list = os.listdir("../files/")
        filename = request_dict['URI'][7:]
        return_string = ""

        if filename == "":
            for now_filename in file_list :
                return_string += "- " + now_filename + "\r\n"
            return dump_responce(request_dict['HTTP-Version'], 200, "OK", return_string)

        elif filename in file_list :
            f = open("../files/" + filename, 'r')
            return_string = f.read()
            f.close()
            return dump_responce(request_dict['HTTP-Version'], 200, "OK", return_string)

        else :
            return dump_responce(request_dict['HTTP-Version'], 404, "Not found", "File Not Found\r\n")

    elif request_dict['URI'] == "/test/":
        return request

    else :
        return dump_responce(request_dict['HTTP-Version'], 404, "Not found", "Page not found\r\n")


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 8000))     # Cвязываем наш сокет с хостом localhost и портом 8000
server_socket.listen(0)                     # Запустим для данного сокета режим прослушивания
                                            # Аргумент — максимальное количество подключений в очереди

print 'Started'

while 1:
    try:
        (client_socket, address) = server_socket.accept()
        print 'Got new client', client_socket.getsockname()     # Принимаем новое подключение (accept), печатаем в консоль адрес клиентского сокета

        request_string = client_socket.recv(2048)               # Формируем входящий запрос. Т.к. мы не можем точно знать, что и в каких объемах клиент нам
                                                                # пошлет, то мы будем получать данные порциями по 2 кб

        client_socket.send(get_response(request_string))        # Вернем клиенту ответ на его запрос
        client_socket.close()

    except KeyboardInterrupt:                                   # В случае закрытия сервера (напр. Ctrl+C), accept() выбросит исключение
        print 'Stopped'
        server_socket.close()                                   # Закрыть серверный сокет
        exit()
