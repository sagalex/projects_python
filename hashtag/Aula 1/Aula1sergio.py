#!/usr/bin/env python
# coding: utf-8

# In[49]:


#!pip install pyautogui # rodar essa linha antes para instalação da biblioteca


# In[50]:


#Declarações Top Down
# !pip install pyautogui # rodar esse comando para importar a biblioteca pyautogui
import pyautogui #para instalar o pyautogui "!pip install pyautogui"
# essa biblioteca tem problemas com caracteres especiais, logo precisa de recurso.
import pyperclip # para copiar e colar texto.
pyautogui.PAUSE = 0.5 # aqui eu estabeleço o dalay para cada comando.
import time
import datetime # trabalha melhor com data para data um documento 
#import pandas # No jupter não é necessário,mas em outra ide ainda seria necessário o "openpyxl" e "numpy"

#Passo 1: Entrar no sistema da empresa (no nosso caso vai ser entrar no link)

#pyautogui.press("win") #preciono a tecla do windows (bandeira)
#pyautogui.write("chrome") # digito o nome do program que aqui é o chrome
#pyautogui.press("enter") # pressiono enter para executar o chrome

pyautogui.hotkey("ctrl", "t")
#pyautogui.write("https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga")
pyperclip.copy("https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")
time.sleep(5) # site está carregando 

#Passo 2: Navegar no sistema e encontrar a base de dados(entrar na pasta Explorar) 
# time.sleep(6) #Usar esse recurso em uma célula separada para dar tempo de obter as coordenadas da tela 
# pyautogui.position() comando usado em uma célula independente para descobrir a localizaçãodo botão Exportar no site.
pyautogui.click(x=1349, y=302, clicks=2) # as coordenadas só irão funcionar para o mesmo ajuste de janela usado para capturar essas coordenadas, ou seja maximizada e diferente de restaurada
time.sleep(2) #por garantia do carregamento da tela
#Passo 3: Download da base de dados
#pyautogi.scroll(1100) # para subir ou descer na página do site.
pyautogui.click(x=1384, y=435) #clicou no arquivo
pyautogui.click(x=1764, y=205) #clicou nos 3 pontos
pyautogui.click(x=1558, y=635) #fazer download
time.sleep(7)


# In[51]:


time.sleep(6) # Tempo para posicionar o mouse onde eu quer obter as coordenadas
pyautogui.position() # Artifício das coordenadas do mouse


# In[52]:


#Passo 4: Calcular os indicadores(faturamento, quantidade de produtos)
import pandas as pd # não seria necessário, mas os programadores por convenção usam pd para o alias do pandas
tabela = pd.pandas.read_excel(r"C:\Users\sergi\Downloads\Vendas - Dez.xlsx") # use a tecla TAB apos o comando read para ver as opções de arquivos para importação.
# o "r" antes do caminho faz com que o Python lei os caracteres especiais "\t" "\n" como texto 
# tabela = pd.pandas.read_excel(r"C:\Users\sergi\Downloads\Vendas - Dez.xlsx", sheet_name) #no final tem com ir para a planilha desejada com o sheet_name
display(tabela) # o display é interno do Jupter e melhor que o print para visualizar as informações de tabela


# In[53]:


quantidade = tabela["Quantidade"].sum()
faturamento = tabela["Valor Final"].sum()
print(quantidade)
print(faturamento)


# In[54]:


#Passo 5: Entar no e-mail
pyautogui.hotkey("ctrl", "t")#nova aba do navegador
#pyautogui.write("https://mail.google.com/mail/u/0/#inbox") 
pyperclip.copy("https://mail.google.com/mail/u/0/#inbox") # copio o link do e-mail
pyautogui.hotkey("ctrl", "v")# colo o link do e-mail
pyautogui.press("enter")# pressiono enter
time.sleep(7) # aguardo o carregamento do site do Gmail

#Passo 6: Mandar um e-mail para a diretoria com os indicadores
# clicar no botão de "+"
pyautogui.click(x=1044, y=212)
time.sleep(2)
# escrever o destinatário(para quem eu vou enviar o email)
pyautogui.write("sergio.alexandre@hotmail.com")
pyautogui.press("tab") #selecionar o e-mail
pyautogui.press("tab") #passar para o próximo campo "assunto"

# escrever o assunto
pyperclip.copy("Relatório de Vendas")
pyautogui.hotkey("ctrl","v")
pyautogui.press("tab") #passar para o corpo do e-mail

# enviar o email
# esse "f" é de formatar, para formatar o texto
corpoemail = f""" 
Prezados, bom dia

O faturamento de ontem foi de: R$ {faturamento:,.2f}
A quantidade de produtos foi de: {quantidade:,}
    
    Abs
    Sergio Araujo
"""
pyperclip.copy(corpoemail)
pyautogui.hotkey("ctrl","v")

#enviar o e-mail
pyautogui.hotkey("ctrl", "enter") # para enviar o e-mail

# No Youtube tem Como transformar arquivo Python em executável
# no Youtube tem Como Executar código python automaticamente 


# In[ ]:





# In[ ]:




