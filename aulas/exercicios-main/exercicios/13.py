def calcular_peso_ideal():
    """Calcula o peso ideal com base na altura e sexo."""

    altura = float(input('Digite sua altura em metros:'))
    sexo = input('Digite seu sexo[F/M]:').upper()

    if sexo == 'F':
        peso_ideal = (62.1 * altura) - 44.7
        print(f"O peso ideal para mulheres com {altura}m é: {peso_ideal:.2f} kg")
    elif sexo == 'M':
        peso_ideal = (72.7 * altura) - 58
        print(f"O peso ideal para homens com {altura}m é: {peso_ideal:.2f} kg")
    else:
        print('Caracteres inválidos.')

calcular_peso_ideal()