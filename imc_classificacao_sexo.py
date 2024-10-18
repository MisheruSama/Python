def calcular_imc(peso,altura):
    return peso/(altura**2)
def classificar_imc(imc,sexo):
    if sexo.lower()=='m':
        if imc<20.7:
            return "Abaixo do Peso"
        elif 20.7<=imc<=26.4:
            return "Peso Normal"
        elif 26.4<imc<=27.8:
            return "Levemente acima do Peso"
        elif 27.8<imc<=31.1:
            return "Acima do Peso Ideal"
        else:
            "Obesidade"
    elif sexo.lower()=='f':
        if imc<19.1:
            return "Abaixo do Peso"
        elif 19.1<=imc<=25.8:
            return "Peso Normal"
        elif 25.8<imc<=27.3:
            return "Levemente Acima do Peso"
        elif 27.3<imc<=32.3:
            return "Acima do Peso Ideal"
        else:
            "Obesidade"
    else:
        return "Sexo inválido! Use 'M' para Masculino e 'F' para Feminino"
def main():
    try:
        peso=float(input("Digite o peso em kg: "))
        altura=float(input("Digite a altura em metros: "))
        sexo=input("Digite o sexo('M' para Masculino e 'F' para Feminino): ")

        imc=calcular_imc(peso,altura)
        print(f"Seu IMC é: {imc:.2f}")

        classificacao=classificar_imc(imc,sexo)
        print(f"Classificação: {classificacao}")

    except ValueError:
        print("Por favor, insira valores numéricos válidos para peso e altura.")
main()
    
