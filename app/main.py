def copy_file(command: str) -> None:
    file_name_number1 = command.split(" ")[1]
    file_name_number2 = command.split(" ")[2]
    if not file_name_number1 == file_name_number2:
        with (open(file_name_number1, "r") as file_in,
              open(file_name_number2, "w") as file_out):
            file_out.write(file_in.read())
