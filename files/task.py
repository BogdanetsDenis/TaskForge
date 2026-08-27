class Task():
    def __init__ (self, id_0, name_0, desc_0, command_0, args_0, status_0 = "Готово к запуску"):
        self.id = id_0
        self.name  = name_0
        self.description = desc_0
        self.command = command_0
        self.args = args_0
        self.status = status_0

    def __str__(self):
        return f"\nID: {self.id} \nName: {self.name} \nDiscription: {self.description} \nCommand: {self.command} \nArgs: {self.args} \nStatus: {self.status}"