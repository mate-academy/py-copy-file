def copy_file(command: str) -> None:
    list1 = command.split(" ")
    try:
        if list1[0] == "cp" and list1[1] != list1[2]:
            with (open(list1[1], "r") as file_in,
                  open(list1[2], "w") as file_out):
                file_out.write(file_in.read())
    except IndexError:
        return

    except FileNotFoundError:
        return
