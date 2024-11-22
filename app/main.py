def copy_file(command: str) -> None:
    files_name = command.split(" ")

    if files_name[1] == files_name[2]:
        return
    if len(command) > 1 and command.startswith("cp"):
        with (open(files_name[1], "r") as file_in,
              open(files_name[2], "w") as file_out):
            for line in file_in:
                file_out.write(line)
    else:
        return
