def copy_file(command: str) -> None:
    if command:
        split_command = command.split(" ")

        if len(split_command) == 3 and split_command[0] == "cp":
            file_name1 = split_command[1]
            file_name2 = split_command[2]

            if file_name1 == file_name2:
                return

            with open(file_name1, "r") as f1, open(file_name2, "w") as f2:
                for line in f1.readlines():
                    f2.write(line)
