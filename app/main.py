import os


def copy_file(command: str) -> None:
    # Split the command into parts
    parts = command.split()

    # Check if the command has the correct format
    if len(parts) != 3 or parts[0] != "cp":
        print("Invalid command format. "
              "Please use 'cp source_file target_file'.")
        return

    source_file = parts[1]
    target_file = parts[2]

    # Check if the source and target files are the same
    if source_file == target_file:
        print("Source and target files are the same. Nothing to do.")
        return

    # Check if the source file exists
    if not os.path.exists(source_file):
        print(f"Source file '{source_file}' does not exist.")
        return

    try:
        with (open(source_file, "rb") as file_in,
              open(target_file, "wb") as file_out):
            file_out.write(file_in.read())
        print(f"File '{source_file}' copied to '{target_file}' successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    copy_file("cp file.txt file-copy.txt")
