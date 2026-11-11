class Task:
    def __init__(
        self,
        task_id,
        name,
        command,
        arguments,
        status="Готово к запуску",
    ):
        self.id = task_id
        self.name = name
        self.command = command
        self.args = arguments
        self.status = status

    def __str__(self):
        return (
            f"\nID: {self.id} \nName: {self.name} \nCommand: {self.command} "
            f"\nArgs: {self.args} \nStatus: {self.status}"
        )