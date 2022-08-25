def copy_file(command):
    temp = command.split()
    if temp[0] == "cp" and temp[-1] != temp[-2]:
        with open(f"{temp[-2]}", "r") as file_in, \
                open(f"{temp[-1]}", "w") as file_out:
            file_out.write(f"{file_in.read()}")
