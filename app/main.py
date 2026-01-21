def copy_file(command: str) -> None:
    parts = command.strip().split()

    if len(parts) != 3:
        print("Error: "
              "command must have exactly three parts:"
              " 'cp source target'")
        return

    if parts[0] != "cp":
        print("Error: command must start with 'cp'")
        return

    cp, source, target = parts

    if source == target:
        return

    try:
        with open(source, "r") as file_in, open(target, "w") as file_out:
            for line in file_in:
                file_out.write(line)
    except FileNotFoundError:
        print(f"File '{source}' not found.")
