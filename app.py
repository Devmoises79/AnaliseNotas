import statistics

# Lista para armazenar as notas
notas = []

def adicionar_nota():
    try:
        nota = float(input("Digite a nota do aluno (0 a 10): "))
        if 0 <= nota <= 10:
            notas.append(nota)
            print("Nota adicionada com sucesso!\n")
        else:
            print("Nota inválida. Digite um valor entre 0 e 10.\n")
    except ValueError:
        print("Entrada inválida! Digite um número.\n")

def mostrar_relatorio():
    if not notas:
        print("Nenhuma nota cadastrada ainda.\n")
        return

    print("\n--- RELATÓRIO DE NOTAS ---")
    print(f"Notas cadastradas: {notas}")
    print(f"Média: {statistics.mean(notas):.2f}")
    print(f"Mediana: {statistics.median(notas):.2f}")
    try:
        print(f"Moda: {statistics.mode(notas):.2f}")
    except statistics.StatisticsError:
        print("Moda: Não existe moda única (valores repetidos ou únicos)")
    
    if len(notas) >= 2:
        print(f"Desvio padrão: {statistics.stdev(notas):.2f}")
    else:
        print("Desvio padrão: precisa de pelo menos 2 notas.")
    
    print(f"Maior nota: {max(notas)}")
    print(f"Menor nota: {min(notas)}\n")


def menu():
    while True:
        print("=== Sistema de Análise de Notas ===")
        print("1. Adicionar nota")
        print("2. Mostrar relatório")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_nota()
        elif opcao == "2":
            mostrar_relatorio()
        elif opcao == "3":
            print("Saindo... Até logo!")
            break
        else:
            print("Opção inválida! Tente novamente.\n")

if __name__ == "__main__": 
    menu()
