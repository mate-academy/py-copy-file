def copy_file(command: str) -> None:
    copy_command, first_file, second_new_file = command.split()

    if first_file != second_new_file and copy_command == "cp":
        with (open(first_file, "r") as from_first,
              open(second_new_file, "w") as to_second):
            for line in from_first:
                to_second.write(line)
