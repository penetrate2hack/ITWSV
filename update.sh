#! /bin/bash



echo "Choose"
echo " "
echo "1- Trity (Best 34 tools)"
echo " "
echo "2- Lsript"
echo " "
echo "3- RED_HAWK"
echo " "
echo "4- Pureblood"
echo " "
echo "5- Wapiti"
echo " "


read target
echo " "
cd Tools
if [[ "$target" = 1 ]]
	then chmod +x enter2trity.sh
	./enter2trity.sh
	cd ..
elif [[ "$target" = 2 ]]
	then cd lscript
	l
	cd ..
elif [[ "$target" = 3 ]]
	then cd RED_HAWK
	php rhawk.php
	cd ..
elif [[ "$target" = 4 ]]
	then cd pureblood
	python pureblood.py
	cd ..
elif [[ "$target" = 5 ]]
	then cd wapiti
	echo "Enter URL"
	read url
	wapiti -u $url/
	cd ..

else echo "Not so good"
fi
cd ..
