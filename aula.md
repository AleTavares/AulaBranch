# Code Dojo: POO na Fazenda Lúdica


### Passo 1: A Classe Base `Animal` (Abstração)

**Objetivo:** Criar a classe que servirá de modelo para todos os animais.

**Tarefa:**
1.  Declare a classe `Animal`.
2.  Crie o método construtor `__init__` que recebe `nome` e `idade`.
3.  Implemente o método `apresentar(self)` que retorna a string: `"Olá, sou [nome] e tenho [idade] anos."`
4.  Implemente o método `emitir_som(self)` que retorna a string: `"O animal emite um som."`


**Discussão:**
- O que é **abstração** neste contexto?

- Por que `self` é o primeiro parâmetro de todos os métodos da classe?


### Passo 2: A Subclasse `Cachorro` (Herança)

**Objetivo:** Criar uma classe especializada que herda de `Animal`.

**Tarefa:**
1.  Declare a classe `Cachorro` que herda de `Animal`.
2.  Crie seu construtor `__init__`, que deve receber `nome`, `idade` e o novo atributo `raca`.
3.  Dentro do construtor, chame o construtor da classe mãe (`Animal`) para reaproveitar o código.
4.  Armazene o atributo `raca`.


**Discussão:**
- O que a palavra-chave `super()` faz? Qual a sua importância para a **herança**?

- Um objeto `Cachorro` também é um `Animal`?

### Passo 3: A Subclasse `Cachorro` (Polimorfismo)

**Objetivo:** Especializar o comportamento da subclasse.

**Tarefa:**
1.  Na classe `Cachorro`, sobrescreva (override) o método `emitir_som()`.
2.  A nova implementação deve retornar a string `"Au! Au!"`.


**Discussão:**
- O que é **polimorfismo**? Como ele está sendo aplicado aqui?

- Se não tivéssemos sobrescrito o método, o que `rex.emitir_som()` retornaria?


### Passo 4: As Subclasses `Gato` e `Vaca`

**Objetivo:** Replicar o processo de herança e polimorfismo para outras classes.

**Tarefa:**
1.  Crie a classe `Gato`, que herda de `Animal`, com o atributo extra `cor_pelo` e sobrescreva `emitir_som()` para retornar `"Miau!"`.
2.  Crie a classe `Vaca`, que herda de `Animal`, com o atributo extra `producao_leite_litros` e sobrescreva `emitir_som()` para retornar `"Muuu!"`.


### Passo 5: A Classe `Vaca` (Encapsulamento)

**Objetivo:** Proteger os dados da classe `Vaca`.

**Tarefa:**
1.  Modifique o atributo `producao_leite_litros` para ser **privado**. Em Python, a convenção é usar dois underscores no início (`__`).
2.  Crie um método "getter" chamado `obter_producao_leite()` que apenas retorna o valor do atributo privado.
3.  Crie um método "setter" chamado `registrar_ordenha(litros)` que atualiza o valor do atributo privado.


**Discussão:**
- O que é **encapsulamento**? Por que é útil?

- O que acontece se tentarmos acessar `mimosa.__producao_leite_litros` diretamente de fora da classe?

### Passo 6: Testando Tudo!

**Objetivo:** Instanciar os objetos e verificar se tudo funciona como esperado.

**Tarefa:**
1.  Crie um bloco `if __name__ == "__main__":`.
2.  Instancie um `Cachorro`, um `Gato` e uma `Vaca`.
3.  Use um laço `for` para percorrer uma lista com os três animais, chamando `apresentar()` e `emitir_som()` para cada um.
4.  Teste o encapsulamento da `Vaca`:
    - Imprima a produção de leite usando o getter.
    - Mude a produção de leite usando o setter.
    - Imprima a nova produção para confirmar a alteração.

**Discussão Final:**
- Como os quatro pilares da POO se conectaram para criar este sistema simples e organizado?

- Quais seriam os próximos passos para expandir este sistema?
