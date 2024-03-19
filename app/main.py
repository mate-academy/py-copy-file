def copy_file(command: str) -> None:
    command, initial_file, final_file = command.split(" ")
    if len(command) >= 3:
        if command == "cp":
            with (open(initial_file, "r") as file_old,
                  open(final_file, "w") as file_new):
                copy_value = file_old.readline()
                file_new.write(copy_value)
