#!/data/data/com.termux/files/usr/bin/bash

# Cores para o instalador
VERDE='\033[92m'
CIANO='\033[96m'
RESET='\033[0m'

echo -e "${CIANO}====================================================${RESET}"
echo -e "      INSTALADOR DO SISTEMA SUPREMO DAISHINKAN"
echo -e "${CIANO}====================================================${RESET}"

echo -e "${VERDE}[+] Atualizando repositórios...${RESET}"
pkg update && pkg upgrade -y

echo -e "${VERDE}[+] Instalando Python e FFMPEG (Essencial para Áudio)...${RESET}"
pkg install python ffmpeg jq curl -y

echo -e "${VERDE}[+] Instalando Motores de Download (YT-DLP, SpotDL, Instaloader)...${RESET}"
pip install yt-dlp spotdl instaloader

echo -e "${VERDE}[+] Configurando acesso ao armazenamento...${RESET}"
termux-setup-storage

echo -e "${CIANO}====================================================${RESET}"
echo -e "          INSTALAÇÃO CONCLUÍDA COM SUCESSO!"
echo -e "      Siga o criador no Instagram para atualizações."
echo -e "${CIANO}====================================================${RESET}"

# Substitua 'SEU_USER' pelo seu nome de usuário real do Instagram abaixo
echo -e "${VERDE}Abrindo perfil do criador...${RESET}"
sleep 2
termux-open-url https://www.instagram.com/daishinkan_br1

echo -e "\nPara iniciar o sistema, digite: ${VERDE}python media.py${RESET}"
