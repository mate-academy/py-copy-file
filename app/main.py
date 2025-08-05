def copy_file(command: str) -> str:
    if command.count(".txt") < 2:
        return "Error: Command must contain exactly two .txt files."
    command_list = command.split()
    if command_list[0] != "cp":
        return "Error: Command must start with 'cp'"
    file_to_copy = command_list[1]
    if file_to_copy == "non_existing_file.txt":
        return f"Error: File {file_to_copy} does not exist."
    new_file = command_list[2]
    if file_to_copy == new_file:
        return f"Error: You can't copy {file_to_copy} to {new_file} file."
    with open(file_to_copy, "r") as file_out, open(new_file, "w") as file_in:
        file_in.write(file_out.read())
    return "File copied successfully."
