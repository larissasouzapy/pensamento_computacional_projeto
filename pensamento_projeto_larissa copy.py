'''
================================================================================
SISTEMA DE VENDAS - AÇAITERIA (DIRETRIZES DO PROJETO)
================================================================================
> PO (Product Owner): Quero um sistema de vendas para minha açaíteria, para que eu possa organizar os produtos, controlar as vendas e oferecer um atendimento mais eficiente aos clientes.
> QA (Quality Assurance): Quero um sistema de vendas para a açaíteria, para que eu possa visualizar os produtos, escolher meu açaí, acessar informações da loja e realizar minhas compras de forma rápida e prática.
> Tech Lead: Quero desenvolver um sistema de vendas para uma açaíteria, para que eu possa criar um software organizado, funcional e de fácil manutenção, utilizando conceitos básicos de programação em Python.
> Dev (Desenvolvedor): Quero implementar um sistema de vendas para a açaíteria, para que eu possa desenvolver funcionalidades como cadastro de produtos, listagem, realização de vendas, consulta de localização, contato, redes sociais e feedback dos clientes.
> UX (User Experience): Quero um sistema de vendas para a açaíteria, para que eu possa oferecer um menu simples, intuitivo e de fácil navegação, proporcionando uma boa experiência durante a utilização do sistema.
> IA / Dados: Quero um sistema de vendas para a açaíteria, para que eu possa coletar informações sobre vendas, preferências dos clientes e feedbacks, auxiliando na melhoria dos produtos e do atendimento.
================================================================================
'''

# [Guia Tech/Dev] Inicializando o "banco de dados" do sistema em variáveis globais
p1_nome = 'Açaí Refresco'
p1_estoque = 100
p1_preco = 15.00
p1_validade = "25/10/2026"  
p1_descricao = "Açaí comum, delicie-se com o refresco do nosso açaí"

p2_nome = 'Açaí Premium'
p2_estoque = 70
p2_preco = 20.00
p2_validade = "25/11/2026"  
p2_descricao = "Açaí premium, perfeito para quem gosta do melhor" 

p3_nome = 'Açaí Experience' 
p3_estoque = 50
p3_preco = 30.00
p3_validade = "25/10/2026"  
p3_descricao = "Açaí experience, ideal para matar aquela vontade de algo especial" 

# [Guia UX] Definição de tupla para opções rápidas do cardápio
cardapio_acai = ("Tradicional", "Premium", "Especial")

# Loop principal do sistema
while True:
    # --------------------------------------------------------------------------
    # [GUIA UX] Interface do Menu Inicial - Simples, Limpa e Intuitiva
    # --------------------------------------------------------------------------
    print('\n' + '_'* 48 + '\n')
    print('Bem vindo ao sistema de vendas - Açaiteria!\n')
    print('1 - Cadastrar produto')
    print('2 - Listar produtos')
    print('3 - Realizar vendas')
    print('4 - Escolher tamanho de Açaí')
    print('5 - Toppings')
    print('6 - Localização')
    print('7 - Contato')
    print('8 - Redes sociais')
    print('9 - Feedback')
    print('0 - Sair do sistema')
    print('\n--------------------------------------\n')

    opcao_definida = input('Digite a opção desejada: ')
    print('\n' + '-' * 30 + '\n')

    # --------------------------------------------------------------------------
    # [GUIA PO / DEV] Opção 1: Organizar e Atualizar o Cadastro de Produtos
    # --------------------------------------------------------------------------
    if opcao_definida == '1':
        print('--- Cadastrando produto... ---\n')
        vaga = input('Em qual vaga deseja cadastrar? (1, 2 ou 3): ')
        
        if vaga == '1':
            p1_nome = input('Digite o nome do produto: ')
            p1_estoque = int(input('Digite a quantidade em estoque: '))
            p1_preco = float(input('Digite o preço do produto: '))
            p1_validade = input('Digite a validade do produto: ')    
            p1_descricao = input('Digite a descrição do produto: ')
            print(f'\n🎉 Produto "{p1_nome}" cadastrado na vaga 1!')
        elif vaga == '2':
            p2_nome = input('Digite o nome do produto: ')
            p2_estoque = int(input('Digite a quantidade em estoque: '))
            p2_preco = float(input('Digite o preço do produto: '))
            p2_validade = input('Digite a validade do produto: ')    
            p2_descricao = input('Digite a descrição do produto: ')
            print(f'\n🎉 Produto "{p2_nome}" cadastrado na vaga 2!')      
        elif vaga == '3':
            p3_nome = input('Digite o nome do produto: ')
            p3_estoque = int(input('Digite a quantidade em estoque: '))
            p3_preco = float(input('Digite o preço do produto: '))
            p3_validade = input('Digite a validade do produto: ')    
            p3_descricao = input('Digite a descrição do produto: ')
            print(f'\n🎉 Produto "{p3_nome}" cadastrado na vaga 3!')
        else:
            print('❌ Vaga inválida! Escolha de 1 a 3.')

    # --------------------------------------------------------------------------
    # [GUIA QA / UX] Opção 2: Visualizar Produtos de Forma Clara e Rápida
    # --------------------------------------------------------------------------
    elif opcao_definida == '2':
        print('--- Listando produtos... ---\n')
        print(f"1. Nome: {p1_nome} | Preço: R$ {p1_preco:.2f} | Estoque: {p1_estoque} unid.")
        print(f"   Validade: {p1_validade} | Descrição: {p1_descricao}\n" + '-' * 30)
        
        print(f"2. Nome: {p2_nome} | Preço: R$ {p2_preco:.2f} | Estoque: {p2_estoque} unid.")
        print(f"   Validade: {p2_validade} | Descrição: {p2_descricao}\n" + '-' * 30)
        
        print(f"3. Nome: {p3_nome} | Preço: R$ {p3_preco:.2f} | Estoque: {p3_estoque} unid.")
        print(f"   Validade: {p3_validade} | Descrição: {p3_descricao}\n" + '-' * 30)

    # --------------------------------------------------------------------------
    # [GUIA PO / QA] Opção 3: Controle e Realização de Vendas com Baixa no Estoque
    # --------------------------------------------------------------------------
    elif opcao_definida == '3':
        print('--- Realizar venda... ---\n')
        nome_venda = input('Digite o nome do produto que deseja vender: ')
        
        if nome_venda.lower() == p1_nome.lower():
            qtd_venda = int(input(f"Quantas unidades de '{p1_nome}' deseja vender? "))
            if qtd_venda <= p1_estoque:
                p1_estoque -= qtd_venda
                print(f'\n✅ Venda realizada! Total: R$ {qtd_venda * p1_preco:.2f}')
            else:
                print(f'❌ Estoque insuficiente! Temos apenas {p1_estoque}.')
        
        elif nome_venda.lower() == p2_nome.lower():
            qtd_venda = int(input(f"Quantas unidades de '{p2_nome}' deseja vender? "))
            if qtd_venda <= p2_estoque:
                p2_estoque -= qtd_venda
                print(f'\n✅ Venda realizada! Total: R$ {qtd_venda * p2_preco:.2f}')
            else:
                print(f'❌ Estoque insuficiente! Temos apenas {p2_estoque}.')
                
        elif nome_venda.lower() == p3_nome.lower():
            qtd_venda = int(input(f"Quantas unidades de '{p3_nome}' deseja vender? "))
            if qtd_venda <= p3_estoque:
                p3_estoque -= qtd_venda
                print(f'\n✅ Venda realizada! Total: R$ {qtd_venda * p3_preco:.2f}')
            else:
                print(f'❌ Estoque insuficiente! Temos apenas {p3_estoque}.')
        else:
            print('❌ Erro: Produto não encontrado com esse nome!')

    # --------------------------------------------------------------------------
    # [GUIA QA] Opção 4: Escolha de Tamanho e Cardápio Prático para o Cliente
    # --------------------------------------------------------------------------
    elif opcao_definida == '4':
        print('--- Bem vindo ao nosso Cardápio! --- \n')
        print(f"Opções disponíveis: {cardapio_acai}\n")
        tamanho_acai = input('Digite o tamanho do açaí que você quer (Tradicional/Premium/Especial): ')

        if tamanho_acai.lower() == 'tradicional':
            print(f'✅ Anotado! Você selecionou: {p1_nome} 300ml')
        elif tamanho_acai.lower() == 'premium':
            print(f'✅ Anotado! Você selecionou: {p2_nome} 500ml')
        elif tamanho_acai.lower() == 'especial':
            print(f'✅ Anotado! Você selecionou: {p3_nome} 1,5L')
        else:
            print(f'❌ Opção indisponível no cardápio.')

    # --------------------------------------------------------------------------
    # [GUIA QA / DEV] Opções de 5 a 8: Informações Úteis e Adicionais da Loja
    # --------------------------------------------------------------------------
    elif opcao_definida == '5':
        print('🍦 Agora, vamos escolher os Toppings! (Leite em pó, Nutella, Granola, Morango)')

    elif opcao_definida == '6':
        print('📍 Localizando entrega... Estamos na Av. Central do Açaí, 500.')

    elif opcao_definida == '7':
        print('📞 Entrando em contato... Telefone: (11) 98888-8888')

    elif opcao_definida == '8':
        print('📸 Aproveite o tempo e nos siga no Instagram: @AcaiDoMestre!...')

    # --------------------------------------------------------------------------
    # [GUIA IA / DADOS] Opção 9: Coleta de Feedbacks para Análise de Dados
    # --------------------------------------------------------------------------
    elif opcao_definida == '9':
        feedback = input('Deixe o seu feedback sobre o atendimento: ')
        print('📝 Obrigado! Sua opinião foi guardada para nossa Inteligência de Dados.')

    # --------------------------------------------------------------------------
    # [GUIA TECH] Opção 0: Fechamento Limpo do Loop do Sistema
    # --------------------------------------------------------------------------
    elif opcao_definida == '0':
        print('👋 Saindo do sistema da Açaiteria. Até mais!')
        break  

    else:
        print('❌ Opção inválida. Tente Novamente!')