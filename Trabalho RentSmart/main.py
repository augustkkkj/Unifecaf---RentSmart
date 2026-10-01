import csv as cv  #importa o gerador de arquivos CSV mudando o nome pra cv


#classe principal dos imoveis
#ela vai servir como base pro apartamento, casa e estudio
class Imovel:

    def __init__(self, tipo, aluguelBase, quartos):
        self.tipo = tipo
        self.aluguelBase = aluguelBase
        self.quartos = quartos
        self.valorMensal = aluguelBase  #começa o aluguel com o valor base

    def calcularAluguel(self):
        #esse metodo vai ser sobrescrito pelas classes filhas
        pass


#classe apartamento herdando as informações da classe Imovel
class Apartamento(Imovel):

    def __init__(self, quartos, temGaragem, semCriancas):

        # hama o __init__ da classe Imovel
        #define o tipo como apartamento e o aluguel base como R$ 700
        super().__init__("Apartamento", 700.00, quartos)

        self.temGaragem = temGaragem
        self.semCriancas = semCriancas

    def calcularAluguel(self):

        #se o apartamento tiver 2 quartos adiciona R$ 200 no aluguel
        if self.quartos == 2:
            self.valorMensal += 200.00

        #se tiver garagem adiciona R$ 300 no aluguel
        if self.temGaragem:
            self.valorMensal += 300.00

        #se não tiver crianças recebe 5% de desconto
        if self.semCriancas:
            self.valorMensal *= 0.95

        #retorna o valor final do aluguel
        return self.valorMensal


#classe casa herdando as informações da classe Imovel
class Casa(Imovel):

    def __init__(self, quartos, temGaragem):

        #chama o __init__ da classe Imovel
        #define o tipo como casa e o aluguel base como R$ 900
        super().__init__("Casa", 900.00, quartos)

        self.temGaragem = temGaragem

    def calcularAluguel(self):

        #se a casa tiver 2 quartos adiciona R$ 250
        if self.quartos == 2:
            self.valorMensal += 250.00

        #se tiver garagem adiciona R$ 300
        if self.temGaragem:
            self.valorMensal += 300.00

        #retorna o valor final do aluguel
        return self.valorMensal


#classe estudio herdando as informações da classe Imovel
class Estudio(Imovel):

    def __init__(self, vagasTotais):

        #chama o __init__ da classe Imovel
        #define o tipo como estudio, aluguel base de R$ 1.200 e 1 quarto
        super().__init__("Estudio", 1200.00, 1)

        self.vagasTotais = vagasTotais

    def calcularAluguel(self):

        #se tiver até 2 vagas adiciona R$ 250
        if self.vagasTotais <= 2:
            self.valorMensal += 250.00

        else:
            #calcula quantas vagas passaram das 2 vagas permitidas
            vagasExtras = self.vagasTotais - 2

            #adiciona R$ 250 pelas vagas iniciais
            #e mais R$ 60 para cada vaga extra
            self.valorMensal += 250.00 + (vagasExtras * 60.00)

        #retorna o valor final do aluguel
        return self.valorMensal


#função responsável por criar o arquivo CSV
def geradorCSV(nomeArqui, aluguelMensal, parcelasTaxa, valorParcelasTaxa):

    #abre/cria o arquivo CSV
    #'w' significa que vai escrever no arquivo
    #newline evita linhas vazias no CSV
    #encoding utf-8 permite caracteres como ç e acentos
    with open(nomeArqui, mode='w', newline='', encoding='utf-8') as arquivo:

        #cria o escritor do arquivo CSV
        escritor = cv.writer(arquivo)

        #cria o cabeçalho da tabela
        escritor.writerow([
            'Mes',
            'Aluguel Mensal (R$)',
            'Taxa Contratual (R$)',
            'Total no Mês (R$)'
        ])

        #vai gerar os dados dos 12 meses
        for mes in range(1, 13):

            #enquanto estiver dentro da quantidade de parcelas
            #adiciona o valor da parcela da taxa contratual
            #depois que terminar as parcelas, fica R$ 0
            taxaMes = valorParcelasTaxa if mes <= parcelasTaxa else 0.0

            # soma aluguel + taxa contratual daquele mês
            totalMes = aluguelMensal + taxaMes

            #escreve os dados do mês no arquivo CSV
            escritor.writerow([
                mes,
                f'{aluguelMensal:.2f}',
                f'{taxaMes:.2f}',
                f'{totalMes:.2f}'
            ])


#função principal do programa
#aqui vai ficar o menu e toda interação com o usuario
def home():

    #menu do aplicativo
    print('=== RentSmart - Sistema de Orçamento de Locação ===')
    print('Escolha o tipo de imovel:')
    print('1- Apartamento (Base: R$ 700,00)')
    print('2- Casa (Base: R$ 900,00)')
    print('3- Estúdio (Base: R$ 1.200,00)')

    #pega a opção escolhida pelo cliente
    opc = int(input('Escolha uma das opções: '))

    #começa a variavel vazia
    #depois ela vai receber Apartamento, Casa ou Estudio
    imovel = None

    #escolhas do cliente
    if opc == 1:

        #pergunta a quantidade de quartos
        quartos = int(input('Quantidade de quartos 1 ou 2: '))

        #pergunta se possui garagem
        #se o usuario digitar s, garagem recebe True
        #se digitar qualquer outra coisa recebe False
        garagem = input(
            'Possui vaga de garagem? (s/n): '
        ).lower() == 's'

        #pergunta se possui crianças
        #se responder n, semCrianca recebe True
        semCrianca = input(
            'Possui crianças? (s/n): '
        ).lower() == 'n'

        #cria um objeto da classe Apartamento
        imovel = Apartamento(quartos, garagem, semCrianca)

    elif opc == 2:

        #pergunta a quantidade de quartos
        quartos = int(input('Quantidade de quartos 1 ou 2: '))

        #pergunta se possui garagem
        garagem = input(
            'Possui vaga de garagem? (s/n): '
        ).lower() == 's'

        #cria um objeto da classe Casa
        imovel = Casa(quartos, garagem)

    elif opc == 3:

        #pergunta quantas vagas o cliente deseja
        vagas = int(
            input('Quantas vagas de estacionamento deseja (minimo 2)? ')
        )

        #cria um objeto da classe Estudio
        imovel = Estudio(vagas)

    else:

        # aso o cliente escolha uma opção errada
        #retorna uma mensagem e encerra a função
        print('Opção invalida!!!')
        return

    #chama o metodo calcularAluguel()
    #cada classe possui sua propria forma de calcular
    aluguelFinal = imovel.calcularAluguel()

    #define o valor total da taxa contratual
    taxaContratual = 2000.00

    #pergunta em quantas vezes o cliente deseja parcelar a taxa
    parcelas = int(
        input(
            'Em quantas vezes deseja parcelar a taxa contratual '
            'de R$2.000 (1 a 5): '
        )
    )

    #verifica se a quantidade de parcelas está dentro do permitido
    if parcelas < 1 or parcelas > 5:

        #caso seja uma quantidade invalida,
        #automaticamente define como 1 parcela
        parcelas = 1

    #calcula o valor de cada parcela da taxa contratual
    valorParcelaTaxa = taxaContratual / parcelas

    #mostra o resumo do orçamento na tela
    print("\n--- RESUMO DO ORÇAMENTO ---")
    print(f"Tipo de Imóvel: {imovel.tipo}")
    print(f"Valor Mensal do Aluguel: R$ {aluguelFinal:.2f}")

    print(
        f"Taxa Contratual Total: R$ {taxaContratual:.2f} "
        f"(dividida em {parcelas}x de R$ {valorParcelaTaxa:.2f})"
    )

    #define o nome do arquivo CSV que será criado
    nomeCSV = 'Projeto Locação 12 meses.csv'

    #chama a função responsável por gerar o arquivo CSV 
    geradorCSV(
        nomeCSV,
        aluguelFinal,
        parcelas,
        valorParcelaTaxa
    )

    #informa para o usuario que o arquivo foi criado
    print(
        f'\nProjeção de 12 meses gerada com sucesso '
        f'no arquivo: {nomeCSV}'
    )


#verifica se esse arquivo está sendo executado diretamente
#se estiver, chama a função principal home()
if __name__ == '__main__':
    home()