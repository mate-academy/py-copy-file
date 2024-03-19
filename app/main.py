def copy_file(command: str) -> None:
    if len(command.split()) != 3:
        return "Command must be exactly 3 characters"
    command, initial_file, final_file = command.split(" ")
    if initial_file != final_file and command == "cp":
        with (open(initial_file, "r") as file_old,
              open(final_file, "w") as file_new):
            copy_value = file_old.read()
            file_new.write(copy_value)


copy_file("cp baba.txt apple.txt")
