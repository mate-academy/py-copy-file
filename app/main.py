def copy_file(command_line: str) -> None:
    (command,
     file_name,
     new_file_name) = command_line.split(" ")
    # we are cheking on correct data input
    if command != "cp" or file_name == new_file_name:
        return
    # we are opening current file and creat new file
    # using mode "w" and write down there data from
    # current_file
    with (open(file_name, "r") as file_in,
          open(new_file_name, "w") as file_out):
        for line in file_in.readlines():
            file_out.write(line)
