class CommandError(Exception):
    pass


def copy_file(command: str) -> None:
    command = command.split()
    if len(command) != 3 and command[0] == "cp":
        raise CommandError("Unsupported format of command")

    file_name, new_file_name = command[1:]
    if file_name != new_file_name:
        try:
            with (open(file_name, "r") as source,
                    open(new_file_name, "w") as new_file):
                new_file.write(source.read())
            print("Copying done!")
        except FileNotFoundError as e:
            print(e)
