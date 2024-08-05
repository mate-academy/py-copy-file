def copy_file(command: str) -> None:
    com = command.split()
    source_file = com[1]
    destination_file = com[2]
    if len(com) != 3 or com[0] != "cp":
        raise ValueError("Command should be in wrong format")
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
