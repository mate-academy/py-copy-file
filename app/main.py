def copy_file(command: str) -> None:
    command_comps = command.split()
    if command_comps[0] == "cp" and command_comps[1] != command_comps[2]:
        with (open(command_comps[1], "r") as file_obj,
              open(command_comps[2], "w") as copy_file_obj):
            copy_file_obj.write(file_obj.read())
            file_obj.close()
            copy_file_obj.close()
