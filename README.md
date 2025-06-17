Documentação do Sistema de Bilheteria Online

Visão Geral

Este sistema de bilheteria online permite que usuários realizem cadastro, login, entrem em filas virtuais, reservem assentos e gerenciem suas reservas para eventos. O sistema foi desenvolvido em Python, utilizando manipulação de arquivos CSV para persistência dos dados e uma arquitetura modular para facilitar manutenção e escalabilidade.

---

Como Utilizar

1. Pré-requisitos

- Python 3.10+ instalado em sua máquina.
- Recomenda-se o uso do terminal do VS Code ou Prompt de Comando do Windows.
- Certifique-se de que todos os arquivos do projeto estejam salvos com encoding UTF-8.

2. Instalando Dependências

Se houver dependências externas, instale-as com:

pip install -r requirements.txt

3. Executando a Aplicação

1. Abra o terminal na raiz do projeto (bilheteria).
2. Execute o comando abaixo para iniciar o sistema:

python code/bilheteria.py

3. Siga as instruções exibidas no terminal para navegar pelas funcionalidades do sistema, como cadastro, login, reserva de assentos, etc.

---

Arquitetura do Sistema

A arquitetura do sistema está documentada no arquivo Bilheteria.drawio, localizado na raiz do projeto.  
Esse arquivo pode ser aberto com o draw.io (https://app.diagrams.net/) ou com extensões compatíveis no VS Code.

Estrutura Geral

- code/: Contém todo o código-fonte do sistema.
  - services/: Serviços organizados por domínio (autenticação, fila virtual, reserva, etc.).
  - repositories/: Camada de acesso a dados (leitura e escrita em CSV).
  - models/: Definição das entidades do sistema.
  - controllers/: Lógica de controle e orquestração das operações.
  - utils/: Utilitários, como manipulação de CSV.
- bilheteria.py: Ponto de entrada da aplicação.
- Bilheteria.drawio: Diagrama da arquitetura do sistema.
