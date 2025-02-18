def copy_file(command: str) -> None:
    file_names = command.split()
    if len(file_names) != 3 or file_names[0] != "cp":
        return

    if file_names[1] == file_names[2]:
        return

    try:
        with (
            open(file_names[1], "r") as file_in,
            open(file_names[2], "w") as file_out
        ):
            file_out.write(file_in.read())
    except FileNotFoundError:
        print(f"File '{file_names[1]}' not found.")
    except Exception as e:
        print(f"Error: {e}.")
