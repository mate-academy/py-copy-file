def copy_file(command: str) -> None:
    command, old_file, new_file = command.split()
    if command != "cp" or len(command.split()) != 3:
        print("Incorrect command")
    elif old_file != new_file:
        with (open(old_file, "r") as file_in,
              open(new_file, "w") as file_out):
            file_out.write(file_in.read())

