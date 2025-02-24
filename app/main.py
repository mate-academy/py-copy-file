def copy_file(command: str) -> None:
    command = command.split()

    if len(command) != 3 or command[0] != "cp":
        print("Invalid command")
        return

    source_file = command[1]
    dest_file = command[2]

    if source_file == dest_file:
        return

    try:
        with open(source_file, "r") as file_in:
            with open(dest_file, "w") as file_out:
                file_out.write(file_in.read())
    except FileNotFoundError:
        print(f"The file {source_file} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
