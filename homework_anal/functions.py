def show_data() -> None:
    ''' Выводит информацию из справочника'''
    with open('book.txt', 'r', encoding='utf-8') as f:
        print(f.read())

def add_data() -> None:
    ''' Добавляет информацию из справочника'''
    fio= input('Введите ФИО')
    tel_number= input('Введите номер телефона')
    with open('book.txt', 'a', encoding='utf-8') as f:
        f.write(f'\n{fio} | {tel_number}')
    print ('успешно!')


def find_data() -> None:
    ''' Осуществляет поиск по справочнику'''
    data= input('Введите данные для поиска')
    with open('book.txt', 'r', encoding='utf-8') as f:
        tel_book= f.read()
    print('Результаты поиска: ')
    print(search(tel_book, data))

def search(book: str, info:str) -> str:
    book= book.split('\n')
    return  '\n'.join([post for post in book if info in post])

def delete_person() -> None:
    '''Удаляет данные'''
    data = input('Кого удаляем?: ')
    with open("book.txt", "r", encoding="utf8" ) as f:
        tel_book = f.readlines()
    with open("book.txt", "w", encoding="utf8" ) as f:
        for person in tel_book:
            if person!=data:
                f.write(person)

def change_person() -> None:
    '''Изменяет данные'''
    old_name = input('Кого хотим переименовать?: ')
    new_name = input('Как хотим его назвать?: ')
    with open("book.txt", "r", encoding="utf8" ) as f:
        old_data = f.read()
    new_data=old_data.replace(old_name, new_name)
    with open("book.txt", "w", encoding="utf8" ) as f:
        f.write(new_data)