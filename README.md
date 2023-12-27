faturamento =  1200 # numero inteiro = int
custo = 770

novas_vendas = 300 
faturamentos = faturamento + novas_vendas

taxa_de_imposto = 0.1 # numero decimal = Float
mensagem = "o faturamento foi de" # texto = string
teve_lucro = False # booleano 


imposto = taxa_de_imposto * faturamento
print("Faturamento", faturamento)
print("custo", custo)
print("Lucro", faturamento - custo - imposto)
print(mensagem, faturamento)
