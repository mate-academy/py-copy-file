def copy_file(command: str) -> None:
    comand_parts = command.split(" ")
    if len(comand_parts) == 3 and comand_parts[0] == "cp":
        source_file = comand_parts[1]
        destination_file = comand_parts[2]
        if source_file == destination_file:
            return
        try:
            with (open(source_file, "r") as file_in,
                  open(destination_file, "w") as file_out):
                for line in file_in:
                    file_out.write(line)
        except FileNotFoundError:
            pass
