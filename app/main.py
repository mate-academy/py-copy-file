def copy_file(command: str) -> None:
    todolist = command.split(" ")
    file_name = todolist[1]
    file_copy_name = todolist[2]
    with open(file_name, "w") as some_info:
        some_info.write(input())
    if file_name != file_copy_name:
        with open(file_name, "r") as content_out, \
                open(file_copy_name, "w") as content_in:
            copy_text = content_out.read()
            content_in.write(copy_text)
    else:
        print("Does nothing")
