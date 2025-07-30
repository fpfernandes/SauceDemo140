Feature: Selecionar Produtos

    Scenario: Selecionar produto "Sauce Labs Backpack"
        Given que acesso o site Sauce SauceDemo140
        When preencho os campos de login com usuario standard_user e senha secret_sauce
        Then sou direcionado para pagina Home

    