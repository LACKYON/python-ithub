from datetime import date, datetime
from pathlib import Path

TASKS_FILE = Path(__file__).with_name("tasks.txt")
RED = "\033[31m"
YELLOW = "\033[33m"
GREEN = "\033[32m"
RESET = "\033[0m"


def load_tasks():
    if not TASKS_FILE.exists():
        return []
    with TASKS_FILE.open("r", encoding="utf-8") as file:
        return [line.rstrip("\n").split("|", 2) for line in file if line.strip()]


def save_tasks(tasks):
    with TASKS_FILE.open("w", encoding="utf-8") as file:
        file.writelines(f"{task[0]}|{task[1]}|{task[2]}\n" for task in tasks)


def task_color(deadline):
    task_date = date.fromisoformat(deadline)
    today = date.today()
    if task_date < today:
        return RED, "Просрочена"
    if task_date == today:
        return YELLOW, "На сегодня"
    return GREEN, "Будущая"


def show_tasks(tasks):
    if not tasks:
        print("Список задач пуст.")
    for number, task in enumerate(tasks, start=1):
        color, status = task_color(task[1])
        mark = "✓" if task[2] == "done" else " "
        print(f"{color}{number}. [{mark}] {task[0]} — срок {task[1]} ({status}){RESET}")


def add_task(tasks):
    title = input("Название задачи: ").strip()
    deadline = input("Срок (ГГГГ-ММ-ДД): ").strip()
    date.fromisoformat(deadline)
    tasks.append([title, deadline, "open"])
    save_tasks(tasks)
    print("Задача сохранена.")


def finish_task(tasks):
    show_tasks(tasks)
    number = int(input("Номер выполненной задачи: "))
    tasks[number - 1][2] = "done"
    save_tasks(tasks)
    print("Задача отмечена выполненной.")


def delete_task(tasks):
    show_tasks(tasks)
    number = int(input("Номер задачи для удаления: "))
    tasks.pop(number - 1)
    save_tasks(tasks)
    print("Задача удалена.")


def main():
    tasks = load_tasks()
    while True:
        print("\n1 — показать задачи\n2 — добавить\n3 — отметить выполненной\n4 — удалить\n0 — выход")
        choice = input("Выберите действие: ").strip()
        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            try:
                add_task(tasks)
            except ValueError:
                print("Проверьте дату: используйте формат ГГГГ-ММ-ДД.")
        elif choice == "3":
            try:
                finish_task(tasks)
            except (ValueError, IndexError):
                print("Такого номера нет.")
        elif choice == "4":
            try:
                delete_task(tasks)
            except (ValueError, IndexError):
                print("Такого номера нет.")
        elif choice == "0":
            break
        else:
            print("Неизвестная команда.")


if __name__ == "__main__":
    main()
