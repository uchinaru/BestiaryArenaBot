### 🐲 Bestiary Arena Bot

Automação para interações dentro da Bestiary Arena, utilizando Selenium para controle da interface via navegador. O bot é capaz de realizar login, escolher regiões, mapas, utilizar poções de stamina, iniciar farm, gerenciar monstros com base na genética e muito mais!

#### 🚀 Funcionalidades

* 🔐 Login automático com credenciais do Discord

* 🌍 Seleção automática de regiões e mapas

* ⚔️ Detecção de batalhas, vitórias e derrotas

* 🧬 Verificação genética de monstros

* 🧪 Uso automático de poções de stamina

* 🌿 Início automático de farm

* 📜 Acesso a missões e mapas com boost diário

* ⚙️ Clique em botões de auto-configuração

* 🎒 Acesso ao inventário do personagem

#### 📁 Estrutura do Projeto
📦 Bestiary Arena Bot

 ┣ 📄 main.py

 ┣ 📄 README.md

 ┣ 📄 LOGIN.txt

#### LOGIN.txt: Arquivo contendo o email e senha do Discord.

* Linha 1: Email

* Linha 2: Senha

#### 📌 Observações

Certifique-se de que o arquivo LOGIN.txt está presente e com as informações corretas.

O bot depende de elementos visuais, portanto mudanças na interface do site podem afetar seu funcionamento.

#### 🧠 Descrição dos Métodos

* def logar(self): 🔐  
  - Realiza login no Discord com as credenciais fornecidas.

* def load_login(self): 📄  
  - Lê o arquivo de login e define os dados de acesso.

* def set_region(self, idregion): 🌍  
  - Define a região do jogo com base no ID.

* def set_map_region_carlin(self, idmapa): 🏰  
  - Retorna mapa da região de Carlin.

* def set_map_region_rookgaard(self, idmapa): 🌾  
  - Retorna mapa da região de Rookgaard.

* def set_map_region_folda(self, idmapa): ❄️  
  - Retorna mapa da região de Folda.

* def set_map_region_abdendriel(self, idmapa): 🌲  
  - Retorna mapa da região de Ab'Dendriel.

* def set_map_region_kazordoon(self, idmapa): ⛏️  
  - Retorna mapa da região de Kazordoon.

* def set_map_region_venore(self, idmapa): 🐍  
  - Retorna mapa da região de Venore.

* def change_regions(self, region): 🔁  
  - Altera a região atual via interface.

* def change_maps(self, idmapa): 🗺️  
  - Altera o mapa atual da região selecionada.

* def start_farm(self): 🌿  
  - Inicia o farm automático.

* def access_inventory(self): 🎒  
  - Acessa o inventário do personagem.

* def use_stamina_potion(self): 🧪  
  - Usa poções de stamina até atingir o mínimo necessário.

* def set_stamina(self): ⚡  
  - Atualiza o valor de stamina atual do personagem.

* def stamine_regem(self): 💊  
  - Usa poções de stamina se necessário.

* def access_quest(self): 📜  
  - Acessa a aba de missões.

* def access_map_boost_daily(self): 🚀  
  - Acessa o mapa com boost diário.

* def get_auto_configure_button(self): ⚙️  
  - Clica no botão de auto configuração.

* def get_dialog_battle(self): ⚔️  
  - Verifica se a batalha foi finalizada.

* def get_dialog_victory_or_defeat(self): 🏆💀  
  - Retorna "Vitória" ou "Derrota" da batalha.

* def verify_monster(self, monster_name_param): 🧬  
  - Verifica se o monstro deve ser mantido ou vendido com base na genética.

* def close_modal_defeat(self): ❌  
  - Fecha o modal de derrota após a batalha.

* def click_on_screen(self): 🖱️  
  - Realiza um clique na tela para manter a interação.


#### ⚙️ Requisitos

* Python 3.8+

* Selenium

* Navegador compatível com WebDriver (ex: Chrome ou Firefox)

##### Instale as dependências com:

* pip install -r requirements.txt