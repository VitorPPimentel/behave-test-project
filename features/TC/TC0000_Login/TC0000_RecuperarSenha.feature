#language: pt

@TC0000 @TC0000_02_RecuperarSenha
Funcionalidade: Recuperar a senha no modelo bright

    @TC0000_02_01 
    Esquema do Cenário: Login Sucesso
        Dado que esteja na página de login do Bright
        Quando clico no botão recuperar senha 
        E insiro o <email> para recuperar
        Então a senha é enviada para meu email

        Exemplos:
            | email             | senha  |
            | datacom@gmail.com | 123456 |

    
    @TC0000_02_02
    Esquema do Cenário: Login Falha, email incorreto
        Dado que esteja na página de login do Bright
        Quando clico no botão recuperar senha 
        E insiro o <email> para recuperar
        Então a mensagem de erro é exibida

        Exemplos:
            | email            | senha   |
            | bright@gmail.co  | 123456  | 

