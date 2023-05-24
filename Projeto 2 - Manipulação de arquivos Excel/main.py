from datetime import date
from openpyxl import Workbook
from openpyxl.styles import PatternFill, Alignment, Font
from openpyxl.chart import LineChart, Reference
from openpyxl.drawing.image import Image

from classes import GerenciadorPlanilha, LeitorAcoes, PropriedadeSerieGrafico

# acao = input("Qual o código da Ação que você quer processar? ").upper()

try:
    acao = 'AZEV4'

    leitor_acoes = LeitorAcoes(caminho_arquivo='./dados/')
    leitor_acoes.processa_arquivo(acao)
        
    gerenciador = GerenciadorPlanilha()
    planilha_dados = gerenciador.adiciona_planilha("Dados")

    gerenciador.adiciona_linha(["DATA", "COTAÇÃO", "BANDA INFERIOR", "BANDA SUPERIOR"])

    indice = 2

    for linha in leitor_acoes.dados:
        # Data
        ano_mes_dia = linha[0].split(" ")[0]
        data = date(
            year=int(ano_mes_dia.split("-")[0]),
            month=int(ano_mes_dia.split("-")[1]),
            day=int(ano_mes_dia.split("-")[2])
        )
        
        # Cotação
        cotacao = float(linha[1])
        
        formula_bb_inferior = f'=AVERAGE(B{indice}:B{indice + 19})-2*STDEV(B{indice}:B{indice + 19})'
        formula_bb_superior = f'=AVERAGE(B{indice}:B{indice + 19})+2*STDEV(B{indice}:B{indice + 19})'

        # Atualiza as células da Planilha Ativa do Excel
        gerenciador.atualiza_celula(celula=f'A{indice}', dado = data)
        gerenciador.atualiza_celula(celula=f'B{indice}', dado = cotacao)
        gerenciador.atualiza_celula(celula=f'C{indice}', dado = formula_bb_inferior)
        gerenciador.atualiza_celula(celula=f'D{indice}', dado = formula_bb_superior)
        
        indice += 1

    gerenciador.adiciona_planilha(titulo_planilha='Gráfico')

    # Mesclagem de células para criação do cabeçalho do Gráfico
    gerenciador.mescla_celulas(celula_inicio='A1', celula_fim='T2')

    gerenciador.aplica_estilos(
        celula='A1',
        estilos=[
            ('font', Font(b=True, sz=18, color="FFFFFF")),
            ('fill', PatternFill("solid", fgColor="07838F")),
            ('alignment', Alignment(vertical="center", horizontal="center"))
        ]
    )

    gerenciador.atualiza_celula('A1', "Histórico de Cotações")

    referencia_cotacoes = Reference(planilha_dados, min_col=2, min_row=2, max_col=4, max_row=indice)
    referencia_datas = Reference(planilha_dados, min_col=1, min_row=2, max_col=1, max_row=indice)

    gerenciador.adiciona_grafico_linha(
        celula='A3',
        comprimento=33.87,
        altura=14.82,
        titulo=f'Cotações - {acao}',
        titulo_eixo_x='Data da Cotação',
        titulo_eixo_y='Valor da Cotação',
        referencia_eixo_x=referencia_cotacoes,
        referencia_eixo_y=referencia_datas,
        propriedades_grafico=[
            PropriedadeSerieGrafico(espessura=0, cor_preenchimento='0a55ab'),
            PropriedadeSerieGrafico(espessura=0, cor_preenchimento='a61508'),
            PropriedadeSerieGrafico(espessura=0, cor_preenchimento='12a154')
        ]
    )

    gerenciador.mescla_celulas(celula_inicio='I32', celula_fim='L35')
    gerenciador.adiciona_imagem(celula='I32', caminho_imagem='./recursos/logo.png')

    gerenciador.salva_arquivo('./saída/Análise de Bollinger.xlsx')


except AttributeError:
    print("Atributo inexistente.")

except ValueError:
    print("Formato de dados incorreto! Favor verificar.")

except FileNotFoundError:
    print("Arquivo não encontrado!")

except Exception as excecao:
    print(f"Ocorreu um erro durante a execução do programa. Erro: {str(excecao)}")