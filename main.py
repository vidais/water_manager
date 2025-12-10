import client,pickle,tui
from pathlib import Path

## @package water_manager
# App for managing water company clients

## Main function of the program
if __name__ == '__main__' :
    
    data_file = Path("clients.pkl") # Load a previously stored db
    if data_file.exists():
        with data_file.open("rb") as f:
            client_db = pickle.load(f)
    else : client_db = []

    tui.clear_screen()
    print("Sistema de Gestão de Faturação do consumo de água") #Title

    while True: # Infinite loop to keep app running until user decides to leaver
        print("Introduza uma opção:",end='') 
        option = input()
    
        match option:
                case 'h': # Help
                    tui.clear_screen()
                    tui.print_options()

                case 'n': # New client
                    tui.clear_screen()
                    client_db.append(client.Client(len(client_db)))

                case 'p': # Visualization Options
                    tui.print_menu(client_db)

                case 'i': # Register a consumption
                    tui.clear_screen()
                    usr_input = input("ID do cliente:")
                    if usr_input.isdigit():
                        id = int(usr_input)
                        if 0<id and id<len(client_db) and client_db[id-1].active:
                            client_db[id-1].register_consumption()
                        else: print("ID do cliente inválido")
                    else : print("Introduza um id de cliente válido")

                case 'dc':
                    tui.clear_screen()
                    usr_input = input("ID do cliente:")
                    if usr_input.isdigit():
                        id = int(usr_input)
                        if 0<id and id<len(client_db):
                            client_db[id-1].active = False
                        else: print("ID do cliente inválido")
                    else : print("Introduza um id de cliente válido")
            
                case 'q': # Quit program, saving db for next use
                    with data_file.open("wb") as f:
                        pickle.dump(client_db,f)
                    print("Base de dados guardada")
                    exit()

        print('\n',end='')
