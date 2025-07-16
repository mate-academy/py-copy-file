def copy_file(copy_string: str) -> None:
    if not copy_string:
        return
    parts = copy_string.strip().split()
    if len(parts) != 3 or parts[0] != "cp":
        return
    _, source, destination = parts
    if source == destination:
        return
    try:
        with open(source, "r") as file_in, open(destination, "w") as file_out:
            file_out.write(file_in.read())
    except FileNotFoundError:
        print(f"File not found: {source}")
    except Exception as e:
        print(f"Error copying file: {e}")
