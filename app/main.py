def copy_file(command: str) -> None:
    inputs = command.split()

    if len(inputs) > 3 or inputs[0] != "cp":
        raise ValueError("Invalid command format.")

    src_filename = inputs[1]
    dst_filename = inputs[2]

    if src_filename == dst_filename:
        return

    with (
        open(f"./{src_filename}", "r")as file_in,
        open(f"./{dst_filename}", "w") as file_out
    ):
        content = file_in.read()
        file_out.write(content)
