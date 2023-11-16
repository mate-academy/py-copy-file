def copy_file(command: str) -> None:
    file_names = command.split()
    if (file_names[1] != file_names[2]
            and len(file_names) == 3
            and file_names[0] == "cp"):
        with (open(file_names[1], "r") as file_in,
              open(file_names[2], "w") as file_out):
            lines = file_in.readlines()
            for line in lines:
                file_out.write(line)
