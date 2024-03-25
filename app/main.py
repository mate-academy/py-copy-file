def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3:
        print("Invalid command format. "
              "Please provide a command in the format: "
              "cp file.txt new_file.txt")
        return

    cp_command, source_file, destination_file = parts

    if source_file == destination_file:
        print("Source and destination files are the same. Nothing to do.")
        return

    try:
        with open(source_file, "r") as file_in, open(destination_file, "w") as file_out:
            file_out.write(file_in.read())  # Copy content from source file to destination file
        print("File copied successfully.")
    except FileNotFoundError:
        print("One of the files does not exist.")
