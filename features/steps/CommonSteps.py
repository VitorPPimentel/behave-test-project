from logging import raiseExceptions
from behave import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from faker import Faker
from datetime import datetime, date , timedelta
from json import dumps
import time, os, requests, json

@given('que esteja logado no sistema')
def step_impl(context):
    context.execute_steps(u'''
        Dado que esteja na página de login do
        Quando insiro mail@mail.com.br no campo email do login
        E insiro 123456 no campo senha do login
        E clico no botão realizar login
    ''')
    time.sleep(2)
#cadastro steps################################
