def copy_file(command: str) -> None:
    command_cp = command.split()
    if len(command_cp) != 3 or command_cp[0] != "cp":
        return

    cp, source, destination = command_cp

    if source == destination:
        return

    try:
        with open(source, "r") as file_in, open(destination, "w") as file_out:
            file_out.write(file_in.read())
    except FileNotFoundError:
        print(f"The file '{source}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
