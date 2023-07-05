def copy_file(command: str) -> None:
    words = command.split()
    if len(words) >= 3:
        in_file_name = words[1]
        out_file_name = words[2]
    else:
        return "Incorrect command!"

    if in_file_name == out_file_name:
        return

    with open(in_file_name, "r") as file_in, \
            open(out_file_name, "w") as file_out:
        file_out.write(file_in.read())
