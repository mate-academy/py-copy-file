def copy_file(command: str) -> None:
    _, initial_file, final_file = command.split(" ")
    with (open(initial_file, "r") as file_old,
          open(final_file, "w") as file_new):
        if command.startswith("cp"):
            copy_value = file_old.readline()
            file_new.write(copy_value)