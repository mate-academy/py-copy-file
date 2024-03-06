def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) == 3 and parts[0] == "cp":
        source, destination = parts[1], parts[2]
        if source == destination:
            return
        try:
            with (open(source, "r") as file_in,
                  open(destination, "w") as file_out):
                file_out.write(file_in.read())
        except FileNotFoundError:
            print(f"File {source} not found.")
        else:
            print("Invalid command format.")
