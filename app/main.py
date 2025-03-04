def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "cp":
        print("Invalid command format. "
              "Use 'cp <source_file> <destination_file>'")
        return
    source_file, destination_file = parts[1], parts[2]

    if source_file == destination_file:
        print("The files are identical. No action was taken")
        return

    try:
        with (open(source_file, "r") as file_in,
              open(destination_file, "w") as file_out):
            file_out.write(file_in.read())
        print(f"File '{source_file}' copied to '{destination_file}'")

    except FileNotFoundError:
        print(f"Error: '{source_file}' not found.")
