# Software passou nos seguintes testes : mypy, pytest
#  black e Flake8

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

proxy = "192.168.0.181:9050"  # endereço local do tor


class TesteUnitario:
    @staticmethod
    def teste_get_current_ip_proxy():
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--proxy-server=socks5://%s" % proxy)
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("http://icanhazip.com/")
        ip = (
            WebDriverWait(driver, 30)
            .until(EC.visibility_of_element_located((By.XPATH, "/html/body/pre")))  # noqa: E501
            .get_attribute("innerHTML")
            .strip()
        )
        assert len(ip) > 10
