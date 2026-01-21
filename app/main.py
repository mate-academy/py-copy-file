def copy_file(command: str) -> None:
    cp_name = command.split()[0]
    first_file_name = command.split()[1]
    second_file_name = command.split()[2]
    if cp_name == "cp":
        if first_file_name != second_file_name:
            with open(first_file_name, "r") as file_in, \
                 open(second_file_name, "w") as file_out:
                result = file_in.read()
                file_out.write(result)
