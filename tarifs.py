import client

def calculate(client : client.Client):
    
    res = 0 
    cons = client.total_unpaid_consumption()

    if not client.social:

        #Caliber
        if client.caliber<=25:
            res += 4.8385
        elif client.caliber<=30:
            res +=19.5959
        elif client.caliber<=50:
            res += 41.1514
        else: res += 111.9318

            # FIXME: Como é que funciona o tarifário variável? Os primeiros metros cúbicos são pagos à tarifa mais baixa ou todos na mesma?
        if cons < 5:
            res += cons * 0.7354
        elif cons < 15:
            res += cons * 1.0509
        elif cons < 25:
            res += cons * 2.0859
        else :
            res += cons * 2.6059

    else:
        if cons < 15:
            res += cons * 0.7354
        elif cons < 25:
            res += cons * 2.0845
        else :
            res += cons * 2.6059

    return res
