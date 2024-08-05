class FileNotFound(Exception):
    pass


def copy_file(command: str) -> None:
    operation, file_name, destination = command.split()

    if operation != "cp" or file_name == destination:
        print("File error")

    try:
        with (open(file_name, "r") as file_in,
              open(destination, "w") as file_out):
            file_out.write(file_in.read())

    except FileNotFound:
        raise "File not found"
