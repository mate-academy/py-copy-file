def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "cp":
        print("Invalid command format. Please provide command in the format: cp file.txt new_file.txt")  # noqa: E501
        return

    source_file = parts[1]
    destination_file = parts[2]

    if source_file == destination_file:
        print("Source and destination file names are the same. No action taken.")  # noqa: E501
        return

    try:
        with open(source_file, "r") as file_in, open(destination_file, "w") as file_out:  # noqa: E501
            file_out.write(file_in.read())
        print(f"File '{source_file}' copied to '{destination_file}' successfully.")  # noqa: E501
    except FileNotFoundError:
        print(f"Error: One or both of the files '{source_file}' and/or '{destination_file}' not found.")  # noqa: E501


copy_file("cp file.txt file.txt")

copy_file("cp file.txt new_file.txt")
print(open("file.txt").read() == open("new_file.txt").read())
