def copy_file(command: str) -> None:
    operator, copies_file, result_file = command.split()
    if copies_file != result_file and operator == "cp":
        with (open(copies_file, "r") as file_in,
              open(result_file, "w") as file_out):
            file_out.write(file_in.read())
