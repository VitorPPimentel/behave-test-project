#language: pt

@All @TC0000 @TC0000_01_Login
Funcionalidade: Login no sistema

    @TC0000_01_01
    Esquema do Cenário: Login Sucesso
        Dado que esteja na página de login
        Quando insiro <email> no campo email do login
        E insiro <senha> no campo senha do login
        E clico no botão realizar login
        Então a página inicial é carregada

        Exemplos:
            | email             | senha  |
            | jonhDoe@email.com | 123456 |


    @TC0000_01_02
    Esquema do Cenário: Login Falha, usuario ou senha incorretos
        Dado que esteja na página de login
        Quando insiro <email> no campo email do login
        E insiro <senha> no campo senha do login
        E clico no botão realizar login
        Então a mensagem de erro é exibida

        Exemplos:
            | email             | senha  |
            | jonhDoe@email.co  | 123456 |
            | jonhDoe@email.com | 12345  |
