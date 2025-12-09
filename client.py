from datetime import date, datetime

class Client:
    def __init__(self,counter):  # Constructor for a new client

        #ID
        self.id = counter + 1

        # Nome
        usr_input = input("Nome: ")  # input() always returns a string
        if usr_input.strip():        # just check it is not empty
            self.name = usr_input
        else:
            print("Nome Inválido")
            return

        # Número da Instalação
        usr_input = input("Número da Instalação: ")
        if usr_input.isdigit():      # check if it is a string of digits
            self.install_number = int(usr_input)
        else:
            print("Número de Instalação Inválido")
            return

        # Morada
        usr_input = input("Morada: ")
        if usr_input.strip():
            self.address = usr_input
        else:
            print("Morada Inválida")
            return

        # Contacto
        usr_input = input("Contacto: ")
        if usr_input.isdigit():
            num = int(usr_input)
            if 900000000 < num < 999999999:
                self.contact = num
            else:
                print("Contacto Inválido")
                return
        else:
            print("Contacto Inválido")
            return

        # NIF
        usr_input = input("NIF: ")
        if usr_input.isdigit():
            num = int(usr_input)
            if 900000000 < num < 999999999:
                self.fiscal = num
            else:
                print("NIF Inválido")
                return
        else:
            print("NIF Inválido")
            return

        # Calibre
        usr_input = input("Calibre: ")
        if usr_input.isdigit():
            self.caliber = int(usr_input)
        else:
            print("Calibre Inválido")
            return

        # Tarifa Social
        usr_input = input("Tarifa Social (S/N): ").strip().upper()
        if usr_input == 'S':
            self.social = True
        else:
            self.social = False

        self.consumption = {}

        def register_consumption(self):
            print("Introduzir um novo consumo")

            usr_input = input("Mês-Ano:").strip() #Get date from user
            try:
                d = datetime.strptime(usr_input,"%m-%Y").date()
            except ValueError:
                print("Mês/Ano Inválido (Use o formato MM-YYYY)")
                return
            
            usr_input = input(f"Consumo de {d.strftime("%m-%Y")}: ").strip() #Get value from user
            value = float(usr_input)
            if value >= 0:
                self.consumption[d]=value
            else: 
                print("Consumo Inválido")
                return




