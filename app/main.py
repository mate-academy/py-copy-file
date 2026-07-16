from os.path import exists


def copy_file(command: str) -> None:
    parts_of_command = command.split()

    if (len(parts_of_command) == 3
            and parts_of_command[1] != parts_of_command[2]
            and parts_of_command[0] == "cp"):
        if exists(parts_of_command[1]):
            with (open(parts_of_command[1], "r") as existing_file,
                  open(parts_of_command[2], "w") as file_copy):
                file_copy.write(existing_file.read())
