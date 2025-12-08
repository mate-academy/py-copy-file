def copy_file(command: str) -> None:
    if command:
        try:
            parsed_command = command.split(" ")
            file_in, file_out = parsed_command[1], parsed_command[2]
            if parsed_command[0] == "cp":
                if file_in != file_out:
                    with (open(file_in, "r") as source,
                          open(file_out, "w") as target):
                        target.write(source.read())
        except IndexError:
            print("Invalid command")
        except FileNotFoundError:
            print("File not found")
            pass
        pass
