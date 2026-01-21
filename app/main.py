def copy_file(command: str) -> None:

    splitted_command = command.split(" ")

    if not command:
        return
    if len(splitted_command) != 3 or splitted_command[0] != "cp":
        return
    if splitted_command[1] == splitted_command[2]:
        return

    file_input = splitted_command[1]
    file_destination = splitted_command[2]

    try:
        with open(file_input, "r") as fin, open(file_destination, "w") as fout:
            fout.write(fin.read())
    except FileNotFoundError:
        return
