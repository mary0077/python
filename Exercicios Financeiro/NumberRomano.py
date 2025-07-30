def romano_para_inteiro(s):
    valores = {
        'I': 1, 'V': 5, 'X': 10,
        'L': 50, 'C': 100,
        'D': 500, 'M': 1000
    }

    total = 0
    i = 0

    while i < len(s):
        # Verifica se há dois caracteres (como IV ou IX)
        if i + 1 < len(s) and valores[s[i]] < valores[s[i + 1]]:
            total += valores[s[i + 1]] - valores[s[i]]
            i += 2
        else:
            total += valores[s[i]]
            i += 1

    return total


# Testes
print(romano_para_inteiro("XIV"))      # 14
print(romano_para_inteiro("MCMXC"))    # 1990
print(romano_para_inteiro("CDXLIV"))   # 444
