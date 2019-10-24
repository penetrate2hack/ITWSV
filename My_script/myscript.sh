#! /bin/bash


echo "   							            "
echo "              ⚡⚡⚡  ⚓⚓⚓⚓  ⌛⌛⌛⌛ ⛔⛔⛔⛔⛔ ⛄⛄⛄⛄⛄⛄  " 
echo "             ⚡   ⚡  ⚓     ⚓ ⌛╔═══⌛═════⛔╗         ⛄"
echo "            ⚡    ⚡  ⚓     ⚓ ⌛║   ⌛     ⛔║         ⛄"
echo "        ╔══⚡⚡⚡⚡⚡⚡⚡⚓⚓⚓ ⌛⌛⌛⌛     ⛔║         ⛄"
echo "        ║ ⚡      ⚡╔═⚓═⚓══╗  ⌛║          ⛔║         ⛄"
echo "        ╚⚡═══════⚡╝ ⚓  ⚓ ║  ⌛║          ⛔║         ⛄"
echo "        ⚡        ⚡  ⚓   ⚓║  ⌛║          ⛔╚═════════⛄╗"
echo "       ⚡         ⚡  ⚓    ⚓⚓⚓║      ⛔⛔⛔⛔⛔      ⛄║"
echo "                             ╚════╝                        ║"
echo "						           ╚by ₳Ɽ₱ł₮ ₭Ⱨ₳Ɽ₵ⱧɆ    "
echo "							Combination of all the 
						popular scripts & tools"
echo ""
echo "Enter domain of your Target Below"
read target
echo " "
echo "Enter path of your output files example --> /root/Desktop/Project/Report"
read address


#7-dmitry
echo "Dmitry scan in progress-"
dmitry $target > $address/dmitry.txt
echo "Dmitry scanning done..."

#1-whois
echo "Whois in progress- "
whois $target > $address/whois.txt
echo "Whois scanning done..."

#2-dnswalk
echo "Dnswalk in progress- "
dnswalk $target. > $address/dnswalk.txt
echo "Dnswalk scanning done..."

#3-fierce
echo "Fierce in progress-"
fierce -dns $target > $address/fierce.txt
echo "Fierce scanning done..."

#4-DNSrecon
echo "DNSrecon-"
dnsrecon -d $target > $address/dnsrecon.txt
echo "DNSrecon scanning done..."

#5-DNSenum
echo "DNS Enum-"
dnsenum $target > $address/dnsenum.txt
echo "DNSenum scanning done..."

#6-nmap
echo "Nmap scan in progress-" 
nmap -v -A $target > $address/nmap.txt
echo "Nmap scanning done..."

#8-theharvester
echo "TheHarvester-"
theharvester -d $target -l 500 -b google  > $address/theharvester.txt
echo "TheHarvester scanning done..."

#9-Nikto
echo "Nikto in Progress-"
nikto -host https://$target > $address/nikto.txt
echo "Nikto scanning done..."

#10-LBD
echo "LBD scan in progress-"
lbd $target > $address/lbd.txt
echo "LBD scanning done..."

#11-SSLscan
echo "SSLscan in progress-"
sslscan $target > $address/sslscan.txt
echo "SSlscan scannning done"

#12-SSLyze
echo "SSLyze scan in progress-"
sslyze --regular $target > $address/sslyze.txt
echo "SSLyze scanning done..."

#13-whatweb
echo "Whatweb progress-"
whatweb $target > $address/whatweb.txt
echo "Whatweb scanning done..."

#14-automater
echo "Automater in progress-"
automater -V $target > $address/automater.txt
echo "Automater scanning done..."

#15-grabber
echo "Grabber in progress-"
cd Grabber
python grabber.py --bsql --url http://$target 
cd results
cat sql_GrabberAttacks.xml bsql_GrabberAttacks.xml xss_GrabberAttacks.xml  touchFiles.xml externalCalls.xml > ./grabber.txt
mv grabber.txt $address
cd ..
cd ..
echo "Grabber scanning done..."

#16-parsero
echo "Parsero in progress-"
cd Parsero
python3 parsero.py -u $target -sb > $address/parsero.txt
cd ..
echo "Parsero scanning done..."

#17-uniscan
echo "Uniscan in progress-"
uniscan -u https://$target -qwedsiogj > $address/uniscan.txt
echo "uniscan scanning done..."

#18-gobuster
#echo "Gobuster in progress-"
#cd gobuster
#gobuster -e -u http://$target/ -w /usr/share/wordlists/dirb/common.txt > $address/#gobuster.txt
#cd ..
#echo "gobuster scanning done..."

#19-metagoofil
echo "Metagoofil in progress-"
cd metagoofil
python metagoofil.py -d $target -t doc,pdf,xls,csv,txt -l 200 -n 50 -o metagoofiles -f metagoofil.html
mv metagoofil.html $address
cd ..
echo "metagoofil scanning done..."

#20-a2sv
echo "Update U2SV First"
cd a2sv
python a2sv.py -u 
echo "a2s v scan in progress-"
python a2sv.py -t $target > $address/a2sv.txt
echo "a2sv scanning done..."
cd ..

#21-wpscanner
echo "wpscanner in progress-"
wpscan --url http://$target --enumerate u --ignore-main-redirect> $address/wpscanner.txt
python wpscanner.py -s http://$target -n 20 >> $address/wpscanner.txt
echo "wpscanner scanning done..."

#22-droopscan
echo "Droopscan in progress-"
droopescan scan wordpress -u http://$target > $address/droopescan.txt
droopescan scan joomla -u http://$target >> $address/droopescan.txt
droopescan scan drupal -u http://$target >> $address/droopescan.txt
droopescan scan silverstripe -u http://$target >> $address/droopescan.txt
droopescan scan moodle -u http://$target >> $address/droopescan.txtq
echo "Droopscan scanning done..."

#23-WPSeku
echo "WPSeku in progress-"
cd WPSeku
python wpseku.py --target http://$target > $address/wpseku.txt
echo "WPSeku scanning done..."

#24-XssPy
echo "XssPy in progress-"
python XssPy.py -u $target -v > $address/XssPy.txt
echo "XssPy scanning done..."

#25-Spaghetti
echo "Spaghetti in progress-"
python Spaghetti/spaghetti.py --url http://$target --scan [0-5] > $address/spaghetti.txt
echo "Spaghetti scanning done..."

#26-Sublist3r
echo "Sublist3r in progress-"
dig -x $target
python sublist3r/sublist3r.py --domain $target > $address/sublist3r.txt
echo "Sublist3r scanning done..."

#27-WAFw00f
echo "WAFw00f in progress-"
wafw00f http://$target > $address/wafw00f.txt
echo "WAFw00f scanning done..."

#28-NSlookup
echo "NSlookup in progress-"
nslookup $target > $address/nslookup.txt
echo "nslookup scanning done..."

#29-Dirsearch
echo "Diresearch in progress-"
cd dirsearch
./dirsearch.py -u $target -e aspx,php > $address/dirsearchphp.txt
cd ..
echo "Dirsearch finished..."

#30-joomscan
echo "Joomscan in progress-"
cd joomscan
joomscan -u http://$target > $address/joomscan.txt
cd ..
echo "Joomscan scanning done..."

#31-keywords guessing for report
cd ..
cd Report
chmod +x keys
./keys

#Report
echo "Generating report-"
echo 'PCFET0NUWVBFIEhUTUw+CjwhLS0KIyBJbnRlcmdyYXRlZCBUb29sIEZvciBXZWIgU2VjdXJpdHkg
VnVsbmVyYWJpbGl0aWVzCiMgQnkgQXJwaXQgS2hhcmNoZQotLT4KPGh0bWw+CjxoZWFkPgo8dGl0
bGU+QXV0by1QZW50ZXN0IFJlcG9ydDwvdGl0bGU+CjxtZXRhIGNoYXJzZXQ9InV0Zi04IiAvPgo8
bWV0YSBuYW1lPSJ2aWV3cG9ydCIgY29udGVudD0id2lkdGg9ZGV2aWNlLXdpZHRoLCBpbml0aWFs
LXNjYWxlPTEiIC8+CjxsaW5rIHJlbD0ic3R5bGVzaGVldCIgaHJlZj0iYXNzZXRzL2Nzcy9tYWlu
LmNzcyIgLz4KPC9oZWFkPgo8Ym9keT4KCjxzZWN0aW9uIGlkPSJiYW5uZXIiPgo8aDI+PHN0cm9u
Zz5JbnRlcmdyYXRlZCBUb29sIEZvciBXZWIgU2VjdXJpdHkgVnVsbmVyYWJpbGl0aWVzPC9zdHJv
bmc+PC9oMj5ieTxwPjxzdHJvbmc+PGk+QXJwaXQgS2hhcmNoZTwvaT48L3N0cm9uZz48L3A+Cjx1
bCBjbGFzcz0iYWN0aW9ucyI+CjxsaT48YSBocmVmPSJodHRwczovL2dpdGh1Yi5jb20vcGVuZXRy
YXRlMmhhY2svSVRXU1YiIGNsYXNzPSJidXR0b24gc3BlY2lhbCI+R2l0aHViPC9hPjwvbGk+Cjxs
aT48YSBocmVmPSJodHRwczovL2luLmxpbmtlZGluLmNvbS8iIGNsYXNzPSJidXR0b24gc3BlY2lh
bCI+TGlua2VkaW48L2E+PC9saT4KPGxpPjxhIGhyZWY9Im1haWx0bzpwZW5ldHJhdGUyaGFja0Bo
b3RtYWlsLmNvbSIgY2xhc3M9ImJ1dHRvbiBzcGVjaWFsIj5FbWFpbDwvYT48L2xpPgo8L3VsPgo8
L3NlY3Rpb24+CjxjZW50ZXI+Cjxicj48aHI+PHN0cm9uZz5SRVBPUlQ8L3N0cm9uZz48YnI+PGJy
Pgo8aWZyYW1lIHNyYz0iY2hlY2sudHh0IiBoZWlnaHQ9IjEwMDAiIHdpZHRoPSIxMDAwIj48L2lm
cmFtZT4gPGJyPgo8aHI+Cjx1bCBjbGFzcz0iYWN0aW9ucyI+CjxsaT48YSBocmVmPSJjb21wbGV0
ZXJlcG9ydC5odG1sIiBjbGFzcz0iYnV0dG9uIHNwZWNpYWwiPkNPTVBMRVRFIFJFUE9SVDwvYT48
L2xpPgo8L3VsPgo8L2NlbnRlcj4KPGZvb3RlciBpZD0iZm9vdGVyIj4KPGRpdiBjbGFzcz0iY29w
eXJpZ2h0Ij4KJmNvcHk7IEFycGl0IEtoYXJjaGU8L2E+Lgo8L2Rpdj4KPC9mb290ZXI+Cgo8c2Ny
aXB0IHNyYz0iYXNzZXRzL2pzL2pxdWVyeS5taW4uanMiPjwvc2NyaXB0Pgo8c2NyaXB0IHNyYz0i
YXNzZXRzL2pzL3NrZWwubWluLmpzIj48L3NjcmlwdD4KPHNjcmlwdCBzcmM9ImFzc2V0cy9qcy91
dGlsLmpzIj48L3NjcmlwdD4KPHNjcmlwdCBzcmM9ImFzc2V0cy9qcy9tYWluLmpzIj48L3Njcmlw
dD4KCjwvYm9keT4KPC9odG1sPgo='| base64 --decode > $address/report.html

echo 'PCFET0NUWVBFIEhUTUw+CjwhLS0KIyBJbnRlcmdyYXRlZCBUb29sIEZvciBXZWIgU2VjdXJpdHkg
VnVsbmVyYWJpbGl0aWVzCiMgQnkgQXJwaXQgS2hhcmNoZQotLT4KPGh0bWw+Cgo8aGVhZD4KPHRp
dGxlPkF1dG8tUGVudGVzdCBSZXBvcnQ8L3RpdGxlPgo8bWV0YSBjaGFyc2V0PSJ1dGYtOCIgLz4K
PG1ldGEgbmFtZT0idmlld3BvcnQiIGNvbnRlbnQ9IndpZHRoPWRldmljZS13aWR0aCwgaW5pdGlh
bC1zY2FsZT0xIiAvPgo8bGluayByZWw9InN0eWxlc2hlZXQiIGhyZWY9ImFzc2V0cy9jc3MvbWFp
bi5jc3MiIC8+CjwvaGVhZD4KPGJvZHkgbSxib3gtc2l6aW5nOiBib3JkZXItYm94Oz4KCjxzZWN0
aW9uIGlkPSJiYW5uZXIiPgo8aDI+PHN0cm9uZz5JbnRlcmdyYXRlZCBUb29sIEZvciBXZWIgU2Vj
dXJpdHkgVnVsbmVyYWJpbGl0aWVzPC9zdHJvbmc+PC9oMj5ieTxwPjxzdHJvbmc+PGk+QXJwaXQg
S2hhcmNoZTwvaT48L3N0cm9uZz48L3A+Cjx1bCBjbGFzcz0iYWN0aW9ucyI+CjxsaT48YSBocmVm
PSJodHRwczovL2dpdGh1Yi5jb20vcGVuZXRyYXRlMmhhY2svSVRXU1YiIGNsYXNzPSJidXR0b24g
c3BlY2lhbCI+R2l0aHViPC9hPjwvbGk+CjxsaT48YSBocmVmPSJodHRwczovL2luLmxpbmtlZGlu
LmNvbS8iIGNsYXNzPSJidXR0b24gc3BlY2lhbCI+TGlua2VkaW48L2E+PC9saT4KPGxpPjxhIGhy
ZWY9Im1haWx0bzpwZW5ldHJhdGUyaGFja0Bob3RtYWlsLmNvbSIgY2xhc3M9ImJ1dHRvbiBzcGVj
aWFsIj5FbWFpbDwvYT48L2xpPgo8L3VsPgo8L3NlY3Rpb24+CjxjZW50ZXIgbSxib3gtc2l6aW5n
OiBib3JkZXItYm94Pgo8YSBocmVmPSJodHRwczovL3d3dy5jeWJlcnByYXRpYmhhLmNvbS9ibG9n
L3VzaW5nLXdob2lzLWEtY29tbWFuZC1mb3ItaW5mb3JtYXRpb24tZ2F0aGVyaW5nLyI+PGhyPjxz
dHJvbmc+V2hvaXM8L2E+IE91dHB1dHM8L3N0cm9uZz48YnI+PGJyPgo8aWZyYW1lIHNyYz0id2hv
aXMudHh0IiBoZWlnaHQ9IjYwMCIgd2lkdGg9IjEwMDAiPjwvaWZyYW1lPiA8YnI+Cjxocj4KPGEg
aHJlZj0iaHR0cHM6Ly90b29scy5rYWxpLm9yZy9pbmZvcm1hdGlvbi1nYXRoZXJpbmcvbm1hcCI+
PGhyPjxzdHJvbmc+Tm1hcDwvYT4gT3V0cHV0PC9zdHJvbmc+PGJyPjxicj4KPGlmcmFtZSBzcmM9
Im5tYXAudHh0IiBoZWlnaHQ9IjYwMCIgd2lkdGg9IjEwMDAiPjwvaWZyYW1lPiA8YnI+Cjxocj4K
PGEgaHJlZj0iaHR0cHM6Ly90b29scy5rYWxpLm9yZy9pbmZvcm1hdGlvbi1nYXRoZXJpbmcvZmll
cmNlIj48aHI+PHN0cm9uZz5GaWVyY2U8L2E+IE91dHB1dDwvc3Ryb25nPjxicj48YnI+CjxpZnJh
bWUgc3JjPSJmaWVyY2UudHh0IiBoZWlnaHQ9IjQ4MCIgd2lkdGg9IjEwMDAiPjwvaWZyYW1lPiA8
YnI+Cjxocj4KPGEgaHJlZj0iaHR0cHM6Ly90b29scy5rYWxpLm9yZy9pbmZvcm1hdGlvbi1nYXRo
ZXJpbmcvZG5zd2FsayI+PGhyPjxzdHJvbmc+RE5TV2FsazwvYT4gT3V0cHV0PC9zdHJvbmc+PGJy
Pjxicj4KPGlmcmFtZSBzcmM9ImRuc3dhbGsudHh0IiBoZWlnaHQ9IjEwMCIgd2lkdGg9IjEwMDAi
PjwvaWZyYW1lPiA8YnI+Cjxocj4KPGEgaHJlZj0iaHR0cHM6Ly90b29scy5rYWxpLm9yZy9pbmZv
cm1hdGlvbi1nYXRoZXJpbmcvZG5zcmVjb24iPjxocj48c3Ryb25nPkROU3JlY29uPC9hPiBPdXRw
dXQ8L3N0cm9uZz48YnI+PGJyPgo8aWZyYW1lIHNyYz0iZG5zcmVjb24udHh0IiBoZWlnaHQ9IjMw
MCIgd2lkdGg9IjEwMDAiPjwvaWZyYW1lPiA8YnI+Cjxocj4KPGEgaHJlZj0iaHR0cHM6Ly90b29s
cy5rYWxpLm9yZy9pbmZvcm1hdGlvbi1nYXRoZXJpbmcvbm1hcCI+PGhyPjxzdHJvbmc+RE5TZW51
bTwvYT4gT3V0cHV0PC9zdHJvbmc+PGJyPjxicj4KPGlmcmFtZSBzcmM9ImRuc2VudW0udHh0IiBo
ZWlnaHQ9IjYwMCIgd2lkdGg9IjEwMDAiPjwvaWZyYW1lPiA8YnI+Cjxocj4KPGEgaHJlZj0iaHR0
cHM6Ly90b29scy5rYWxpLm9yZy9pbmZvcm1hdGlvbi1nYXRoZXJpbmcvZG1pdHJ5Ij48aHI+PHN0
cm9uZz5EbWl0cnk8L2E+IE91dHB1dDwvc3Ryb25nPjxicj48YnI+CjxpZnJhbWUgc3JjPSJkbWl0
cnkudHh0IiBoZWlnaHQ9IjYwMCIgd2lkdGg9IjEwMDAiPjwvaWZyYW1lPiA8YnI+Cjxocj4KPGEg
aHJlZj0iaHR0cHM6Ly90b29scy5rYWxpLm9yZy9pbmZvcm1hdGlvbi1nYXRoZXJpbmcvdGhlaGFy
dmVzdGVyIj48aHI+PHN0cm9uZz50aGVIYXJ2ZXN0ZXI8L2E+IE91dHB1dDwvc3Ryb25nPjxicj48
YnI+CjxpZnJhbWUgc3JjPSJ0aGVoYXJ2ZXN0ZXIudHh0IiBoZWlnaHQ9IjYwMCIgd2lkdGg9IjEw
MDAiPjwvaWZyYW1lPiA8YnI+Cjxocj4KPGEgaHJlZj0iaHR0cHM6Ly90b29scy5rYWxpLm9yZy9p
bmZvcm1hdGlvbi1nYXRoZXJpbmcvbGJkIj48aHI+PHN0cm9uZz5MQkQ8L2E+IE91dHB1dDwvc3Ry
b25nPjxicj48YnI+CjxpZnJhbWUgc3JjPSJsYmQudHh0IiBoZWlnaHQ9IjMwMCIgd2lkdGg9IjEw
MDAiPjwvaWZyYW1lPiA8YnI+Cjxocj4KPGEgaHJlZj0iaHR0cHM6Ly90b29scy5rYWxpLm9yZy9p
bmZvcm1hdGlvbi1nYXRoZXJpbmcvbmlrdG8iPjxocj48c3Ryb25nPk5pa3RvPC9hPiBPdXRwdXQ8
L3N0cm9uZz48YnI+PGJyPgo8aWZyYW1lIHNyYz0ibmlrdG8udHh0IiBoZWlnaHQ9IjYwMCIgd2lk
dGg9IjEwMDAiPjwvaWZyYW1lPiA8YnI+Cjxocj4KPGEgaHJlZj0iaHR0cHM6Ly90b29scy5rYWxp
Lm9yZy93ZWItYXBwbGljYXRpb25zL3doYXR3ZWIiPjxocj48c3Ryb25nPldoYXR3ZWI8L2E+IE91
dHB1dDwvc3Ryb25nPjxicj48YnI+CjxpZnJhbWUgc3JjPSJ3aGF0d2ViLnR4dCIgaGVpZ2h0PSIz
MDAiIHdpZHRoPSIxMDAwIj48L2lmcmFtZT4gPGJyPgo8aHI+CjxhIGhyZWY9Imh0dHBzOi8vdG9v
bHMua2FsaS5vcmcvaW5mb3JtYXRpb24tZ2F0aGVyaW5nL2F1dG9tYXRlciI+PGhyPjxzdHJvbmc+
QXV0b21hdGVyPC9hPiBPdXRwdXQ8L3N0cm9uZz48YnI+PGJyPgo8aWZyYW1lIHNyYz0iYXV0b21h
dGVyLnR4dCIgaGVpZ2h0PSI0MDAiIHdpZHRoPSIxMDAwIj48L2lmcmFtZT4gPGJyPgo8aHI+Cjxh
IGhyZWY9Imh0dHBzOi8vdG9vbHMua2FsaS5vcmcvd2ViLWFwcGxpY2F0aW9ucy9ncmFiYmVyIj48
aHI+PHN0cm9uZz5HcmFiYmVyPC9hPiBPdXRwdXQ8L3N0cm9uZz48YnI+PGJyPgo8aWZyYW1lIHNy
Yz0iZ3JhYmJlci50eHQiIGhlaWdodD0iNjAwIiB3aWR0aD0iMTAwMCI+PC9pZnJhbWU+IDxicj4K
PGhyPgo8YSBocmVmPSJodHRwczovL3Rvb2xzLmthbGkub3JnL2luZm9ybWF0aW9uLWdhdGhlcmlu
Zy9wYXJzZXJvIj48aHI+PHN0cm9uZz5QYXJzZXJvPC9hPiBPdXRwdXQ8L3N0cm9uZz48YnI+PGJy
Pgo8aWZyYW1lIHNyYz0icGFyc2Vyby50eHQiIGhlaWdodD0iMzQwIiB3aWR0aD0iMTAwMCI+PC9p
ZnJhbWU+IDxicj4KPGhyPgo8YSBocmVmPSJodHRwczovL3Rvb2xzLmthbGkub3JnL3dlYi1hcHBs
aWNhdGlvbnMvdW5pc2NhbiI+PGhyPjxzdHJvbmc+VW5pc2NhbjwvYT4gT3V0cHV0PC9zdHJvbmc+
PGJyPjxicj4KPGlmcmFtZSBzcmM9InVuaXNjYW4udHh0IiBoZWlnaHQ9IjYwMCIgd2lkdGg9IjEw
MDAiPjwvaWZyYW1lPiA8YnI+Cjxocj4KPGEgaHJlZj0iaHR0cHM6Ly9naXRodWIuY29tL2hhaHd1
bC9hMnN2Ij48aHI+PHN0cm9uZz5hMnN2PC9hPiBPdXRwdXQ8L3N0cm9uZz48YnI+PGJyPgo8aWZy
YW1lIHNyYz0iYTJzdi50eHQiIGhlaWdodD0iNjAwIiB3aWR0aD0iMTAwMCI+PC9pZnJhbWU+IDxi
cj4KPGhyPgo8YSBocmVmPSJodHRwczovL3Rvb2xzLmthbGkub3JnL2luZm9ybWF0aW9uLWdhdGhl
cmluZy9tZXRhZ29vZmlsIj48aHI+PHN0cm9uZz5NZXRhZ29vZmlsPC9hPiBPdXRwdXQ8L3N0cm9u
Zz48YnI+PGJyPgo8aWZyYW1lIHNyYz0ibWV0YWdvb2ZpbC5odG1sIiBoZWlnaHQ9IjYwMCIgd2lk
dGg9IjEwMDAiPjwvaWZyYW1lPiA8YnI+Cjxocj4KPGEgaHJlZj0iaHR0cHM6Ly90b29scy5rYWxp
Lm9yZy93ZWItYXBwbGljYXRpb25zL3dwc2NhbiI+PGhyPjxzdHJvbmc+V1BTY2FubmVyPC9hPiBP
dXRwdXQ8L3N0cm9uZz48YnI+PGJyPgo8aWZyYW1lIHNyYz0id3BzY2FubmVyLnR4dCIgaGVpZ2h0
PSI2MDAiIHdpZHRoPSIxMDAwIj48L2lmcmFtZT4gPGJyPgo8aHI+CjxhIGhyZWY9Imh0dHBzOi8v
Z2l0aHViLmNvbS9tNGxsMGsvV1BTZWt1Ij48aHI+PHN0cm9uZz5XUFNla3U8L2E+IE91dHB1dDwv
c3Ryb25nPjxicj48YnI+CjxpZnJhbWUgc3JjPSJ3cHNla3UudHh0IiBoZWlnaHQ9IjYwMCIgd2lk
dGg9IjEwMDAiPjwvaWZyYW1lPiA8YnI+Cjxocj4KPGEgaHJlZj0iaHR0cHM6Ly9naXRodWIuY29t
L2ZhaXphbm4yNC9Yc3NQeSI+PGhyPjxzdHJvbmc+WHNzUHk8L2E+IE91dHB1dDwvc3Ryb25nPjxi
cj48YnI+CjxpZnJhbWUgc3JjPSJYc3NQeS50eHQiIGhlaWdodD0iNDAwIiB3aWR0aD0iMTAwMCI+
PC9pZnJhbWU+IDxicj4KPGhyPgo8YSBocmVmPSJodHRwOi8vd3d3LnRlY2h0cmljay5pbi9kZXNj
cmlwdGlvbi80NTYzLXdlYi1hcHBsaWNhdGlvbi1zZWN1cml0eS1zY2FubmVyLWluLWthbGktbGlu
dXgtc3BhZ2hldHRpIj48aHI+PHN0cm9uZz5TcGFnaGV0dGk8L2E+IE91dHB1dDwvc3Ryb25nPjxi
cj48YnI+CjxpZnJhbWUgc3JjPSJzcGFnaGV0dGkudHh0IiBoZWlnaHQ9IjM1MCIgd2lkdGg9IjEw
MDAiPjwvaWZyYW1lPiA8YnI+Cjxocj4KPGEgaHJlZj0iaHR0cHM6Ly90b29scy5rYWxpLm9yZy9p
bmZvcm1hdGlvbi1nYXRoZXJpbmcvc3VibGlzdDNyIj48aHI+PHN0cm9uZz5TdWJsaXN0M3I8L2E+
IE91dHB1dDwvc3Ryb25nPjxicj48YnI+CjxpZnJhbWUgc3JjPSJzdWJsaXN0M3IudHh0IiBoZWln
aHQ9IjUwMCIgd2lkdGg9IjEwMDAiPjwvaWZyYW1lPiA8YnI+Cjxocj4KPGEgaHJlZj0iaHR0cHM6
Ly9naXRodWIuY29tL0VuYWJsZVNlY3VyaXR5L3dhZncwMGYiPjxocj48c3Ryb25nPldBRncwMGY8
L2E+IE91dHB1dDwvc3Ryb25nPjxicj48YnI+CjxpZnJhbWUgc3JjPSJ3YWZ3MDBmLnR4dCIgaGVp
Z2h0PSIyOTAiIHdpZHRoPSIxMDAwIj48L2lmcmFtZT4gPGJyPgo8aHI+CjxhIGhyZWY9Imh0dHBz
Oi8vd3d3LmdlZWtzZm9yZ2Vla3Mub3JnL25zbG9va3VwLWNvbW1hbmQtaW4tbGludXgtd2l0aC1l
eGFtcGxlcy8iPjxocj48c3Ryb25nPk5TbG9va3VwPC9hPiBPdXRwdXQ8L3N0cm9uZz48YnI+PGJy
Pgo8aWZyYW1lIHNyYz0ibnNsb29rdXAudHh0IiBoZWlnaHQ9IjEzMCIgd2lkdGg9IjEwMDAiPjwv
aWZyYW1lPiA8YnI+Cjxocj4KPGEgaHJlZj0iaHR0cHM6Ly90b29scy5rYWxpLm9yZy9pbmZvcm1h
dGlvbi1nYXRoZXJpbmcvdGxzc2xlZCI+PGhyPjxzdHJvbmc+U1NMY2FuPC9hPiBPdXRwdXQ8L3N0
cm9uZz48YnI+PGJyPgo8aWZyYW1lIHNyYz0ic3Nsc2Nhbi50eHQiIGhlaWdodD0iNjAwIiB3aWR0
aD0iMTAwMCI+PC9pZnJhbWU+IDxicj4KPGhyPgo8YSBocmVmPSJodHRwczovL3Rvb2xzLmthbGku
b3JnL2luZm9ybWF0aW9uLWdhdGhlcmluZy9zc2x5emUiPjxocj48c3Ryb25nPlNTTHl6ZTwvYT4g
T3V0cHV0PC9zdHJvbmc+PGJyPjxicj4KPGlmcmFtZSBzcmM9InNzbHl6ZS50eHQiIGhlaWdodD0i
NjAwIiB3aWR0aD0iMTAwMCI+PC9pZnJhbWU+IDxicj4KPGhyPgo8YSBocmVmPSJodHRwczovL3d3
dy5rYWxpbGludXguaW4vMjAxOC8xMi9kaXJzZWFyY2guaHRtbCI+PGhyPjxzdHJvbmc+RGlyc2Vh
cmNoPC9hPiBPdXRwdXQ8L3N0cm9uZz48YnI+PGJyPgo8aWZyYW1lIHNyYz0iZGlyc2VhcmNocGhw
LnR4dCIgaGVpZ2h0PSI2MDAiIHdpZHRoPSIxMDAwIj48L2lmcmFtZT4gPGJyPgo8aHI+CjxhIGhy
ZWY9Imh0dHBzOi8vZW4ua2FsaS50b29scy9hbGwvP3Rvb2w9MzcxIj48aHI+PHN0cm9uZz5Ecm9v
cGVzY2FuPC9hPiBPdXRwdXQ8L3N0cm9uZz48YnI+PGJyPgo8aWZyYW1lIHNyYz0iZHJvb3Blc2Nh
bi50eHQiIGhlaWdodD0iMjUwIiB3aWR0aD0iMTAwMCI+PC9pZnJhbWU+IDxicj4KPGhyPgo8YSBo
cmVmPSJodHRwczovL3Rvb2xzLmthbGkub3JnL3dlYi1hcHBsaWNhdGlvbnMvam9vbXNjYW4iPjxo
cj48c3Ryb25nPkpvb21zY2FuPC9hPiBPdXRwdXQ8L3N0cm9uZz48YnI+PGJyPgo8aWZyYW1lIHNy
Yz0iam9vbXNjYW4udHh0IiBoZWlnaHQ9IjQwMCIgd2lkdGg9IjEwMDAiPjwvaWZyYW1lPiA8YnI+
Cjxocj4KPC9jZW50ZXI+Cjxmb290ZXIgaWQ9ImZvb3RlciI+CjxkaXYgY2xhc3M9ImNvcHlyaWdo
dCI+CiZjb3B5OyBBcnBpdCBLaGFyY2hlPC9hPi4KPC9kaXY+CjwvZm9vdGVyPgoKPHNjcmlwdCBz
cmM9ImFzc2V0cy9qcy9qcXVlcnkubWluLmpzIj48L3NjcmlwdD4KPHNjcmlwdCBzcmM9ImFzc2V0
cy9qcy9za2VsLm1pbi5qcyI+PC9zY3JpcHQ+CjxzY3JpcHQgc3JjPSJhc3NldHMvanMvdXRpbC5q
cyI+PC9zY3JpcHQ+CjxzY3JpcHQgc3JjPSJhc3NldHMvanMvbWFpbi5qcyI+PC9zY3JpcHQ+Cgo8
L2JvZHk+CjwvaHRtbD4K'| base64 --decode > $address/completereport.html


echo "Report generated and saved at /root/Desktop/Project/Report "
echo "Great day ahead!!!"



