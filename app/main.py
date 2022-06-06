def copy_file(command: str):
    lst = command.split(" ")
    if lst[0] == "cp" and lst[1] != lst[2]:
        with open(f"{lst[1]}", "r") as file_in, open(f"{lst[2]}", "w") as file_out:
            file_out.write(file_in.read())
