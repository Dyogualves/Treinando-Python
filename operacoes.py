faturamento = 1000
custo = 700

novas_vendas= 300

faturamento = faturamento + novas_vendas # Somar
imposto = faturamento * 0.1 # Multiplicar
lucro = faturamento - custo  - imposto # Subtrair  


print(faturamento)
print(lucro)
margem_lucro = lucro / faturamento # Dividir 
print(margem_lucro)

restituicao = imposto * 0.1 
print(restituicao)

# Mod resto da divisão 
# 10 % 3 
print(10 % 3)
tempo_em_meses = 160
tempo_em_anos = int(tempo_em_meses / 12)
print(tempo_em_anos, "anos")
print(tempo_em_meses % 12, "meses")

numero = 123.37
print(round(numero))



