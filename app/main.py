def copy_file(command: str) -> None:
    elements = command.split()
    if elements[0] == "cp" and elements[1] != elements[1]:
        with open(elements[1], "r") as f_in, open(elements[2], "w") as f_out:
            f_out.write(f_in.read())
