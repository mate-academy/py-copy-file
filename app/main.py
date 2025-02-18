def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "cp":
        print("Invalid command")
        return

    source_file = parts[1]
    destination_file = parts[2]

    if source_file == destination_file:
        print("Source and destination file names are the same. Doing nothing.")
        return

    try:
        with (open(source_file, "r") as file_in,
              open(destination_file, "w") as file_out):
            file_out.write(file_in.read())
        print(f"File copied from {source_file} to {destination_file}")
    except FileNotFoundError:
        print(f"Error: {source_file} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
