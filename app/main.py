def copy_file(command: str) -> None:
    split_command = command.split()

    if len(split_command) != 3:
        return

    if split_command[0] != "cp":
        return

    first = split_command[1]
    sec = split_command[2]

    # якщо однакові — нічого не робимо
    if first == sec:
        return

    try:
        with open(first, "r") as file, open(sec, "w") as new_file:
            for line in file:
                new_file.write(line)
    except FileNotFoundError:
        return
