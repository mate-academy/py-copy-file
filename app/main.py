def copy_file(command: str) -> None:
    _command = command.split()
    if len(_command) != 3:
        print("Wrong command!")
        return
    cp, name, new_name = _command
    if cp != "cp":
        print('Command should be "cp".')
        return
    if name == new_name:
        print("This file exists.")
        return
    with (
        open(name, "r") as source_file,
        open(new_name, "w") as new_file
    ):
        new_file.write(source_file.read())
