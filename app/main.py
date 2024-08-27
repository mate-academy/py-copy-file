def copy_file(command: str) -> None:
    part = command.split()
    if len(part) != 3 or part[0] != "cp":
        return
    source = part[1]
    destination = part[2]
    if source == destination:
        return
    try:
        with open(source, "r") as old_name, open(destination, "w") as new_file:
            new_file.write(old_name.read())
    except FileNotFoundError:
        print(f"File {source} does not exist.")
    except Exception as e:
        print(str(e))
