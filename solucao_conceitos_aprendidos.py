import csv # Importou biblioteca csv, que permite python ler arquivos.csv
import time #importou biblioteca time, que permite que python faça calculos de tempo, hora, minuto... 

# Criou uma função que entra uma string (caminho do arquivo.csv) e retorna um dicionário
def processar_temperaturas(path_do_csv: str) -> dict:
    # Criou 4 dicionários
    minimas = {}
    maximas = {}
    somas = {}
    contagens = {}
    # Ainda dentro da função with para abrir e fechar arquivo
    # open para abrir o arquivo
        # path_do_csv é o paramentro que será inserido quando função processar_temperaturas for chamado
        # "r" significa que open vai apenas ler o arquivo
        # utf-8 serve para programa reconhecer acentos e ç
        # Chamou este arquivo aberto de "arquivo"
    with open(path_do_csv, "r", encoding="utf-8") as arquivo:
        # Criou variavel leitor
        # com csv.reader pediu para ler o arquivo e definiu ";" como separador dos valores, como se dividisse as colunas
        leitor = csv.reader(arquivo, delimiter=";")
        # Aqui começa o loop. Para cada linha do arquivo...
        for linha in leitor:
            # Criou variável estacao e definiu que o nome da estacao é o primeiro valor da linha. Mantendo o tipo string
            estacao = linha[0]
            # Criou a variável temperatura, e definiu que é segundo valor da linha. E definiu tipo float
            temperatura = float(linha[1])
            # Abriu condição. Se a variavel estacao está no dicionário contagens...
            if estacao in contagens:
                # Aquela estação vai somar mais 1 dentro de contagens
                contagens[estacao] += 1
                # Somas daquela estacao vai somar/acumular
                somas[estacao] += temperatura
                # Ainda tem nova condicional dentro da anterior: Se temperatura for menor que a temperatura desta estação no dict minimas...
                if temperatura < minimas[estacao]:
                    # Ele vai substituir o valor pelo novo minimo
                    minimas[estacao] = temperatura
                # Se a temperatura for maior do que a temperatura daquela estacao...
                if temperatura > maximas[estacao]:
                    # Ele vai substituir o valor pelo novo máximo
                    maximas[estacao] = temperatura
            # Else = Se a variável não está no dicionário contagens...
            else:
                # Ele cria aquela estação no dicionário contagens com valor 1, e define aquela temperatura como soma, min e max
                contagens[estacao] = 1
                somas[estacao] = temperatura
                minimas[estacao] = temperatura
                maximas[estacao] = temperatura
    # Ok, aqui acaba primeira parte da nova função "processar_temperaturas"
    # Ele cria a váriável resultados, tipo dicionário
    resultados = {}
    # E abre novo looping. Para cada estação no dicionário contagens, ele vai... (E em contagens, tem só 1 estação de cada por causa do que foi feito antes)
    for estacao in contagens:
        # Criou variável que calcula média. Pega o Valor do dicionário soma e divide pelo valor do dicionário contagens
        media = somas[estacao] / contagens[estacao]
        # Aqui ele registra no dicionário resultados a minimas, a média e a máxima. Obviamente de cada estacao por causa do for na linha 52
        resultados[estacao] = f"{minimas[estacao]:.1f}/{media:.1f}/{maximas[estacao]:.1f}"
    # No final ele entrega um dicionário(na ordem alfabética(da variável resultado))
    return dict(sorted(resultados.items())) # Só tenho dúvida porque o ".items" - Consultei caderno e entendi. Vai entregar os pares chave-valor


# Criou variavel inicio, e usa função da biblioteca time, que registra a hora que código passa por aqui.
inicio = time.time()
# Mostra que iniciou o processamento
print("Iniciando o processamento do arquivo.")

# Criou variável resultados e definiu para usar a função criada anteriormente e definiu o paramentro como data/measurements.txt
resultados = processar_temperaturas("data/measurements.txt")

# Criou nova variavel, que é o tempo que programa chegou aqui
fim = time.time()

# novo loop, para cada estação ("linha") do dicionário resultados (mostrando pares de chave e valor)
for estacao, metricas in resultados.items():
    # mostrar na tela nome da estação : metricas -- Ok, confesso que esta parte da "metricas", que não entendi, não lembro de ter visto , no meio do objeto do for
    print(f"{estacao}: {metricas}")

# Por fim ele mostra a diferença da variavel fim e da variavel inicio. Que vai ser o tempo todal para rodar o programa
print(f"\nProcessamento concluído em {fim - inicio:.2f} segundos.")
