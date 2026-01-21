def copy_file(command: str) -> None:

    if not command.strip():
        return

    command_elements = command.split()

    if len(command_elements) != 3 or command_elements[0] != "cp":
        return

    _, source_file, destination_file = command_elements

    if source_file == destination_file:
        return

    try:
        with (open(source_file, "r") as file_in,
              open(destination_file, "w") as file_out):
            file_out.write(file_in.read())
    except FileNotFoundError:
        print(f"Error: The file {source_file} does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    copy_file("cp file.txt new_file.txt")
