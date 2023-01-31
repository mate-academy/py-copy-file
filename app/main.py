def copy_file(command: str) -> None:
    comm_list = command.split(" ")

    if comm_list[0].strip() != "cp" \
            or comm_list[1].strip() == comm_list[2].strip():
        return

    with open(comm_list[1], "r") as file_old, open(comm_list[2], "w") \
            as file_new:
        file_new.write(file_old.read())
