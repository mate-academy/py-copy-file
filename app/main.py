def copy_file(command: str) -> None:
    parts = command.split(" ")
    if len(parts) < 3 or parts[1] == parts[2]:
        raise ValueError("Invalid command")

    try:
        with open(parts[1], "r") as source_file:
            with open(parts[2], "w") as destination_file:
                destination_file.write(source_file.read())
    except FileNotFoundError:
        print("One of the specified files does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
