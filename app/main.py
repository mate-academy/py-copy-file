def copy_file(command: str) -> None:
    _, input_file, output_file = command.split()
    if input_file != output_file:
        with open(input_file, "rb") as f_in, open(output_file, "wb") as f_out:
            f_out.write(f_in.read())
