def copy_file(command: str) -> None:
    linux_command, source_name, new_file = command.split(" ")
    if (
            linux_command != "cp" or not (
            source_name.endswith(".txt") or
            new_file.endswith(".txt")
    )):
        raise ValueError("Check your command and try again")
    if source_name == new_file:
        raise ValueError("Names should not have the same name")
    try:
        source = open(source_name, "r")
    except (FileNotFoundError, IOError):
        print("File not found")
    else:
        with source as file_in, open(new_file, "w") as file_out:
            file_out.write(file_in.read())
        print(f"File {source_name} copied to {new_file} successfully")
