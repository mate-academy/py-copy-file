def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3:
        return

    _, filename, new_filename = parts
    if filename == new_filename:
        return

    try:
        with open(filename, "rb") as source,\
                open(new_filename, "wb") as destination:
            destination.write(source.read())
    except FileNotFoundError:
        print(f"File not found: {filename}")
    except Exception as e:
        print(f"An error occurred: {e}")
