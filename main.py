print('Начало работы\nСписок команд:\n add — добавить задачу; \n list — показать задачи; \n done — отметить выполненной; \n delete — удалить задачу; \n exit — выйти.\n Введите команду')

import json

try:
    with open('data/data.json', 'r', encoding='utf-8') as f:
        tasks = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    tasks = []

while True:    
    command = input('> ')
    if command == 'exit' or command == 'Exit':
        break
    elif command == 'add' or command == 'Add':
        new_task = {"id": None, "title": None, "done": False}
        
        if tasks == []:
            new_task["id"] = 1
        else:
            new_task["id"] = max(task["id"] for task in tasks) + 1
        
        new_task["title"] = input('Введите задачу: ').strip()

        tasks.append(new_task)  

        with open('data/data.json', 'w', encoding='utf-8') as f:
            json.dump(tasks, f, ensure_ascii=False, indent=2)  

        print('Задача добавлена:', new_task)




        



