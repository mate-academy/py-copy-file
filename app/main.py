def check_command_string(line: str) -> None:
    command_lst = line.split()
    if len(command_lst) != 3 or command_lst[0] != "cp":
        raise ValueError("must be: keyword *cp* and two filename")
    if "." not in command_lst[1] or "." not in command_lst[2]:
        raise ValueError("must be: filename with *.txt at the end")


def copy_file(line: str) -> None:
    check_command_string(line)
    line_lst = line.split()
    input_file_name, output_file_name = line_lst[1:]
    with (open(input_file_name, "r") as file_in,
          open(output_file_name, "a") as file_out):
        file_out.write(file_in.read())
