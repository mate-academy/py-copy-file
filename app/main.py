def copy_file(command: str, target_file: str, source_file: str) -> str:
    parts = command.split()
    if len(parts) != 3 or parts != "cp":
        return "Invalid command. Please provide a valid 'cp' command."

    if source_file[1] == target_file[2]:
        return

    with open(source_file, "r") as file1, open(target_file, "w") as file2:
        new_file = file1.read()
        file2.write(new_file)
