def copy_file(copy_data: str) -> None:
    command, file_name, new_file = copy_data.split()

    if command == "cp" and file_name != new_file:
        with open(file_name, "r") as file_in, open(new_file, "w") as file_out:
            file_out.write(file_in.read())
