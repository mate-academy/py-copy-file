from re import match


def copy_file(command: str) -> None:
    command_check = match(r"cp .*\.txt .*\.txt", command)

    if command_check:
        first_file_name = command.split()[1]
        second_file_name = command.split()[2]

        if first_file_name != second_file_name:
            with (open(first_file_name, "r") as first_file,
                  open(second_file_name, "w") as second_file):
                for line in first_file:
                    second_file.write(line)
