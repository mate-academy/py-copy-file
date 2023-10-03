def copy_file(command: str) -> None:
    # command = cp file.txt file-cope.txt

    file_name = command.split()
    if len(file_name) != 3:
        return "Command has exactly 3 parts!"

    _, main_file, destination_file = file_name

    if main_file == destination_file:
        return "Files are the same!"

    try:
        with (
            open(main_file, "r") as file_in,
            open(destination_file, "w") as file_out
        ):
            file_out.write(file_in.read())
        return "Files were copied successfully!"
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error: {e}")
