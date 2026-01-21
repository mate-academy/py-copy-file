def copy_file(command: str) -> None:
    parts = command.strip().split()

    if len(parts) != 3 or parts[0] != "cp":
        return

    _, source, target = parts

    if source == target:
        return

    try:
        with open(source, "r") as file_in, open(target, "w") as file_out:
            file_out.write(file_in.read())
    except FileNotFoundError:
        print(f"File '{source}' not found.")
    except Exception as e:
        print(f"Error: {e}")
