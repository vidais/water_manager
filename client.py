from datetime import datetime

class Client:
    def __init__(self,counter):  # Constructor for a new client

        #ID
        self.id = counter + 1
        
        #Status
        self.active = True

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
            if 100000000 < num < 999999999:
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

        self.consumption = []

        print("Cliente Registado")
        return
    def total_unpaid_consumption(self):
        return sum(cons.value for cons in self.consumption if not cons.status)

    def register_consumption(self):
        print("Introduzir um novo consumo")

        # Create a new Consumption, which asks the user for data
        consumption = Consumption()

        # Only add if the data is valid
        if consumption.period is not None and consumption.value is not None:
            self.consumption.append(consumption)
            print("Consumo Registado")
        else:
            print("Consumo não registado (dados inválidos)")
    
    def __str__(self):
        lines = [
            f"ID: {self.id}",
            f"Nome: {self.name}",
            f"Número de Instalação: {self.install_number}",
            f"Morada: {self.address}",
            f"Contacto: {self.contact}",
            f"NIF: {self.fiscal}",
            f"Calibre: {self.caliber}",
            f"Tarifa Social: {'Sim' if self.social else 'Não'}",
        ]

        if self.consumption:
            lines.append("Consumos:")
            for cons in self.consumption:
                lines.append(f"  {cons}")  # uses Consumption.__str__()
        else:
            lines.append("Sem consumos registados.")

        return "\n".join(lines)

    def to_dict(self):
            return {
                "id": self.id,
                "name": self.name,
                "install_number": self.install_number,
                "address": self.address,
                "contact": self.contact,
                "fiscal": self.fiscal,
                "caliber": self.caliber,
                "social": self.social,
                # convert datetime keys to strings for JSON
                "consumption": {d.strftime("%m-%Y"): v for d, v in self.consumption.items()},
            }

    @classmethod
    def from_dict(cls, data: dict):
        # create an empty client without running __init__ prompts
        obj = cls.__new__(cls)
        obj.id = data["id"]
        obj.name = data["name"]
        obj.install_number = data["install_number"]
        obj.address = data["address"]
        obj.contact = data["contact"]
        obj.fiscal = data["fiscal"]
        obj.caliber = data["caliber"]
        obj.social = data["social"]
        from datetime import datetime
        obj.consumption = {
            datetime.strptime(k, "%m-%Y").date(): v
            for k, v in data.get("consumption", {}).items()
        }
        return obj

class Consumption:
    def __init__(self):
        # Period (month-year)
        usr_input = input("Mês-Ano: ").strip()
        try:
            self.period = datetime.strptime(usr_input, "%m-%Y").date()
        except ValueError:
            print("Mês/Ano Inválido (Use o formato MM-YYYY)")
            self.period = None
            self.value = None
            self.status = False
            return

        # Value
        usr_input = input(f"Consumo de {self.period.strftime('%m-%Y')}: ").strip()
        try:
            value = float(usr_input)
        except ValueError:
            print("Consumo Inválido (não é número)")
            self.period = None
            self.value = None
            self.status = False
            return

        if value < 0:
            print("Consumo Inválido (negativo)")
            self.period = None
            self.value = None
            self.status = False
            return

        self.value = value
        self.status = False  # por exemplo: False = não faturado / não pago

    def __str__(self):
        if self.period is None:
            return "Consumo inválido"
        return f"{self.period.strftime('%m-%Y')}: {self.value}"
