def copy_file(command: str) -> None:
    # Split the command string into its components
    parts = command.split()

    if len(parts) != 3:
        print(
            "Invalid command format. "
            "Please provide command in the format: cp old_file new_file"
        )
        return

    _, old_file, new_file = parts

    # Validate if the source and destination filenames are the same
    if old_file == new_file:
        print(
            "The source and destination filenames are the same. "
            "Nothing to do."
        )
        return

    # Validate the command
    if parts[0] != "cp":
        print("Invalid command. Please use 'cp' command.")
        return

    try:
        with open(old_file, "r") as file_in, open(new_file, "w") as file_out:
            file_out.write(file_in.read())
        print(f"File '{old_file}' copied to '{new_file}' successfully.")
    except FileNotFoundError:
        print(f"Error: File '{old_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
