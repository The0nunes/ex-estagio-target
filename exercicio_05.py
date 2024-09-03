# 5) Escreva um programa que inverta os caracteres de um string.
# IMPORTANTE:
# a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
# b) Evite usar funções prontas, como, por exemplo, reverse;

string = input('Digite: ')

string_invertida = ""

for letra in string:
    string_invertida = letra + string_invertida

print(f'String original: {string}')
print(f'String invertida: {string_invertida}')
