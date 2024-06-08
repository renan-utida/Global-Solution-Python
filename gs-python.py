"""

Global Solution - 1ESPG
Computational Thinking With Python - Prof Paulo Viniccius Vieira

Clean Ocean - Protegendo nossas águas, preservando nosso futuro.
Integrantes:

Renan Dias Utida - RM 558540
Gustavo Melanda da Nova - RM 556081

"""

# Função para exibir a mensagem de boas-vindas ao usuário
def boas_vindas():
    usuario = input("Digite seu nome: ")
    print()
    print(f"Olá {usuario}!")
    print("Seja bem-vindo à Clean Ocean!")
    print("Somos uma empresa dedicada ao combate à poluição dos oceanos e à preservação dos recifes de corais.")
    print()
    print("Ao participar deste programa, você estará ajudando a preservar todo o ecossistema marinho, incluindo os recifes de corais!")
    print()
    print("Neste programa, iremos realizar um Sistema de Reciclagem Inteligente nas Praias!")
    print("Iremos simular a sua contribuição para a reciclagem de materiais nas regiões costeiras.")
    print("A cada item reciclado, você estará acumulando pontos que podem ser trocados por benefícios!")
    print()
    print("Ao atingir 500 pontos, sua pontuação será aumentada em 10%!")
    print()

# Função para listar os materiais e pontuações
def listar_materiais():
    print()
    print("Materiais encontrados nos arredores da praia para participar da promoção")
    print("Plásticos:")
    print("1- Garrafas plásticas de água e refrigerantes - 15 pontos cada")
    print("2- Sacolas plásticas - 5 pontos cada")
    print("3- Canudos plásticos - 4 pontos cada")
    print("4- Embalagens de alimentos (Inteiro) - 5 pontos cada")
    print("Metais:")
    print("5- Latas de alumínio de refrigerantes e cervejas - 10 pontos cada")
    print("6- Tampas de garrafas metálicas - 2 pontos cada")
    print("Vidros:")
    print("7- Garrafas de vidro - 25 pontos")
    print("8- Frascos de conservas - 20 pontos")
    print()

# Função para adicionar materiais ao carrinho de reciclagem
def adicionar_ao_carrinho_de_reciclagem(carrinho):
    listar_materiais()
    materiais = [
        (1, "Garrafas plásticas de água e refrigerantes", 15),
        (2, "Sacolas plásticas", 5),
        (3, "Canudos plásticos", 4),
        (4, "Embalagens de alimentos", 5),
        (5, "Latas de alumínio de refrigerantes e cervejas", 10),
        (6, "Tampas de garrafas metálicas", 2),
        (7, "Garrafas de vidro", 25),
        (8, "Frascos de conservas", 20)
    ]

    while True:
        print("Digite o número do material que você encontrou ou 0 para sair.")
        material_num = int(input("Número do material: "))
        if material_num == 0:
            break

        material_encontrado = None
        for item in materiais:
            if item[0] == material_num:
                material_encontrado = item
                break

        if material_encontrado is None:
            print("Material inválido. Tente novamente.")
            print()
            continue

        quantidade = int(input("Quantidade: "))
        material_nome, pontos = material_encontrado[1], material_encontrado[2]
        carrinho.append((material_nome, pontos, quantidade))
        print(f"{quantidade}x {material_nome} foram adicionados ao carrinho.")
        print()
    print()

# Função para visualizar os itens no carrinho
def visualizar_carrinho(carrinho):
    if not carrinho:
        print()
        print("O carrinho está vazio.")
        print()
        return

    total_pontos = sum(item[1] * item[2] for item in carrinho)
    bonus = 0
    if total_pontos >= 500:
        bonus = total_pontos * 0.1

    print()
    print("Itens no carrinho de reciclagem:")

    # Agrupar itens por nome e somar as quantidades
    itens_agrupados = {}
    for item in carrinho:
        material_nome, pontos, quantidade = item
        if material_nome in itens_agrupados:
            itens_agrupados[material_nome][1] += quantidade
        else:
            itens_agrupados[material_nome] = [pontos, quantidade]

    for material_nome, (pontos, quantidade) in itens_agrupados.items():
        print(f"{material_nome} - {quantidade}x - {pontos} pontos cada")

    print(f"Total de pontos: {total_pontos}")

    if bonus > 0:
        print(f"Você ganhou um bônus de 10%! Bônus: {bonus:.2f} pontos")
        print(f"Pontuação total com bônus: {total_pontos + bonus:.2f}")

    print()


# Função para finalizar o carrinho de reciclagem e mostrar promoções disponíveis
def finalizar_carrinho_e_mostrar_promocoes(carrinho):
    # Verifica se o carrinho está vazio
    if not carrinho:
        print()
        print("O carrinho está vazio. Adicione materiais antes de finalizar o carrinho.")
        print()
        return

    print()
    print("Finalizando o carrinho de reciclagem...")
    print("Por favor, insira seus dados para continuar:")

    # Coleta as informações do cliente
    cliente = cadastrar_cliente()

    # Calcula o total de pontos
    total_pontos = sum(item[1] * item[2] for item in carrinho)
    bonus = 0

    # Adiciona um bônus de 10% se o total de pontos for maior ou igual a 500
    if total_pontos >= 500:
        bonus = total_pontos * 0.1

    print()
    print(f"Parabéns! Você coletou um total de {total_pontos} pontos!")

    if bonus > 0:
        print(f"Você ganhou um bônus de 10%! Bônus: {bonus:.2f} pontos")
        total_pontos += bonus
        print(f"Pontuação total com bônus: {total_pontos:.2f}")

    # Exibe as promoções disponíveis com base na pontuação total
    print("Promoções disponíveis:")
    if total_pontos >= 1200:
        print("1 - Almoço gratuito em algum restaurante")
        print("2 - Vale compras de 100 reais")
    elif total_pontos >= 400:
        print("1 - Vale compras de 20 reais")
    elif total_pontos >= 150:
        print("1 - Vale refeição de 5 reais")

    # Solicita a escolha de uma promoção
    escolha = input("Escolha uma promoção (ou pressione Enter para sair sem promoção): ")

    # Verifica a escolha do usuário e exibe a mensagem correspondente
    if escolha == '1' and total_pontos >= 150:
        if total_pontos >= 1200:
            print()
            print("A Clean Ocean e todo ecossistema marinho agradecem a sua contribuição com a reciclagem!")
            print()
            print("Foi enviado um voucher de Almoço Gratuito para o email cadastrado.")
            print("Para desbloquear, entregue os materiais registrados ao ponto de coleta mais próximo!")
            print("E para participar novamente da promoção, deverá esperar 1 mês após o desbloqueio do voucher!")
        elif total_pontos >= 400:
            print()
            print("A Clean Ocean e todo ecossistema marinho agradecem a sua contribuição com a reciclagem!")
            print()
            print("Foi enviado um voucher de Vale Compras de 20 reais para o email cadastrado.")
            print("Para desbloquear, entregue os materiais registrados ao ponto de coleta mais próximo!")
            print("E para participar novamente da promoção, deverá esperar 1 mês após o desbloqueio do voucher!")
        elif total_pontos >= 150:
            print()
            print("A Clean Ocean e todo ecossistema marinho agradecem a sua contribuição com a reciclagem!")
            print()
            print("Foi enviado um voucher de Vale Refeição de 5 reais para o email cadastrado.")
            print("Para desbloquear, entregue os materiais registrados ao ponto de coleta mais próximo!")
            print("E para participar novamente da promoção, deverá esperar 1 mês após o desbloqueio do voucher!")
    elif escolha == '2' and total_pontos >= 1200:
        print()
        print("A Clean Ocean e todo ecossistema marinho agradecem a sua contribuição com a reciclagem!")
        print()
        print("Foi enviado um voucher de Vale Compras de 100 reais para o email cadastrado.")
        print("Para desbloquear, entregue os materiais registrados ao ponto de coleta mais próximo!")
        print("E para participar novamente da promoção, deverá esperar 1 mês após o desbloqueio do voucher!")
    else:
        print()
        print("A Clean Ocean e todo ecossistema marinho agradecem a sua contribuição com a reciclagem!")

    # Limpa o carrinho após finalizar a reciclagem
    carrinho.clear()
    print()


# Função para cadastrar o cliente e confirmar dados
def cadastrar_cliente():
    cliente = []
    print()
    # Coleta informações pessoais do cliente
    cliente.append(input("Nome Completo: "))
    cliente.append(input("Email: "))
    cliente.append(int(input("CPF: ")))
    dia_nascimento = int(input("Data de nascimento - Dia: "))
    mes_nascimento = int(input("Data de nascimento - Mês: "))
    ano_nascimento = int(input("Data de nascimento - Ano: "))
    cliente.append((dia_nascimento, mes_nascimento, ano_nascimento))

    # Coleta o endereço do cliente
    endereco = [
        input("Endereço - Rua: "),
        int(input("Endereço - Número: ")),
        input("Endereço - Complemento: ")
    ]
    cliente.extend(endereco)

    # Coleta informações adicionais de endereço
    cliente.append(int(input("CEP: ")))
    cliente.append(input("Cidade: "))
    cliente.append(input("Estado: "))
    cliente.append(input("Praia onde será feita a entrega: "))

    while True:
        print()
        # Exibe os dados coletados para confirmação
        print("Confirme seus dados:")
        print(f"1. Nome Completo: {cliente[0]}")
        print(f"2. Email: {cliente[1]}")
        print(f"3. CPF: {cliente[2]}")
        print(f"4. Data de nascimento (D/M/A): {cliente[3][0]}/{cliente[3][1]}/{cliente[3][2]}")
        print(f"5. Endereço: Rua {cliente[4]}, {cliente[5]} - {cliente[6]}")
        print(f"6. CEP: {cliente[7]}")
        print(f"7. Cidade: {cliente[8]}")
        print(f"8. Estado: {cliente[9]}")
        print(f"9. Praia: {cliente[10]}")

        # Solicita confirmação dos dados
        confirmacao = input("Os dados estão corretos? (1 - Sim, 2 - Não): ")

        if confirmacao == '1':
            break
        elif confirmacao == '2':
            while True:
                print()
                # Permite ao usuário corrigir os dados incorretos
                campo_errado = input("Qual campo está errado? (1-9): ")
                if campo_errado in map(str, range(1, 10)):
                    campo_errado = int(campo_errado)
                    if campo_errado == 4:
                        # Coleta novamente a data de nascimento
                        dia_nascimento = int(input("Digite o novo dia de nascimento: "))
                        mes_nascimento = int(input("Digite o novo mês de nascimento: "))
                        ano_nascimento = int(input("Digite o novo ano de nascimento: "))
                        cliente[3] = (dia_nascimento, mes_nascimento, ano_nascimento)
                    elif campo_errado == 5:
                        # Coleta novamente o endereço
                        cliente[4] = input("Endereço - Rua: ")
                        cliente[5] = int(input("Endereço - Número: "))
                        cliente[6] = input("Endereço - Complemento: ")
                    elif campo_errado == 6:
                        # Coleta novamente o CEP
                        cliente[7] = int(input("Digite o novo valor para CEP: "))
                    elif campo_errado == 7:
                        # Coleta novamente a cidade
                        cliente[8] = input("Digite o novo valor para cidade: ")
                    elif campo_errado == 8:
                        # Coleta novamente o estado
                        cliente[9] = input("Digite o novo valor para estado: ")
                    elif campo_errado == 9:
                        # Coleta novamente a praia
                        cliente[10] = input("Digite o novo valor para praia: ")
                    else:
                        # Coleta novamente nome, email ou CPF
                        campos = ['nome', 'email', 'cpf']
                        cliente[campo_errado - 1] = input(f"Digite o novo valor para {campos[campo_errado - 1]}: ")
                    break
                else:
                    print()
                    print("Opção inválida. Por favor, escolha um número entre 1 e 9.")
        else:
            print()
            print("Opção inválida. Por favor, responda com 1 ou 2.")

    return cliente

# Execução do programa principal
boas_vindas()

# Inicializa o carrinho de reciclagem vazio
carrinho_reciclagem = []

# Loop principal do programa para interação com o usuário
while True:
    # Exibe o menu principal
    print("Menu:")
    print("1. Listar materiais disponíveis para reciclagem e promoções")
    print("2. Adicionar materiais ao carrinho de reciclagem")
    print("3. Visualizar carrinho de reciclagem")
    print("4. Finalizar carrinho de reciclagem e mostrar promoções disponíveis")
    print("5. Sair")
    opcao = input("Escolha uma opção (1-5): ")

    if opcao == '1':
        # Lista os materiais disponíveis para reciclagem e promoções
        listar_materiais()
    elif opcao == '2':
        # Adiciona materiais ao carrinho de reciclagem
        adicionar_ao_carrinho_de_reciclagem(carrinho_reciclagem)
    elif opcao == '3':
        # Visualiza os itens no carrinho de reciclagem
        visualizar_carrinho(carrinho_reciclagem)
    elif opcao == '4':
        # Finaliza o carrinho de reciclagem e mostra as promoções disponíveis
        finalizar_carrinho_e_mostrar_promocoes(carrinho_reciclagem)
    elif opcao == '5':
        # Encerra o programa
        print("Clean Ocean. Protegendo nossas águas, preservando nosso futuro!")
        print("Encerrando o programa!")
        break
    else:
        # Exibe uma mensagem de erro para opções inválidas
        print()
        print("Opção inválida. Por favor, escolha uma opção válida.")
        print()
