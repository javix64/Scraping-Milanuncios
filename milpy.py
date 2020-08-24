import requests, time, csv
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
options = Options()
options.headless = True
browser = webdriver.Firefox(options=options)

last_page = 2338
save_page = []
save_data = []
url_base = ''
for i in range(1,last_page):
    url_base = 'https://www.milanuncios.com/telefonia/?pagina='+str(i)
    print('Estamos en la pagina:'+url_base)
    browser_url = browser.get(url_base)
    output = 'data.csv'
    data_file = open(output, 'w')
    writer = csv.writer(data_file)
    writer.writerow(['url','titulo','descripcion','ubicacion','vendedor','precio','particular', 'stats_visto', 'stats_contactado', 'stats_compartido', 'stats_favorito', 'stats_renovados'])
    scroll = 400

    for i in range(1,11):
        # Scroll down to bottom
        scroll = scroll+1000
        browser.execute_script("window.scrollTo(0, "+str(scroll)+");")
        time.sleep(0.4)
    links = browser.find_elements_by_xpath('//a[@class="ma-AdCard-bodyTitleLink"]')    

    for link in links:
        save_href = link.get_attribute('href')
        save_page.append(save_href)

    for website in save_page:
        browser.get(website)
        url = str(website)
        element_present0 = EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div[1]/div[5]/div/div[2]/div[2]/div[1]'))
        WebDriverWait(browser, 6).until(element_present0)
        titulo = browser.find_element_by_xpath('//h1').text
        descripcion = browser.find_element_by_xpath('//p[@class="pagAnuCuerpoAnu"]').text
        ubicacion = browser.find_element_by_xpath('//div[@class="pagAnuCatLoc"]').text
        vendedor = browser.find_element_by_xpath('//div[@class="pagAnuContactNombre"]').text
        precio = browser.find_element_by_xpath('//div[@class="pagAnuPrecioTexto"]').text
        particular = browser.find_element_by_xpath('//div[@class="pagAnuSubtitle"]/div[2]').text
        stats_visto = browser.find_element_by_xpath('//div[@class="pagAnuStats"]/div[3]/div[1]/div[1]').text
        stats_contactado = browser.find_element_by_xpath('//div[@class="pagAnuStats"]/div[3]/div[2]/div[1]').text
        stats_compartido = browser.find_element_by_xpath('/html/body/div[1]/div[1]/div[5]/div/div[2]/div[2]/div[4]/div[1]/div[1]').text
        stats_favorito = browser.find_element_by_xpath('/html/body/div[1]/div[1]/div[5]/div/div[2]/div[2]/div[4]/div[2]/div[1]').text
        stats_renovados = browser.find_element_by_xpath('/html/body/div[1]/div[1]/div[5]/div/div[2]/div[2]/div[5]/div/div[1]').text
        #save_data.append([url,titulo,descripcion,ubicacion,vendedor,precio,particular, stats_visto, stats_contactado, stats_compartido, stats_favorito, stats_renovados])
        writer.writerow([url,titulo,descripcion,ubicacion,vendedor,precio,particular, stats_visto, stats_contactado, stats_compartido, stats_favorito, stats_renovados])
        print('Estamos en el item:'+str(website))


"""
Entramos en la url principal
https://www.milanuncios.com/telefonia/?pagina=
guardamos en un array los enlaces
entrar en cada enlace del array
y obtener:
    -titulo
    -descripcion
    -ubicacion
    -sacar precio
    -particular?
    -estadisticas

"""