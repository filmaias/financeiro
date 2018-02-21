def calcula_inss(a):
    if a <= 1000.0:
        return 0.0
    elif a <= 2000.0:
        return a*0.1
    else:
        return a*0.2

def desconto_dep(dep):
    return 100.0*dep

def calcula_ir(salario,dep):
    salario_base=salario-calcula_inss(salario)-desconto_dep(dep)
    if salario_base <= 1400:
        return 0.0
    elif salario_base <= 2500.0:
        return salario_base*0.12
    elif salario_base <= 5000.0:
        return salario_base*0.2
    else:
        return salario_base*0.275


def salario_liquido(salario,dep):
    return salario - calcula_inss(salario) - calcula_ir(salario,dep)

a=float(input("Salário bruto: "))
dep=int(input("Qtd de dependentes: "))

final=salario_liquido(a,dep)

print ("O salário liquído é de %.1f reais" %final )
