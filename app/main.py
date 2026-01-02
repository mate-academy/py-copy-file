def copy_file(command: str) -> None:
    file_names = command.split()

    if len(file_names) != 3:
        return

    action, source, target = file_names

    if action != "cp":
        return

    if source == target:
        return

    try:
        with open(source, "r") as file_one, open(target, "w") as file_two:
            for line in file_one:
                file_two.write(line)
    except FileNotFoundError:
        print(f"Error: Source file '{source}' does not exist.")
