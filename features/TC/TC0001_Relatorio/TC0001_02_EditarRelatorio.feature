#language: pt

@All @TC0001 @TC0001_02_EditarRelatorio
Funcionalidade: Edição de relatórios no sistema

    @TC0001_02_01
    Cenário: Editar um relatório com Sucesso
        Dado que eu esteja logado no sistema
        E tenha um relatório já criado
        Quando acesso a página de relatórios
        E pesquiso o relatório criado
        E clico no botão de editar relatório
        E preencho o nome do relatório
        E seleciono as apis a serem consumidas por esse relatório
        E clico em salvar
        Então o relatório é atualizado com sucesso e a mensagem de sucesso é exibida


    @TC0001_02_02
    Cenário: Editar um relatório com Falha, removendo apis consumidas
        Dado que eu esteja logado no sistema
        E tenha um realtório já criado
        Quando acesso a página de relatórios
        E pesquiso o relatório criado
        E clico no botão de editar relatório
        E preencho o nome do relatório
        E não seleciono as apis a serem consumidas por esse relatório
        Então o botão de salvar não deve estar habilitado

    
    @TC0001_02_03
    Cenário: Editar um relatório com Falha, removendo nome do relatório
        Dado que eu esteja logado no sistema
        E tenha um realtório já criado
        Quando acesso a página de relatórios
        E pesquiso o relatório criado
        E clico no botão de editar relatório
        E removo o nome do relatório
        E seleciono as apis a serem consumidas por esse relatório
        Então o botão de salvar não deve estar habilitado
