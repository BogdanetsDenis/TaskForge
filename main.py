status = 0 

while status == 0 or status == 1:
    from files.data import commands, user_input, tasks, check, line, print_task, task_is_run
    from queue import Queue, Empty
    status = 0
    i = 0

    line()
    print("\t\tTASKFORGE v1.0")
    line()

    for el in commands:
        print(f"{commands[i]}. {user_input[commands[i]]}")
        i += 1

    while status == 0:
        act = input("\nВыберете действие: ")
        status = check(act)

        from files.data import id
        task_is_run()

        if act in commands:
            print(f"Вы выбрали: {user_input[act]}")
            if act == commands[2]:
                from files.data import create_task
                task = create_task(tasks)
                if task != None:
                    tasks.append(task)
            elif act == commands[3]:
                print_task(tasks)
            elif act == commands[4]:
                from files.data import starting_task
                starting_task(tasks)
                

        else:
            print(f"'{act}'\n не найдено в коммандах. Попробуйте ещё раз.")