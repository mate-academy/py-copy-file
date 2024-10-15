
def copy_file(command: str) -> None:
    command_parts = command.split()
    if command_parts[0] != "cp":
        print("Invalid command format.")
        return
    first_txt, second_txt = command_parts[1], command_parts[2]
    if first_txt == second_txt:
        print("Source and destination files are the same.")
        return
    else:
        with (open(first_txt, "r") as file_in,
              open(second_txt, "w") as file_out):
            file_out.write(file_in.read())
