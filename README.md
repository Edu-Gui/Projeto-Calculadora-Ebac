🧮 Calculadora em Python
📌 Sobre o projeto

Este projeto foi desenvolvido como parte da atividade Analista de Dados v3 — Pratique | Projeto 1, da EBAC.

O objetivo é desenvolver uma calculadora em Python capaz de realizar as quatro operações matemáticas básicas: adição, subtração, multiplicação e divisão.

O programa recebe valores informados pelo usuário, valida as entradas e apresenta o resultado da operação escolhida.

🎯 Funcionalidades
Adição: soma dois números inteiros.
Subtração: calcula a diferença entre dois números inteiros.
Multiplicação: multiplica dois números inteiros.
Divisão: divide o primeiro número pelo segundo, impedindo a divisão por zero.
Validação de entradas: impede campos vazios e entradas que não sejam números inteiros válidos.
Validação de operação: informa quando o usuário escolhe uma opção inválida.
🛠️ Tecnologias utilizadas
Python 3
Shell Script (.sh)
Git
GitHub
📂 Estrutura do projeto
Projeto-Calculadora-Ebac/
├── calculadora.py
├── executar.sh
└── README.md


Descrição dos arquivos:

calculadora.py: contém o código-fonte da calculadora.
executar.sh: script utilizado para executar o programa Python.
README.md: documentação do projeto, com explicações e instruções de execução.
💻 Como executar o projeto
1. Pré-requisitos

É necessário ter o Python 3 instalado no computador.

Para verificar se o Python está instalado, abra o terminal e execute:

python3 --version

2. Clonar o repositório

Para baixar o projeto do GitHub, execute:

git clone https://github.com/Edu-Gui/Projeto-Calculadora-Ebac.git


Em seguida, entre na pasta do projeto:

cd Projeto-Calculadora-Ebac

3. Executar o código Python

No terminal, execute:

python3 calculadora.py


O programa solicitará que o usuário digite dois números inteiros e escolha a operação matemática desejada.

Após a escolha, o resultado será exibido na tela.

▶️ Como executar o arquivo .sh

O arquivo executar.sh permite iniciar o programa Python por meio de um script de shell.

1. Criar o arquivo

Na pasta do projeto, crie um arquivo chamado executar.sh com o seguinte conteúdo:

#!/bin/bash
python3 calculadora.py

2. Conceder permissão de execução

No terminal, execute:

chmod +x executar.sh


Esse comando permite executar o arquivo como um programa.

3. Executar o script

Para iniciar a calculadora, utilize:

./executar.sh


O script executará automaticamente o arquivo calculadora.py.

Observação: os comandos apresentados são destinados ao Linux e macOS ou a ambientes compatíveis, como o Git Bash. É necessário ter o Python 3 instalado.

🧠 Explicação do código Python
1. Função ler_inteiro()

A função ler_inteiro(mensagem) recebe uma mensagem e solicita ao usuário que informe um número inteiro.

O comando input() captura o valor digitado, enquanto o método strip() remove espaços em branco no início e no final da entrada.

Se o usuário não digitar nada, o programa apresenta a mensagem:

Erro: o campo não pode ficar vazio.


Em seguida, solicita uma nova entrada.

O bloco try/except tenta converter o valor informado para inteiro por meio da função int().

Caso a conversão não seja possível, o programa apresenta:

Erro: digite um número inteiro válido.


O laço while True mantém a solicitação ativa até que um número inteiro válido seja informado.

2. Entrada dos números

O programa solicita dois números inteiros ao usuário:

num1 = ler_inteiro("Digite o primeiro número: ")
num2 = ler_inteiro("Digite o segundo número: ")


Os valores são armazenados nas variáveis num1 e num2 e utilizados nos cálculos.

3. Menu de operações

O programa apresenta um menu com quatro opções:

Opção	Operação
1	Adição
2	Subtração
3	Multiplicação
4	Divisão

A opção escolhida pelo usuário é armazenada na variável operador.

4. Realização dos cálculos

O programa utiliza as estruturas condicionais if, elif e else para identificar a operação selecionada.

Adição (+): soma os dois números.
Subtração (-): subtrai o segundo número do primeiro.
Multiplicação (*): multiplica os dois números.
Divisão (/): divide o primeiro número pelo segundo, desde que o divisor não seja zero.

Após realizar o cálculo, o programa apresenta o resultado utilizando print().

Se o usuário escolher uma opção diferente de 1, 2, 3 ou 4, o programa apresenta uma mensagem informando que a opção é inválida.

5. Tratamento da divisão por zero

Antes de realizar a divisão, o programa verifica se o segundo número é diferente de zero:

if num2 != 0:
    resultado = num1 / num2
    print("Resultado:", resultado)
else:
    print("Erro: não é possível dividir por zero.")


Essa condição evita a tentativa de realizar uma divisão por zero e apresenta uma mensagem de erro quando necessário.

🧪 Exemplos de utilização
Exemplo 1 — Adição
Digite o primeiro número: 10
Digite o segundo número: 5

Escolha uma operação:
1 - Adição
2 - Subtração
3 - Multiplicação
4 - Divisão

Digite o número da operação: 1
Resultado: 15

Exemplo 2 — Multiplicação
Digite o primeiro número: 6
Digite o segundo número: 4
Digite o número da operação: 3
Resultado: 24

Exemplo 3 — Divisão por zero
Digite o primeiro número: 10
Digite o segundo número: 0
Digite o número da operação: 4
Erro: não é possível dividir por zero.

Exemplo 4 — Entrada inválida
Digite o primeiro número:
Erro: o campo não pode ficar vazio.

📚 Aprendizados

Com o desenvolvimento deste projeto, foi possível praticar:

Criação e utilização de funções em Python.
Entrada e validação de dados.
Conversão de tipos de dados.
Estruturas condicionais (if, elif e else).
Laços de repetição (while).
Operações matemáticas.
Tratamento de erros com try/except.
Execução de scripts Shell (.sh).
Versionamento e hospedagem de código com Git e GitHub.
Documentação de projetos por meio do arquivo README.md.
🚀 Projeto de entrega

O código-fonte e a documentação do projeto estão disponíveis no GitHub.

Repositório do projeto: Projeto Calculadora EBAC

Link para submissão da atividade: https://github.com/Edu-Gui/Projeto-Calculadora-Ebac

👨‍💻 Autoria

Projeto desenvolvido para fins educacionais como parte da atividade Analista de Dados v3 — Pratique | Projeto 1, da EBAC.

O projeto tem como objetivo aplicar conhecimentos básicos de programação em Python, validação de dados, estruturas condicionais, operações matemáticas e documentação de código.
