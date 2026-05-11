## Aula 04 — SRP

A decisão mais difícil foi separar a responsabilidade de notificação do ServicoEmprestimo. Inicialmente parecia mais simples deixar os prints de e-mail dentro da própria lógica de negócio, porque o envio acontece durante o empréstimo. Porém, analisando o princípio SRP discutido por Valente no Capítulo 5, percebi que isso criaria dois motivos diferentes para alteração na mesma classe: mudanças na regra de negócio e mudanças na notificação.

A separação exigiu pensar melhor sobre as fronteiras entre os componentes e aumentou um pouco o número de arquivos, mas trouxe mais organização e clareza para o sistema. O critério utilizado foi justamente o conceito de responsabilidade única apresentado por Valente, buscando garantir maior coesão e menor acoplamento entre os módulos.