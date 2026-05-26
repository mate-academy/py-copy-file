def copy_file(command: str) -> None:
    com_split = command.split(" ")
    if len(com_split) == 3 and com_split[0] == "cp":
        part_1 = com_split[1]
        part_2 = com_split[2]
        try:
            with open(part_1, "r") as file_in, open(part_2, "w") as file_out:
                for line in file_in:
                    file_out.write(line)
        except FileNotFoundError:
            pass
