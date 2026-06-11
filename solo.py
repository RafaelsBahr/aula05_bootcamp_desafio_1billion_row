import csv
import time

def processar_temperaturas (path_arquivo: str) -> dict:
    maximas = {}
    minimas = {}
    contagens = {}
    somas = {}
    with open(path_arquivo, "r", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo, delimiter=";")
        for linha in leitor:
            estacao = linha[0]
            temperatura = float(linha[1])
            if estacao in contagens:
                contagens[estacao] += 1
                somas[estacao] += temperatura
                if temperatura < minimas[estacao]:
                    minimas[estacao] = temperatura
                if temperatura > maximas[estacao]:
                    maximas[estacao] = temperatura
            else:
                contagens[estacao] = 1
                somas[estacao] = temperatura
                minimas[estacao] = temperatura
                maximas[estacao] = temperatura
    resultado = {}
    for estacao in contagens:
        media = somas[estacao] / contagens[estacao]
        resultado[estacao] = f"{minimas[estacao]:.1f}/{media:.1f}/{maximas[estacao]:.1f}"
    return dict(sorted(resultado.items()))

inicio = time.time()
resultados = processar_temperaturas("data/measurements.txt")
fim = time.time()


for estacao, metricas in resultados.items():
    print(f"{estacao}: {metricas}")

print(f"\nProcessamento concluído em {fim - inicio:.2f} segundos.")
