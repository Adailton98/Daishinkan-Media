import os
import getpass # Adicione isso no topo do arquivo com os outros imports

# Cores e Estilo
VERDE = '\033[92m'
AZUL = '\033[94m'
AMARELO = '\033[93m'
VERMELHO = '\033[91m'
CIANO = '\033[96m'
RESET = '\033[0m'
NEGRITO = '\033[1m'

def fazer_login():
    os.system('clear')
    usuario_correto = "DAI" 
    senha_correta = "IAD"
    tentativas = 3

    print(f"{CIANO}{NEGRITO}┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
    print(f"┃          PAINEL DE ACESSO RESTRITO v6.0          ┃")
    print(f"┃            SEGURANÇA DAISHINKAN ATIVA            ┃")
    print(f"┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛{RESET}")

    while tentativas > 0:
        print(f"\n{AMARELO}Tentativas restantes: {tentativas}{RESET}")
        user = input(f"👤 Usuário: ")
        
        # O getpass faz a senha ficar invisível ao digitar
        senha = getpass.getpass(f"🔑 Senha (invisível): ")

        if user == usuario_correto and senha == senha_correta:
            print(f"\n{VERDE}✅ Acesso Autorizado! Iniciando sistemas...{RESET}")
            os.system("sleep 2")
            return True
        else:
            tentativas -= 1
            print(f"\n{VERMELHO}❌ Credenciais Incorretas!{RESET}")
    
    print(f"\n{VERMELHO}SISTEMA BLOQUEADO. Procure o administrador.{RESET}")
    return False

def menu():
    os.system('clear') # Único clear necessário no início
    
    # 1. Desenha a Arte ASCII
    print(f"{CIANO}{NEGRITO}")
    print(r"""
    ▓█████▄  ▄▄▄       ██▓  ██████  ██░ ██  ██▓ ███▄    █  ██ ▄█▀ ▄▄▄      ███▄    █ 
    ▒██▀ ██▌▒████▄    ▓██▒▒██    ▒ ▓██░ ██ ▓██▒ ██ ▀█   █  ██▄█▒ ▒████▄    ██ ▀█   █ 
    ░██   █▌▒██  ▀█▄  ▒██▒░ ▓██▄   ▒██▀▀██ ▒██▒▓██  ▀█ ██▒▓███▄░ ▒██  ▀█▄ ▓██  ▀█ ██▒
    ░▓█▄   ▌░██▄▄▄▄██ ░██░  ▒   ██▒░▓█ ░██ ░██░▓██▒  ▐▌██▒▓██ █▄ ░██▄▄▄▄██ ▓██▒  ▐▌██▒
    ░▒████▓  ▓█   ▓██▒░██░▒██████▒▒░▓█▒░██▓░██░▒██░   ▓██░▒██▒ █▄ ▓█   ▓██▒▒██░   ▓██░
    """)
    
    # 2. Desenha o Menu (Sem dar 'clear' novamente!)
    print(f"{CIANO}{NEGRITO}┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
    print(f"┃          SISTEMA SUPREMO DAISHINKAN v6.0         ┃")
    print(f"┃          Criado por: @SEU_INSTAGRAM              ┃")
    print(f"┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛{RESET}")
    print(f"  {CIANO}┌── Áudio & Música ────────────────────────────┐{RESET}")
    print(f"  {VERDE} [1]{RESET} Link YouTube (MP3)   {VERDE}[2]{RESET} Buscar por Nome")
    print(f"  {VERDE} [3]{RESET} Playlist YouTube     {VERDE}[4]{RESET} Spotify (Link)")
    print(f"  {CIANO}├── Social Media & Vídeo ──────────────────────┤{RESET}")
    print(f"  {VERDE} [5]{RESET} Vídeo (TT/IG/YT)     {VERDE}[6]{RESET} Foto (Instagram)")
    print(f"  {CIANO}└── Sistema ───────────────────────────────────┘{RESET}")
    print(f"  {VERMELHO} [7]{RESET} Limpar Tudo          {AMARELO}[8]{RESET} Atualizar Motores")
    print(f"  {NEGRITO} [0]{RESET} Sair")
    print(f"{CIANO}──────────────────────────────────────────────────{RESET}")

    # ... resto do menu ...

    os.system('clear')
    print(f"{CIANO}{NEGRITO}┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
    print(f"┃          SISTEMA SUPREMO DAISHINKAN v6.0         ┃")
    print(f"┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛{RESET}")
    print(f"  {CIANO}┌── Áudio & Música ────────────────────────────┐{RESET}")
    print(f"  {VERDE} [1]{RESET} Link YouTube (MP3)   {VERDE}[2]{RESET} Buscar por Nome")
    print(f"  {VERDE} [3]{RESET} Playlist YouTube     {VERDE}[4]{RESET} Spotify (Link)")
    print(f"  {CIANO}├── Social Media & Vídeo ──────────────────────┤{RESET}")
    print(f"  {VERDE} [5]{RESET} Vídeo (TT/IG/YT)     {VERDE}[6]{RESET} Foto (Instagram)")
    print(f"  {CIANO}└── Sistema ───────────────────────────────────┘{RESET}")
    print(f"  {VERMELHO} [7]{RESET} Limpar Tudo          {AMARELO}[8]{RESET} Atualizar Motores")
    print(f"  {NEGRITO} [0]{RESET} Sair")
    print(f"{CIANO}──────────────────────────────────────────────────{RESET}")

def baixar_midia(opcao):
    raiz_destino = os.path.expanduser("~/storage/downloads/Daishinkan_Media")
    os.system(f"mkdir -p {raiz_destino}")
    comando = ""

    if opcao == '1':
        link = input(f"\n🔗 {NEGRITO}Link do YouTube: {RESET}")
        comando = f'yt-dlp -x --audio-format mp3 -o "{raiz_destino}/%(title)s.%(ext)s" "{link}"'

    elif opcao == '2':
        nome = input(f"\n🔍 {NEGRITO}Nome da música: {RESET}")
        comando = f'yt-dlp -x --audio-format mp3 -o "{raiz_destino}/%(title)s.%(ext)s" "ytsearch:{nome}"'

    elif opcao == '3':
        link = input(f"\n📂 {NEGRITO}Link da Playlist: {RESET}")
        comando = f'yt-dlp -x --audio-format mp3 -o "{raiz_destino}/%(playlist_title)s/%(title)s.%(ext)s" "{link}"'

    elif opcao == '4':
        link = input(f"\n🎧 {NEGRITO}Link do Spotify: {RESET}")
        # Correção Spotdl: Entra na pasta primeiro e baixa
        comando = f'cd "{raiz_destino}" && spotdl download "{link}"'

    elif opcao == '5':
        link = input(f"\n🎬 {NEGRITO}Link do Vídeo: {RESET}")
        caminho_cookies = os.path.expanduser("~/tiktok_cookies.txt")
        if os.path.exists(caminho_cookies):
            print(f"{VERDE}🍪 Cookies detectados!{RESET}")
            comando = f'yt-dlp --cookies {caminho_cookies} -f "best" --no-check-certificates -o "{raiz_destino}/%(title)s.%(ext)s" "{link}"'
        else:
            comando = f'yt-dlp -f "best" -o "{raiz_destino}/%(title)s.%(ext)s" "{link}"'

    elif opcao == '6':
        link = input(f"\n📸 {NEGRITO}Link da Imagem: {RESET}")
        comando = f'instaloader --dirname-pattern="{raiz_destino}" -- -{link.split("/")[-2]}'

    elif opcao == '7':
        confirmar = input(f"{VERMELHO}Apagar tudo em Daishinkan_Media? (s/n): {RESET}")
        if confirmar.lower() == 's':
            os.system(f"rm -rf {raiz_destino}/*")
            print(f"{VERDE}Limpagem concluída!{RESET}")

    elif opcao == '8':
        print(f"{AZUL}Atualizando componentes...{RESET}")
        os.system("pip install --upgrade yt-dlp spotdl instaloader")
    
    if comando:
        os.system(comando)
        print(f"\n{VERDE}✅ Concluído!{RESET}")
    
    # SOLUÇÃO PARA NÃO TRAVAR:
    input(f"\n{AMARELO}➔ Pressione ENTER para voltar ao menu...{RESET}")

# Loop Principal
# No final do arquivo, substitua o loop antigo por este:
if __name__ == "__main__":
    if fazer_login(): # O sistema chama o login primeiro
        while True:
            menu() # Se o login der certo, ele entra no menu
            escolha = input(f"{NEGRITO}Escolha uma opção: {RESET}")
            if escolha == '0':
                print(f"{AMARELO}Encerrando sistema...{RESET}")
                break
            baixar_midia(escolha)

