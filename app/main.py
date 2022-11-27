def copy_file(command: str) -> None:
    command, file, new_file = command.split()

    if file != new_file and command == "cp":
        with open(file, "r") as current_file, open(new_file, "a") as copy:
            for line in current_file.readlines():
                copy.write(f"{line}\n")
