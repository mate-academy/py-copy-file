def copy_file(command: str) -> None:
    total = command.split()
    if len(total) == 3 and total[0] == "cp":
        curr_file = total[1]
        second_file = total[2]
        if curr_file != second_file:
            with (open(curr_file, "r") as file_in,
                  open(second_file, "w") as file_out):
                read = file_in.read()
                file_out.write(read)
