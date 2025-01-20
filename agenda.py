# Desafio 01: Agenda

def adicionar_contato(contatos, nome_contato, telefone_contato, email_contato):
    contato = {"contato": nome_contato, "telefone": telefone_contato, "email": email_contato, "favorito": False}
    contatos.append(contato)
    print(f"Contato {nome_contato, telefone_contato, email_contato} adicionado com sucesso!")
    return


def ver_contatos(contatos):
    print("\nLista de contatos:")
    for indice, contato in enumerate(contatos):
      status = "⭐️" if contato["favorito"] else " "
      nome_contato = contato["contato"]
      telefone_contato = contato["telefone"]
      email_contato = contato["email"]
      print(f"{indice + 1}. [{status}] {nome_contato} - {telefone_contato} - {email_contato}")
    return

def atualizar_nome_contatos(contatos, indice_contato, novo_nome_contato, novo_telefone_contato, novo_email_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
      contatos[indice_contato_ajustado]["contato"] = novo_nome_contato
      contatos[indice_contato_ajustado]["telefone"] = novo_telefone_contato
      contatos[indice_contato_ajustado]["email"] = novo_email_contato
      print(f"Contato {indice_contato} atualizado para {novo_nome_contato} - {novo_telefone_contato} - {novo_email_contato}!")
    else:
      print("Contato não encontrado")
    return

def favoritar_contato(contatos, indice_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
      contatos[indice_contato_ajustado]["favorito"] = True
      print(f"Contato {indice_contato} marcado como favorito!")
    else:
      print("Contato não encontrado!")
    return

def desfavoritar_contato(contatos, indice_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
      contatos[indice_contato_ajustado]["favorito"] = False
      print(f"Contato {indice_contato} desmarcado como favorito!")
    else:
      print("Contato não encontrado!")
    return

def deletar_contatos(contatos, indice_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
      contatos.pop(indice_contato_ajustado)
      print(f"Contato {indice_contato} deletado com sucesso!")
    else:
      print("Contato não encontrado!")
    return


contatos = []
while True:
    print("\nMinha Agenda:")
    print("1. Adicionar contato")
    print("2. Ver contatos")
    print("3. Atualizar contato")
    print("4. Favoritar contato")
    print("5. Desfavoritar contato")
    print("6. Deletar contato")
    print("7. Sair")

    escolha = input("Digite a opção desejada: ")

    if escolha == "1":
        nome_contato = input("Digite o nome do contato que deseja adicionar: ")
        telefone_contato = input("Digite o telefone do contato que deseja adicionar: ")
        email_contato = input("Digite o email do contato que deseja adicionar: ")
        adicionar_contato(contatos, nome_contato, telefone_contato, email_contato)
        
    elif escolha == "2":
        ver_contatos(contatos)
        
    elif escolha == "3":
        ver_contatos(contatos)
        indice_contato = int(input("Digite o número da tarefa que deseja atualizar: "))
        novo_nome_contato = input("Digite o novo nome do contato: ")
        novo_telefone_contato = input("Digite o novo telefone do contato: ")
        novo_email_contato = input("Digite o novo email do contato: ")
        atualizar_nome_contatos(contatos, indice_contato, novo_nome_contato, novo_telefone_contato, novo_email_contato)
        
    elif escolha == "4":
        ver_contatos(contatos)
        favoritar_contato(contatos, input("Digite o número do contato que deseja favoritar: "))
    elif escolha == "5":
        ver_contatos(contatos)
        desfavoritar_contato(contatos, input("Digite o número do contato que deseja desfavoritar: "))    
    elif escolha == "6":
        ver_contatos(contatos)
        deletar_contatos(contatos, input("Digite o número do contato que deseja deletar: "))
    elif escolha == "7":
        print("Sair")
        break
    else:
        print("Opção inválida")
