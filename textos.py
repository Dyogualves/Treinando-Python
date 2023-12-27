faturamento = 1000
custo = 700

lucro = faturamento - custo

# print(f"Faturamento: {faturamento}, Custo: {custo}, Lucro: {lucro} ")

# print("faturamento:" + str(faturamento)  + ",Custo: " + str(custo) + ", Lucro: " + str(lucro) )


email = "EMAIL_falso@gmail.com"

print(email.lower())
print(email.find("@")) # -1, se não encontar o elemento. Se encontrar: a posição do elemento

posicao = email.find("@")
servidor = email[posicao+1:]
print(servidor)


# tamanho de um texto

tamanho = len(email)
print(tamanho)

# trocar um pedaco de texto
email_trocado = email.replace("gmail.com", "hotmail.com")
print(email_trocado)

