def copy_file(command: str) -> None:
    files = command[3:].split(" ")
    with open(f"{files[0]}", "r") as f_in, open(f"{files[1]}", "w") as f_out:
        f_out.write(f_in.read())
