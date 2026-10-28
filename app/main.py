def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) == 3 and parts[0] == "cp" and parts[1] != parts[2]:
        try:
            with open(parts[1], "r") as f_in, open(parts[2], "w") as f_out:
                f_out.write(f_in.read())
        except FileNotFoundError:
            pass
