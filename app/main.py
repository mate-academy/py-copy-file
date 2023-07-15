
def copy_file(command: str) -> None:
    command, first_file, second_file = command.split()
    if not first_file == second_file:
        with (open(first_file, "r") as f_to_read,
              open(second_file, "w") as f_to_write):
            f_to_write.write(f_to_read.read())
