#language: pt

@All @TC0001 @TC0001_03_ApagarRelatorio
Funcionalidade: Deletar relatório
    @TC0001_03_01
    Cenário: Apagar relatório com sucesso
        Dado que eu esteja logado no sistema
        E tenha um relatório já criado
        Quando acesso a página de relatórios
        E pesquiso o relatório criado
        E clico no botão de apagar relatório
        Então o relatório será apagado e a mensagem de sucesso aparece