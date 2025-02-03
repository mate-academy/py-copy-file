def copy_file(command: str) -> None:
    data = command.split()

    if data[1] == data[2]:
        return

    try:
        with open(data[1], "r") as f_in, open(data[2], "w") as f_out:
            file_data = f_in.read()
            f_out.write(file_data)
    except FileNotFoundError:
        print(f"Error: {data[1]} not found.")
    except PermissionError:
        print("Error: Permission denied to read/write files.")
