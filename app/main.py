def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "cp":
        raise ValueError(
            "Invalid command format. Use 'cp source_file destination_file'."
        )

    source_file = parts[1]
    destination_file = parts[2]

    if source_file == destination_file:
        return

    try:
        with open(source_file, "r") as file_in:
            with open(destination_file, "w") as file_out:
                file_out.write(file_in.read())
    except FileNotFoundError:
        print(f"Error: '{source_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    copy_file("cp file.txt new_file.txt")
