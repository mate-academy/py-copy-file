def copy_file(command: str) -> None:
    operation, file_name, destination = command.split()

    try:
        if file_name != destination and operation == "cp":
            with (open(file_name, "r") as file_in,
                  open(destination, "w") as file_out):
                file_out.write(file_in.read())
    except FileNotFoundError:
        print("File not found")
