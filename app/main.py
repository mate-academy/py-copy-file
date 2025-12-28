def copy_file(command: str) -> None:
    command_list = command.split(" ")
    if command_list[0] == "cp" and len(command_list) == 3:
        if command_list[1] != command_list[2]:
            try:
                with (open(command_list[1], "r") as file_input,
                      open(command_list[2], "w") as file_output):
                    for line in file_input:
                        file_output.write(line)
            except FileNotFoundError:
                print("File not found")

            except PermissionError:
                print("Permission denied")
            except IOError:
                print("Error writing to file")
            except Exception:
                print("Something else went wrong")
        else:
            return
    else:
        return
