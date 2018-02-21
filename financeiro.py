def inss(salario):
    return salario*0.2

def ir(salario,dep):
    return salario-(100*dep)-inss(salario)
