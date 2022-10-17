def copy_file(command: str) -> None:
    file_name = command.split()
    if file_name[1] != file_name[2]:
        with open(file_name[1], "r") as file_in, \
             open(file_name[2], "w") as file_out:
            result = file_in.read()
            file_out.write(result)
