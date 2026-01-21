def command_validation(command: str) -> None:
    if len(command.split(" ")) != 3:
        raise ValueError
    if "cp" not in command:
        raise ValueError
    if command.split(" ")[1] == command.split(" ")[2]:
        raise ValueError
    with open(command.split(" ")[1]):
        pass


def copy_file(command: str) -> None:
    try:
        command_validation(command)
    except Exception as ex:
        print(f"Your command isn't correct, here is the error: {ex}")
        return

    origin_file_name = command.split(" ")[1]
    copy_file_name = command.split(" ")[2]

    with open(origin_file_name, "r") as origin, open(copy_file_name, "w") as copy_file:  # noqa: E501
        content = origin.read()
        copy_file.write(content)
