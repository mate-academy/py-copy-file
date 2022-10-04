def copy_file(command: str):
    sep_cm = command.split(" ")
    if sep_cm[1] == sep_cm[2]:
        return
    if sep_cm[0] == "cp":
        with (open(f"{sep_cm[1]}", "r") as file_in,
              open(f"{sep_cm[2]}", "w") as file_out):
            file_out.writelines(file_in.readlines())
