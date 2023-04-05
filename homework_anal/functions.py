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

def delete_person(name):
    '''Удаляет данные'''
    persons = read_data()
    with open("data.txt", "w", encoding="utf8" ) as file:
        for person in persons:
            if name != person:
                file.write(person) 

def change_person(new_name, old_name):
    '''Изменяет данные'''
    persons = read_data()
    with open("data.txt", "w", encoding="utf8" ) as file:
        for person in persons:
            if  old_name != person:
                file.write(person)
            else:
                file.write(new_name + "\n")