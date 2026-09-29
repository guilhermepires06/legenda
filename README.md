# 📄 Guia de Instalação - Live Subtitle Translator

Siga os passos abaixo para configurar e executar a ferramenta no seu computador Windows[cite: 2, 3].

---

## 🛠️ 1. Pré-requisitos Obrigatórios

1. **Python 3.10 ou superior** instalado no sistema (com a opção de adicionar ao PATH ativada).
2. **Tesseract OCR** para Windows:
   - Descarregue e instale a partir do repositório oficial do UB-Mannheim.
   - Certifique-se de que fica instalado no caminho padrão: `C:\Program Files\Tesseract-OCR\tesseract.exe`.

---

## ⚙️ 2. Passo a Passo da Instalação

### Passo 1: Obter os Ficheiros
Crie uma pasta no seu computador e guarde lá o ficheiro principal com o nome `rodar_tradutor.py`.

### Passo 2: Abrir o Terminal na Pasta
Abra a pasta do projeto no Explorador de Ficheiros do Windows. 
Na barra de endereços no topo, clique, escreva `powershell` e prime **Enter**.

### Passo 3: Criar um Ambiente Virtual (Isolado)
Para garantir que as dependências ficam isoladas e limpas, crie o ambiente virtual executando:
```powershell
python -m venv .venv
``

### Passo 4: Ativar o Ambiente Virtual
Ative o ambiente criado executando o seguinte comando no PowerShell[cite: 2, 3]:
```powershell
.venv\Scripts\Activate.ps1
``

### Passo 5: Executar o Programa
Com o ambiente virtual ativo, corra o script principal[cite: 2, 3]:
```powershell
python rodar_tradutor.py
``

### Passo 6: Utilizar o Tradutor
Abra o menu gráfico, clique em "Selecionar Área e Traduzir", selecione a área do ecrã com o rato e veja a tradução em tempo real.
