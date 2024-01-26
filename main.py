import os
import shutil


# Реализовать прототип консольной программы - проводника, для работы с файлами. Создать функции создания, удаления,
# перемещения, копирования(файла, папки) с использованием системы контроля версий git. Зарегистрироваться на Github и
# выгрузить с помощью git программу в созданный репозиторий. Прикрепить ссылку на репозиторий.

def menu_action():
    """
        Функция меню предназначена ввода выбора действия и запуск функции этого действия.
    """
    print("\033[34m{}".format("Выберите одно действие в программе:"))
    action = 1
    while action != 0:
        print("\033[34m{}".format("    1 - Создать файл/папку\n"
                                  "    2 - Удалить файл/папку\n"
                                  "    3 - Переместить файл/папку\n"
                                  "    4 - Копировать файл/папку\n"
                                  "    exit - Выход\n"))
        action = input("Введите номер действия: ")
        if action == '1':
            print('Создать файл/папку')
            create_folder_file()
            print('------------------- \n')
        elif action == '2':
            print('Удалить файл/папку')
            remove_folder_file()
            print('------------------- \n')
        elif action == '3':
            print('Переместить файл/папку')
            move_folder_file()
            print('------------------- \n')
        elif action == '4':
            print('Копировать файл/папку\n')
            copy_folder_file()
            print('------------------- \n')
        elif action == 'exit':
            print('Выход')
            break
        else:
            print('Вы ввели не верное значение, попробуйте снова!')
            continue


def path_input(path_or_file):
    """
    Проверка пути до файла/директории. На выходе проверенный существующий путь.
    """
    while True:
        try:
            path = input(f"{path_or_file}")
            if not os.path.exists(path):
                continue
            return path
        except FileNotFoundError:
            print("Вы ввели путь которого не существует. Попробуйте снова еще раз...")


def create_folder_file():
    """
    Функция создания файла или папки. Пользователь вводит путь, проверяется его корректность. Далее проверяется это
    путь до файла или папки. Если путь до файла, то просим пользователя ввести путь еще раз т.к. файл или папку можно
    создать только в папке.
    """
    action = 1
    while action != 0:
        print("\033[34m{}".format("    1 - Создать файл\n"
                                  "    2 - Создать папку\n"
                                  "    3 - Выход\n"))
        action = input("Введите номер действия: ")
        if action == '1':
            path = path_input("Введите путь где вы хотите создать файл: ")
            if os.path.isdir(path):
                file_name = input("Введите название файла: ")
                open(fr"{path}\{file_name}", "x")
                print(f"Файл {file_name} создан")
            elif os.path.isfile(path):
                print("Вы ввели путь до файла, а нужен путь до директории, введите пожалуйста путь повторно!")
            print('------------------- \n')
        elif action == '2':
            path = path_input("Введите путь где вы хотите создать папку: ")
            if os.path.isdir(path):
                folder_name = input("Введите название папки: ")
                os.mkdir(fr"{path}\{folder_name}")
                print(f"Папка {folder_name} создана")
            elif os.path.isfile(path):
                print("Вы ввели путь до файла, а нужен путь до директории, введите пожалуйста путь повторно!")
            print('------------------- \n')
        elif action == '3':
            print('Выход')
            break
        else:
            print('Вы ввели не верное значение, попробуйте снова!')
            continue


def remove_folder_file():
    """
    Функция удаляет файл или папки. Пользователь вводит путь, проверяется его корректность. Далее проверяется это
    путь до файла или папки. В зависимости от этого выбирается необходимый метод удаления.
    """
    action = 1
    while action != 0:
        print("\033[34m{}".format("    1 - Удалить файл\n"
                                  "    2 - Удалить папку вместе с ее содержимым\n"
                                  "    3 - Выход\n"))
        action = input("Введите номер действия: ")
        if action == '1':
            path = path_input("Введите путь к файлу: ")
            if os.path.isdir(path):
                file_name = input("Введите название файла: ")
                os.remove(fr"{path}\{file_name}")
                print(f"Файл {file_name} удален")
            elif os.path.isfile(path):
                print("Вы ввели путь до файла, а нужен путь до директории, введите пожалуйста путь повторно!")
            print('------------------- \n')
        elif action == '2':
            path = path_input("Введите путь к директории:")
            if os.path.isdir(path):
                folder_name = input("Введите название папки:")
                shutil.rmtree(fr"{path}\{folder_name}")
                print(f"Папка {folder_name} удалена")
            elif os.path.isfile(path):
                print("Вы ввели путь до файла, а нужен путь до директории, введите пожалуйста путь повторно!")
            print('------------------- \n')
        elif action == '3':
            print('Выход')
            break
        else:
            print('Вы ввели не верное значение, попробуйте снова!')
            continue


def move_folder_file():
    """
    Перемещение файла или папки с содержимым. Пользователь выбирает действие, затем вводит что
    переместить, а затем куда переместить. Каждый ввод проверяет наличие файла папки и доступности места
    куда необходимо перенести.
    """
    action = 1
    while action != 0:
        print("\033[34m{}".format("    1 - Переместить файл/папку\n"
                                  "    2 - Выход\n"))
        action = input("Введите номер действия: ")
        if action == '1':
            path = path_input("Введите путь до файла или папки")
            if os.path.isfile(path):
                path_file_move = path_input("Введите путь куда необходимо переместить файл: ")
                shutil.move(fr"{path}", path_file_move)
                print(f"Файл перемещён в директорию {path_file_move}")
            elif os.path.isdir(path):
                path_file_move = path_input("Введите путь куда необходимо переместить папку: ")
                shutil.move(fr"{path}", path_file_move)
                print(f"Папка перемещена в директорию {path_file_move}")
            print('------------------- \n')
        elif action == '2':
            print('Выход')
            break
        else:
            print('Вы ввели не верное значение, попробуйте снова!')
            continue


def copy_folder_file():
    """
    Функция копирования файлов и папок. На входе пользователь указывает, что он хочет сделать, вводит путь до
    файла/папке и путь до директории куда необходимо скопировать. В зависимости от этого проверяются корректность
    путей и используются методы copy и copytree.
    """
    action = 1
    while action != 0:
        print("\033[34m{}".format("    1 - Копировать файл\n"
                                  "    2 - Копировать папку вместе с ее содержимым\n"
                                  "    3 - Выход\n"))
        action = input("Введите номер действия: ")
        if action == '1':
            path = path_input("Введите путь к файлу: ")
            if os.path.isfile(path):
                copy_path = path_input("Введите путь куда нужно скопировать файл: ")
                if os.path.isdir(copy_path):
                    shutil.copy(path, copy_path, follow_symlinks=True)
                    print(f"Файл скопирован в директорию: {copy_path}")
            else:
                print("Вы не корректно ввели пути, попробуйте ввести еще раз!")
                continue
        elif action == '2':
            path = path_input("Введите путь к папке: ")
            if os.path.isdir(path):
                copy_path = path_input("Введите путь куда нужно скопировать папку: ")
                if os.path.isdir(copy_path):
                    shutil.copytree(path, copy_path, symlinks=True, dirs_exist_ok=True)
                print(f"Папка скопирована в директорию: {copy_path}")
            else:
                print("Вы не корректно ввели пути, попробуйте ввести еще раз!")
                continue
            print('------------------- \n')
        elif action == '3':
            print('Выход')
            break
        else:
            print('Вы ввели не верное значение, попробуйте снова!')
            continue


# main program ##############################################################

print("\033[34m{}".format('Данная программа предназначена для работы с файлами и папками'))
print('---------------------------------------------------------------------------------------------------------')

menu_action()