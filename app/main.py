def copy_file(command):
    # Divide a string do comando pelos espaços
    parts = command.split()
    
    # Verifica se o comando possui a estrutura esperada (cp, origem, destino)
    if len(parts) >= 3:
        _, src, dest = parts[:3]
        
        # Não faz nada se a origem e o destino forem o mesmo arquivo
        if src == dest:
            return
        
        # Copia o conteúdo usando dois gerenciadores de contexto simultaneamente
        with open(src, "rb") as file_in, open(dest, "wb") as file_out:
            file_out.write(file_in.read())
  
