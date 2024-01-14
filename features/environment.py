from selenium import webdriver
from behave.contrib.scenario_autoretry import patch_scenario_with_autoretry
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import json, time, os

def before_scenario(context, scenario):
    #################################### Definições de chrome options #################################### 
    # Define as opções de inicialização do browser
    options = webdriver.ChromeOptions()

    # Verifica se no behave.ini as opções estão ativas para segundo plano e modo anonimo (headless e icognito)
    if context.config.userdata["headless"] == "true":
        options.add_argument("--headless")
    if context.config.userdata["icognito"] == "true":
        options.add_argument("--incognito")

    # Inicia o navegador chrome e instala o driver necessário para execução
    context.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    # isso define um caminhão padrão para o download em headless
    prefs = {"download.default_directory" : os.path.join(os.path.expanduser("~"), "Downloads")}
    options.add_experimental_option("prefs",prefs)

    # coloca o navegador em tela cheia
    context.browser.maximize_window()
    # Define o implicity wait para o cenário
    context.browser.implicitly_wait(context.config.userdata["implicity_wait"])

    #################################### Leitura dos profiles ####################################

    # Carrega o profile default
    with open('features/profiles/default.json') as profile_file:
        default_profile_json = json.load(profile_file)
        context.variables = default_profile_json

        # Busca e carrega o profile definido na tag profile no behave.ini
        try:
            profile = context.config.userdata["profile"]
            with open("features/profiles/"+profile+".json") as profile_file:
                chosen_profile_json = json.load(profile_file)
                default_profile_json.update(chosen_profile_json)
                context.variables = default_profile_json
        except:
            # Caso o arquivo de profile não exista, retorna a exceção
            raise Exception(profile + ".json file not found at /profiles. Loading only the default profile...")

    # Apenas para visualização da tela antes de encerrar o navegador
    time.sleep(3)

    #Encerra o navegador
    context.browser.quit()

# Para visualização da tela pois o código é muito rápido  
# def after_step(context, scenario):
#     time.sleep(1)