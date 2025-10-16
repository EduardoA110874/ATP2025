# ...existing code...
# Implementação da aplicação de gestão de cinema

def _find_sala(cinema, filme):
    for i, (nlugares, vendidos, f) in enumerate(cinema):
        if f == filme:
            return i
    return None

def inserirSala(cinema, sala):
    """
    sala: (nlugares:int, vendidos:list[int], filme:str)
    Se já existir uma sala com o mesmo filme não insere.
    """
    nlugares, vendidos, filme = sala
    if _find_sala(cinema, filme) is not None:
        print(f"Sala com o filme '{filme}' já existe.")
        return cinema
    if not isinstance(nlugares, int) or nlugares <= 0:
        print("Número de lugares inválido.")
        return cinema
    cinema.append((nlugares, list(vendidos), filme))
    return cinema

def listar(cinema):
    """Lista todos os filmes em exibição (com alguns dados)."""
    if not cinema:
        print("Nenhuma sala no cinema.")
        return
    print("Salas / Filmes em exibição:")
    for nlugares, vendidos, filme in cinema:
        print(f" - '{filme}': lotação {nlugares}, vendidos {len(vendidos)}")

def disponivel(cinema, filme, lugar):
    """
    Retorna True se o lugar está livre na sala onde o filme é exibido.
    Retorna False se o lugar está ocupado, inválido ou o filme não existe.
    """
    idx = _find_sala(cinema, filme)
    if idx is None:
        return False
    nlugares, vendidos, f = cinema[idx]
    if not (1 <= lugar <= nlugares):
        return False
    return lugar not in vendidos

def vendebilhete(cinema, filme, lugar):
    """
    Vende um bilhete (regista o lugar como ocupado) e retorna o cinema actualizado.
    Se não for possível, imprime uma mensagem e devolve o cinema sem alterações.
    """
    idx = _find_sala(cinema, filme)
    if idx is None:
        print(f"Filme '{filme}' não encontrado.")
        return cinema
    nlugares, vendidos, f = cinema[idx]
    if not (1 <= lugar <= nlugares):
        print("Lugar inválido.")
        return cinema
    if lugar in vendidos:
        print(f"Lugar {lugar} já está ocupado em '{filme}'.")
        return cinema
    vendidos = list(vendidos)  # copia para evitar efeitos laterais indesejados
    vendidos.append(lugar)
    cinema[idx] = (nlugares, vendidos, f)
    print(f"Bilhete vendido para '{filme}', lugar {lugar}.")
    return cinema

def listardisponibilidades(cinema):
    """Lista para cada sala o filme e o número de lugares disponíveis."""
    if not cinema:
        print("Nenhuma sala no cinema.")
        return
    print("Disponibilidades por sala:")
    for nlugares, vendidos, filme in cinema:
        disponiveis = nlugares - len(vendidos)
        print(f" - '{filme}': {disponiveis} lugar(es) disponíveis ({len(vendidos)} ocupados)")

def removeSala(cinema, filme):
    """Remove a sala só se não houver bilhetes vendidos; retorna cinema atualizado."""
    idx = _find_sala(cinema, filme)
    if idx is None:
        print(f"Filme '{filme}' não encontrado.")
        return cinema
    nlugares, vendidos, f = cinema[idx]
    if vendidos:
        print("Não é possível remover sala com lugares vendidos.")
        return cinema
    cinema.pop(idx)
    print(f"Sala com filme '{filme}' removida.")
    return cinema

def liberarLugar(cinema, filme, lugar):
    """Liberta um lugar ocupado (remove da lista de vendidos)."""
    idx = _find_sala(cinema, filme)
    if idx is None:
        print(f"Filme '{filme}' não encontrado.")
        return cinema
    nlugares, vendidos, f = cinema[idx]
    if lugar not in vendidos:
        print(f"Lugar {lugar} não está ocupado em '{filme}'.")
        return cinema
    vendidos = [l for l in vendidos if l != lugar]
    cinema[idx] = (nlugares, vendidos, f)
    print(f"Lugar {lugar} libertado em '{filme}'.")
    return cinema

def menu():
    print("""
(1) Inserir sala
(2) Listar filmes
(3) Verificar disponibilidade
(4) Vender bilhete
(5) Listar disponibilidades
(6) Remover sala (sem vendas)
(7) Libertar lugar
(0) Sair
""")

if __name__ == "__main__":
    cinema = []
    # exemplos iniciais
    cinema = inserirSala(cinema, (150, [], "Twilight"))
    cinema = inserirSala(cinema, (200, [], "Hannibal"))

    opcao = None
    while opcao != "0":
        menu()
        opcao = input("Opção: ").strip()
        if opcao == "1":
            filme = input("Nome do filme: ").strip()
            try:
                nl = int(input("Lotação (número inteiro): ").strip())
            except ValueError:
                print("Lotação inválida.")
                continue
            cinema = inserirSala(cinema, (nl, [], filme))
        elif opcao == "2":
            listar(cinema)
        elif opcao == "3":
            filme = input("Filme: ").strip()
            try:
                lugar = int(input("Lugar: ").strip())
            except ValueError:
                print("Lugar inválido.")
                continue
            print("Disponível:" , disponivel(cinema, filme, lugar))
        elif opcao == "4":
            filme = input("Filme: ").strip()
            try:
                lugar = int(input("Lugar: ").strip())
            except ValueError:
                print("Lugar inválido.")
                continue
            cinema = vendebilhete(cinema, filme, lugar)
        elif opcao == "5":
            listardisponibilidades(cinema)
        elif opcao == "6":
            filme = input("Filme a remover: ").strip()
            cinema = removeSala(cinema, filme)
        elif opcao == "7":
            filme = input("Filme: ").strip()
            try:
                lugar = int(input("Lugar a libertar: ").strip())
            except ValueError:
                print("Lugar inválido.")
                continue
            cinema = liberarLugar(cinema, filme, lugar)
        elif opcao == "0":
            print("A sair.")
        else:
            print("Opção inválida.")
# ...existing code...