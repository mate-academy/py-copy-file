def copy_file(command: str) -> None:

    parts = command.split()

    if len(parts) != 3 or parts[0] != "cp":
        print("Invalid command format.")
        return

    source_file, new_file = parts[1], parts[2]

    if source_file == new_file:
        print("No action taken.")
        return

    try:
        with (
            open(source_file, "r") as file_in,
            open(new_file, "w") as file_out
        ):

            file_out.write(file_in.read())
        print(f"Successfully copied {source_file} content to {new_file}.")

    except FileNotFoundError:
        print(f"Error: The file {source_file} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}.")
