import asyncio
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from time import sleep
from threading import Thread
from random import randint

#  from dataclasses import dataclass, field
from typing import List, Any
from stem import Signal
from stem.control import Controller


class Navegar(Thread):
    """
    Sistema de clicar no vídeo do youtube.
    Pode clicar em vários vídeos ao mesmo tempo
    com várias repetições dos cliques
    em tempos randômicos.
    O youtube pode bloquear o seu ip. Use o sistema
    por sua conta e risco.
    """

    def __init__(
        self,
        qtd_repeticoes: int,
        duracao_video: List[int],
        url: str,
        proxy: str,
        num_obj: int,
        qtd_objetos: int,
    ):
        super(Navegar, self).__init__()
        self.qtd_repeticoes = qtd_repeticoes
        self.duracao_video = duracao_video
        self.url = url
        self.proxy = proxy
        self.num_obj = num_obj
        self.qtd_objetos = qtd_objetos
        self.erros: List[Any] = []

    def run(self):
        """Conecta no proxy e faz requisição para youtube

        :param qtd_repeticoes: Quantas vezes vai rodar o objeto
        :type amount: int
        :param duracao_video: Lista com tempo randômico [mini tempo, máximo tempo]
        :type amount: list
        :param url: Link da página no youtube
        :type amount: str
        :param proxy: Endereço proxy
        :type amount: str
        :param num_obj: Quantidade de objetos acessando ao mesmo tempo
        :type amount: int

        """
        for i in range(self.qtd_repeticoes):
            try:
                # Parâmetros proxy
                chrome_options = webdriver.ChromeOptions()
                chrome_options.add_argument(
                    "--proxy-server=socks5://%s" % self.proxy
                )
                chrome_options.add_argument("--disable-gpu")
                chrome_options.add_argument("--incognito")
                chrome_options.add_argument("--disable-dev-shm-usage")
                chrome_options.add_argument("--no-sandbox")
                self.driver = webdriver.Chrome(options=chrome_options)
                self.driver.get("http://icanhazip.com/")
                ip = (
                    WebDriverWait(self.driver, 30)
                    .until(
                        EC.visibility_of_element_located(
                            (By.XPATH, "/html/body/pre")
                        )
                    )
                    .get_attribute("innerHTML")
                    .strip()
                )
                print(ip)
                self.driver.get(self.url)
                # Clicar no botão reject all cookies
                WebDriverWait(self.driver, 30).until(
                    EC.visibility_of_element_located(
                        (
                            By.XPATH,
                            "//*[@id='content']/div[2]/div[6]/div[1]/ytd-button-renderer[1]/yt-button-shape/button",  # noqa: E501
                        )
                    )
                ).click()
                # Precisa esperar até clicar no botão do cookie
                sleep(30)
                WebDriverWait(self.driver, 45).until(
                    EC.element_to_be_clickable(
                        (By.XPATH, "//button[@aria-label='Play']")
                    )
                ).click()
                sleep(randint(self.duracao_video[0], self.duracao_video[1]))
                sleep(5)
            except TimeoutException as ex:
                self.erros.append(ex)
                pass
            except Exception as e:
                self.erros.append(e)
                pass
            finally:
                if self.driver:
                    self.driver.close()
                    self.driver.quit()
                    asyncio.run(self.get_current_ip())
                else:
                    print("Error: Please check if tor is up.")
                print(f"Número video: { (self.num_obj) + (i)* self.qtd_objetos }")  # noqa: E501
        return {"erros": self.erros}

    async def get_current_ip(self):
        """Conecta no Tor para alterar o endereço
        A senha padrão do tor é tor mas pode ser
        alterado caso seja necesário.
        """

        with Controller.from_port(port=9051) as controller:
            try:
                controller.authenticate(password="tor")
                controller.signal(Signal.NEWNYM)
                sleep(controller.get_newnym_wait())
            except Exception as e:
                print(e)
                self.erros.append(e)
                pass
        return {"error": self.erros}
