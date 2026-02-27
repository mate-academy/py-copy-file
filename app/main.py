def copy_file(command: str) -> None:
    if len(command) != 0:
        instructions = command.split(" ")
        if len(instructions) == 3:
            file_in_name = instructions[1]
            file_out_name = instructions[2]
            if instructions[0] == "cp" and file_in_name != file_out_name:
                try:
                    with open(file_in_name, "r") as file_in, \
                            open(file_out_name, "w") as file_out:
                        for line in file_in.readlines():
                            file_out.write(line)
                except FileNotFoundError:
                    print(f"The file {file_in_name} does not exist.")
