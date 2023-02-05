def copy_file(command: str) -> None:

    if command.count(" ") > 2 or command.count(" ") < 2:
        return "wrong command"

    command, old_file, new_file = command.split(" ")
    if old_file == new_file:
        return

    with open(old_file, "r") as file_in, open(new_file, "w") as file_out:
        data = file_in.read()
        file_out.write(data)
