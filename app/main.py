class ValidationError(Exception):
    def __init__(self, message: str) -> None:
        self.message = message

    def __str__(self) -> str:
        return f"Передані дані не відповідають умові: {self.message}"


def copy_file(command: str) -> None:
    try:
        command = command.split(" ")
        if len(command) != 3:
            raise ValidationError("Команда має містити рівно три аргументи: "
                                  "'cp <існуючий_файл> <новий_файл>'")
        if command[0] != "cp":
            raise ValidationError("Першим аргументом має бути команда 'cp'")
        if command[1] == command[2]:
            raise ValidationError("Назва нового файлу має "
                                  "відрізнятися від поточного")
        with (open(command[1], "r") as file_in,
              open(command[2], "w") as file_out):
            for content in file_in.readlines():
                file_out.write(content)
    except ValidationError as error:
        print(error)
