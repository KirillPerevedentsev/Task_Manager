import json

print('Начало работы\nСписок команд:\n add — добавить задачу; \n list — показать задачи; \n done — отметить выполненной; \n delete — удалить задачу; \n exit — выйти.\n Введите команду')

try:
    with open('data/data.json', 'r', encoding='utf-8') as f:
        tasks = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    tasks = []
    
def add_comm():
    new_task = {"id": None, "title": None, "done": False}
    
    if tasks == []:
        new_task["id"] = 1
    else:
        new_task["id"] = max(task["id"] for task in tasks) + 1
    
    new_task["title"] = input('Введите задачу: ').strip()

    if new_task["title"] == '':
        print('Пустое название нельзя')
        return

    tasks.append(new_task)

    with open('data/data.json', 'w', encoding='utf-8') as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)
    
    status = 'Не выполнено' if new_task['done'] == False else 'Выполнено'

    print('Задача добавлена:',f"ID: {new_task['id']}, задача: {new_task['title']}, статус: {status}.")

def delete_comm():
    if tasks == []:
        print('Актуальные задачи отсутствуют')
    else:
        try:
            del_id = int(input('Введите ID: '))
        except ValueError:
            print('ID должен быть числом')
            return    
        for task in tasks:
            if task['id'] == del_id:
                tasks.remove(task)
                with open('data/data.json', 'w', encoding='utf-8') as f:
                    json.dump(tasks, f, ensure_ascii=False, indent=2)
                print('Задача удалена')
                break
        else:
            print('Задача с таким ID не найдена')

def done_comm():
    if tasks == []:
        print('Актуальные задачи отсутствуют')
    else:
        try:
            done_id = int(input('Введите ID задачи: '))
        except ValueError:
            print('ID должен быть числом')
            return    
        for task in tasks:
            if task['id'] == done_id and task['done']:
                print(f'Задача с ID {done_id} уже была выполнена')
                break
            elif task['id'] == done_id:
                task['done'] = True
                with open('data/data.json', 'w', encoding='utf-8') as f:
                    json.dump(tasks, f, ensure_ascii=False, indent=2)
                print(f'Задача с ID {done_id} выполнена!')
                break
        else:
            print('Задача с таким ID не найдена')

def list_comm():
    if tasks == []:
        print('Актуальные задачи отсутствуют')
    else:
        for el in tasks:
            status = 'Выполнено' if el['done'] == True else 'Не выполнено'
            print(f"Номер ID: {el['id']};\n Задача: {el['title']};\n Статус: {status}.")
            
while True:
    command = input('> ').strip().lower()

    if command == 'exit':
        print("Завершение программы")
        break
    elif command == 'add':
        add_comm()
    elif command == 'list':
        list_comm()
    elif command == 'delete':
        delete_comm()
    elif command == 'done':
        done_comm()
    else:
        print('Некорректная команда')

