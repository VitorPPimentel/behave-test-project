#language: pt

@All @TC0001 @TC0001_01_CriarRelatorio
Funcionalidade: Criar relatório no sistema
    
    @TC0001_01_01
    Cenário: criar um relatório com sucesso
        Dado que eu esteja logado no sistema
        Quando acesso a página de criação de relatórios
        E clico em novo relatório
        E preencho o nome do relatório
        E seleciono as apis que serão consumidas para esse relatório
        E clico em salvar
        Então o relatório será criado com sucesso e a mensagem de sucessso será exibida

    @TC0001_01_02
    Cenário: criar um relatório com erro
        Dado que eu esteja logado no sistema
        Quando acesso a página de criação de relatórios
        E clique em novo relatório
        E não seleciono as apis que serão consumidas para esse relatório
        Então o botão de salvar não deverá estar habilitado
