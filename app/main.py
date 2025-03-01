def copy_file(command: str) -> None:
    parts = command.split(" ")
    if len(parts) < 3:
        return
    *rest, file, new_file = parts
    if file == new_file:
        print("File name is the same, copying aborted.")
        return
    try:
        with open(f"{file}.txt", "r") as file_in, open(f"{new_file}.txt", "w") as file_out:
            file_out.write(file_in.read())
    except FileNotFoundError:
        print("No such file")
