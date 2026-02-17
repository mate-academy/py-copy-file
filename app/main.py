def copy_file(command: str) -> None:
    words = command.split()
    if words:
        if words[0] == "cp" and len(words) == 3:
            file_in_name = words[1]
            file_out_name = words[2]
            if not file_in_name == file_out_name:
                try:
                    with open(
                        file_in_name, "r"
                    ) as file_in, open(
                        file_out_name, "w"
                    ) as file_out:
                        file_in_input = file_in.read()
                        file_out.write(file_in_input)
                except FileNotFoundError:
                    return
