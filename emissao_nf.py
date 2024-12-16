import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import customtkinter as ctk
import time

def emitir_nf():
    CNPJ = entry_cnpj.get()
    DESCRICAO = entry_description.get()
    VALOR = entry_valor.get()

    if not CNPJ or not DESCRICAO or not VALOR:
        label_status.configure(text="Por favor, preencha todos os campos!", text_color="red")
        return

    # Inicializar o WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    wait = WebDriverWait(driver, 15)

    try:
        driver.get("https://nfse.recife.pe.gov.br/senhaweb/login.aspx")
        print("Página inicial carregada.")

        certificado_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ctl00_cphCabMenu_hlLoginICP"]/img')))
        certificado_btn.click()
        print("Selecionado: Possui Certificado Digital?")

        print("Aguardando o usuário escolher o certificado...")
        main_window_handle = driver.current_window_handle
        while len(driver.window_handles) > 1:
            time.sleep(1)  
        driver.switch_to.window(main_window_handle)
        print("Certificado Digital selecionado.")

        acessar_sistema_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ctl00_cphCabMenu_btAcesso"]')))
        acessar_sistema_btn.click()
        print("Clicado: Acessar o Sistema.")

        emitir_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ctl00_cphCabMenu_linkEmissaoNota"]/strong')))
        emitir_btn.click()
        print("Clicado: Emitir Nota Fiscal.")

        cnpj_input = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="ctl00_cphCabMenu_tbCPFCNPJTomador"]')))
        cnpj_input.send_keys(CNPJ)
        print("CNPJ preenchido.")

        avancar_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ctl00_cphCabMenu_btAvancar"]')))
        avancar_btn.click()
        print("Clicado: Avançar.")

        descricao_input = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="ctl00_cphCabMenu_tbDiscriminacao"]')))
        descricao_input.send_keys(DESCRICAO)
        print("Descrição preenchida.")

        valor_input = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="ctl00_cphCabMenu_tbValor"]')))
        valor_input.send_keys(VALOR)
        print("Valor preenchido.")

        prever_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ctl00_cphCabMenu_btPrever"]')))
        prever_btn.click()
        print("Clicado: Prever Nota Fiscal.")

        label_status.configure(text="Nota Fiscal prevista com sucesso!", text_color="green")

    except Exception as e:
        print(f"Erro: {e}")
        label_status.configure(text=f"Erro: {e}", text_color="red")
    finally:
        time.sleep(5)


# Configuração da interface gráfica
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Emissão de Nota Fiscal")
root.geometry("400x500")


label_title = ctk.CTkLabel(root, text="Sistema de Emissão de NF", font=("Arial", 20, "bold"))
label_title.pack(pady=10)

label_cnpj = ctk.CTkLabel(root, text="CNPJ (Formato: 00.000.000/0000-00)", font=("Arial", 12))
label_cnpj.pack(pady=5)
entry_cnpj = ctk.CTkEntry(root, placeholder_text="Ex: 00.000.000/0000-00", width=300)
entry_cnpj.pack(pady=5)

label_description = ctk.CTkLabel(root, text="Descrição", font=("Arial", 12))
label_description.pack(pady=5)
entry_description = ctk.CTkEntry(root, placeholder_text="Digite a descrição", width=300)
entry_description.pack(pady=5)

label_valor = ctk.CTkLabel(root, text="Valor (Formato: 100,00)", font=("Arial", 12))
label_valor.pack(pady=5)
entry_valor = ctk.CTkEntry(root, placeholder_text="Ex: 100,00", width=300)
entry_valor.pack(pady=5)

button_emitir = ctk.CTkButton(root, text="Emitir NF", command=emitir_nf)
button_emitir.pack(pady=20)

label_status = ctk.CTkLabel(root, text="")
label_status.pack(pady=10)

root.mainloop()