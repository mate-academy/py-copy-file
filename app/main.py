def copy_file(file_name: str) -> None:
    list1 = file_name.split(" ")

    if list1[1] != list1[2]:
        with open(list1[1], "r") as file_in, open(list1[2], "w") as file_out:
            file_out.write(file_in.read())
