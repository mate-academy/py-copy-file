# write your code here
def copy_file(command):
    if not command.split()[1] == command.split()[2]:
        with open(command.split()[1], "r") as file_in, \
                open(command.split()[2], "w") as file_out:
            content = file_in.read()
            file_out.write(content)
