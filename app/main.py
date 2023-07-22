def copy_file(command: str) -> None:
    work_list = command.split()
    file_source = work_list[1]
    file_copy = work_list[2]
    list_file_source = []
    with open(file_source, "r") as file_in, open(file_copy, "w"):
        line_number = 1
        for line in file_in:
            list_file_source.append(line)
            line_number += 1
    with open(file_copy, "a") as file_out:
        for line_list in list_file_source:
            file_out.write(line_list)
