def copy_file(command: str) -> None:
    try:
        command_name, source, destination = command.split()
    except ValueError:
        print("Invalid command format. Usage: cp <source> <destination>")
        return

    if command_name != "cp":
        return

    if source == destination:
        return

    with open(source, "r") as file_in, open(destination, "w") as file_out:
        file_out.write(file_in.read())
