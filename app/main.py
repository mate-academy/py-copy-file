import shutil


def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "cp":
        raise ValueError("Invalid command format. Use: "
                         "'cp source_file destination_file'")

    source, destination = parts[1], parts[2]

    if source == destination:
        return  # Do nothing if the source and destination are the same

    try:
        with open(source, "r") as file_in, open(destination, "w") as file_out:
            shutil.copyfileobj(file_in, file_out)
    except FileNotFoundError:
        print(f"Error: The file '{source}' does not exist.")
    except IOError as e:
        print(f"Error: {e}")
