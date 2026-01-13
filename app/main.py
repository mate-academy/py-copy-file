def copy_file(command: str) -> None:
    cp_lst = command.split()
    if len(cp_lst) == 3 and cp_lst[1] != cp_lst[2] and cp_lst[0] == "cp":
        try:
            with (open(cp_lst[1], "rb") as file_in,
                  open(cp_lst[2], "wb") as file_out):
                for line in file_in:
                    file_out.write(line)
        except FileNotFoundError:
            pass
