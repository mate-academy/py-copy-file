def copy_file(command: str) -> None:
    comm_ls = command.split()
    if len(comm_ls) != 3:
        return
    if comm_ls[0] == "cp" and comm_ls[1] != comm_ls[2]:
        file_name_in = comm_ls[1]
        file_name_out = comm_ls[2]
        try:
            with (open(file_name_in, "r") as file_in,
                  open(file_name_out, "w") as file_out):
                file_out.write(file_in.read())
        except IOError:
            print("File copy error.")
