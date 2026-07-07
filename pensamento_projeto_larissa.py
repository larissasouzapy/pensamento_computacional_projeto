'''
>>Projeto Açaiteria:
> PO (Como dono da açaíteria: Quero um sistema de vendas para minha açaíteria,
> para que eu possa organizar os produtos, controlar as vendas e oferecer um atendimento mais eficiente aos clientes.)

> QA (Como cliente: Quero um sistema de vendas para a açaíteria,
> para que eu possa visualizar os produtos, escolher meu açaí, acessar informações da loja e realizar minhas compras de forma rápida e prática.)

> Tech (Como programador: Quero desenvolver um sistema de vendas para uma açaíteria,
> para que eu possa criar um software organizado, funcional e de fácil manutenção, utilizando conceitos básicos de programação em Python.)

> Dev (Como desenvolvedor: Quero implementar um sistema de vendas para a açaíteria,
> para que eu possa desenvolver funcionalidades como cadastro de produtos, listagem, realização de vendas, consulta de localização, contato, redes sociais e feedback dos clientes.)

> UX (Como designer de experiência do usuário: Quero um sistema de vendas para a açaíteria,
> para que eu possa oferecer um menu simples, intuitivo e de fácil navegação, proporcionando uma boa experiência durante a utilização do sistema.)

> IA (Como analista de dados: Quero um sistema de vendas para a açaíteria,
> para que eu possa coletar informações sobre vendas, preferências dos clientes e feedbacks, auxiliando na melhoria dos produtos e do atendimento.)
'''



# Ufa, quebrei a maldição
# print('Olá, Mundo!')

# Inicializando as variáveis para o produto 1 (vazio)
p1_nome = 'Açaí refresco'
p1_estoque = 100
p1_preco = 15.00
p1_validade = 25/10/2026
p1_descrição = "acaí comum, delicie-se com o rerefresco do nosso açaí"

# Iniciando as variáveis para  produto 2 (vazio)
p2_nome = 'Açaí premium'
p2_estoque = 70
p2_preco = 20.00
p2_validade = 25/11/2026
p2_descrição = "acaí premium, perfeito para quem gosta do melhor" 

#iniciando as variáveis para  produto 3 (vazio)
p3_nome = 'Açaí experience' 
p3_estoque = 50
p3_preco =30.00
p3_validade = 25/10/2026
p3_descrição = "acaí experience, ideial para matar aquela vontade de algo especial" 

# Inicializando as variáveis para o Tamanho do Açaí
cardapio_acai = ("Tradicional", "Premium", "Especial")

while True:
    print('_'* 48 + '\n')
    print('Bem vindo ao sistema de vendas - Açaiteria!\n')
    print('1 - Cadastrar produto')
    print('2 - Listar produtos')
    print('3 - Realizar vendas')
    print('4 - Açaí')
    print('5 - Toppings')
    print('6 - Localização')
    print('7 - Contato')
    print('8 - Redes sociais')
    print('9-  Feedback')
    print('0 - Sair do sistema')
    print('\n--------------------------------------\n')

opcao__definida = int(input('Digite a opcao deseja: '))
if opcao__definida == 1:
    print('Cadatrando produtos...')

elif opcao__definida == 2:
    print('Listando produtos...')

elif opcao__definida == 3:
    print('Realizando Vendas...')

elif opcao__definida == 4:
    print('Preparando Pedido...') 

elif opcao__definida == 5:
    print('Acrescentando os complementos...')

elif opcao__definida == 6:
    print('Localizando entrega...')

elif opcao__definida == 7:
    print('Entrando em contato...')
        
elif opcao__definida == 8:
    print('Avalição do produto...')

elif opcao__definida == 9:
    print('Pronto! Conheca nos mais na nossa comunidade...')


else:
    print('Ops, houve algum erro, tente novamente!')

opcao__definida = (input('Digite a opção desejada: '))

if opcao__definida == '1':
    print('Cadastranto produto...\n')
    if p1_nome == "Açaí Tradicional":
            p1_nome = input('Digite o nome do produto: ')
            p1_estoque = int(input('Digite a quantidade em estoque: '))
            p1_preco = float(input('Digite o preço do produto: '))
            p1_validade = input('Digite a validade do produto: ')    
            p1_descricao = input('Digite a descrição do produto: ')
            print(f'\n🎉 Produto "{p1_nome}" cadastrado na vaga 1!')
    elif p2_nome == "Açaí Premium":
              p2_nome = input('Digite o nome do produto: ')
              p2_estoque = int(input('Digite a quantidade em estoque: '))
              p2_preco = float(input('Digite o preço do produto: '))
              p2_validade = input('Digite a validade do produto: ')    
              p2_descricao = input('Digite a descrição do produto: ')
              print(f'\n🎉 Produto "{p2_nome}" cadastrado na vaga 2!')      
    elif p3_nome == "Açaí Especial":
        p3_nome = input('Digite o nome do produto: ')
        p3_estoque = int(input('Digite a quantidade em estoque: '))
        p3_preco = float(input('Digite o preço do produto: '))
        p3_validade = input('Digite a validade do produto: ')    
        p3_descricao = input('Digite a descrição do produto: ')
        print(f'\n🎉 Produto "{p3_nome}" cadastrado na vaga 3!')

    else:
        print('❌ Sistema cheio! Limite de 3 produtos atingido.')


elif opcao__definida == '2':
    print('Listando produto...')

    if p1_nome == "Açaí Tradicional" and p2_nome == "Açaí Premium" and p3_nome == "Açaí Especial":
         
        print('Nenhum produto cadastrado no sistema ainda.')

    else:
            # Mostra o Produto 1 se ele existir
            if p1_nome != "Açaí Tradicional":
                print(f"Nome: {p1_nome} | Preço: R$ {p1_preco:.2f} | Estoque: {p1_estoque} unid.")

                print(f"Validade: {p1_validade} | Descrição: {p1_descricao}")

                print('-' * 30)
                
            # Mostra o Produto 2 se ele existir
            if p2_nome != "Açaí Premium":

                print(f"Nome: {p2_nome} | Preço: R$ {p2_preco:.2f} | Estoque: {p2_estoque} unid.")

                print(f"Validade: {p2_validade} | Descrição: {p2_descricao}")

                print('-' * 30)

            # Mostra o Produto 3 se ele existir
            if p3_nome != "Açaí Especial":

                print(f"Nome: {p3_nome} | Preço: R$ {p3_preco:.2f} | Estoque: {p3_estoque} unid.")

                print(f"Validade: {p3_validade} | Descrição: {p3_descricao}")

                print('-' * 30)


elif opcao__definida == '3':
    print('Realizar venda...')

    if p1_nome == "Açaí Tradicional" and p2_nome == "Açaí Premium" and p3_nome == "Açaí Especial":
            print(f'Não há produtos cadastrados para realizar vendas.')
    else:
            nome_venda = input('Digite o nome do produto que deseja vender: ')
            
            # Testamos o nome digitado contra o Produto 1
            if nome_venda.lower() == p1_nome.lower() and p1_nome != "Açaí Tradicional":
                qtd_venda = int(input(f"Quantas unidades de '{p1_nome}' deseja vender? "))
                if qtd_venda <= p1_estoque:
                    p1_estoque -= qtd_venda
                    total = qtd_venda * p1_preco
                    print(f'\n✅ Venda realizada! Total: R$ {total:.2f}')
                    print(f'Estoque atual de {p1_nome}: {p1_estoque} unidades.')
                else:
                    print(f'❌ Estoque insuficiente! Temos apenas {p1_estoque}.')
            
            # Testamos contra o Produto 2
            elif nome_venda.lower() == p2_nome.lower() and p2_nome != "Açaí Premium":
                qtd_venda = int(input(f"Quantas unidades de '{p2_nome}' deseja vender? "))
                if qtd_venda <= p2_estoque:
                    p2_estoque -= qtd_venda
                    total = qtd_venda * p2_preco
                    print(f'\n✅ Venda realizada! Total: R$ {total:.2f}')
                    print(f'Estoque atual de {p2_nome}: {p2_estoque} unidades.')
                else:
                    print(f'❌ Estoque insuficiente! Temos apenas {p2_estoque}.')
                    
            # Testamos contra o Produto 3
            elif nome_venda.lower() == p3_nome.lower() and p3_nome != "Açaí Especial":
                qtd_venda = int(input(f"Quantas unidades de '{p3_nome}' deseja vender? "))
                if qtd_venda <= p3_estoque:
                    p3_estoque -= qtd_venda
                    total = qtd_venda * p3_preco
                    print(f'\n✅ Venda realizada! Total: R$ {total:.2f}')
                    print(f'Estoque atual de {p3_nome}: {p3_estoque} unidades.')
                else:
                    print(f'❌ Estoque insuficiente! Temos apenas {p3_estoque}.')
            
            else:
                print('🔥 Erro: Produto não encontrado!')


elif opcao__definida == '4':
     print('Bem vindo ao nosso Cardápio! \n')
     print(cardapio_acai)

tamanho_acai = input('\n''Digite o tamanho do açaí que você quer: ')

if tamanho_acai == 'Tradicional':
     print(f'✅ Anotado! Você selecionou: {p1_nome} 300ml''\n')

elif tamanho_acai == 'Premium':
     print(f'✅ Anotado! Você selecionou: {p2_nome} 500ml''\n')

elif tamanho_acai  == 'Especial':
     print(f'✅ Anotado! Você selecionou: {p3_nome} 1,5L''\n')

else:
     print(f'Desculpe, nós não temos essa opção no cardápio. Tente novamente')


elif opcao__definida == '5':
    print('Agora, vamos escolher os Toppings!')

elif opcao__definida == 6:
    print('Visualizando a sua localização..')

elif opcao__definida == 7:
    print('Entrando em contato...')

elif opcao__definida == 8:
    print('Aproveite esse tempo de entrega e nos siga nas redes sociais!...')

elif opcao__definida == 9:
    print('Pronto! Gostariamos que você enviasse o seu feedback')

else:
    print('Humm, Algo deu errado. Tente Novamente!')