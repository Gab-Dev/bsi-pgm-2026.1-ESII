# Diagramas e Decomposição do Projeto

## Decomposição em camadas

### models/
- Equipamento: representa os equipamentos do sistema e concentra apenas os dados do domínio.
- Emprestimo: representa um empréstimo realizado no sistema.

### services/
- ServicoEmprestimo: concentra as regras de negócio relacionadas aos empréstimos.
- Notificador: responsável apenas pelo envio de notificações.

### repositories/
- RepositorioEmprestimo: responsável pelo acesso e armazenamento dos dados.

### main.py
- Responsável pela interação com o usuário via terminal.



## Diagramas de sequência

### UC01 — Registrar Empréstimo

```mermaid
sequenceDiagram
    actor Atendente
    participant main as main.py
    participant servico as ServicoEmprestimo
    participant repo as RepositorioEmprestimo
    participant notif as Notificador

    Atendente->>main: informa equip_id, nome, email, dias
    main->>servico: registrar(equip_id, nome, email, dias)
    servico->>repo: buscar_equipamento(equip_id)
    repo-->>servico: Equipamento

    alt equipamento disponível
        servico->>repo: salvar_emprestimo(emprestimo)
        servico->>repo: marcar_indisponivel(equip_id)
        servico->>notif: notificar_emprestimo(email, data_devolucao)
        servico-->>main: True
    else equipamento indisponível
        servico-->>main: False
    end
```


### UC02 — Registrar Devolução

```mermaid
sequenceDiagram
    actor Atendente
    participant main as main.py
    participant servico as ServicoEmprestimo
    participant repo as RepositorioEmprestimo
    participant notif as Notificador

    Atendente->>main: informa emprestimo_id
    main->>servico: registrar_devolucao(emprestimo_id)

    servico->>repo: buscar_emprestimo(emprestimo_id)
    repo-->>servico: Emprestimo

    alt empréstimo encontrado
        servico->>repo: marcar_disponivel(equip_id)
        servico->>repo: finalizar_emprestimo(emprestimo_id)
        servico->>notif: notificar_devolucao(email)
        servico-->>main: True
    else empréstimo não encontrado
        servico-->>main: False
    end
```



### UC03 — Listar Empréstimos em Atraso

```mermaid
sequenceDiagram
    actor Atendente
    participant main as main.py
    participant servico as ServicoEmprestimo
    participant repo as RepositorioEmprestimo

    Atendente->>main: solicitar atrasados
    main->>servico: listar_atrasados()

    servico->>repo: buscar_atrasados()
    repo-->>servico: lista_emprestimos

    loop para cada empréstimo
        servico-->>main: mostrar empréstimo
    end
```