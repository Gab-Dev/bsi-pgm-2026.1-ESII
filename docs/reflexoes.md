## Aula 04 — SRP

A decisão mais difícil foi separar a responsabilidade de notificação do ServicoEmprestimo. Inicialmente parecia mais simples deixar os prints de e-mail dentro da própria lógica de negócio, porque o envio acontece durante o empréstimo. Porém, analisando o princípio SRP discutido por Valente no Capítulo 5, percebi que isso criaria dois motivos diferentes para alteração na mesma classe: mudanças na regra de negócio e mudanças na notificação.

A separação exigiu pensar melhor sobre as fronteiras entre os componentes e aumentou um pouco o número de arquivos, mas trouxe mais organização e clareza para o sistema. O critério utilizado foi justamente o conceito de responsabilidade única apresentado por Valente, buscando garantir maior coesão e menor acoplamento entre os módulos.

## Aula 05 — OCP

A aplicação do OCP através de polimorfismo melhorou a organização do sistema, pois cada tipo de equipamento passou a ser responsável pelo próprio cálculo de multa. Isso eliminou os blocos de if/elif do serviço e reduziu o acoplamento entre as regras de negócio e os tipos específicos de equipamento.

Entretanto, como discutido por Valente no Capítulo 5, o OCP possui limites. Caso surgisse um requisito muito diferente, como multas calculadas por hora ou dependendo do dia da semana, talvez a hierarquia atual não fosse suficiente. Nesse cenário, seria necessário repensar a decomposição, possivelmente utilizando estratégias ou composição em vez de apenas herança.

Portanto, o OCP funciona bem para variações previsíveis, mas não elimina totalmente futuras modificações arquiteturais quando os requisitos mudam de forma radical..