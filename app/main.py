def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3:
        print("Invalid command")
        return

    cmd, file_name, new_file_name = parts

    if cmd == "cp" and file_name != new_file_name:
        try:
            with (open(file_name, "r") as file_in,
                  open(new_file_name, "w") as file_out):
                file_out.write(file_in.read())
        except FileNotFoundError:
            print("File not found")
