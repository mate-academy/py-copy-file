class FileNotFoundError(Exception):
    pass


def copy_file(command: str) -> None:
    operation, source_file, destination_file = command.split()

    if operation.lower() != "cp" or source_file == destination_file:
        print("Invalid operation or source/destination files are the same.")
        return

    try:
        with (open(source_file, "r") as file_in,
              open(destination_file, "w") as file_out):
            file_out.write(file_in.read())
    except FileNotFoundError:
        print(f"Error: One or both of the files ({source_file}, "
              f"{destination_file}) not found.")
