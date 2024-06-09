def copy_file(command: str) -> None:
    split_cmd = command.split()
    cp, file_in, file_out = split_cmd
    if len(split_cmd) < 3:
        print("Invalid value")
        return
    if cp != "cp":
        print("Command must be 'cp'")
    if file_in != file_out:
        with open(file_in, "r") as r, open(file_out, "a") as w:
            w.write(r.read())
