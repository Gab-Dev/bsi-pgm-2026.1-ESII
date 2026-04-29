# Resenha Aula 3 — Modelos UML e Design de Componentes
**Aluno:** Gabriel Levy Siqueira de Brito
**Data:** 29/04/2026

## Questão 1 — Modelos UML como ferramentas de modelagem

### (a) Estrutura × comportamento
O diagrama de classes se concentra na estrutura estática, ele evidencia a existência de objetos, seus atributos e as inter-relações entre eles (quem conhece quem). Nesse caso, o comportamento dinâmico e a sequência das operações se tornam invisíveis. Por outro lado, o diagrama de sequência se concentra na troca de mensagens ao longo de todo o tempo, destacando a ordem cronológica das frequências. Valente sustenta que são complementares, pois enquanto a classe estabelece a "estrutura" e as funcionalidades de um objeto, a sequência demonstra de que maneira esses objetos interagem para executar uma tarefa particular.

### (b) Consequência prática
O diagrama de classes auxilia na tomada de decisões sobre a organização e o acoplamento, ele determina se uma relação deve ser de composição ou se uma classe deve herdar da outra. Ele é essencial para as decisões de interface e da lógica, pois ele auxilia na determinação dos métodos públicos necessários para que o fluxo de mensagens de um caso de uso funcione sem interrupções nenhuma.

### (c) Aplicação ao UC01
O texto do casos_de_uso.md descreve a intenção do usuário no caso de uso "Registrar Empréstimo" (UC01). O diagrama de sequência mostraria detalhes técnicos que o texto não menciona, como a sequência precisa em que o sistema valida o status do equipamento e do usuário, além dos objetos (como um RepositorioEquipamento ou um ServicoEmprestimo) que trocam mensagens para realizar o registro.

## Questão 2 — Arquitetura, design e os princípios de decomposição

### (a) Definições
Para mim, a coesão é o objetivo de um módulo: se ele realiza apenas uma tarefa de forma eficiente e todos os elementos internos contribuem para isso, ele é coeso. Acoplamento é o grau de dependência entre as partes; quanto menos uma classe precisar conhecer os detalhes internos da outra para operar, melhor. O termo de esconder detalhes de implementação, como variáveis privadas, e expor apenas o que é necessário por meio de uma interface é chamada de ocultamento de informação.

### (b) Relações entre os princípios
O baixo acoplamento é possibilitado pelo ocultamento de informações, uma vez que, ao esconder detalhes internos, as alterações em um módulo não afetam os demais que o utilizam. Ele está relacionado à coesão ao assegurar que o módulo gerencie seus próprios dados. Sim, há uma tensão: para manter um módulo altamente específico e coeso, podemos acabar criando vários pequenos módulos que precisam se comunicar, o que pode elevar o acoplamento do sistema como um todo.

### (c) Aplicação ao projeto v2.0
De acordo com o ADR-001, a distribuição das classes seria a seguinte:  
- models/: Equipamento e Usuário. Devem possuir elevada coesão, englobando apenas as entidades de negócio e suas regras fundamentais.  
- repositories/: EquipamentoRepository. Concentra-se em esconder informações sobre o método de armazenamento dos dados (SQL, arquivo, etc.).  
- services/: ServicoEmpréstimo. Esta camada diminui o acoplamento entre a interface e os modelos, gerenciando a lógica do UC01.  
- main.py: ponto de entrada que conecta as camadas para dar início à aplicação.

## Questão 3 — Crítica fundamentada à documentação do sistema legado

### (a) Pontos frágeis
- Uso de variáveis globais: No código legado, o uso de estruturas globais para armazenar dados viola o princípio de ocultamento de informação e cria um acoplamento arriscado, em que qualquer parte do código pode modificar o estado do sistema de maneira imprevisível. 
- Baixa coesão em funções principais: funções que tentam validar, processar e imprimir resultados ao mesmo tempo têm baixa coesão, o que dificulta a manutenção e o reuso.

### (b) Ponto forte
A divisão inicial em arquivos distintos, embora ainda desorganizada, já representa um esforço para modularização. Segundo Valente, isso é positivo, pois demonstra uma intenção de dividir o problema em partes menores, o que torna mais fácil a transição para uma arquitetura em camadas mais clara na versão 2.0.

### (c) Síntese
A clareza ao apresentar as dívidas técnicas (DT01-DT07) indica que o desenvolvedor estava ciente das restrições, configurando uma dívida técnica intencional para a entrega do protótipo. Para a v2.0, essa atitude dá início a um ciclo de refatoração consciente, no qual o foco deixa de ser o "apenas funcionar" e passa a ser a sustentabilidade do código.

## Questão 4 — Tipos como contratos: dicionários × classes

### (a) Prevenção de erros
Se substituirmos dicionários por classes, falhas de digitação como equipamento["disponivel"] (escrevendo "disponivel" de forma incorreta) seriam detectadas durante o desenvolvimento ou compilação, ao invés de ocorrerem como KeyError em produção. Ademais, a classe assegura que o tipo do valor seja o apropriado (um booleano em vez de uma string, por exemplo).

### (b) Capacidade de evolução
Uma classe possibilita a inclusão de métodos como calcular_multa() sem modificar quem já utiliza o objeto, uma vez que o comportamento permanece encapsulado. Ao usar um dicionário, seria necessário criar funções externas e passar o dicionário para elas, o que dispersaria a lógica e tornaria mais difícil aprimorar o design sem comprometer outras partes do sistema.

### (c) Comunicação do design
Um tipo com o nome de Equipamento transmite uma intenção e um modelo mental explícito do que esse objeto simboliza no domínio do problema. Um dict é genérico e anônimo, não fornecendo informações sobre as regras de negócio vinculadas a esses dados. Por outro lado, o tipo funciona como um contrato que orienta o desenvolvedor.