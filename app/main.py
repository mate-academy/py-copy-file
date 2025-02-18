def copy_file(command: str) -> None:
    if len(command) == 3 and command.startswith("cp"):
        cp_command, file_for_copy, new_file = command.split()

        if file_for_copy != new_file:
            with (open(file_for_copy, "r") as file_in,
                  open(new_file, "w") as file_out):
                file_out.write(file_in.read())
