def copy_file(command: str) -> None:
    work_list = command.split()
    if work_list[0] != "cp":
        return None
    file_source = work_list[1]
    file_copy = work_list[2]
    if file_source != file_copy:
        with (
            open(file_source, "r") as file_in,
            open(file_copy, "w") as file_out
        ):
            data_work = file_in.read()
            file_out.write(data_work)
