import random

# Nucleotídeos possíveis
nucleotideos = ["A", "T", "C", "G"]

# Tabela simplificada de códons -> aminoácidos
tabela_genetica = {
    "ATG": "Metionina (Início)",
    "TAA": "STOP", "TAG": "STOP", "TGA": "STOP",
    "CGT": "Arginina", "CGA": "Arginina", "CGC": "Arginina",
    "GTT": "Valina", "GTA": "Valina", "GTG": "Valina",
    "ACT": "Treonina", "ACC": "Treonina", "ACA": "Treonina",
    "TTT": "Fenilalanina", "TTC": "Fenilalanina"
}

def gerar_dna(tamanho=12):
    return "".join(random.choice(nucleotideos) for _ in range(tamanho))

def traduzir_dna(dna):
    proteina = []
    for i in range(0, len(dna), 3):  # lê de 3 em 3 (códons)
        codon = dna[i:i+3]
        if len(codon) < 3:
            continue
        aminoacido = tabela_genetica.get(codon, "???")
        proteina.append(aminoacido)
        if aminoacido == "STOP":
            break
    return proteina

def main():
    print("=== GERADOR DE DNA ===")
    dna = gerar_dna(30)
    print("Sequência de DNA:", dna)
    proteina = traduzir_dna(dna)
    print("\nTradução em aminoácidos:")
    print(" - ".join(proteina))

if __name__ == "__main__":
    main()
