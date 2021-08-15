import requests
import os
from datetime import datetime
import re
from colorama import Fore, Back, Style
requests.packages.urllib3.disable_warnings()


fr  =   Fore.RED											
fc  =   Fore.CYAN											
fw  =   Fore.WHITE											
fg  =   Fore.GREEN
fy	=	Fore.YELLOW	
fb	=	Fore.BLUE										
sd  =   Style.DIM											
sn  =   Style.NORMAL										
sb  =   Style.BRIGHT

def scan():

	website = input('{}Domain to scan -> '.format(fy))

	if '://' not in website:
		target = 'http://'+website
	else:
		target = website

	kepala = {
	"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
	"accept-encoding": "gzip, deflate, br",
	"accept-language": "en,en-US;q=0.9",
	"cache-control": "max-age=0",
	"dnt": "1",
	"sec-ch-ua-mobile": "?0",
	"sec-fetch-dest": "document",
	"sec-fetch-mode": "navigate",
	"sec-fetch-site": "none",
	"sec-fetch-user": "?1",
	"upgrade-insecure-requests": "1",
	"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
	}

	config = {
	"/.wp-config.php.swp",
	"/wp-config.inc",
	"/wp-config.old",
	"/wp-config.txt",
	"/wp-config.html",
	"/wp-config.php.bak",
	"/wp-config.php.dist",
	"/wp-config.php.inc",
	"/wp-config.php.old",
	"/wp-config.php.save",
	"/wp-config.php.swp",
	"/wp-config.php.txt",
	"/wp-config.php.zip",
	"/wp-config.php.html",
	"/wp-config.php~",
	"/wp-admin/.wp-config.php.swp",
	"/wp-admin/wp-config.inc",
	"/wp-admin/wp-config.old",
	"/wp-admin/wp-config.txt",
	"/wp-admin/wp-config.html",
	"/wp-admin/wp-config.php.bak",
	"/wp-admin/wp-config.php.dist",
	"/wp-admin/wp-config.php.inc",
	"/wp-admin/wp-config.php.old",
	"/wp-admin/wp-config.php.save",
	"/wp-admin/wp-config.php.swp",
	"/wp-admin/wp-config.php.txt",
	"/wp-admin/wp-config.php.zip",
	"/wp-admin/wp-config.php.html",
	"/wp-admin/wp-config.php~",
	"/wp-content/.wp-config.php.swp",
	"/wp-content/wp-config.inc",
	"/wp-content/wp-config.old",
	"/wp-content/wp-config.txt",
	"/wp-content/wp-config.html",
	"/wp-content/wp-config.php.bak",
	"/wp-content/wp-config.php.dist",
	"/wp-content/wp-config.php.inc",
	"/wp-content/wp-config.php.old",
	"/wp-content/wp-config.php.save",
	"/wp-content/wp-config.php.swp",
	"/wp-content/wp-config.php.txt",
	"/wp-content/wp-config.php.zip",
	"/wp-content/wp-config.php.html",
	"/wp-content/wp-config.php~",
	"/wp-includes/.wp-config.php.swp",
	"/wp-includes/wp-config.inc",
	"/wp-includes/wp-config.old",
	"/wp-includes/wp-config.txt",
	"/wp-includes/wp-config.html",
	"/wp-includes/wp-config.php.bak",
	"/wp-includes/wp-config.php.dist",
	"/wp-includes/wp-config.php.inc",
	"/wp-includes/wp-config.php.old",
	"/wp-includes/wp-config.php.save",
	"/wp-includes/wp-config.php.swp",
	"/wp-includes/wp-config.php.txt",
	"/wp-includes/wp-config.php.zip",
	"/wp-includes/wp-config.php.html",
	"/wp-includes/wp-config.php~"
	}

	log = {
	'/debug.log',
	'/wp-content/debug.log',
	'/wp-admin/debug.log',
	'/wp-includes/debug.log'
	}

	user = {
	'/wp-json/wp/v2/users',
	'/?rest_route=/wp/v2/users'
	}

	date = datetime.now()
	tanggal = date.strftime("%d_%m_%Y %H_%M_%S")

	#Denial Of Service
	try:
		r1 = requests.get('{}/wp-admin/load-styles.php?&load=common'.format(target), headers=kepala, verify=False)

		if r1.status_code == 200:
			print('{}[INFO] {}{} {} -> OK! Denial of Service in load-styles.php'.format(fc, fw, target, fg))
			open('{}.txt'.format(tanggal), 'a').write('#Denial of Service in load-styles.php#'+'\n'+target+'/wp-admin/load-styles.php?&load=common'+'\n'+'\n')
		elif 'auto-generated' in r1.text:
			print('{}[INFO] {}{} {} -> OK! Denial of Service in load-styles.php'.format(fc, fw, target, fg))
			open('{}.txt'.format(tanggal), 'a').write('#Denial of Service in load-styles.php#'+'\n'+target+'/wp-admin/load-styles.php?&load=common'+'\n'+'\n')
		else:
			print('{}[INFO] {}{} {} -> Not Vuln Denial of Service in load-styles.php'.format(fc, fw, target, fr))

	except:
		print('{}[INFO] {}{} {} -> Not Vuln Denial of Service in load-styles.php'.format(fc, fw, target, fr))

	try:
		r2 = requests.get('{}/wp-admin/load-scripts.php?load=react'.format(target), headers=kepala, verify=False)

		if r2.status_code == 200:
			print('{}[INFO] {}{} {} -> OK! Denial of Serice in load-scripts.php'.format(fc, fw, target, fg))
			open('{}.txt'.format(tanggal), 'a').write('#Denial of Service in load-scripts.php#'+'\n'+target+'/wp-admin/load-scripts.php?load=react'+'\n'+'\n')
		elif 'react.production.min.js' in r2.text:
			print('{}[INFO] {}{} {} -> OK! Denial of Serice in load-scripts.php'.format(fc, fw, target, fg))
			open('{}.txt'.format(tanggal), 'a').write('#Denial of Service in load-scripts.php#'+'\n'+target+'/wp-admin/load-scripts.php?load=react'+'\n'+'\n')
		else:
			print('{}[INFO] {}{} {} -> Not Vuln Denial of Service in load-scripts.php'.format(fc, fw, target, fr))

	except:
		print('{}[INFO] {}{} {} -> Not Vuln Denial of Service in load-scripts.php'.format(fc, fw, target, fr))



	# Logs file exposed

	for a in log:
		logs = a.strip()

	try:
		r3 = requests.get('{}{}'.format(target, logs), headers=kepala, verify=False)

		if r3.status_code == 200:
			print('{}[INFO] {}{} {} -> OK! Logs file found!'.format(fc, fw, target, fg))
			open('{}.txt'.format(tanggal), 'a').write('#Exposed Logs file#'+'\n'+target+logs+'\n'+'\n')
		else:
			print('{}[INFO] {}{} {} -> Not found Logs file'.format(fc, fw, target, fr))

	except:
		print('{}[INFO] {}{} {} -> Not found Logs file'.format(fc, fw, target, fr))



	# Backup wp-config exposed

	for b in config:
		configs = b.strip()

	try:
		r4 = requests.get('{}{}'.format(target, configs), headers=kepala, verify=False)

		if r4.status_code == 200:
			print('{}[INFO] {}{} {} -> OK! Backup WP-Config found!'.format(fc, fw, target, fg))
			open('{}.txt'.format(tanggal), 'a').write('#Exposed Backup WP-Config file#'+'\n'+target+configs+'\n'+'\n')
		else:
			print('{}[INFO] {}{} {} -> Not found Backup WP-Config'.format(fc, fw, target, fr))
	
	except:
		print('{}[INFO] {}{} {} -> Not found Backup WP-Config'.format(fc, fw, target, fr))



	# Information disclosure wordpress username

	for c in user:
		users = c.strip()

	try:
		r5 = requests.get('{}{}'.format(target, users), headers=kepala, verify=False)

		if r5.status_code == 200:
			print('{}[INFO] {}{} {} -> OK! Users Disclosure'.format(fc, fw, target, fg))
			open('{}.txt'.format(tanggal), 'a').write('#Information Disclosure Username#'+'\n'+target+users+'\n'+'\n')
		elif '"id"' in r5.text:
			print('{}[INFO] {}{} {} -> OK! Users Disclosure'.format(fc, fw, target, fg))
			open('{}.txt'.format(tanggal), 'a').write('#Information Disclosure Username#'+'\n'+target+users+'\n'+'\n')
		else:
			print('{}[INFO] {}{} {} -> Not found Users Disclosure'.format(fc, fw, target, fr))
	
	except:
		print('{}[INFO] {}{} {} -> Not found Users Disclosure'.format(fc, fw, target, fr))



	# Bruteforce vulnerability

	try:
		r6 = requests.get('{}/?author=1'.format(target), headers=kepala, verify=False)
		regex1 = re.findall('/author/(.*?)/feed/', r6.text)

		for gex1 in regex1:
			ex1 = gex1

		datalogin = {
		"log": ex1,
		"pwd": "test",
		"wp-submit": "Log In",
		"redirect_to": target+"/wp-admin/",
		"testcookie": "1"
		}

		r7 = requests.post('{}/wp-login.php'.format(target), headers=kepala, data=datalogin, verify=False)

		if 'Lost your password?' in r7.text:
			print('{}[INFO] {}{} {} -> OK! Vuln Wordpress Bruteforce, with username : {}{}'.format(fc, fw, target, fg, fy, ex1))
			open('{}.txt'.format(tanggal), 'a').write('#Wordpress Bruteforce#'+'\n'+target+'/wp-login.php'+'\n'+'Username : '+ex1+'\n'+'\n')
		else:
			print('{}[INFO] {}{} {} -> Not Vuln Wordpress Bruteforce'.format(fc, fw, target, fr))

	except:
		print('{}[INFO] {}{} {} -> Not Vuln Wordpress Bruteforce'.format(fc, fw, target, fr))



	# XSPA Vulnerability

	try:
		r8 = requests.post('{}/xmlrpc.php'.format(target), headers=kepala, verify=False)

		if '<name>faultCode</name>' in r8.text:
			print('{}[INFO] {}{} {} -> OK! High possibility XSPA bug found!'.format(fc, fw, target, fg))
			open('{}.txt'.format(tanggal), 'a').write('#XSPA Vulnerabilityl#'+'\n'+target+'/xmlrpc.php'+'\n'+'\n')
		else:
			print('{}[INFO] {}{} {} -> XSPA Vulnerability not found'.format(fc, fw, target, fr))
	
	except:
		print('{}[INFO] {}{} {} -> XSPA Vulnerability not found'.format(fc, fw, target, fr))



def banner():
	print("""


$$$$$$$\  $$\                     $$\                           
$$  __$$\ \__|                    $$ |                          
$$ |  $$ |$$\  $$$$$$$\  $$$$$$\  $$ |  $$\  $$$$$$\  $$$$$$$\  
$$ |  $$ |$$ |$$  _____|$$  __$$\ $$ | $$  |$$  __$$\ $$  __$$\ 
$$ |  $$ |$$ |\$$$$$$\  $$$$$$$$ |$$$$$$  / $$$$$$$$ |$$ |  $$ |
$$ |  $$ |$$ | \____$$\ $$   ____|$$  _$$<  $$   ____|$$ |  $$ |
$$$$$$$  |$$ |$$$$$$$  |\$$$$$$$\ $$ | \$$\ \$$$$$$$\ $$ |  $$ |
\_______/ \__|\_______/  \_______|\__|  \__| \_______|\__|  \__|
                                                                                                             
	Wordpress Common Vulnerability Scanner v.1.0

Author : Abdi Pranata
Contact : sinon@tatsumi-crew.net

Thanks to : Muhammad Daffa & Zekkel AR

""")


if __name__ == "__main__":
	os.system('cls' if os.name == 'nt' else 'clear')
	banner()
	scan()
