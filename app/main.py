def copy_file(command: str) -> None:
    file_name, new_file_name = command.split()[1:]
    with open(file_name, "r") as file_in, open(new_file_name, "w") as file_out:
        temp = file_in.read()
        file_out.write(temp)
        file_in.close()
        file_out.close()
