def copy_file(command: str) -> None:
    check_list = command.split(" ")
    if check_list[0] != "cp" or check_list[1] == check_list[2]:
        return None

    with (open(check_list[1], "r")
          as file_in, open(check_list[2], "w") as file_out):
        file_out.write(file_in.read())
