def copy_file(command: str) -> None:
    if command:
        command_ = command.split()
        if len(command_) == 3 and command_[0] == "cp":
            source_file = command_[1]
            target_file = command_[2]
            if source_file != target_file:
                try:
                    with (open(source_file, "r") as file_in,
                          open(target_file, "w") as file_out):
                        for line in file_in:
                            file_out.write(line)
                except FileNotFoundError as e:
                    print(e)
