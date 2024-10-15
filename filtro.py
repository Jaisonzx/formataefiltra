import json
import tkinter as tk
from tkinter import filedialog, messagebox

def filter_numbers():
    # Abrir o diálogo para selecionar o arquivo JSON
    input_file = filedialog.askopenfilename(
        title="Selecione o arquivo JSON",
        filetypes=[("JSON files", "*.json")]
    )
    
    if not input_file:
        return  # Se o usuário cancelar a seleção do arquivo
    
    try:
        # Carregar o arquivo JSON
        with open(input_file, 'r') as file:
            data = json.load(file)
        
        # Verificar se a estrutura de dados é uma lista de dicionários com as chaves 'exists' e 'number'
        if not all(isinstance(item, dict) and 'exists' in item and 'number' in item for item in data):
            messagebox.showerror("Erro", "O arquivo JSON não contém a estrutura esperada.")
            return
        
        # Filtrar os números que possuem 'exists' como True
        total_numbers = len(data)  # Total de números antes do filtro
        filtered_numbers = [item['number'] for item in data if item['exists']]
        removed_numbers = total_numbers - len(filtered_numbers)  # Números removidos
        
        # Abrir o diálogo para selecionar o local de salvamento do arquivo .txt
        output_file = filedialog.asksaveasfilename(
            title="Salvar arquivo",
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt")]
        )
        
        if not output_file:
            return  # Se o usuário cancelar a escolha do local de salvamento
        
        # Salvar os números filtrados em um arquivo .txt
        with open(output_file, 'w') as file:
            for number in filtered_numbers:
                file.write(f"{number}\n")
        
        # Exibir mensagem de sucesso com a quantidade de números removidos
        messagebox.showinfo("Sucesso", f"Números filtrados salvos em: {output_file}\n{removed_numbers} números foram removidos.")
    
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

# Configurar a janela principal do Tkinter
root = tk.Tk()
root.title("Filtro de Números de Telefone")
root.geometry("300x150")

# Botão para selecionar o arquivo e filtrar
btn_filter = tk.Button(root, text="Selecionar Arquivo e Filtrar", command=filter_numbers)
btn_filter.pack(pady=20)

# Rodar a aplicação
root.mainloop()
