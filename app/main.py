def copy_file(string: str) -> None:
    string = string.split(" ")
    command = string[0]
    file_name = string[1]
    new_file_name = string[2]
    if command == "cp" and file_name != new_file_name:
        with open(f"{file_name}", "r") as file:
            content = file.read()

        with open(f"{new_file_name}", "w") as new_file:
            new_file.write(content)
