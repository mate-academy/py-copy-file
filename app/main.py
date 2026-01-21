def copy_file(command: str) -> None:
    try:
        operation, file_name, destination = command.split()

        if file_name == destination or operation != "cp":
            return

        try:
            with (open(file_name, "r") as file_in,
                  open(destination, "w") as file_out):
                file_out.write(file_in.read())
        except FileNotFoundError:
            print(f"File '{file_name}' not found!")
    except ValueError:
        print("Invalid command format!")
