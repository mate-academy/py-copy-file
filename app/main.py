# write your code here
def copy_file(command: str) -> None:
    user_command = command.split()
    if len(user_command) != 3:
        return
    origin = user_command[1]
    copy = user_command[2]
    if origin == copy:
        return
    try:
        with open(origin, "r") as file_in, open(copy, "w") as file_out:
            file_out.write(file_in.read())
    except FileNotFoundError:
        return


copy_file("cp file.txt file.txt")
