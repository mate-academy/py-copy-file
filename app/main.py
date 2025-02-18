# write your code here
def copy_file(command: str) -> None:
    total = command.split()
    if len(total) == 3 and total[0] == "cp":
        current_file, second_file = total
        if current_file != second_file:
            with (open(current_file, "r") as file_in,
                  open(second_file, "w") as file_out):
                read = file_in.read()
                file_out.write(read)
