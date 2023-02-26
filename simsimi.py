###----------[ IMPORT MODULE LAIN ]---------- ###
import os,sys,time,requests,json
from datetime import datetime
from requests.exceptions import ConnectionError

###----------[ IMPORT MODULE RICH ]---------- ###
from rich.panel import Panel
from rich import print as prints
from rich.console import Console
from rich.columns import Columns
console = Console()

###----------[ WARNA PRINT RICH ]---------- ###
M = "[#FF0000]" # MERAH
H = "#00FF00" # HIJAU
P = "[#FFFFFF]" # PUTIH
U = "[#AF00FF]" # UNGU
J = "#FF8F00" # JINGGA
	
###----------[ LOGO AUTHOR DAN VERSI ]---------- ###
class Logo:
	
	###----------[ BERSIHKAN LAYAR ]---------- ###
	def bersihkan_layar(self):
		if "linux" in sys.platform.lower():
			try:os.system("clear")
			except:pass
		elif "win" in sys.platform.lower():
			try:os.system("cls")
			except:pass
		else:
			try:os.system("clear") 
			except:pass

	###----------[ LOGO ]---------- ###
	def logonya(self):
		self.bersihkan_layar()
		prints(Panel(f"""{M}███████ ██ ███    ███ ███████ ██ ███    ███ ██ {P}Free SimSimi Bot Chat
{M}██      ██ ████  ████ ██      ██ ████  ████ ██ {P}Src: https://simsimi.net
{M}███████ ██ ██ ████ ██ ███████ ██ ██ ████ ██ ██ {P}
     ██ ██ ██  ██  ██      ██ ██ ██  ██  ██ ██ Thans For Using Tools
███████ ██ ██      ██ ███████ ██ ██      ██ ██ Made By Indonesian Coder""",width=80,style=f"{U.replace('[','').replace(']','')}"))
		
###----------[ SIMSIMI ]---------- ###
class SimSimi:
	
	def __init__(self):
		self.url = "https://api.simsimi.net/v2/"
		self.ses = requests.Session()
		self.headers = {"host": "api.simsimi.net","upgrade-insecure-requests": "1","accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","content-type": "application/x-www-form-urlencoded","origin": "https://api.simsimi.net/"}
		
	###----------[ DELAY ]---------- ###
	def delay(self):
		animasi = ["sedang mengetik.","sedang mengetik..","sedang mengetik...","sedang mengetik...."]
		for z in animasi:
			print(f"\r {z}",end="")
			time.sleep(0.5)
			
	###----------[ MENU ]---------- ###
	def main(self):
		Logo().logonya()
		print("\n")
		while True:
			
			###----------[ APPEND ]---------- ###
			kamu = []
			bot = []

			try:
				###----------[ BAGIAN KAMU ]---------- ###
				pesan = console.input(f"\n\n\r Pesan Kamu ▶ ")
				print("\033[4A")
				kamu.append(f'\n{str(datetime.now().strftime("%H:%M"))}')
				kamu.append(Panel(f"{P}{pesan}", style=f"{H}"))
				console.print("Kamu",Columns(kamu),justify="right")
				
				###----------[ BAGIAN DELAY ]---------- ###
				print(f"\n")
				self.delay()
				
				###----------[ BAGIAN BOT ]---------- ###
				req = self.ses.get(f"{self.url}?text={kamu}&lc=id&cf=false", headers=self.headers)
				response = json.loads(req.text)["success"]
				print("\033[3A")
				bot.append(Panel(f"{P}{response}", style=f"{J}"))
				bot.append(f'\n{str(datetime.now().strftime("%H:%M"))}')
				console.print("SimSimi",Columns(bot),justify="left")
				
				###----------[ KONDISI KONEKSI ERROR ]---------- ###
			except ConnectionError:
				console.print(f"{P}────────────────Tidak Ada Koneksi────────────────", justify="center")
		
SimSimi().main()