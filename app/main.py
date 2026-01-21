def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "cp":
        print("Invalid command!")
        return

    source_file, destination_file = parts[1], parts[2]

    if source_file == destination_file:
        print("It is impossible to copy yourself.")
        return

    try:
        with open(source_file, "r") as f_source, \
             open(destination_file, "w") as f_destination:
            f_destination.write(f_source.read())
    except Exception as e:
        print(f"Copy error: {e}")
