import random

def lancar_moeda(prob_cara=0.5):
    return "CARA" if random.random() < prob_cara else "COROA"

def simulacao():
    print("=== SIMULADOR DE MOEDA DA SORTE ===")
    
    # Sorteia se a moeda é justa ou viciada
    justa = random.choice([True, False])
    prob_cara = 0.5 if justa else random.choice([0.7, 0.8, 0.3, 0.2])
    
    n = int(input("Quantos lançamentos deseja simular? "))
    resultados = [lancar_moeda(prob_cara) for _ in range(n)]
    
    print("\nResultado dos lançamentos:")
    print(resultados)
    
    print("\nFrequência:")
    print("CARA:", resultados.count("CARA"))
    print("COROA:", resultados.count("COROA"))
    
    palpite = input("\nVocê acha que a moeda é justa ou viciada? ").lower()
    
    if (justa and palpite == "justa") or (not justa and palpite == "viciada"):
        print("✅ Acertou! A moeda tinha probabilidade de", prob_cara, "para CARA.")
    else:
        print("❌ Errado! A moeda tinha probabilidade de", prob_cara, "para CARA.")

if __name__ == "__main__":
    simulacao()
