import os


def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "cp":
        raise ValueError(
            "Invalid command format. Use 'cp source_file destination_file'."
        )

    source_file_path = parts[1]
    destination_file_path = parts[2]

    if source_file_path == destination_file_path:
        return

    if not os.path.isfile(source_file_path):
        print(
            f"Error: Source file '{source_file_path}' "
            "does not exist or is not a valid file."
        )

    try:
        with open(source_file_path, "r") as source_file:
            with open(destination_file_path, "w") as destination_file:
                destination_file.write(source_file.read())
        print("File copied successfully!")
    except FileNotFoundError:
        print(f"Error: '{source_file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    copy_file("cp file.txt new_file.txt")
