def copy_file(command: str) -> None:
    # Split the command into parts
    parts = command.split()

    # Check if the command is valid
    # (it should be in the format "cp source destination")
    if len(parts) != 3 or parts[0] != "cp":
        print("Invalid command format. Use 'cp source destination'.")
        return

    source_file = parts[1]
    destination_file = parts[2]

    # Check if the source and destination files are the same
    if source_file == destination_file:
        return  # Do nothing

    # Try to copy the content of the source file to the destination file
    try:
        with (open(source_file, "r") as file_in,
              open(destination_file, "w") as file_out):
            file_out.write(file_in.read())
    except FileNotFoundError:
        print(f"Error: '{source_file}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
