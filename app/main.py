def copy_file(command: str) -> None:
    # Split the command string into its components
    parts = command.split()

    # Check if the command has exactly 3 parts
    if len(parts) != 3:
        print(
            "Invalid command format. "
            "Please provide command in the format: cp old_file new_file"
        )
        return

    # Extract the filenames from the command
    _, old_file, new_file = parts

    # Check if the old_file and new_file are the same
    if old_file == new_file:
        print(
            "The source and destination filenames are the same. "
            "Nothing to do."
        )
        return

    # Copy the content of old_file to new_file
    try:
        with open(old_file, "r") as file_in, open(new_file, "w") as file_out:
            file_out.write(file_in.read())
        print(f"File '{old_file}' copied to '{new_file}' successfully.")
    except FileNotFoundError:
        print(f"Error: File '{old_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


# Example use:
copy_file("cp file.txt file.txt")  # Does nothing

copy_file("cp file.txt new_file.txt")
print(open("file.txt").read() == open("new_file.txt").read())  # True
