import subprocess
import threading
from queue import Queue, Empty

from files.task import Task

commands = ["e", "r", "1", "2", "3"]
line = 48 * "="
result_queues = {}
tasks = []
running_task_id = []

user_input = {
    commands[0]: "Выход",
    commands[1]: "Перезапуск программы",
    commands[2]: "Добавить задачу",
    commands[3]: "Показать задачу",
    commands[4]: "Запустить задачу",
}


def check(action):
    if action == commands[0]:
        return 2
    elif action == commands[1]:
        return 1
    else:
        return 0


def create_task(task_list):
    task_id = input("Введите id: ")
    for existing_task in task_list:
        if existing_task.id == task_id:
            print("Данный ID уже занят. Попробуйте ещё раз.")
            return None
    name = input("Введите имя: ")
    command = input("Введите команду: ")
    arguments = input("Введите значения: ")
    arguments = arguments.split(" ")
    return Task(task_id, name, command, arguments)


def print_task(task_list):
    print(line)
    for task in task_list:
        print(task)
    print(line)


def starting_task(task_list):
    print_task(task_list)
    user_id = input("Введите ID задачи: ")
    count = 1
    for task in task_list:
        if user_id == task.id:
            result_queue = Queue()
            result_queues[task.id] = result_queue
            print(f"Задача c ID '{task.id}' запускается...")
            thread = threading.Thread(
                target=activate_subprocess,
                args=(task.command, task.args, result_queue),
            )
            thread.start()
            global running_task_id
            running_task_id.append(user_id)
            task.status = "Выполняется"
            break
        elif count == len(task_list):
            print(f"Задачи с ID: {user_id} не существует.")
            break


def activate_subprocess(command, arguments, result_queue):
    command_parts = ["cmd", "/c", command]
    for argument in arguments:
        command_parts.append(argument)
    result = subprocess.run(
        command_parts,
        capture_output=True,
        text=True,
        encoding="cp866",
    )
    result_queue.put(result)


def task_is_run():
    for task in tasks:
        if task.id in running_task_id:
            result_queue = result_queues.get(task.id)
            if result_queue:
                try:
                    result = result_queue.get_nowait()
                    if result.returncode == 0:
                        task.status = result.stdout
                    else:
                        task.status = result.stderr
                    running_task_id.remove(task.id)
                    del result_queues[task.id]
                except Empty:
                    pass
