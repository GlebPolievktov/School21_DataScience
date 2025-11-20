import sys

clients = ['andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com',
    'john@snow.is', 'bill_gates@live.com', 'mark@facebook.com',
    'elon@paypal.com', 'jessica@gmail.com']
participants = ['walter@heisenberg.com', 'vasily@mail.ru',
    'pinkman@yo.org', 'jessica@gmail.com', 'elon@paypal.com',
    'pinkman@yo.org', 'mr@robot.gov', 'eleven@yahoo.com']
recipients = ['andrew@gmail.com', 'jessica@gmail.com', 'john@snow.is']

def call_center()->list:
    list_1 = []
    list_1 = set(clients) - set(recipients)
    return list(list_1)
def potential_clients()->list:
    list_2 = []
    list_2 = set(participants) - set(clients)
    return list(list_2)
def loyalty_program()->list:
    list_3 = []
    list_3 = set(clients) - set(participants)
    return list(list_3)
def main():
    if sys.argv[1] == 'call_center':
        return call_center()
    elif sys.argv[1] == 'potential_clients':
        return potential_clients()
    elif sys.argv[1] == 'loyalty_program':
        return loyalty_program()
    raise ValueError("Error")

if __name__ == "__main__":
    if len(sys.argv[:]) == 2:
        print(main())
    else:
        sys.exit(0)

    

