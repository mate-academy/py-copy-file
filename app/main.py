def copy_file(command: str):
    lst = command.split(" ")

    with open(f"{lst[1]}", "r") as f_in, open(f"{lst[2]}", "w") as f_out:
        copy_data = f_in.read()
        f_out.write(f"{copy_data}")
