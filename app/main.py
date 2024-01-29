def copy_file(command: str) -> None:
    operator, copies_file, new_file = command.split()
    if copies_file != new_file and operator == "cp":
        with (open(copies_file, mode="r") as file_input,
              open(new_file, mode="w") as file_output):
            file_output.write(file_input.read())
