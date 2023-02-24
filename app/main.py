def copy_file(command: str) -> None:
    sep_command = command.split(" ")
    if len(sep_command) == 3:
        if sep_command[1] != sep_command[2] and sep_command[0] == "cp":
            try:
                with (
                    open(sep_command[1], "r") as file_in,
                    open(sep_command[2], "w") as file_out
                ):
                    file_out.write(file_in.read())
            except FileNotFoundError:
                print("No such file in directory")


copy_file(input("Enter your command: "))
