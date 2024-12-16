# Sistema de Emissão de Nota Fiscal

Este projeto é um aplicativo desenvolvido em Python para a emissão automatizada de Notas Fiscais utilizando automação com Selenium e interface gráfica com CustomTkinter.

---

## 🚀 Funcionalidades

- Emissão de Nota Fiscal através do portal **NFSe Recife**.
- Preenchimento automatizado de campos como **CNPJ**, **descrição do serviço** e **valor**.
- Interação com o Certificado Digital diretamente no navegador.
- Interface gráfica amigável para facilitar o uso.

---

## 🛠️ Tecnologias Utilizadas

- **Python**: Linguagem principal do projeto.
- **Selenium**: Automação de interações no navegador.
- **PyAutoGUI**: Interação com o sistema operacional.
- **CustomTkinter**: Biblioteca para criar a interface gráfica.
- **PyInstaller**: Para converter o script em um executável `.exe`.

---

## 📦 Como Instalar e Executar

1. **Pré-requisitos**:
   - Instale o Python (3.9 ou superior) [Download Python](https://www.python.org/downloads/).
   - Instale o **Google Chrome** e o **ChromeDriver** compatível.

2. **Clone o repositório**:
   ```bash
   git clone https://github.com/seu_usuario/sistema-emissao-nf.git
   cd sistema-emissao-nf
   ```

3. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Execute o projeto**:
   ```bash
   python emissao_nf.py
   ```

---

## 🔧 Como Gerar o Executável

Para criar o arquivo `.exe` do projeto:

1. Instale o PyInstaller:
   ```bash
   pip install pyinstaller
   ```

2. Gere o executável:
   ```bash
   pyinstaller --onefile --windowed emissao_nf.py
   ```

3. O executável será gerado na pasta `dist/`.

---

## 🖥️ Como Usar

1. Abra o aplicativo.
2. Preencha os campos:
   - **CNPJ**: Insira o CNPJ no formato `00.000.000/0000-00`.
   - **Descrição**: Digite a descrição do serviço.
   - **Valor**: Informe o valor total no formato `100,00`.
3. Clique em **Emitir NF**.
4. No popup do Certificado Digital, selecione o certificado e clique em **OK**.
5. Aguarde a emissão da Nota Fiscal.

---
