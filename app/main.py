def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3:
        print("Error: Invalid format.")
        return

    cp, file, new_file = parts

    if cp != "cp":
        print("Error: Command must start with 'cp'.")
        return

    if file == new_file:
        print("Error. File and new_file are the same file.")
        return

    try:
        with open(file, "r") as file_in, open(new_file, "w") as file_out:
            content = file_in.read()
            file_out.write(content)

    except FileNotFoundError:
        print("Error: File Not Found")
    except PermissionError:
        print("Error: Permission Error")
