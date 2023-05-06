def copy_file(command: str) -> None:
    split_command = command.split()
    cmd, input_path, output_path = split_command

    if len(split_command) != 3:
        raise ValueError(
            "Your command is wrong, try this format: 'cp file1.txt file2.txt'")
    if cmd != "cp":
        raise ValueError(
            "Your command is wrong, try this format: 'cp file1.txt file2.txt'")
    if input_path == output_path:
        return
    with open(input_path, "rb") as f_in, open(output_path, "wb") as f_out:
        f_out.write(f_in.read())
