from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from colorama import init, Fore, Back, Style
import os
import time

class BestiaryBot:

    def __init__(self):
        self.SITE_LINK = "https://bestiaryarena.com/pt/game"
        self.EMAIL_USER = ""
        self.PASSWORD = ""
        self.STAMINA_NECESSARIA = 24
        self.STAMINA_ATUAL = ""
        self.GENETICA_MOB = 50
        self.timeouts = 20
        self.REGION_Rookgaard = "/html/body/div[3]/div/div/div[1]/div[2]/div/div[1]/div/label[1]"
        self.REGION_Carlin = "/html/body/div[3]/div/div/div[1]/div[2]/div/div[1]/div/label[2]"
        self.REGION_Folda = "/html/body/div[3]/div/div/div[1]/div[2]/div/div[1]/div/label[3]"
        self.REGION_AbDendriel = "/html/body/div[3]/div/div/div[1]/div[2]/div/div[1]/div/label[4]"
        self.REGION_Kazordoon = "/html/body/div[3]/div/div/div[1]/div[2]/div/div[1]/div/label[5]"
        self.REGION_Venore = "/html/body/div[3]/div/div/div[1]/div[2]/div/div[1]/div/label[6]"

        self.MAP_CITY_BOARDGAMES = "/html/body/div[3]/div/div/div[1]/div[2]/div/div[1]/div/label[1]"
        self.MAP_CARLIN_SEWERS = "/html/body/div[3]/div/div/div[1]/div[2]/div/div[1]/div/label[2]"
        self.MAP_ISLE_OF_KINGS = "/html/body/div[3]/div/div/div[1]/div[2]/div/div[1]/div/label[3]"
        self.MAP_GHOSTLANDS_SURFACE = "/html/body/div[3]/div/div/div[1]/div[2]/div/div[1]/div/label[4]"
        self.MAP_GHOSTLANDS_LIBRARY = "/html/body/div[3]/div/div/div[1]/div[2]/div/div[1]/div/label[5]"
        self.MAP_GHOSTLANDS_RITUAL_SITE = "/html/body/div[3]/div/div/div[1]/div[2]/div/div[1]/div/label[6]"
        self.MAP_DEMON_SKELETON_HELL = "/html/body/div[3]/div/div/div[1]/div[2]/div/div[1]/div/label[7]"
        self.MAP_ZATHROTHS_THRONE = "/html/body/div[3]/div/div/div[1]/div[2]/div/div[1]/div/label[8]"
        self.MAP_DEMONRAGE_SEAL = "/html/body/div[3]/div/div/div[1]/div[2]/div/div[1]/div/label[9]"
        self.MAP_BANSHEES_LAST_ROOM = "/html/body/div[3]/div/div/div[1]/div[2]/div/div[1]/div/label[10]"
        self.MAP_MAZE_GATES = "/html/body/div[3]/div/div/div[1]/div[2]/div/div[1]/div/label[11]"
        self.MAP_LABYRINTH_DEPTHS = "/html/body/div[3]/div/div/div[1]/div[2]/div/div[1]/div/label[12]"
        self.MAP_HIDDEN_CITY_OF_DEMONA = "/html/body/div[3]/div/div/div[1]/div[2]/div/div[1]/div/label[13]"
        self.MAP_TELEPORTER_TRAP = "/html/body/div[3]/div/div/div[1]/div[2]/div/div[1]/div/label[14]"

        self.MAP_SEWERS = "/html/body/div[3]/div/div/div[1]/div[2]/div/div[1]/div/label[1]"
        self.MAP_WHEAT_FIELD = "/html/body/div[3]/div/div/div[1]/div[2]/div/div[1]/div/label[2]"
        self.MAP_EVERGREEN_FIELDS = "/html/body/div[3]/div/div/div[1]/div[2]/div/div[1]/div/label[3]"
        self.MAP_WOLFS_DEN = "/html/body/div[3]/div/div/div[1]/div[2]/div/div[1]/div/label[4]"
        self.MAP_HONEYFLOWER_TOWER = "/html/body/div[3]/div/div/div[1]/div[2]/div/div[1]/div/label[5]"
        self.MAP_SPIDER_LAIR = "/html/body/div[3]/div/div/div[1]/div[2]/div/div[1]/div/label[6]"
        self.MAP_GOBLIN_BRIDGE = "/html/body/div[3]/div/div/div[1]/div[2]/div/div[1]/div/label[7]"
        self.MAP_GOBLIN_TEMPLE = "/html/body/div[3]/div/div/div[1]/div[2]/div/div[1]/div/label[8]"
        self.MAP_MINOTAUR_MAGE_ROOM = "/html/body/div[3]/div/div/div[1]/div[2]/div/div[1]/div/label[9]"
        self.MAP_ROTTEN_GRAVEYARD = "/html/body/div[3]/div/div/div[1]/div[2]/div/div[1]/div/label[10]"
        self.MAP_KATANA_QUEST = "/html/body/div[3]/div/div/div[1]/div[2]/div/div[1]/div/label[11]"
        self.MAP_BEAR_ROOM = "/html/body/div[3]/div/div/div[1]/div[2]/div/div[1]/div/label[12]"
        self.MAP_MINOTAUR_HELL = "/html/body/div[3]/div/div/div[1]/div[2]/div/div[1]/div/label[13]"
        self.MAP_AMBERS_RAFT = "/html/body/div[3]/div/div/div[1]/div[2]/div/div[1]/div/label[14]"
        self.MAP_SWAMPY_PATH = "/html/body/div[3]/div/div/div[1]/div[2]/div/div[1]/div/label[15]"
        self.MAP_LONESOME_DRAGON = "/html/body/div[3]/div/div/div[1]/div[2]/div/div[1]/div/label[16]"

        self.MAP_FOLDA_BOAT = "/html/body/div[3]/div/div/div[1]/div[2]/div/div[1]/div/label[1]"
        self.MAP_CAVE_ENTRANCE = "/html/body/div[3]/div/div/div[1]/div[2]/div/div[1]/div/label[2]"
        self.MAP_FROZEN_AQUIFER = "/html/body/div[3]/div/div/div[1]/div[2]/div/div[1]/div/label[3]"
        self.MAP_ALAWARS_VAULT = "/html/body/div[3]/div/div/div[1]/div[2]/div/div[1]/div/label[4]"
        self.MAP_VEGA_MOUNTAIN = "/html/body/div[3]/div/div/div[1]/div[2]/div/div[1]/div/label[5]"
        self.MAP_SANTA_CLAUS_HOME = "/html/body/div[3]/div/div/div[1]/div[2]/div/div[1]/div/label[6]"
        self.MAP_HEDGE_MAZE = "/html/body/div[3]/div/div/div[1]/div[2]/div/div[1]/div/label[1]"
        self.MAP_ABDENDRIEL_HIVE = "/html/body/div[3]/div/div/div[1]/div[2]/div/div[1]/div/label[2]"
        self.MAP_ELVENBANE = "/html/body/div[3]/div/div/div[1]/div[2]/div/div[1]/div/label[3]"
        self.MAP_FEMOR_HILLS = "/html/body/div[3]/div/div/div[1]/div[2]/div/div[1]/div/label[4]"
        self.MAP_ORCISH_BARRACKS = "/html/body/div[3]/div/div/div[1]/div[2]/div/div[1]/div/label[5]"
        self.MAP_THE_ORC_KING_HALL = "/html/body/div[3]/div/div/div[1]/div[2]/div/div[1]/div/label[6]"
        self.MAP_ORC_FORTRESS_OUTSKIRTS = "/html/body/div[3]/div/div/div[1]/div[2]/div/div[1]/div/label[1]"
        self.MAP_THE_FARMS = "/html/body/div[3]/div/div/div[1]/div[2]/div/div[1]/div/label[2]"
        self.MAP_DWARVEN_BREWERY = "/html/body/div[3]/div/div/div[1]/div[2]/div/div[1]/div/label[3]"
        self.MAP_MINE_HUB = "/html/body/div[3]/div/div/div[1]/div[2]/div/div[1]/div/label[4]"
        self.MAP_EMPEROR_KRUZAKS_TREASURE_ROOM = "/html/body/div[3]/div/div/div[1]/div[2]/div/div[1]/div/label[5]"
        self.MAP_MAD_TECHNOMANCERS_LAB = "/html/body/div[3]/div/div/div[1]/div[2]/div/div[1]/div/label[6]"
        self.MAP_DWARVEN_BRIDGE = "/html/body/div[3]/div/div/div[1]/div[2]/div/div[1]/div/label[1]"
        self.MAP_WYDAS_HOUSE = "/html/body/div[3]/div/div/div[1]/div[2]/div/div[1]/div/label[2]"
        self.MAP_A_SECLUDED_HERB = "/html/body/div[3]/div/div/div[1]/div[2]/div/div[1]/div/label[3]"
        self.MAP_AMAZON_CAMP = "/html/body/div[3]/div/div/div[1]/div[2]/div/div[1]/div/label[4]"
        self.MAP_DRAGON_LAIR = "/html/body/div[3]/div/div/div[1]/div[2]/div/div[1]/div/label[5]"
        self.MAP_CORYM_BASE_LOUNGE = "/html/body/div[3]/div/div/div[1]/div[2]/div/div[1]/div/label[6]"
        self.MAP_SHADOWTHORN = "/html/body/div[3]/div/div/div[1]/div[2]/div/div[1]/div/label[7]"

        chrome_options = Options()

        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
        self.driver.get(self.SITE_LINK)

    def logar(self):
        button_logar = WebDriverWait(self.driver, self.timeouts).until((ec.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/section/div/div[1]/a/button/div"))))
        button_logar.click()

        email_discord_text = WebDriverWait(self.driver, self.timeouts).until((ec.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[2]/div/div[1]/div/div/div/div/form/div[2]/div/div[1]/div[2]/div[1]/div/div/div[2]/input"))))
        email_discord_text.send_keys(self.EMAIL_USER)

        password_discord_text = WebDriverWait(self.driver, self.timeouts).until((ec.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[2]/div/div[1]/div/div/div/div/form/div[2]/div/div[1]/div[2]/div[2]/div/div/input"))))
        password_discord_text.send_keys(self.PASSWORD)

        button_enter_discord = WebDriverWait(self.driver, self.timeouts).until((ec.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[2]/div/div[1]/div/div/div/div/form/div[2]/div/div[1]/div[2]/button[2]"))))
        button_enter_discord.click()

        button_authorize_discord = WebDriverWait(self.driver, self.timeouts).until((ec.element_to_be_clickable((By.XPATH,"/html/body/div[2]/div[2]/div/div[1]/div/div/div/div/div/footer/div/div/button[2]/div"))))
        button_authorize_discord.click()

    def load_login(self):
        with open("LOGIN.txt", "r") as login:
            dados = login.readlines()

            self.EMAIL_USER = dados[0].replace("\n", "")
            self.PASSWORD = dados[1]

    def set_region(self, idregion):
        if idregion == 1:
            return self.REGION_Rookgaard

        if idregion == 2:
            return self.REGION_Carlin

        if idregion == 3:
            return self.REGION_Folda

        if idregion == 4:
            return self.REGION_AbDendriel

        if idregion == 5:
            return self.REGION_Kazordoon

        if idregion == 6:
            return self.REGION_Venore

    def set_map_region_carlin(self, idmapa):
        if idmapa == 1:
            return self.MAP_CITY_BOARDGAMES

        if idmapa == 2:
            return self.MAP_CARLIN_SEWERS

        if idmapa == 3:
            return self.MAP_ISLE_OF_KINGS

        if idmapa == 4:
            return self.MAP_GHOSTLANDS_SURFACE

        if idmapa == 5:
            return self.MAP_GHOSTLANDS_LIBRARY

        if idmapa == 6:
            return self.MAP_GHOSTLANDS_RITUAL_SITE

        if idmapa == 7:
            return self.MAP_DEMON_SKELETON_HELL

        if idmapa == 8:
            return self.MAP_ZATHROTHS_THRONE

        if idmapa == 9:
            return self.MAP_DEMONRAGE_SEAL

        if idmapa == 10:
            return self.MAP_BANSHEES_LAST_ROOM

        if idmapa == 11:
            return self.MAP_MAZE_GATES

        if idmapa == 12:
            return self.MAP_LABYRINTH_DEPTHS

        if idmapa == 13:
            return self.MAP_HIDDEN_CITY_OF_DEMONA

        if idmapa == 14:
            return self.MAP_TELEPORTER_TRAP

    def set_map_region_rookgaard(self, idmapa):
        if idmapa == 1:
            return self.MAP_SEWERS

        if idmapa == 2:
            return self.MAP_WHEAT_FIELD

        if idmapa == 3:
            return self.MAP_EVERGREEN_FIELDS

        if idmapa == 4:
            return self.MAP_WOLFS_DEN

        if idmapa == 5:
            return self.MAP_HONEYFLOWER_TOWER

        if idmapa == 6:
            return self.MAP_SPIDER_LAIR

        if idmapa == 7:
            return self.MAP_GOBLIN_BRIDGE

        if idmapa == 8:
            return self.MAP_GOBLIN_TEMPLE

        if idmapa == 9:
            return self.MAP_MINOTAUR_MAGE_ROOM

        if idmapa == 10:
            return self.MAP_ROTTEN_GRAVEYARD

        if idmapa == 11:
            return self.MAP_KATANA_QUEST

        elif idmapa == 12:
            return self.MAP_BEAR_ROOM

        elif idmapa == 13:
            return self.MAP_MINOTAUR_HELL

        elif idmapa == 14:
            return self.MAP_AMBERS_RAFT

        elif idmapa == 15:
            return self.MAP_SWAMPY_PATH

        elif idmapa == 16:
            return self.MAP_LONESOME_DRAGON

    def set_map_region_folda(self, idmapa):
        if idmapa == 1:
            return self.MAP_FOLDA_BOAT

        if idmapa == 2:
            return self.MAP_CAVE_ENTRANCE

        if idmapa == 3:
            return self.MAP_FROZEN_AQUIFER

        if idmapa == 4:
            return self.MAP_ALAWARS_VAULT

        if idmapa == 5:
            return self.MAP_VEGA_MOUNTAIN

        if idmapa == 6:
            return self.MAP_SANTA_CLAUS_HOME

    def set_map_region_abdendriel(self, idmapa):
        if idmapa == 1:
            return self.MAP_HEDGE_MAZE

        if idmapa == 2:
            return self.MAP_ABDENDRIEL_HIVE

        if idmapa == 3:
            return self.MAP_ELVENBANE

        if idmapa == 4:
            return self.MAP_FEMOR_HILLS

        if idmapa == 5:
            return self.MAP_ORCISH_BARRACKS

        if idmapa == 6:
            return self.MAP_THE_ORC_KING_HALL

    def set_map_region_kazordoon(self, idmapa):
        if idmapa == 1:
            return self.MAP_ORC_FORTRESS_OUTSKIRTS

        if idmapa == 2:
            return self.MAP_THE_FARMS

        if idmapa == 3:
            return self.MAP_DWARVEN_BREWERY

        if idmapa == 4:
            return self.MAP_MINE_HUB

        if idmapa == 5:
            return self.MAP_EMPEROR_KRUZAKS_TREASURE_ROOM

        if idmapa == 6:
            return self.MAP_MAD_TECHNOMANCERS_LAB

    def set_map_region_venore(self, idmapa):
        if idmapa == 1:
            return self.MAP_DWARVEN_BRIDGE

        if idmapa == 2:
            return self.MAP_WYDAS_HOUSE

        if idmapa == 3:
            return self.MAP_A_SECLUDED_HERB

        if idmapa == 4:
            return self.MAP_AMAZON_CAMP

        if idmapa == 5:
            return self.MAP_DRAGON_LAIR

        if idmapa == 6:
            return self.MAP_CORYM_BASE_LOUNGE

        if idmapa == 7:
            return self.MAP_SHADOWTHORN

    def change_regions(self, region):
        try:
            button_select_maps = WebDriverWait(self.driver, self.timeouts).until((ec.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/div/main/div/div[1]/div[2]/button[2]"))))
            button_select_maps.click()

            button_regiao = WebDriverWait(self.driver, self.timeouts).until((ec.element_to_be_clickable((By.XPATH, region))))
            button_regiao.click()

            time.sleep(2)

            button_next = WebDriverWait(self.driver, self.timeouts).until((ec.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/div[4]/button[2]"))))
            button_next.click()
        except:
            print(Fore.RED + f" ❌ Região não acessivel" + Fore.RESET)

    def change_maps(self, idmapa):
        try:
            button_regiao = WebDriverWait(self.driver, self.timeouts).until((ec.element_to_be_clickable((By.XPATH, idmapa))))
            button_regiao.click()
            time.sleep(2)
            button_selecione = WebDriverWait(self.driver, self.timeouts).until((ec.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/div[4]/div/button"))))
            button_selecione.click()
        except:
            print(Fore.RED + f" ❌ Mapa não acessivel" + Fore.RESET)

    def start_farm(self):
        try:
            button_star_farm = WebDriverWait(self.driver, self.timeouts).until((ec.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/div/main/div/div[1]/div[2]/div[1]/div/button"))))
            button_star_farm.click()
            return True
        except:
            return False

    def access_inventory(self):
        button_inventory = WebDriverWait(self.driver, self.timeouts).until((ec.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/div/header/div/div/nav/ul/li[1]/button"))))
        button_inventory.click()

    def use_stamina_potion(self):
        try:
            self.access_inventory()
            potions = WebDriverWait(self.driver, self.timeouts).until(ec.presence_of_all_elements_located((By.XPATH, "//img[@alt='stamina potion']")))

            i = 0
            self.set_stamina()
            while int(self.STAMINA_ATUAL) <= self.STAMINA_NECESSARIA:
                potions[i].click()
                botao_usar = WebDriverWait(self.driver, self.timeouts).until(ec.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Usar poção')]")))
                botao_usar.click()
                botao_fechar = WebDriverWait(self.driver, self.timeouts).until(ec.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Fechar')]")))
                botao_fechar.click()
                self.set_stamina()
                i = i + 1

            self.click_on_screen()

        except Exception as e:
            print(Fore.RED + f" ❌ Nenhuma poção encontrada" + Fore.RESET)

    def set_stamina(self):
        stamina = WebDriverWait(self.driver, self.timeouts).until((ec.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/div/header/div/div/div/button[1]/div/span/span[1]"))))
        self.STAMINA_ATUAL = int(stamina.text)

    def stamine_regem(self):
        self.set_stamina()

        if int(self.STAMINA_ATUAL) <= self.STAMINA_NECESSARIA:
            self.use_stamina_potion()

    def access_quest(self):
        button_quest = WebDriverWait(self.driver, self.timeouts).until((ec.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/div/header/div/div/nav/ul/li[2]/button/span"))))
        button_quest.click()

    def access_map_boost_daily(self):
        button_map_boost_daily = WebDriverWait(self.driver, self.timeouts).until((ec.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div/div[2]/span"))))
        button_map_boost_daily.click()

        try:
            button_selecione = WebDriverWait(self.driver, self.timeouts).until((ec.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/div[4]/div/button"))))
            button_selecione.click()
            return True
        except Exception as e:
            print(Fore.RED + f" ❌ Impossivel acessar o mapa boost" + Fore.RESET)
            return False

    def get_auto_configure_button(self):
        try:
            auto_configure_button = WebDriverWait(self.driver, self.timeouts).until((ec.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/div/main/div/div[1]/div[1]/div/div/button"))))
            auto_configure_button.click()
        except Exception as e:
            print(Fore.RED + f" ❌ Botão auto configure não localizado" + Fore.RESET)
            return False
        else:
            print(Fore.LIGHTCYAN_EX + Style.BRIGHT + f" ✔️ Botão auto configure localizado:" + Fore.RESET)
            return True

    def get_dialog_battle(self):
        try:
            modal_dialog = WebDriverWait(self.driver, self.timeouts).until(ec.visibility_of_element_located((By.XPATH, "/html/body/div[3]")))

            if modal_dialog.is_displayed():
                print(Fore.LIGHTCYAN_EX + Style.BRIGHT + f" ⚔️ Batalha finalizada" + Fore.RESET)
                return True

        except Exception as e:
            print(Fore.RED + f" ⚔️ Em batalha" + Fore.RESET)
            return False

    def get_dialog_victory_or_defeat(self):
        try:
            resultado_elemento = WebDriverWait(self.driver, self.timeouts).until(ec.visibility_of_element_located((By.XPATH, "//h2[contains(@class, 'widget-top-text')]//p")))
            texto = resultado_elemento.text.strip()

            if "Derrota" in texto:
                return "Derrota"
            elif "Vitória" in texto:
                return "Vitória"
        except Exception as e:
            print(Fore.RED + f" ❌ Vendendo o monstro de genetica: " + Fore.RESET)

    def verify_monster(self, monster_name_param):
        try:
            monster_name = WebDriverWait(self.driver, self.timeouts).until((ec.presence_of_element_located((By.XPATH, "/html/body/div[3]/div/div/div[1]/div[1]/div[2]/div[1]/div/span"))))
            monster_genes = WebDriverWait(self.driver, self.timeouts).until((ec.presence_of_element_located((By.XPATH, "/html/body/div[3]/div/div/div[1]/div[1]/div[2]/div[1]/div/div[2]/span/span"))))
            genetica = int(monster_genes.text.replace("%", ""))

            print(Fore.YELLOW + Style.BRIGHT + f" 🧬 GENETICA DO MONSTRO: " + str(genetica) + Fore.RESET)

            if genetica >= self.GENETICA_MOB and monster_name.text == monster_name_param:
                print(Fore.LIGHTCYAN_EX + Style.BRIGHT + f" 🗳️ Mantendo o monstro " + monster_name.text + " de genetica: " + str(genetica) + Fore.RESET)
                time.sleep(3)
            else:
                time.sleep(2)
                print(Fore.RED + f" 💵 Vendendo o monstro " + monster_name.text + " de genetica: " + str(genetica) + Fore.RESET)
                button_sell_monster = WebDriverWait(self.driver, self.timeouts).until((ec.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/div[1]/div[1]/div[2]/div[1]/button"))))
                button_sell_monster.click()
                time.sleep(7)

            button_close = WebDriverWait(self.driver, self.timeouts).until((ec.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/div[3]/button"))))
            button_close.click()
            time.sleep(2)

        except:
            print(Fore.RED + f" ❌ Erro ao verificar monstro: " + Fore.RESET)

    def close_modal_defeat(self):
        botao_fechar = WebDriverWait(self.driver, self.timeouts).until(ec.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Fechar')]")))
        botao_fechar.click()
        print(Fore.RED + f" ❌ Morreu em batalha: " + Fore.RESET)

    def click_on_screen(self):
        actions = ActionChains(self.driver)
        actions.move_by_offset(10, 18).click().perform()


BestiaryBot = BestiaryBot()
BestiaryBot.load_login()
BestiaryBot.logar()
BestiaryBot.change_regions(BestiaryBot.set_region(4))
BestiaryBot.change_maps(BestiaryBot.set_map_region_abdendriel(1))
BestiaryBot.get_auto_configure_button()

contador = 0
while contador < 99999:
    BestiaryBot.stamine_regem()
    BestiaryBot.start_farm()

    while not BestiaryBot.get_dialog_battle():
        BestiaryBot.get_dialog_battle()
        if "Vitória" in BestiaryBot.get_dialog_victory_or_defeat():
            BestiaryBot.verify_monster("Elf Scou")
        else:
            BestiaryBot.close_modal_defeat()
        break

    contador = contador + 1
    BestiaryBot.click_on_screen()
