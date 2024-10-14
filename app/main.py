import os


def copy_file(command: str) -> None:
    done_lst_path = command.split()

    if done_lst_path[1] == done_lst_path[2]:
        return

    if done_lst_path[0] != "cp":
        print("Wrong command use 'cp'.")
        return

    if not os.path.exists(done_lst_path[1]):
        print(f"File {done_lst_path[1]} not exist.")
        return

    try:
        with (open(done_lst_path[1], "r") as source_file,
              open(done_lst_path[2], "w") as destination_file):
            read_all = source_file.read()
            destination_file.write(read_all)
    except IOError as e:
        print(f"Error during copy file {e}")
