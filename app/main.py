def copy_file(command: str) -> None:
    comand_list = command.split()

    if len(comand_list) != 3:
        raise ValueError(f"Not enough values to unpack: "
                         f"{len(comand_list)} of 3")

    cmd, source_path, destination_path = comand_list

    if cmd != "cp":
        raise ValueError("Invalid command. Only 'cp' command is supported.")

    if source_path == destination_path:
        print("Source file and destination file have the same name. "
              "No action needed.")
        return

    with (
        open(source_path, "r") as file_in,
        open(destination_path, "w") as file_out
    ):
        file_out.write(file_in.read())
