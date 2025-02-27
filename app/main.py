def copy_file(command: str) -> None:
    """
    Copies a file in the current directory like the Linux cp command.

    Args:
        command: A string with the command "cp", the file name to copy,
                 and the new file name, separated by spaces.
    """
    parts = command.split()
    if len(parts) != 3 or parts[0] != "cp":
        return  # Invalid command

    source_file = parts[1]
    destination_file = parts[2]

    if source_file == destination_file:
        return  # Do nothing if source and destination are the same

    try:
        with open(source_file, "r") as file_in, \
                open(destination_file, "w") as file_out:
            file_out.write(file_in.read())
    except FileNotFoundError:
        pass  # do nothing if file not found.


# Example usage:
# Create a dummy file for testing
with open("file.txt", "w") as f:
    f.write("This is a test file.")

copy_file("cp file.txt file.txt")  # Does nothing
copy_file("cp file.txt new_file.txt")

try:
    print(open("file.txt").read() == open("new_file.txt").read())
except FileNotFoundError:
    print("One of the files was not created.")

# test for file not found
copy_file("cp file_not_found.txt new_file_2.txt")

# test for bad command
copy_file("copy bad command")

# test for bad command
copy_file("cp file.txt")
