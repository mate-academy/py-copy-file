def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "cp":
        return
    source = parts[1]
    destination = parts[2]
    if source == destination:
        return
    try:
        with open(source, "r") as old_file, open(destination, "w") as new_file:
            new_file.write(old_file.read())
    except FileNotFoundError:
        print(f"File {source} does not exist.")
    except Exception as e:
        print(e)
