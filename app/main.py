def copy_file(command: str) -> None:
    try:
        prompt = command.split(" ")[0]
        if prompt != "cp":
            return
        file_name, new_file_name = command.split(" ")[1], command.split(" ")[2]
        if file_name == new_file_name:
            pass
        else:
            with open(file_name, "r") as f, open(new_file_name, "w") as nf:
                nf.write(f.read())
    except FileNotFoundError:
        pass
    except IndexError:
        pass
