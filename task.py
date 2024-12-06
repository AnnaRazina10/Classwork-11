from .models import Task
import json
import os
import pandas as pd


TASKS_FILE = f"{os.getcwd()}/storage/tasks.json"


def load_tasks():
    try:
        with open(TASKS_FILE, "r") as file:
            return [Task.from_dict(task) for task in json.load(file)]
    except:
        return []


def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump([task.to_dict() for task in tasks], file, indent=4)


def create_task():
    tasks = load_tasks()
    task_id = len(tasks) + 1
    title = input("Введите заголовок задачи: ")
    description = input("Введите описание задачи: ")
    priority = input("Введите приоритет задачи: ")
    due_date = input("Введите дедлайн задачи: ")
    task = Task(task_id, title, description, False, priority, due_date)
    tasks.append(task)
    save_tasks(tasks)
    print("Задача успешно создана.")


def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("Список задач пуст.")
        return
    for task in tasks:
        print(
            f"{task.id}. {task.title} - {task.priority} - {task.due_date} - {'Выполнено' if task.done else 'Не выполнено'}"
        )


def export_tasks_to_csv():
    tasks = load_tasks()
    df = pd.DataFrame([task.to_dict() for task in tasks])
    df.to_csv(f"{os.getcwd()}/storage/tasks.csv", index=False)
    print("Задачи успешно экспортированы в CSV.")


def import_tasks_from_csv():
    df = pd.read_csv(f"{os.getcwd()}/storage/tasks.csv")
    tasks = [Task.from_dict(row) for index, row in df.iterrows()]
    save_tasks(tasks)
    print("Задачи успешно импортированы из CSV.")
