
#показывает справочник
def read_file():
    with open(path_file, 'r', encoding='UTF-8') as f:
       for line in f:
          print(line.strip())

#добавляет строку
def write_file():
    with open(path_file, 'a', encoding='UTF-8') as f:
       f.writelines("/n" + input())
#поиск
def find_file():
    find_info=input()
    with open(path_file, 'r', encoding='UTF-8') as f:
        for line in f:
            if find_info in line.casefold():
                print(line)

#Изменить данные 
def change_file():
    find_info=input("Кого ищим?")
    new_info=input("На что меняем")
    with open(path_file, 'r+', encoding='UTF-8') as f:
        for line in f:
            if  find_info != line:
                f.write(line)
            else:
                f.write(new_info + "\n")

#удалить 
def delite():
    del_info=input()
    with open(path_file, 'r+', encoding='UTF-8') as f:
        for line in f:
            if del_info != line:
                f.write(line)


path_file=r'Telephon_directory.txt'
while True:
    mode = input('Выберите режим работы справочника 0-показать файл, 1-добавить, 2-поиск, 3-изменить, 4-удалить , 5-выход: ')
    if mode == '0':
        read_file()
    elif mode == '1':
        write_file()
    elif mode == '2':
        find_file()
    elif mode == '3':
        change_file()
    elif mode == '4':
        delite()
    elif mode == '5':
        break
    else:
        print('No mode')