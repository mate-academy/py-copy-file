def copy_file(command: str) -> None:
    if "cp" in command:
        todolist = command.split()
        *other, file_name, file_copy_name = todolist

        if file_name != file_copy_name:
            with open(file_name, "r") as content_out, \
                    open(file_copy_name, "w") as content_in:

                copy_text = content_out.read()
                content_in.write(copy_text)
        else:
            print("Does nothing")
