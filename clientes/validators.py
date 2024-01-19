import re
from validate_docbr import CPF


def check_cpf(numero):
    cpf = CPF()
    return cpf.validate(numero)

def check_nome(nome):
    return nome.isalpha()

def check_rg(rg):
    return len(rg) == 9

def check_cel(celular):
    modelo = "[0-9]{2} [0-9]{5}-[0-9]{4}"
    resposta = re.findall(modelo, celular)
    return resposta
    