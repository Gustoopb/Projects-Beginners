import random

chars = 'abcdefghijklmnopqrstuvxwyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-=!@#$%¨&*()_+'

password_count = int(input("Digite quantas senhas você vai querer:"))

password_len = int(input("Digite o numero do tamanho da senha que você quer:"))

for x in range(0, password_count):
    password = ''
    for x in range(0, password_len):
        password_chars = random.choice(chars)
        password = password + password_chars
    print("As senhas que você quer: ", password)