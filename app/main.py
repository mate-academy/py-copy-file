
def copy_file(command: str) -> None:
    date = command.split()
    if date[0] != "cp":
        return
    first_txt, second_txt = date[1], date[2]
    if first_txt == second_txt:
        return
    else:
        with (open(first_txt, "r") as file_in,
              open(second_txt, "w") as file_out):
            file_out.write(file_in.read())
