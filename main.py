import client

def print_options():
    print("Opções Disponíveis:")
    print("(n) Novo Cliente")
    print("(i) Introduzir consumo")
    print("(h) Ajuda")
    print("(q) Sair")

if __name__ == '__main' :
    client_db = [] #Start with a clean DB  TODO: Maybe change this to be presistent between uses
    client_counter = 0

    print("Sistema de Gestão de Faturação do consumo de água")
    print("Introduza uma opção:",end='')
    
    option = input()

    while True:
        match option:
            case 'h':
                print_options()
            case 'n':
                client_db.append(client.Client(client_counter))
            case 'i':
                usr_input = input("ID do cliente:")
                if usr_input.isdigit():
                    id = int(usr_input)
                    client_db[id-1].register_consumption()
                else : print("Introduza um id de cliente válido")
            case 'q':
                exit()


