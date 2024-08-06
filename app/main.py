def copy_file(command: str) -> None:
    temp_lst = command.split()
    if len(temp_lst) != 3 or any(value for value in temp_lst) is None:
        raise ValueError("incorrect data. You must specify 'command' \
        'file name' and 'name of the copy to create'")
    if temp_lst[0] != "cp":
        raise ValueError(f"Unknown command {temp_lst[0]}")
    if temp_lst[1] == temp_lst[2]:
        raise ValueError("You can not create new file with same name")
    with open(temp_lst[1], "r") as file_in, open(temp_lst[2], "w") as file_out:
        file_out.write(file_in.read())
    print(f"File {temp_lst[1]} was successfully copied to {temp_lst[2]}")
