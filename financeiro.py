def calcula_inss(salario):
    if salario <= 1000.0:
        return 0.0
    elif salario <= 2000.0:
        return salario*0.1
    else:
        return salario*0.2

def calcula_ir(salario_base):
    if salario_base <= 1400:
        return 0.0
    elif salario_base <= 2500.0:
        return salario_base*0.12
    elif salario <= 5000.0:
        return salario_base*0.2
    else:
        salario*0.275

def desconto_dep(dep):
    return 100.0*dep

    

def salario_liquido(salario,dep):
    return salario - calcula_inss(salario) - calcula_ir(salario,dep)
