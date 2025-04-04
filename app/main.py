def copy_file(command: str) -> None:
    try:
        parts = command.split()
        if len(parts) != 3 or parts[0] != "cp":
            return

        file_name, new_file = parts[1], parts[2]

        if file_name == new_file:
            return

        with open(file_name, "r") as file_in, open(new_file, "w") as file_out:
            file_out.write(file_in.read())

    except FileNotFoundError:
        print("No such file")
