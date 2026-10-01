# RentSmart — Sistema de Orçamento de Locação

O **RentSmart** é uma aplicação desenvolvida em Python para automatizar o processo de cálculo de orçamentos de locação de imóveis (casas, apartamentos e estúdios) para a **R.M Imóveis**. O sistema aplica regras comerciais específicas, calcula o valor mensal do aluguel considerando adicionais e descontos, gerencia taxas contratuais parceladas e gera uma projeção financeira detalhada de 12 meses em um arquivo CSV.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **Programação Orientada a Objetos (POO)**: Utilização de classes, herança e polimorfismo (`super()`, sobrescrita de métodos).
- **Módulo `csv`**: Para manipulação e exportação de dados tabulares.

---

## 📋 Regras de Negócio Implementadas

1. **Categorias de Imóveis e Aluguel Base:**
   - **Apartamento:** R$ 700,00 (1 quarto)
   - **Casa:** R$ 900,00 (1 quarto)
   - **Estúdio:** R$ 1.200,00 (1 quarto, pacote inicial de 2 vagas)

2. **Adicionais e Descontos:**
   - **Apartamento com 2 quartos:** Adicional de R$ 200,00.
   - **Casa com 2 quartos:** Adicional de R$ 250,00.
   - **Garagem (Casas e Apartamentos):** Adicional de R$ 300,00.
   - **Desconto para Apartamentos sem Crianças:** 5% de desconto aplicado após os adicionais.
   - **Estúdios (Estacionamento):** Pacote inicial de até 2 vagas por R$ 250,00. Vagas extras acima de 2 custam R$ 60,00 cada.

3. **Taxa Contratual:**
   - Valor fixo de R$ 2.000,00, podendo ser parcelado de 1 a 5 vezes.

4. **Projeção de 12 Meses:**
   - Geração automática de um arquivo CSV contendo a evolução mês a mês do aluguel somado às parcelas da taxa contratual.

---

## 🚀 Como Executar o Projeto

### Pré-requisitos
Certifique-se de ter o [Python instalado](https://www.python.org/) em sua máquina.

### Passos para Execução

1. Clone este repositório ou baixe os arquivos do projeto:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   ```

2. Navegue até o diretório do projeto pelo terminal/prompt de comando:
   ```bash
   cd nome-do-repositorio
   ```

3. Execute o script principal:
   ```bash
   python main.py
   ```

4. Siga as instruções interativas exibidas no terminal para escolher o tipo de imóvel, informar os opcionais e definir o parcelamento da taxa contratual.

---

## 📁 Estrutura do Código

- `Imovel`: Classe base contendo atributos e métodos genéricos compartilhados.
- `Apartamento`: Classe filha que herda de `Imovel` e implementa o cálculo específico de apartamentos (quartos, garagem e desconto de crianças).
- `Casa`: Classe filha que herda de `Imovel` e implementa o cálculo para casas.
- `Estudio`: Classe filha que herda de `Imovel` e implementa a lógica customizada para vagas de estacionamento.
- `geradorCSV()`: Função utilitária responsável por exportar a projeção anual para o arquivo `Projeto Locação 12 meses.csv`.
- `home()`: Função controladora que gerencia o menu interativo e a experiência do usuário.

---

## 📹 Vídeo Pitch

O vídeo de apresentação demonstrando o funcionamento do sistema, lógica e código está disponível no link abaixo:
👉 [Link do Vídeo no YouTube](https://seu-link-do-video.com)

---

## 👨‍💻 Autor

Desenvolvido como parte da entrega acadêmica para a disciplina de *Algorithmic Thinking & Introduction to Object-Oriented Programming*.
