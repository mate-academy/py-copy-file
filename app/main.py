def copy_file(command: str) -> None:
    file_names = command.split()[1:]
    file_one = file_names.split()[0]
    file_two = file_names.split()[1]

    if file_one != file_two:
        with open(file_one, "r") as file_in, open(file_two, "w") as file_out:
            file_out.write(file_in.read)
