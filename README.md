# 📄 Guia de Instalação - Live Subtitle Translator[cite: 2, 3]

Siga os passos abaixo para configurar e executar a ferramenta no seu computador Windows[cite: 2, 3].

---

## 🛠️ 1. Pré-requisitos Obrigatórios[cite: 2, 3]

1. **Python 3.10 ou superior** instalado no sistema (com a opção de adicionar ao PATH ativada)[cite: 2, 3].
2. **Tesseract OCR** para Windows[cite: 2, 3]:
   - Descarregue e instale a partir do repositório oficial do UB-Mannheim[cite: 2, 3].
   - Certifique-se de que fica instalado no caminho padrão: `C:\Program Files\Tesseract-OCR\tesseract.exe`[cite: 2, 3].

---

## ⚙️ 2. Passo a Passo da Instalação[cite: 2, 3]

### Passo 1: Obter os Ficheiros[cite: 2, 3]
Crie uma pasta no seu computador e guarde lá o ficheiro principal com o nome `rodar_tradutor.py`[cite: 2, 3].

### Passo 2: Abrir o Terminal na Pasta[cite: 2, 3]
Abra a pasta do projeto no Explorador de Ficheiros do Windows[cite: 2, 3]. Na barra de endereços no topo, clique, escreva `powershell` e prime **Enter**[cite: 2, 3].

### Passo 3: Criar um Ambiente Virtual (Isolado)[cite: 2, 3]
Para garantir que as dependências ficam isoladas e limpas, crie o ambiente virtual executando[cite: 2, 3]:
```powershell
python -m venv .venv
```[cite: 2, 3]

### Passo 4: Ativar o Ambiente Virtual[cite: 2, 3]
Ative o ambiente criado executando o seguinte comando no PowerShell[cite: 2, 3]:
```powershell
.venv\Scripts\Activate.ps1
```[cite: 2, 3]

### Passo 5: Executar o Programa[cite: 2, 3]
Com o ambiente virtual ativo, corra o script principal[cite: 2, 3]:
```powershell
python rodar_tradutor.py
```[cite: 2, 3]

### Passo 6: Utilizar o Tradutor[cite: 2, 3]
Abra o menu gráfico, clique em "Selecionar Área e Traduzir", selecione a área do ecrã com o rato e veja a tradução em tempo real[cite: 2, 3].
