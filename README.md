# 🎥 Live Subtitle Translator (OCR + Google Translate)

Uma ferramenta desenvolvida em Python com interface gráfica (**GUI**) que captura em tempo real uma área específica do ecrã (como a zona de legendas de um curso, vídeo ou stream), faz o reconhecimento ótico de caracteres (**OCR**) e traduz o texto instantaneamente para **Português**, exibindo-o numa sobreposição flutuante discreta.

---

## 🚀 Funcionalidades

- **Menu Gráfico Interativo:** Interface moderna feita em Tkinter, permitindo controlar tudo através de botões, sem precisar de interagir com o terminal.
- **Seleção de Área Personalizada:** Permite selecionar com o rato exatamente a zona do ecrã a monitorizar (arrastar para definir o retângulo de captura da legenda).
- **OCR em Tempo Real:** Utiliza o `Tesseract OCR` otimizado com melhoria de contraste e escala de cinzentos para máxima precisão.
- **Tradução Automática Instantânea:** Integração com o Google Translate (`googletrans`) com um sistema de **cache local** para evitar latência e chamadas repetidas em frases frequentes.
- **Interface Flutuante (*Overlay*):** Janela preta translúcida posicionada na parte inferior do ecrã. **Basta um clique na legenda para parar a tradução e voltar instantaneamente ao menu principal**.
- **Instalação Automática de Dependências:** O script deteta e instala automaticamente todos os pacotes necessários na primeira execução.

---

## 📋 Pré-requisitos Obrigatórios

1. **Python 3.10 ou superior** instalado no sistema (com a opção de adicionar ao PATH ativada).
2. **Tesseract OCR** para Windows:
   - Descarrega e instala a partir do [repositório oficial do UB-Mannheim](https://github.com/UB-Mannheim/tesseract/wiki).
   - Certifica-te de que fica instalado no caminho padrão: `C:\Program Files\Tesseract-OCR\tesseract.exe`.

---

## ⚙️ Passo a Passo Completo (Passos 4, 5 e 6 para Rodar o Sistema)

### Passo 1: Obter os Ficheiros
Cria uma pasta no teu computador (por exemplo: `C:\Users\TeuUtilizador\Desktop\legenda`) e guarda lá o ficheiro principal com o nome `rodar_tradutor.py`.

### Passo 2: Abrir o Terminal na Pasta
1. Abre a pasta do projeto no Explorador de Ficheiros do Windows.
2. Na barra de endereços no topo, clica, escreve `powershell` e prime **Enter**.

### Passo 3: Criar um Ambiente Virtual (Isolado)
Para garantir que as dependências ficam isoladas e limpas, cria o ambiente virtual:
```powershell
python -m venv .venv

Passo 4: Ativar o Ambiente Virtual
Ativa o ambiente criado executando o seguinte comando no PowerShell:

PowerShell
.venv\Scripts\Activate.ps1
Nota: Se aparecer um erro de permissão a informar que a execução de scripts está desativada, executa primeiro este comando na consola:

Set-ExecutionPolicy Unrestricted -Scope Process

Depois, volta a executar o comando de ativação (.venv\Scripts\Activate.ps1).

Quando ativo, verás (.venv) no início da linha do terminal.

Passo 5: Executar o Programa
Com o ambiente virtual ativo ((.venv) visível no terminal), basta correres o script principal:

PowerShell
python rodar_tradutor.py
(Na primeira execução, o script descarrega e instala automaticamente todas as bibliotecas necessárias como mss, pytesseract, pillow, googletrans e legacy-cgi).

Passo 6: Usar o Tradutor
Uma janela gráfica de menu vai abrir-se no ecrã automaticamente.

Clica no botão "Selecionar Área e Traduzir".

O ecrã ficará ligeiramente escuro/cinzento; clica e arrasta o rato à volta das legendas do vídeo.

A tradução aparecerá automaticamente numa barra preta na parte inferior do ecrã.

Para parar a tradução e voltar ao menu principal, basta clicar em cima da barra de tradução.

🛠 Tecnologias Utilizadas
Python (Linguagem principal)

Tkinter (Menu gráfico, seletor de ecrã e janela de overlay)

MSS (Captura de ecrã ultrarrápida)

Pillow & ImageEnhance (Processamento de imagem e melhoria de contraste para otimizar o OCR)

PyTesseract (Extração de texto via OCR)

Googletrans (Tradução automática em tempo real)

📝 Licença
Este projeto é de código aberto e está licenciado sob a licença MIT. Sinta-se livre para contribuir, modificar e melhorar!


