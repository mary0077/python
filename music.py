import numpy as np
from scipy.io.wavfile import write

# Frequências da escala de Dó maior (C4 a C5)
notas = {
    'C4': 261.63,
    'D4': 293.66,
    'E4': 329.63,
    'F4': 349.23,
    'G4': 392.00,
    'A4': 440.00,
    'B4': 493.88,
    'C5': 523.25,
}

# Parâmetros do áudio
sample_rate = 44100  # 44.1 kHz
duracao = 0.5  # duração de cada nota em segundos

# Gerar escala
escala = np.array([], dtype=np.float32)

for freq in notas.values():
    t = np.linspace(0, duracao, int(sample_rate * duracao), False)
    onda = 0.5 * np.sin(2 * np.pi * freq * t)  # volume reduzido
    escala = np.concatenate((escala, onda))

# Normalizar para 16-bit
escala_int16 = np.int16(escala / np.max(np.abs(escala)) * 32767)

# Salvar o arquivo .wav
write("escala.wav", sample_rate, escala_int16)

print("Arquivo 'escala.wav' gerado com sucesso!")
