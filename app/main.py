def copy_file(command: str):
    list_args = command.split()
    print(list_args)
    if list_args[1] != list_args[2]:
        with open(f"{list_args[1]}", "r") as file_in,\
                open(f"{list_args[2]}", "w") as file_out:
            c = file_in.read()
            file_out.write(f"{c}")
