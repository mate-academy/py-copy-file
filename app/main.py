def copy_file(command: str) -> None:
    _, target, new_name = command.split()

    if target == new_name:
        return

    with open(target, "r") as file_in, open(new_name, "w") as file_out:
        file_out.write(file_in.read())
