[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-9f69c29eadd1a2efcce9672406de9a39573de1bdf5953fef360cfc2c3f7d7205.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=9244903)
# Atividade: Descrição da Atividade

## Orientações

1. Cada questões deve ser entregue dentro de uma pasta. Exemplo: "questao01","questao02",...,"questaoXX".

2. Dentro de cada pasta deve ter um arquivo chamado principal.py.

3. Para todas as questões, utilize crie um arquivo principal.py para iniciar o programa e realizar testes.

4. Para todas as questões, sempre que possível, aplique os tópicos discutidos em sala até o momento.

5. Tente não utilizar funções prontas do Python, como por exemplo, funções de ordenação ou cálculo de potência.

# Atividades

1. Construa uma função que receba dois inteiros e retorne a soma deles.
   Ex:

   ```python
   soma(1,2) # 3
   soma(2,3) # 5
   ```

1. Construa uma função que receba dois inteiros e retorne o menor entre eles.
   Ex:
   ```python
   menor(1,2) # 1
   menor(2,3) # 2
   ```
1. Construa uma função que receba um inteiro e retorne se ele é par ou ímpar.
   Ex:

   ```python
   par_impar(1) # impar
   par_impar(2) # par
   ```

1. Construa uma função que receba um vetor de inteiros e retorne o maior elemento.

   Ex:

   ```python
   vetor = [1,2,3,4,5,6,7,8,9,10]
   print(menor_elemento(vetor))
   # 1
   ```

1. Construa uma função que receba um vetor de inteiros ordenados e retorne o menor elemento.
1. Construa uma função receba uma string e retorne o número de vogais que ela possui.

   Ex:

   ```python
   vogais("abacate") # 3
   vogais("banana") # 3
   vogais("uva") # 2
   ```

1. Construa uma função que dada uma string, retorne uma nova string com os caracteres em ordem inversa.

   Ex:

   ```python
   inverte("abacate") # etacaba
   inverte("banana") # ananab
   inverte("uva") # avu
   ```

1. Construa uma função para calcular a potência de um número inteiro. A função deve receber dois parâmetros, o primeiro é a base e o segundo é o expoente. A função deve retornar o resultado da potência.

   Ex:

   ```python
   potencia(2,3) # 8
   potencia(3,2) # 9
   potencia(2,4) # 16
   ```

1. Construa uam função que dado um vetor de inteiros retorne a média dos elementos do vetor.

   Ex:

   ```python
   media([1,2,3,4,5,6,7,8,9,10]) # 5.5
   media([1,2,3,4,5,6,7,8,9]) # 5
   media([1,2,3,4,5,6,7,8]) # 4.5
   ```

1. Construa uma função que dada uma matriz de tamanho NxM retorne a soma de todos os seus elementos.
   Ex:

   ```python
   matriz = [[1,2,3,1],[4,5,6,2],[7,8,9,3]]
   soma_matriz(matriz) # 51
   ```

1. Construa uma função que dada uma matriz de tamanho NxN retorne a soma dos seus elementos da diagonal principal.
   Ex:

   ```python
   matriz = [[1,2,3],[4,5,6],[7,8,9]]
   soma_diagonal_principal(matriz) # 15
   ```

1. [Desafio] Construa uma função que dado um vetor de inteiros em que todos elementos aparecem duas vezes, exceto por um. Encontre esse um.

   Ex:

   ```python
   vetor = [1,2,3,5,4,3,2,1,4]
   print(unico(vetor))
   # 5
   ```

   Ex:

   ```python
   vetor = [9,9,2,2,1,3,1,4,4]
   print(unico(vetor))
   # 3
   ```

1. [Desafio] Dado um vetor de inteiros e a definição de que uma **Soma Corrida** do vetor é dada por $soma\_corrida[i]=soma({numeros[0]...numeros[i]})$. Construa uma funcão que receba um vetor e retorne a soma corrida.

   Ex:

   ```python
    vetor = [1,2,3,4,5]
    print(soma_corrida(vetor))
    # [1,3,6,10,15]
   ```

   - O valor resultante na posição i do vetor de retorno é igual soma dos elementos da posição 0 até a posição i do vetor original.

   **numeros** = [1,2,3,4,5]  
    **somar_corrida**[0] = 1  
    **somar_corrida**[1] = 1+2  
    **somar_corrida**[2] = 1+2+3  
    **somar_corrida**[3] = 1+2+3+4  
    **somar_corrida**[4] = 1+2+3+4+5

   print(soma_corrida)  
    [1,3,6,10,15]

1. [Desafio] Dado um vetor de tamanho NxM representando uma tabela de contas de clientes N em M bancos. O valor de cada posição $contas[N][M]$ representa o saldo do cliente $N$ no banco $M$. Construa uma função que receba a tabela de contas e retorne a soma dos valores em conta para o cliente mais rico.

   Ex:

   ```python
   contas = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]
   print(mais_rico(contas))
   # 65
   ```
