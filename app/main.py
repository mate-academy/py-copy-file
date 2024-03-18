def copy_file(command: str) -> None:
    split_command = command.split(" ")
    initial_file = split_command[1]
    final_file = split_command[2]
    with (open(initial_file, "r") as file_old,
          open(final_file, "w") as file_new):
        copy_value = file_old.readline()
        file_new.write(copy_value)
