def copy_file(command: str) -> None:

    todolist = command.split()
    cmd, file_name, file_copy_name = todolist
    if cmd == "cp":
        if file_name != file_copy_name:
            with open(file_name, "r") as content_out, \
                    open(file_copy_name, "w") as content_in:

                copy_text = content_out.read()
                content_in.write(copy_text)
        else:
            print("Does nothing")
