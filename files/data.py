commands = ["e","r","1","2","3"]
user_input = {commands[0]:"Выход", commands[1]:"Перезапуск программы", commands[2]:"Добавить задачу", commands[3]:"Показать задачу", commands[4]:"Запустить задачу"}
result_queues = [None]
tasks = []
id = None
def check(p_1):
    if p_1 == commands[0]:
        return 2
    elif p_1 == commands[1]:
        return 1
    else:
        return 0

def create_task(tasks):
    from files.task import Task
    id_0 = input("Введите id: ")
    for el in tasks:
        if el.id == id_0:
            print("Данный ID уже занят. Попробуйте ещё раз.")
            return None       
    name_0 = input("Введите имя: ")
    desc_0 = input("Укажите описание: ")
    command_0 = input("Введите команду: ")
    args_0 = input("Введите значения: ")
    args_0 = args_0.split(" ")
    return Task(id_0, name_0, desc_0, command_0, args_0)

def line():
    print("=============================================")

def print_task(tasks):
    line()
    for el in tasks:
        print(el)
    line()

def  starting_task(tasks):
    print_task(tasks)
    user_id = input("Введите ID задачи: ")
    count = 1
    for el in tasks:
        if user_id == el.id:
            from files.data import activate_subprocess
            from queue import Queue, Empty
            import threading
            result_queue = Queue()
            result_queues.append(result_queue)
            print(f"Задача ID: {el.id} запускается...")
            thread = threading.Thread(target=activate_subprocess, args=(el.command,el.args,result_queue))  
            thread.start()
            global id 
            id = user_id
            el.status = "Выполняется"
            break
        elif count == len(tasks):
            print(f"Задачи с ID: {user_id} не существует.")
            break
    
def activate_subprocess(command, args, result_queue):
    import subprocess
    start = ["cmd", "/c", command]
    for el in args:
        start.append(el)
    result = subprocess.run(start, capture_output=True, text=True, encoding="cp866")
    result_queue.put(result)



def task_is_run():
    for el in tasks:
        if el.id == id:
            from files.data import result_queues
            if result_queues != None:                            
                for queue in result_queues:
                    try:
                        result = queue.get_nowait()
                        if result.returncode == 0:
                            el.status = result.stdout
                        else:
                            el.status = result.stderr
                    except:
                        pass 