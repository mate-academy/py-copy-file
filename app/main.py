def copy_file(command: str) -> None:
    if len(command.split()) != 3:
        return "wrong command"

    command, old_file, new_file = command.split(" ")

    if old_file == new_file:
        return "the file names do match"

    if command == "cp":
        with open(old_file, "r") as file_in, open(new_file, "w") as file_out:
            data = file_in.read()
            file_out.write(data)
    else:
        return f"unknown command '{command}'"
