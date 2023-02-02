def copy_file(command: str) -> None:
    comm_list = command.split(" ")

    if comm_list[0].strip() == "cp":
        if comm_list[1].strip() != comm_list[2].strip():
            if len(comm_list) == 3:
                with open(comm_list[1], "r") as file_old, open(
                        comm_list[2],
                        "w"
                ) as file_new:
                    file_new.write(file_old.read())

    return
