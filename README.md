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

test_login_with_credentials:
Testul verifică funcționalitatea de conectare pe site-ul PrestaShop.
Navighează la site și da click pe linkul de conectare.
Introduce un nume de utilizator și o parolă, trimite formularul și așteaptă încărcarea paginii.
În cele din urmă, afirmă că „Your account” este prezent în sursa paginii, indicând o conectare reușită.

test_jeans_hover_menu:
Acest test demonstrează funcționalitatea de trecere cu mouse-ul și click pe un element de meniu drop-down.
Acesta navighează la site și trece mouse-ul peste elementul de meniu cu ID-ul „categoria-3”.
Odată ce elementul de meniu este vizibil, mută mouse-ul la un alt element de meniu cu ID „categoria-4” și dă clic pe el.
Testul afirmă că titlul paginii conține cuvântul „Jeans” pentru a verifica navigarea cu succes.

test_contact_subject_select:
Acest test validează selecția unui subiect de contact într-un formular de contact.
Acesta navighează la pagina de contact a site-ului web și afirmă că titlul paginii conține cuvântul „Contact”.
Localizează un elementul „id_contact” folosind clasa Select de la Selenium.
Testul selectează o opțiunea cu valoarea „1” și verifică dacă textul opțiunii selectate este „Webmaster”.






