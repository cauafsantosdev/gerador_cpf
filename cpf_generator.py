def menu():
    while True:
        print(f"{'GERADOR DE CPF':^30}")
        print("-" * 30)
        print(" [1] GERAR CPF\n [2] LISTA DE CPFS\n [0] SAIR: ")
        print("-" * 30)
        option = int(input("-> "))
        if option < 0 or option > 2:
            print("OPÇÃO INVÁLIDA! Tente novamente.\n")
        else:
            break
        
    return option


def db_write(cpf):
    with open("cpf_list.txt", "a") as file:
        file.write(f"{cpf}\n")


def db_show():
    try:
        with open("cpf_list.txt", "r") as file:  
            cpf_list = file.read().splitlines()
    except FileNotFoundError:
        print(f"Nenhum CPF foi gerado\n")
        return
    
    print(f"\n{'LISTA DE CPFs':^30}")
    print("-" * 30)

    for i, cpf in enumerate(cpf_list, start=1):
        print(f"{i} -> {cpf}")
    print()
        

def generator():
    from random import randint

    cpf = [randint(0, 9) for _ in range(9)]

    digit10 = sum((10 - i) * j for i, j in enumerate(cpf)) % 11
    digit10 = digit10 if digit10 < 10 else 0
    cpf.append(digit10)

    digit11 = sum((11 - i) * j for i, j in enumerate(cpf)) % 11
    digit11 = digit11 if digit11 < 10 else 0
    cpf.append(digit11)

    cpf_str = ''.join(map(str, cpf))
    formatted_cpf = f"{cpf_str[:3]}.{cpf_str[3:6]}.{cpf_str[6:9]}-{cpf_str[9:]}"

    return formatted_cpf