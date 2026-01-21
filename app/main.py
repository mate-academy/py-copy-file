def copy_file(cmd_name: str) -> None:
    cp_part, old_file, new_file = cmd_name.split()

    if cp_part != "cp":
        return

    if old_file == new_file:
        return

    try:
        with open(old_file, "r") as file_in, open(new_file, "w") as file_out:
            file_out.write(file_in.read())
    except FileNotFoundError as e:
        print(f"Error: Source file not found: {e}")
