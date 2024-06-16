def copy_file(command: str) -> None:
    first_file, second_file = command[3:].split(" ")
    if first_file == second_file:
        pass
    else:
        content = []
        with open(first_file, "r") as file_data:
            content = file_data.read()
        with open(second_file, "w") as file_copy:
            file_copy.write(content)
