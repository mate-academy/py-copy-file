def copy_file(command: str) -> str:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "cp":
        print("Invalid command. Please provide a valid 'cp' command.")
        return

    source_file, target_file = parts[1], parts[2]

    if source_file == target_file:
        print("Source and target file paths are the same. No action taken.")
        return

    try:
        with open(source_file, "r") as file1, open(target_file, "w") as file2:
            file2.write(file1.read())
    except Exception as e:
        print(f"An error occurred: {str(e)}")
