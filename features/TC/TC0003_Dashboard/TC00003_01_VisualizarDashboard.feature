#language: pt

Funcionalidade: visualizar dashboard
    Cenário: visualizar a dashboard com sucesso
        Dado que eu esteja logado no sistema
        E tenha um relatório já criado
        Quando acesso a página de dashboard
        Então o dashboard do relatório aparece com sucesso