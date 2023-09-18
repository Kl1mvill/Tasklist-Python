import os


# Очистка консоли
def clear_console():
    os.system("cls")


# Функция читает файл "todolist.txt" и возвращает список дел.
# Если файла нет возвращаем пустой список.
def load_todo_list(filename="todolist.txt"):
    try:
        with open(filename, encoding="utf-8") as todo_file:
            return [line.strip() for line in todo_file.readlines()]
    except FileNotFoundError:
        return []


# Сохранение списка todo_list в файл "todolist.txt".
# Записывается переводом строк.
def save_list_file(todo_list, filename="todolist.txt"):
    with open(filename, "w", encoding="utf-8") as todo_file:
        todo_file.write("\n".join(todo_list))


# Удаление элемента из списка todo_list.
def removing_from_list(todo_list):
    show_todo_list(todo_list)
    item_number = int(input('\nWhat would you like to delete? '))

    if item_number <= len(todo_list):
        del todo_list[item_number]
    else:
        print('You named a non-existent case')


# Добавление элемента в список todolist.
def add_todo_item(todo_list):
    todo_list.append(input("Task text: "))


# Функция изменяет какой-то элемент из списка todolist.
def changing_element(todo_list):
    show_todo_list(todo_list)
    changeable_element = int(input('\nWhich element do you want to change? '))

    if changeable_element <= len(todo_list):
        todo_list[changeable_element] = input('Enter the change: ')
    else:
        print('You named a non-existent case')


# Вывод списка todolist.
def show_todo_list(todo_list):
    print("Todo list:")
    if not todo_list:
        print("Nothing to do")
    else:
        for i, item in enumerate(todo_list):
            print(f"{i}. {item}")


# Меню для управления программой.
def show_menu(todo_list):
    print("-----------------------------------")
    print("1. Show", "2. Add", "3. Delete", "4. Edit", "5. Exit", sep="\n")

    command = input("Choose option index: ")  # Индекс действия, которое надо совершить.
    clear_console()

    if command == "1":
        show_todo_list(todo_list)
    elif command == "2":
        add_todo_item(todo_list)
    elif command == "3":
        removing_from_list(todo_list)
    elif command == "4":
        changing_element(todo_list)
    elif command == "5":
        save_list_file(todo_list)
        raise SystemExit
    else:
        print("Command not found!")


# Запуск программы.
def main():
    todo_list = load_todo_list()

    while True:
        show_menu(todo_list)


if __name__ == "__main__":
    main()  # Запуск программы
