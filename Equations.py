import math

def resolver_primeiro_grau(a, b):
    if a == 0:
        if b == 0:
            return "Infinitas soluções (Identidade)"
        else:
            return "Sem solução"
    return f"Raiz única: x = {-b / a:.2f}"

def resolver_segundo_grau(a, b, c):
    if a == 0:
        return resolver_primeiro_grau(b, c)
    
    delta = (b ** 2) - (4 * a * c)
    print(f"-> Delta (Δ): {delta:.2f}")
    
    if delta < 0:
        return "A equação não possui raízes reais."
    elif delta == 0:
        return f"Possui uma raiz real única: x = {-b / (2 * a):.2f}"
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        return f"Possui duas raízes reais:\nx1 = {x1:.2f}\nx2 = {x2:.2f}"

while True:
    
    print("CALCULADORA DE EQUAÇÕES")
    print("1. Equação do 1º Grau (ax + b = 0)")
    print("2. Equação do 2º Grau (ax² + bx + c = 0)")
    print("3. Sair do Programa")
    
    opcao = input("Escolha uma opção: ").strip()

    if opcao == "3":
        print("\nFechando a calculadora...")
        break 
        
    if opcao == "1":
        print("\n[Grau 1] Estrutura: ax + b = 0")
        num_a = float(input("Digite o valor de a: "))
        num_b = float(input("Digite o valor de b: "))
        print(f"\nResultado: {resolver_primeiro_grau(num_a, num_b)}")

    elif opcao == "2":
        print("\n[Grau 2] Estrutura: ax² + bx + c = 0")
        num_a = float(input("Digite o valor de a: "))
        num_b = float(input("Digite o valor de b: "))
        num_c = float(input("Digite o valor de c: "))
        print(f"\nResultado: {resolver_segundo_grau(num_a, num_b, num_c)}")

    else:
        print("\nOpção inválida! Tente novamente.")
      
