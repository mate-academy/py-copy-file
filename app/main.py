def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "cp":
        raise ValueError("Invalid command format")

    old_file = parts[1]
    new_file = parts[2]

    if old_file == new_file:
        print("Nothing to do.")
        return

    try:
        with open(old_file, "r") as file_in, open(new_file, "w") as file_out:
            for line in file_in:
                file_out.write(line)
        print(f"File '{old_file}' successfully copied to '{new_file}'")
    except FileNotFoundError:
        print(f"File '{old_file}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
