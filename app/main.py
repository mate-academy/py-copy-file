def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "cp":
        print("The command is not correct")
        return

    cp_command, file_name, copy_name = parts
    if file_name == copy_name:
        print(f"File with a name: {copy_name} already exists")
        return

    try:
        with open(file_name, "r") as file_in, open(copy_name, "w") as file_out:
            for line in file_in:
                file_out.write(line)
    except Exception as e:
        print(f"Error: {e}")
