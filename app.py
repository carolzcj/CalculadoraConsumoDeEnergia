#Entrada de dados
aparelho = input("Digite o nome do aparelho:")
potencia = float(input("Digite a potência em watts(W): "))
horas_dia = float(input("Digite o tempo de uso diário em horas:"))

#Calculo
consumo_mensal = (potencia * horas_dia * 30)/1000

#Calculo de Custo
custo_kwh = 0.75
custo_estimado = consumo_mensal * custo_kwh

#Saida de dados
print("\n--- Resultado ---")
print(f"Aparelho: {aparelho}")
print(f"Consumo estimado: {consumo_mensal:.2f} kWh/mês")
print(f"Custo estimado: R$ {custo_estimado:.2f}")