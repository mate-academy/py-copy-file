def copy_file(command: str) -> None:
    list_of_com = command.split()
    if len(list_of_com) > 0 and list_of_com[0] == "cp":
        try:
            with (open(list_of_com[1], "r") as file_in,
                  open(list_of_com[2], "w") as file_out):
                if file_in != file_out:
                    file_out.write(file_in.read())
        except FileNotFoundError:
            print("No such file or directory.")
        except IndexError:
            print("The command is incorrect."
                  "Here is an example: cp file.txt file.txt")
