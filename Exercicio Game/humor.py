import random

playlists = {
    "feliz": ["Dançando no Sol", "Café com Sorrisos", "Energia Infinita", "Alegria sem Fim"],
    "triste": ["Chuva no Coração", "Silêncio Profundo", "Noites Vazias", "Saudades Eternas"],
    "raiva": ["Explosão Sonora", "Tempestade de Fogo", "Gritos na Cidade", "Caos Total"],
    "calmo": ["Brisa da Manhã", "Mar Sereno", "Lua Tranquila", "Silêncio e Paz"],
    "motivado": ["Conquista do Amanhã", "Subindo ao Topo", "Força Inquebrável", "Foco e Vitória"]
}

def gerar_playlist(humor):
    humor = humor.lower()
    if humor in playlists:
        print(f"\n🎵 Playlist para {humor.upper()}:")
        for musica in random.sample(playlists[humor], 3):  # escolhe 3 aleatórias
            print("-", musica)
    else:
        print("😅 Não conheço esse humor ainda. Tente: feliz, triste, raiva, calmo, motivado.")

def main():
    print("=== GERADOR DE PLAYLIST DE HUMOR ===")
    while True:
        humor = input("Como você está se sentindo hoje? ")
        gerar_playlist(humor)
        
        continuar = input("\nQuer gerar outra playlist? (s/n): ").lower()
        if continuar != "s":
            print("Encerrando o gerador de playlists. Até mais! 🎶")
            break

if __name__ == "__main__":
    main()
