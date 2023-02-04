import random
import string

def gera_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + "!@#$%&*()"
    senha = "".join(random.choices(caracteres, k=tamanho))
    return senha

tamanho = int(input("Qual o tamanho da senha que você deseja? "))

senha = gera_senha(tamanho)
print(senha)
