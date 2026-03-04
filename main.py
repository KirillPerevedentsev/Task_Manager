import service

DATA_PATH = "data/data.json"

print(
    "\nНачало работы\n"
    "Список команд:\n"
    " add — добавить задачу;\n"
    " list — показать задачи;\n"
    " done — отметить выполненной;\n"
    " delete — удалить задачу;\n"
    " help — список команд;\n"
    " exit — выйти.\n"
    "Введите команду"
)

tasks = service.load_tasks(DATA_PATH)
        
while True:
    command = input('\n>').strip().lower()

    if command == 'exit':
        print("Завершение программы")
        break
    elif command == 'add':
        service.add_comm(tasks, DATA_PATH)
    elif command == 'list':
        service.list_comm(tasks)
    elif command == 'delete':
        service.delete_comm(tasks, DATA_PATH)
    elif command == 'done':
        service.done_comm(tasks, DATA_PATH)
    elif command == 'help':
        service.help_comm()
    else:
        print('Некорректная команда')

