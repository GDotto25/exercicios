cobertura_tinta = 3
capacidade_lata = 18
preco_lata = 80.0

tamanho_area = float(input("Digite o tamanho da área a ser pintada (em m²): "))

litros = tamanho_area/cobertura_tinta
latas_inteiras = int(litros/capacidade_lata)

if(litros%capacidade_lata != 0):
    latas_inteiras += 1

valor_total = latas_inteiras * preco_lata

print("Quantidade de litros de tinta necessárias: ", litros)
print("Quantidade de latas de tintas necessárias: ", latas_inteiras)
print("Valor total da compra : RS$ ", valor_total)
