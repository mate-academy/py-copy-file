import os


def copy_file(command: str) -> None:
    """
    Copy a file in the current directory like the Linux cp command.

    Args:
        command (str): A string with the command 'cp', source file name,
                       and destination file name, separated by spaces.
    """
    # Split the command into parts
    parts = command.split()

    # Check if the command is valid and has the correct format
    if len(parts) != 3 or parts[0] != "cp":
        return

    # Extract source and destination file names
    source_file = parts[1]
    dest_file = parts[2]

    # Do nothing if source and destination files are the same
    if source_file == dest_file:
        return

    # Check if the source file exists
    if not os.path.exists(source_file):
        print(f"Error: File '{source_file}' not found.")
        return

    # Copy the content from source to destination
    with open(source_file, "r") as file_in, open(dest_file, "w") as file_out:
        file_out.write(file_in.read())


if __name__ == "__main__":
    # Example usage
    copy_file("cp file.txt new_file.txt")
