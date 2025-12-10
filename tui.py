import os

from client import Client

## Clears the screen
# Used before printing some other menu
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

## Prints all options available to the user
def print_options():
    print("Opções Disponíveis:")
    print("(n) Novo Cliente")
    print("(i) Novo consumo")
    print("(p) Menu de Visualização")
    print("(h) Ajuda")
    print("(q) Sair")

## Prints a table composed of an header and a list of all clients registered
# @parameter client_db Client list to print
def print_clients_table(client_db):
    # Header
    print(f"{'ID':<4} {'Nome':<20} {'Instalação':<12} {'Contacto':<10} {'NIF':<10}")
    print("-" * 60)

    # Rows
    for client in client_db:
        print(f"{client.id:<4} {client.name:<20} {client.install_number:<12} {client.contact:<10} {client.fiscal:<10}")

## Prints a table composed of an header and a list of all consumptions 
# @parameter client object containing all information for this specific client
def print_client_consumptions_table(client: Client):
    # Header
    print(f"{'ClienteID':<10} {'Nome':<20} {'Período':<10} {'Consumo':>10}")
    print("-" * 60)

    if not client.consumption:
        print("Sem consumos registados.")
        return

    # Rows for this one client
    for cons in client.consumption:
        period_str = cons.period.strftime("%m-%Y")
        print(f"{client.id:<10} {client.name:<20} {period_str:<10} {cons.value:>10.2f}")

## Prints the options for the visualization menu
def print_pmenu_options():
    print("(c) Mostrar todos os clientes")
    print("(i) Mostrar consumos para um cliente")
    print("(p) Mostrar conta corrente de um cliente")
    print("(q) Voltar ao menu principal")

## Handles the menu for visualization options
# @parameter client_db list of all clients currently registered
def print_menu(client_db: list[Client]):

    clear_screen()
    print_pmenu_options()
    usr_input = input("Introduza uma opção de visualização:")

    match usr_input:
        case 'c': # Print Clients
            clear_screen()
            if len(client_db) == 0:
                print("Sem clientes registados")
            else:
                print_clients_table(client_db)
        
        case 'i': # Print Consumptions for one client
            clear_screen()
            usr_input = input("ID do cliente:")
            if usr_input.isdigit():
                id = int(usr_input)
                if 0<id and id<len(client_db) and client_db[id-1].active:
                    print_client_consumptions_table(client_db[id-1])
                else: print("ID do cliente inválido")
            else : print("Introduza um id de cliente válido")

        case 'q': #Go back to the main menu
            return
