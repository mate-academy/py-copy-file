def copy_file(command: str) -> None:
    spl_cmd = command.split()
    if len(spl_cmd) == 3 and spl_cmd[1] != spl_cmd[2] and spl_cmd[0] == "cp":
        file_old = spl_cmd[1]
        file_new = spl_cmd[2]
        try:
            with (open(file_old, "r") as file_in,
                  open(file_new, "w") as file_out):
                file_out.write(file_in.read())
        except FileNotFoundError:
            pass
