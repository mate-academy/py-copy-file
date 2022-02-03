def copy_file(command):
    user_command = command.split()
    if user_command[0] == "cp" and user_command[1] != user_command[2]:
        with open(f"{user_command[1]}", "r") as fin:
            with open(user_command[2], "w") as fout:
                for line in fin:
                    fout.write(line)


copy_file("cp file.txt new_file.txt")
