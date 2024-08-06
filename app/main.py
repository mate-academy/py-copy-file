def copy_file(command: str) -> None:
    action, source_file, destination_file = command.split()

    if action != "cp" or len(command.split()) != 3:
        raise ValueError("Command in wrong format")
    if source_file != destination_file:
        try:
            with (
                open(source_file, "r") as file_in,
                open(destination_file, "w") as file_out
            ):
                file_out.write(file_in.read())
        except FileNotFoundError:
            print(f"Error: The file {source_file} does not exist.")
        except Exception as e:
            print(f"Error occurred: {e}")
