from files.data import (
    check,
    commands,
    create_task,
    line,
    print_task,
    starting_task,
    task_is_run,
    tasks,
    user_input,
)

status = 0
while status == 0 or status == 1:

    status = 0
    i = 0

    print(f"{line}\n\t\tTASKFORGE v1.1\n{line}")

    for _ in commands:
        print(f"{commands[i]}. {user_input[commands[i]]}")
        i += 1

    while status == 0:
        act = input("\nВыберете действие: ")
        status = check(act)
        task_is_run()

        if act in commands:
            print(f"Вы выбрали: {user_input[act]}")
            if act == commands[2]:
                task = create_task(tasks)
                if task != None:
                    tasks.append(task)
            elif act == commands[3]:
                print_task(tasks)
            elif act == commands[4]:
                starting_task(tasks)

        else:
            print(f"'{act}'\n не найдено в коммандах. Попробуйте ещё раз.")
