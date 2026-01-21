def copy_file(command: str) -> None:
    if not command.startswith("cp "):
        print("Wrong command. Command should start with 'cp'.")
        return

    parts = command.split()

    if len(parts) != 3:
        print("Wrong command. Command should have exactly three parts.")
        return

    source_file = parts[1].strip()
    copied_file = parts[2].strip()

    if source_file == copied_file:
        return

    try:
        with open(
            source_file,
            mode="r"
        ) as file, open(
            copied_file,
            mode="w"
        ) as new_file:
            data = file.read()
            new_file.write(data)
        print(f"File {source_file} successfully copied to {copied_file}.")
    except FileNotFoundError:
        print(f"Error: file {source_file} not found")
    except IOError as e:
        print(f"Error: {e}")
