#! /bin/bash

echo "╔████████████╔████████████╔██        ██╔████████████╔██       ██"
echo "╚════╗██     ╚════╗██     ║██        ██║██          ║██       ██"
echo "     ║██          ║██     ║██        ██║██          ╚╗██     ██"
echo "     ║██          ║██     ║██        ██║██           ║██     ██"
echo "     ║██          ║██     ║██   ██   ██║████████████ ╚╗██   ██"
echo "     ║██          ║██     ║██  ████  ██╚═════════╗██  ║██   ██"
echo "     ║██          ║██     ║██ ██╔╝██ ██          ║██  ╚╗██ ██"
echo "╔════╝██          ║██     ║████╔╝  ████╔═════════╝██   ║██ ██"
echo "║███████████      ║██     ║███╔╝    ███║████████████   ║█████"
echo "╚══════════╝      ╚═╝     ╚═══╝        ╚═══════════╝   ╚═╦══╝" 
echo "                                         ╔═══════════════╩════════╗"
echo "                                         ║INTEGRATED TOOL FOR WEB ║"
echo "                                         ║SECURITY VULNERABILITIES║"
echo "                                         ║BY- ₳Ɽ₱ł₮ ₭Ⱨ₳Ɽ₵ⱧɆ       ║"
echo "                                         ╚════════════════════════╝"
echo "Choose an option-"
echo " "
echo "1- Auto pentest (Check for vulnerabilities)"
echo " "
echo "2- Tools"
echo " "
echo "3- Install (only for installation)"
echo " "

read target
echo " "
if [[ "$target" = 1 ]]
	then cd My_script
	chmod +x myscript.sh
	./myscript.sh
	cd ..
elif [[ "$target" = 2 ]]
	then ./update.sh
elif [[ "$target" = 3 ]]
	then chmod +x update.sh
	chmod +x requirements.txt
	pip install -r requirements.txt
	cd Tools 
	cd Trity-1
	chmod +x install.py
	chmod +x run.sh
	python install.py
	cd ..
	cd pureblood
	chmod +x requirements.txt
	chmod +x pureblood.py
	pip install -r requirements.txt
	cd ..
	cd RED_HAWK
	chmod +x rhawk.php
	cd ..
	cd lscript
	chmod +x l
	chmod +x install.sh
	./install.sh
	cd ..
	cd ..
else echo "Incorrect Entry"
fi
	

