def copy_file(command: str) -> None:
    comnd, in_file, out_file = command.split()
    if comnd == "cp" and in_file != out_file:
        with (
            open(in_file, "r") as file_in,
            open(out_file, "w") as file_out
        ):
            file_out.write(file_in.read())
