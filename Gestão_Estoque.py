import json
from time import sleep
from datetime import datetime, timedelta
import os

class Cores:
    VERMELHO = '\033[91m'
    VERDE = '\033[92m'
    MAGENTA = '\033[95m'
    RESET = '\033[0m'

arquivo = 'produtos.json' 

def adicionar_produto(nome_produto, quantidade, data_val):
    try:
        with open(arquivo, 'r') as f:
            produtos = json.load(f)
    except FileNotFoundError:
        produtos = []

    produtos.append({'nome_produto': nome_produto, 'quantidade': quantidade, 'data de validade': data_val})

    with open(arquivo, 'w') as f:
        json.dump(produtos, f, indent=3)
    print(Cores.VERDE + 'PRODUTO CADASTRADO NO SISTEMA.' + Cores.RESET)

def listar_produtos():
    try:
        with open(arquivo, 'r') as f:
            produtos = json.load(f)
    except FileNotFoundError:
        produtos = []

    if produtos:
        print('-' * 30)
        print('PRODUTOS REGISTRADOS:')
        print('-' * 30)
        for produto in produtos:
            print('*' * 30)
            print(f"NOME DO PRODUTO: {produto['nome_produto']}, QUANTIDADE: {produto['quantidade']}, DATA DE VALIDADE: {produto['data de validade']}")
            print('*' * 30)
    else:
        print(Cores.VERMELHO + 'NENHUM PRODUTO ENCONTRADO.' + Cores.RESET)

def atualizar_produto(produto_antigo, produto_novo, quantidade_nova, data_val_nova):
    try:
        with open(arquivo, 'r') as f:
            produtos = json.load(f)
    except FileNotFoundError:
        produtos = []

    for produto in produtos:
        if produto['nome_produto'] == produto_antigo:
            produto['nome_produto'] = produto_novo
            produto['quantidade'] = quantidade_nova
            produto['data de validade'] = data_val_nova
            break

    with open(arquivo, 'w') as f:
        json.dump(produtos, f, indent=3)
    print(Cores.VERDE + 'PRODUTO ATUALIZADO COM SUCESSO.' + Cores.RESET)

def checar_produto(nome_produto):
    try:
        with open(arquivo, 'r') as f:
            produtos = json.load(f)
    except FileNotFoundError:
        produtos = []

    encontrado = False

    for produto in produtos:
        if produto['nome_produto'] == nome_produto:
            print(f"NOME DO PRODUTO: {produto['nome_produto']}, QUANTIDADE: {produto['quantidade']}, DATA DE VALIDADE: {produto['data de validade']}")
            encontrado = True
            break
    if not encontrado:
        print('NENHUM PRODUTO CADASTRADO.')

def excluir_produto(nome_produto):
    try:
        with open(arquivo, 'r') as f:
            produtos = json.load(f)
    except FileNotFoundError:
        produtos = []

    produtos = [produto for produto in produtos if produto['nome_produto'] != nome_produto]

    with open(arquivo, 'w') as f:
        json.dump(produtos, f, indent=3)
    print(Cores.VERMELHO + 'PRODUTO EXCLUÍDO COM SUCESSO.' + Cores.RESET)

def verificar_validade(nome_produto):
    try:
        with open(arquivo, 'r') as f:
            produtos = json.load(f)
    except FileNotFoundError:
        produtos = []

    hoje = datetime.now()
    alerta_periodo = timedelta(days=30)

    produtos_vencidos = []
    produtos_pra_vencer = []

    for produto in produtos:
        if produto['nome_produto'] == nome_produto:
            data_val = datetime.strptime(produto['data de validade'], '%Y-%m-%d')
            if data_val < hoje:
                produtos_vencidos.append(produto)
            elif hoje <= data_val <= hoje + alerta_periodo:
                produtos_pra_vencer.append(produto)

    if produtos_vencidos:
        print(Cores.VERMELHO + 'PRODUTOS VENCIDOS:' + Cores.RESET)
        for produto in produtos_vencidos:
            print(f"NOME DO PRODUTO: {produto['nome_produto']}, QUANTIDADE: {produto['quantidade']}, DATA DE VALIDADE: {produto['data de validade']}")

    if produtos_pra_vencer:
        print(Cores.VERMELHO + 'PRODUTOS A VENCER:' + Cores.RESET)
        for produto in produtos_pra_vencer:
            print(f"NOME DO PRODUTO: {produto['nome_produto']}, QUANTIDADE: {produto['quantidade']}, DATA DE VALIDADE: {produto['data de validade']}")

    if not produtos_vencidos:
        print(Cores.VERDE + 'NENHUM PRODUTO VENCIDO FOI ENCONTRADO.' + Cores.RESET)

def menu_inicial():
    print(Cores.VERDE + '-' * 34 + Cores.RESET)
    print(Cores.MAGENTA + 'BEM-VINDO AO ESTOQUE DO ATACADÃO!' + Cores.RESET)
    print('1 - ABRIR GERENCIAMENTO DE ESTOQUE')
    print('2 - SAIR')
    print(Cores.VERDE + '-' * 34 + Cores.RESET)

def exibir_menu():
    print(Cores.MAGENTA + '\nMENU:' + Cores.RESET)
    print('1. ADICIONAR UM PRODUTO')
    print('2. LISTAR PRODUTOS')
    print('3. VERIFICAR VALIDADE')
    print('4. CHECAR PRODUTO')
    print('5. ATUALIZAR PRODUTO')
    print('6. EXCLUIR PRODUTO')
    print('7. VOLTAR AO MENU INICIAL')

def limpar_tela():
    if os.name == 'nt':
        os.system('cls')

def main():
    while True:
        limpar_tela()
        menu_inicial()
        opcao_inicial = int(input('INFORME UMA OPÇÃO: '))

        if opcao_inicial == 1:
            while True:
                exibir_menu()
                opcao = input('\nESCOLHA UMA OPÇÃO: \n>>> ')

                if opcao == "1":
                    nome_produto = input('DIGITE O NOME DO PRODUTO: \n>>> ')
                    quantidade = int(input('DIGITE A QUANTIDADE DE PRODUTOS: \n>>> '))
                    data_val = input('DIGITE A DATA DE VALIDADE DO PRODUTO [AAAA-MM-DD]: \n>>> ')
                    adicionar_produto(nome_produto, quantidade, data_val)
                elif opcao == '2':
                    listar_produtos()
                elif opcao == '3':
                    nome_produto = input('DIGITE O NOME DO PRODUTO: \n>>> ')
                    verificar_validade(nome_produto)
                elif opcao == '4':
                    nome_produto = input('DIGITE O NOME DO PRODUTO: \n>>> ')
                    checar_produto(nome_produto)
                elif opcao == '5':
                    produto_antigo = input('DIGITE O NOME DO PRODUTO A SER ATUALIZADO: \n>>> ')
                    produto_novo = input('DIGITE O NOME DO PRODUTO ATUALIZADO: \n>>> ')
                    quantidade_nova = int(input('DIGITE A NOVA QUANTIDADE DE PRODUTOS: \n>>> '))
                    data_val_nova = input('DIGITE A NOVA DATA DE VALIDADE: \n>>> ')
                    atualizar_produto(produto_antigo, produto_novo, quantidade_nova, data_val_nova)
                elif opcao == '6':
                    nome_produto = input('DIGITE O NOME DO PRODUTO A SER EXCLUÍDO: \n>>> ')
                    excluir_produto(nome_produto)
                elif opcao == '7':
                    print(Cores.MAGENTA + 'VOLTANDO AO MENU INICIAL...' + Cores.RESET)
                    sleep(3)
                    break
                else:
                    print(Cores.VERMELHO + 'OPÇÃO INVÁLIDA. TENTE NOVAMENTE!' + Cores.RESET)

        elif opcao_inicial == 2:
            print(Cores.MAGENTA + 'SAINDO...' + Cores.RESET)
            sleep(3)
            break

        else:
            print(Cores.VERMELHO + 'OPÇÃO INVÁLIDA. TENTE NOVAMENTE!' + Cores.RESET)

if __name__ == "__main__":
    main()
