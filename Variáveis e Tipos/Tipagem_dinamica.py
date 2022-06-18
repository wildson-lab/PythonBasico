# Este código demonstra a tipagem dinâmica do Python
# Observe que a mesma variavel assume diversos tipos durante a execução

var = "Wildson Lab"
print(f"A variável var é do tipo {type(var)}.")

var = 42
print(f"Agora var é do tipo {type(var)}.")

var = 3.14
print(f"Agora var é do tipo {type(var)}.")

var = True
print(f"Agora var é do tipo {type(var)}.")

var = {"arroz", "feijão", "batata"}
print(f"Agora var é do tipo {type(var)}.")
