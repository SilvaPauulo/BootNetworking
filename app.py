from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Vai acessar o Google e digitar a seguinte URL:
driver = webdriver.Chrome()
driver.get('https://www.linkedin.com/notifications/?filter=all')


#Vai selecionar o campo email:
driver.find_element(By.XPATH,'//*[@id="username"]').click()
print(f'Cliquei no campo email ...')
print(f'-' * 50)

#Vai inserir o email
driver.find_element(By.CSS_SELECTOR,'#username').send_keys('insira_seu_email')
print(f'E-mail inserido no campo email ...')
print(f'-' * 50)

#Vai selecionar o campo senha:
driver.find_element(By.XPATH,'//*[@id="password"]').click()
print(f'Cliquei no campo de senha ...')
print(f'-' * 50)

#Vai inserir a senha:
driver.find_element(By.XPATH,'//*[@id="password"]').send_keys('insira_sua_senha')
print(f'Senha inserida ...')
print(f'-' * 50)

#Ele vai clicar em entrar
driver.find_element(By.XPATH,'//*[@id="organic-div"]/form/div[3]/button').click()
print(f'Clicando em Entrar ...')
print(f'-' * 50)

#Vai clicar em Pesquisar
driver.find_element(By.XPATH,'//*[@id="global-nav-search"]/div').click()
print(f'Clicando em pesquisar ...')
print(f'-' * 50)

# Para problemas de visibilidade de elementos ele ira aguardar 15 segundos, para o elemento ficar visivel.
wait = WebDriverWait(driver, timeout=15)

# Aguardando os 15 segundos ele vai selecionar o elemento CSS:
elemento = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#global-nav-typeahead > input")))

# Ele vai fazer uma breve validação no terminal para ver se o elemento esta visivel se true = visivel , se false = invisivel
visibilidade_do_elemento = driver.find_element(By.CSS_SELECTOR,'#global-nav-typeahead > input').is_displayed()
print(visibilidade_do_elemento)
print(f'-' * 50)


# E por utimo ele vai inserir o input do usuario que são as informações sobre a sua procura;
driver.find_element(By.CSS_SELECTOR,'#global-nav-typeahead > input').send_keys('Dados')
print(f'Campo sendo preenchido ... com a informação do usuario ...')
print(f'-' * 50)

#Exibir todos os resultados
driver.find_element(By.CSS_SELECTOR,'#global-nav-search > div').click()
print(f'Clicando em exibir todos os resultados ...')

#Ele vai selecionar a opção pessoas:
driver.find_element(By.CSS_SELECTOR,'body > div.application-outlet > div.authentication-outlet > div.scaffold-layout.scaffold-layout--breakpoint-none.scaffold-layout--sidebar-main-aside.scaffold-layout--single-column.scaffold-layout--reflow.search-marvel-srp-container__layout-main-aside--542 > div > div.scaffold-layout__row.scaffold-layout__content.scaffold-layout__content--sidebar-main-aside.scaffold-layout__content--has-sidebar.scaffold-layout__content--has-aside > div > div > div > section > ul > li:nth-child(2) > button').click()
print(f'Clicou na seção pessoas ...')

print(f'-' * 50)

#Ele vai clicar no botão  conectar
driver.find_element(By.XPATH,'/html[1]/body[1]/div[4]/div[3]/div[2]/div[1]/div[1]/main[1]/div[1]/div[1]/div[2]/div[1]/ul[2]/li[1]/div[1]/div[1]/div[1]/div[3]/div[1]/button[1]/span[1]').click()
print(f'Clicou em se conectar com o usuario ...')

#Ele vai clicar em adicionar nota:
driver.find_element(By.XPATH,'//*[@id="ember3014"]/span').click()
print('Clicou no botão adicionar nota ...')

#Vai clicar dentro do input:
driver.find_element(By.XPATH,'//*[@id="custom-message"]').click()
print(f'Clicou no input para digitar a mnensagem !')

#Vai digitar o texto
driver.find_element(By.XPATH,'//*[@id="custom-message"]').send_keys('Dados')
print(f'texto digitado ...')




