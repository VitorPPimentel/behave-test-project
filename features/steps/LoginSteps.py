from logging import raiseExceptions
from behave import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

@given("que esteja na página de login")
def step_impl(context):
    context.browser.get(context.variables["url_login"])

@when("insiro {email} no campo email do login")
def step_impl(context, email):
    field_login = context.browser.find_element('id','input-18')
    field_login.send_keys(email)

@when("insiro {senha} no campo senha do login")
def step_impl(context, senha):
    field_senha = context.browser.find_element('id','password')
    field_senha.send_keys(senha)

@When("clico no botão realizar login")
def step_impl(context):
    button = context.browser.find_element('xpath','//*[@id="app"]/div/main/div/div[1]/div/div/div/div/div/div/div/div[1]/div[2]/button/span')
    button.click()

@then("a página inicial é carregada")
def step_impl(context):
    texto = context.browser.find_element('xpath','//*[@id="app"]/div/main/div/div/div/div/div/h2')
    assert texto.text == "Seja bem vindo!"

@then("a mensagem de erro é exibida")
def step_impl(context):
    card_confirmacao = context.browser.find_element('xpath', '/html/body/div/div/div/div/main/div/div[2]/div/div/div[1]')
    wait = WebDriverWait(context.browser, 10)
    wait.until(EC.visibility_of(card_confirmacao))
    
    texto_erro = context.browser.find_element('xpath','/html/body/div/div/div/div/main/div/div[2]/div/div/div[1]')
    texto_esperado = "Error ao autenticar."
    assert texto_esperado in texto_erro.text

