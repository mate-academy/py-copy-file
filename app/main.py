def copy_file(command: str) -> None:
    done_lst_path = command.split()
    if done_lst_path[1] == done_lst_path[2]:
        return
    with (open(done_lst_path[1], "r") as file_in,
          open(done_lst_path[2], "w") as file_out):
        read_all = file_in.read()
        file_out.write(read_all)
