#language: pt

@TC0000 @TC0000_02_RecuperarSenha
Funcionalidade: Recuperar a senha no sistema

    @TC0000_02_01 
    Esquema do Cenário: Recuperação de senha com sucesso
        Dado que esteja na página de login
        Quando clico no botão recuperar senha 
        E insiro o <email> para recuperar
        E a página de código de recuperação aparece
        E eu insiro o código de recuperação no campo
        E a página de trocar de senha aparece
        E insiro <nova_senha> no campo nova senha
        E insiro <nova_senha> no campo nova senha confirmação
        Então a página inicial do sistema é carregada

        Exemplos:
            | email         | senha  | nova_senha |
            | mail@mail.com | 123456 | 654321     |

    @TC0000_02_02
    Esquema do Cenário: Recuperação de senha Falha, email incorreto
        Dado que esteja na página de login
        Quando clico no botão recuperar senha 
        E insiro o <email> para recuperar
        Então a mensagem de erro é exibida

        Exemplos:
            | email         | senha   |
            | mail@mail.com | 123456  | 

