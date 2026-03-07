import json
import uuid

def load_tasks(path) -> list:
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        tasks = []
        with open(path, "w", encoding="utf-8") as f:
            json.dump(tasks, f, ensure_ascii=False, indent=2)
        return tasks


def save_tasks(tasks: list, path: str) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)


def add_comm(tasks: list, path: str) -> None:
    title = input("Введите название задачи: ").strip()
    if title == "":
        print("Пустое название нельзя")
        return
    
    description = input("Введите описание задачи: ").strip()
    if description == "":
        new_task = {
            "id": uuid.uuid4().hex[:8],  
            "title": title,
            "done": False,
            }
    else:
        new_task = {
            "id": uuid.uuid4().hex[:8],  
            "title": title,
            "description": description,
            "done": False,
            }

    tasks.append(new_task)
    save_tasks(tasks, path)

    print(f"\nЗадача добавлена: ID: {new_task['id']}, задача: {new_task['title']}.")


def list_comm(tasks: list) -> None:
    if not tasks:
        print("Актуальные задачи отсутствуют")
        return

    for task in tasks:
        status = "Выполнено" if task["done"] else "Не выполнено"
        print(f"ID: {task['id']} | Задача: {task['title']} | Статус: {status}")


def desc_comm(tasks: list) -> None:
    if not tasks:
        print("Актуальные задачи отсутствуют")
        return
    
    desc_id = input("Введите ID: ").strip()
    for task in tasks:
        try:
            if task["id"] == desc_id:
                print(
                    f' Название задачи: {task["title"]}\n'
                    f' Описание: {task["description"]}'
                    )
                return
        except KeyError:
            print(f'Задача "{task["title"]}" не имеет описания')
            return

    print("Задача с таким ID не найдена")


def delete_comm(tasks: list, path: str) -> None:
    if not tasks:
        print("Актуальные задачи отсутствуют")
        return

    del_id = input("Введите ID: ").strip()

    for task in tasks:
        if task["id"] == del_id:
            tasks.remove(task)
            save_tasks(tasks, path)
            print(f'Задача "{task["title"]}" удалена')
            return

    print("Задача с таким ID не найдена")


def done_comm(tasks: list, path: str) -> None:
    if not tasks:
        print("Актуальные задачи отсутствуют")
        return

    done_id = input("Введите ID задачи: ").strip()

    for task in tasks:
        if task["id"] == done_id:
            if task["done"]:
                print(f"Задача с ID {done_id} уже была выполнена")
                return

            task["done"] = True
            save_tasks(tasks, path)
            print(f'Задача "{task["title"]}" выполнена!')
            return

    print("Задача с таким ID не найдена")


def help_comm():
    print(
    "Список команд:\n"
    " add — добавить задачу;\n"
    " disc — отобразить описание задачи;\n"
    " list — показать задачи;\n"
    " done — отметить выполненной;\n"
    " delete — удалить задачу;\n"
    " help — список команд;\n"
    " exit — выйти."
    )
    