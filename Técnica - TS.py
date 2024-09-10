"""
Mylena Viana Nunes - 10/09/24
"""

# Questão 1
INDICE = 13
SOMA = 0
K = 0

while K < INDICE:
    K = K + 1
    SOMA = SOMA + K

print(SOMA)


# Questão 2
def pertence_fibonacci(n):
    a, b = 0, 1
    while a < n:
        a, b = b, a + b
    return a == n

numero = int(input("Informe um numero: "))
if pertence_fibonacci(numero):
    print(f"O numero {numero} pertence a sequencia de Fibonacci.")
else:
    print(f"O numero {numero} nao pertence a sequencia de Fibonacci.")


# Questão 3
import json

dados_json = '''
{
    "faturamento": [100, 200, 150, 0, 0, 300, 250, 0, 0, 400, 500, 600, 0, 700, 0, 0, 800, 900, 1000, 0, 1100, 1200, 0, 1300, 0, 1400, 1500, 1600, 1700, 1800, 0, 1900, 2000, 0, 2100, 2200, 0, 2300, 2400, 2500, 2600, 2700, 2800, 2900, 3000]
}
'''

dados = json.loads(dados_json)
faturamento = dados['faturamento']

dias_com_faturamento = [f for f in faturamento if f > 0]

menor_valor = min(dias_com_faturamento)
maior_valor = max(dias_com_faturamento)

media_mensal = sum(dias_com_faturamento) / len(dias_com_faturamento)

dias_acima_da_media = len([f for f in dias_com_faturamento if f > media_mensal])

print(f"Menor valor de faturamento: R${menor_valor:.2f}")
print(f"Maior valor de faturamento: R${maior_valor:.2f}")
print(f"Numero de dias com faturamento acima da media: {dias_acima_da_media}")


# Questão 4
faturamento_estados = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

total_faturamento = sum(faturamento_estados.values())

percentuais = {estado: (valor / total_faturamento) * 100 for estado, valor in faturamento_estados.items()}

for estado, percentual in percentuais.items():
    print(f"Percentual de representação do estado {estado}: {percentual:.2f}%")


# Questão 5
def inverter_string(s):
    string_invertida = ""
    for char in s:
        string_invertida = char + string_invertida
    return string_invertida

entrada = input("Informe a string para inverter: ")
resultado = inverter_string(entrada)
print(f"String invertida: {resultado}")