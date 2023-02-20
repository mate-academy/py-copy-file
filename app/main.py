def copy_file(comand: str) -> None:
    names = comand.split(" ")
    if names[1] == names[2]:
        print("Does nothing")
    if names[1] != names[2]:
        with open(names[1], "r") as file_in, open(names[2], "w") as file_out:
            for i in file_in:
                file_out.write(i)
