import os


def copy_file(command: str) -> None:
    files_txt = command.split()
    if len(files_txt) == 3:
        file_in_txt, file_out_txt = files_txt[1], files_txt[2]
        if files_txt[0] == "cp":
            if os.path.exists(file_in_txt):
                if file_in_txt == file_out_txt:
                    return
                with (open(file_in_txt, "r") as file_in,
                      open(file_out_txt, "w") as file_out):
                    for line in file_in:
                        file_out.write(line)
