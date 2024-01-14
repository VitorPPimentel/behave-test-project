#language: pt

@All @TC0000 @TC0000_01_Login
Funcionalidade: Login Bright 

    @TC0000_01_01
    Esquema do Cenário: Login Sucesso
        Dado que esteja na página de login do Bright
        Quando insiro <email> no campo email do login
        E insiro <senha> no campo senha do login
        E clico no botão realizar login
        Então a página inicial é carregada

        Exemplos:
            | email             | senha  |
            | rafael@datacomrn.com.br | 123456 |


    @TC0000_01_02
    Esquema do Cenário: Login Falha, usuario ou senha incorretos
        Dado que esteja na página de login do Bright
        Quando insiro <email> no campo email do login
        E insiro <senha> no campo senha do login
        E clico no botão realizar login
        Então a mensagem de erro é exibida
        

        Exemplos:
            | email             | senha   |
            | bright@gmail.co   | 123456 |
            | bright@gmail.com  | 12345  |
