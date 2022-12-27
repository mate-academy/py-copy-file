def copy_file(command: str) -> None:
    sours_fl, new_fl = command.split()[0], command.split()[2]
    if sours_fl != new_fl:
        with open(sours_fl, "r") as file_in, open(new_fl, "w") as file_out:
            file_out.write(file_in.read())
