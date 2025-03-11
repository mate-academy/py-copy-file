def copy_file(commend: str) -> None:
    splitted = commend.split(" ")
    if len(splitted) == 3 and splitted[0] == "cp":
        try:
            with (open(splitted[1], "r") as file_in,
                  open(splitted[2], "w") as file_out):
                file_out.write(file_in.read())
        except FileNotFoundError:
            print("No such file or directory")
