def copy_file(command: str) -> None:

    command_list = command.split()
    file_orig_name = command_list[1]
    file_copy_name = command_list[2]

    if file_orig_name != file_copy_name:
        with (open(file_orig_name, "r") as orig_f,
              open(file_copy_name, "w") as copy_f):
            copy_f.write(orig_f.read())
