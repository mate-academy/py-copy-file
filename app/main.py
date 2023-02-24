def copy_file(command: str) -> None:
    split = command.split(" ")
    if split[1] != split[2] and split[0] == "cp":
        try:
            with (open(split[1], "r") as file_in,
                  open(split[2], "w") as file_out
                  ):
                for line in file_in:
                    file_out.write(line)
        except FileNotFoundError:
            print("No such file in directory")


copy_file(input("Enter your command: "))
