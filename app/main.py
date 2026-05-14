def copy_file(command: str) -> None:

    la_commande = command.split()
    if len(la_commande) != 3:
        return
    else:
        commande = la_commande[0]
        fichier_originaire = la_commande[1]
        fichier_destination = la_commande[2]

        if fichier_originaire == fichier_destination or commande != "cp":
            return
        else:
            try:
                with (open(fichier_originaire,
                           "r", encoding="utf8") as source_file,
                      open(fichier_destination,
                           "w", encoding="utf8") as destination_file):
                    destination_file.write(source_file.read())
            except FileNotFoundError:
                return
