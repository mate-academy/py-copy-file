def copy_file(command: str) -> None:
    if len(command.split()) == 3:
        cmd, file_copy, file_new = command.split()
    if cmd != "cp" or file_copy == file_new:
        raise ValueError("Invalid command or file names are the same.")

    try:
        with (
            open(file_copy, "r") as file_in,
            open(file_new, "w") as file_out
        ):
            content_in = file_in.read()
            file_out.write(content_in)
    except ValueError:
        print("ValueError: Data entry error.")
    except Exception as e:
        print(f"Error copying the file: {e}")
