def copy_file(command: str) -> None | str:
    command = command.split()
    original = command[1]
    copy_original = command[2]

    if command[0] != "cp":
        return "Error: unknown command"
    if original == copy_original:
        return

    with open(original, "r") as file_in, open(copy_original, "w") as file_out:
        file_out.write(file_in.read())
