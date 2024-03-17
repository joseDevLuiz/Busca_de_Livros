import pandas as pd
from translate import Translator
from selenium import webdriver
from selenium.webdriver.common.by import By

# Area de funçoes

def traduzindo(texto):
    tradutor = Translator(to_lang='pt')
    traducao = tradutor.translate(texto)
    return print(traducao)


# COMEÇANDO O CODIGO

# Abrindo tabela

tabela = pd.read_excel('Preço_e_Livros.xlsx')

# Abrindo o Chrome
navegador = webdriver.Chrome()

# Books To Scrape
navegador.get('https://books.toscrape.com/')
navegador.implicitly_wait(15)

# Livros Cristaos

navegador.find_element('xpath', '//*[@id="default"]/div[1]/div/div/aside/div[2]/ul/li/ul/li[42]/a').click()

# Vendo e Salvando Preços

precos = []
preco = navegador.find_elements(By.CLASS_NAME, 'price_color')
for elemento in preco:
    precos.append(elemento.text)

# Vendo e Salvando Nomes

nomes = []
nome = navegador.find_elements(By.CLASS_NAME, 'thumbnail')
for elemento_imagem in nome:
    texto_alt = elemento_imagem.get_attribute('alt')
    nomes.append(texto_alt)

# Excel

tabela = pd.read_excel('Preço_e_Livros.xlsx')

# Incluindo Dados do Site

tabela.loc[0, 'Nome'] = nomes[0]
tabela.loc[0, 'Preço'] = precos[0]

tabela.loc[1, 'Nome'] = nomes[1]
tabela.loc[1, 'Preço'] = precos[1]

tabela.loc[2, 'Nome'] = nomes[2]
tabela.loc[2, 'Preço'] = precos[2]

# tabela.to_excel('Preço_e_Livros.xlsx', index=False)
