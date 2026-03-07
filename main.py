import service

DATA_PATH = "data/data.json"

print(
    "\nНачало работы\n"
    "\nЧтобы отобразить список команд, введите команду \"help\"\n"
    "\nВведите команду"
)

tasks = service.load_tasks(DATA_PATH)
        
while True:
    command = input('\n>').strip().lower()

    if command == 'exit':
        print("Завершение программы")
        break
    elif command == 'add':
        service.add_comm(tasks, DATA_PATH)
    elif command == 'disc':
        service.desc_comm(tasks)
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

