def copy_file(command: str) -> None:
    command = command.split()
    if len(command) < 3:
        return
    if "cp" not in command:
        return
    elif command[1] == command[2]:
        return
    try:
        with (open(f"{command[1]}", "r") as file,
              open(f"{command[2]}", "w") as file_copy):
            for row in file:
                file_copy.write(row)
    except FileNotFoundError:
        return
