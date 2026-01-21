def copy_file(command: str) -> None:
    try:
        parts_of_command = command.split()
        if len(parts_of_command) == 3 and parts_of_command[0] == "cp":
            original_file = parts_of_command[1]
            copied_file = parts_of_command[2]

            if original_file != copied_file:
                with (open(original_file, "r") as file_out,
                      open(copied_file, "w") as file_in):
                    file_in.write(file_out.read())
    except FileNotFoundError:
        pass
