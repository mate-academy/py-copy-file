def copy_file(command: str) -> None:
    copy_command, copy_file, new_file = command.split()[2]

    if copy_file != new_file and copy_command == "cp":
        with open(copy_file, "r") as from_f, open(copy_file, "a") as in_f:
            for line in from_f:
                in_f.write(line)
