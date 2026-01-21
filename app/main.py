def copy_file(command: str):
    f1 = (command.split(" "))[1]
    f2 = (command.split(" "))[2]
    if f1 != f2:
        with open(f1, "r") as file_in, open(f2, "w") as file_out:
            s = file_in.read()
            file_out.write(s)


if __name__ == "__main__":
    copy_file("cp readme1.txt readme2.txt")
