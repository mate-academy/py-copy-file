def copy_file(command: str) -> None:
    parts = command.split(" ")

    if (len(parts) != 3 or parts[0] != "cp"
            or not parts[1].endswith(".txt") or not parts[2].endswith(".txt")):
        return

    file1 = parts[1]
    file2 = parts[2]

    if file1 == file2:
        return

    try:
        with open(file1, "r") as file_in, open(file2, "w") as file_out:
            # read_content = file_in.read()
            file_out.write(file_in.read())
    except FileNotFoundError:
        print(f"Error: {file1} not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
