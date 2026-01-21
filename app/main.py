def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "cp":
        print("Invalid command format. Use: cp <source> <destination>")
        return
    source, destination = parts[1], parts[2]
    if source == destination:
        print(f"File '{source}' cannot be copied to itself.")
        return
    try:
        with open(source, "r") as file_in, open(destination, "w") as file_out:
            file_out.write(file_in.read())
        print(f"File '{source}' successfully copied to '{destination}'.")
    except FileNotFoundError:
        print(f"Source file '{source}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
