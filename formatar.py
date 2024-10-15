import tkinter as tk
from tkinter import filedialog

def format_phone_numbers(phone_numbers):
    formatted_numbers = []
    
    for phone in phone_numbers:
        # Remove qualquer coisa que não seja número
        clean_number = ''.join(filter(str.isdigit, phone))
        # Adiciona o formato desejado com código do país (55 no seu caso)
        if not clean_number.startswith('55'):
            clean_number = '55' + clean_number
        
        # Adiciona à lista no formato com aspas
        formatted_numbers.append(f'"{clean_number}"')
    
    # Junta os números com vírgula e coloca o último sem vírgula
    result = ',\n    '.join(formatted_numbers)
    
    return f'{result}'

def select_file_and_format():
    # Abre janela para selecionar o arquivo .txt
    root = tk.Tk()
    root.withdraw()  # Oculta a janela principal do Tkinter
    
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    
    if not file_path:
        print("Nenhum arquivo selecionado.")
        return
    
    # Lê o conteúdo do arquivo
    with open(file_path, 'r', encoding='utf-8') as file:
        phone_numbers = file.readlines()
    
    # Remove espaços e quebras de linha do arquivo lido
    phone_numbers = [line.strip() for line in phone_numbers]
    
    # Formata os números
    formatted_output = format_phone_numbers(phone_numbers)
    
    # Exibe o resultado formatado
    print("Números formatados:\n")
    print(formatted_output)

    # Salva o resultado formatado em um novo arquivo .txt
    save_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    
    if save_path:
        with open(save_path, 'w', encoding='utf-8') as output_file:
            output_file.write(formatted_output)
        print(f"Números formatados salvos em: {save_path}")
    else:
        print("Nenhum arquivo foi salvo.")

# Executa o script
if __name__ == "__main__":
    select_file_and_format()
