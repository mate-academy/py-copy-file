def copy_file(command: str) -> None:
    ls = command.split(" ")
    if len(ls) == 3:
        if ls[0] == "cp":
            if ls[1] == ls[2]:
                print("Does nothing")
            with open(ls[1], "r") as file_in, open(ls[2], "w") as file_out:
                file_out.write(file_in.read())
