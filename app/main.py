def copy_file(command: str) -> None:
    division = command.split(" ")
    if len(division) == 3 and division[0] == "cp":
        if division[1] != division[2]:
            try:
                with (open(division[1], "r") as file_in,
                      open(division[2], "w") as file_out):
                    read_text = file_in.read()
                    file_out.write(read_text)
            except Exception:
                pass
