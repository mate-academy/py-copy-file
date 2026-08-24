def copy_file(command: str) -> None:
    if command.startswith("cp "):
        list_of_com = command.split()
        if len(list_of_com) == 3:
            try:
                with (open(list_of_com[1], "r") as file_in,
                      open(list_of_com[2], "w") as file_out):
                    if file_in != file_out:
                        file_out.write(file_in.read())
            except FileNotFoundError:
                print("No such file or directory.")
