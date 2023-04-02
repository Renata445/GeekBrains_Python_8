def show_txt():
    """эта ф-ция показывает содержимое справочника"""
    with open('phone_book.txt', 'r', encoding='utf-8') as file:
        book = file.read()  # .split('\n')
    return book


def new_txt():
    """добавляет строку в справочник"""
    with open('phone_book.txt', 'a', encoding='utf-8') as file:
        file.write(input('Введите новую строку: ' + '\n'))


def find_txt():
    """Эта ф-ция ищет информацию в справочнике"""
    with open('phone_book.txt', 'r', encoding='utf-8') as file:
        book = file.read().split('\n')
        temp = input('что ищем?: ')
        for i in book:
            if temp in i:
                print(i)


def delete_person(name):
    """Удаляет данные"""
    persons = read_data()
    with open("phone_book.txt", "w", encoding="utf8") as file:
        for person in persons:
            if name != person:
                file.write(person)



while True:
    mode = input('Выберите режим работы справочника' + '\n'
                 + '0-поиск, 1-чтение файла, 2-добавление в файл, 3-удаление, 4-выход: ')
    if mode == '1':
        print(show_txt())
    elif mode == '0':
        find_txt()
    elif mode == '2':
        new_txt()
    elif mode == '3':
        name = input('кого удаляем?: ')
        delete_person(name)
    elif mode == '4':
        break
    else:
        print('No mode')