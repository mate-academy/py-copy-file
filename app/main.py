def copy_file(command: str) -> None:
    path, source_name, new_file = command.split(" ")
    if path != "cp" or not (
            source_name.endswith(".txt")
            | new_file.endswith(".txt")
    ):
        raise ValueError("Check your command and try again")
    if source_name == new_file:
        raise NameError("Names should not have the same name")
    if open(source_name).read() == open(new_file).read():
        raise ValueError("Content was copied yet")
    try:
        source = open(source_name, "r")
    except (FileNotFoundError, IOError):
        print("File not found")
    else:
        with source as file_in, open(new_file, "a") as file_out:
            for line in file_in:
                file_out.write(line)
        print(f"File {source_name} copied to {new_file} successfully")
        file_in.close()
        file_out.close()
