General Info
Acesta este un proiect realziat in Pycharm 

Tehnologii folosite:
python

Setup
Pentru a rula acest proiect trebuie instalat local pycharm
https://www.jetbrains.com/pycharm/download/download-thanks.html?platform=mac&code=PCC
Dupa care cu ajutorul terminalului din pycharm si folosind pip instalam selenium

Project
In cadrul proiectului am creat o clasa TestUser
Am definit metodele setUP si tearDown care se scriu inaintea fiecarui test pe care il rulam
Am ales sa incep testarea pagini login, am gasit elementele in pagina web de care aveam nevoie si folosind "keys" am completat
campurile necesare pentru logare, am trimis si un user gresit pe care l-ma sters folosin "user clear"
In a doua pagina pe care am ales-o pentru testare am folosit ActionChains deoarece aveam un element hover iar acesta este folosit pentru 
actiuni de acest fel (drag and drop,etc)
In ultima pagina testata "Contact us" am ales formularul si anume lista in care se putea alege subiectul mesajului transmis, 
avand doua optiuni am ales sa folosesc select pentru a alege una dintre ele.







