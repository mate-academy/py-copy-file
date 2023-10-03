def copy_file(command: str) -> None:
    comm, file_name_number1, file_name_number2 = command.split()
    if file_name_number1 != file_name_number2 and comm == "cp":
        with (open(file_name_number1, "r") as file_in,
              open(file_name_number2, "w") as file_out):
            file_out.write(file_in.read())
