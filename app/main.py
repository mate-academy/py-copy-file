def copy_file(command: str):
    requirements = command.split()
    if requirements[0] == "cp" and requirements[1] != requirements[2]:
        with open(requirements[1], "r") as file_in, \
                open(requirements[2], "w") as file_out:
            file_out.write(file_in.read())
