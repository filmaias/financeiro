def calcula_inss(salario):
    if salario <= 1000:
        return 0.0
    elif salario <= 2000:
        return salario*0.1
    else:
        return salario*0.2

def calcula_ir(salario,dep):
    return (salario-(100*dep)-inss(salario))*0.05

def salario_liquido(salario,dep):
    return salario - calcula_inss(salario) - calcula_ir(salario,dep)
