Prezentare a proiectului de testare:
În cadrul acestui proiect de testare, am folosit limbajul de programare Python și framework-ul Selenium pentru a automatiza testele pe platforma PrestaShop. Scopul proiectului a fost să verificăm funcționalitatea și integritatea aplicației web, identificând eventuale erori sau probleme care ar putea afecta experiența utilizatorilor.
Structura proiectului:
* 		Am creat un modul Python denumit "Automation" care conține clasele de test și alte funcții utile pentru testare.
* 		Am utilizat framework-ul unittest pentru a defini și executa testele automate.
* 		Am folosit biblioteca Selenium pentru a interacționa cu elementele paginilor web și a efectua acțiuni de testare.
Testele efectuate:
* 		Testul "test_login_with_credentials" a verificat funcționalitatea de autentificare a utilizatorului, încercând să se autentifice cu diferite combinații de email și parolă și verificând rezultatul.
* 		Testul "test_jeans_hover_menu" a testat funcționalitatea de hover pe meniul "Jeans" și selectarea opțiunii corespunzătoare.
* 		Testul "test_contact_subject_select" a verificat corectitudinea selecției subiectului de contact în pagina de contact.
*     Testul "test_search_product" a verificat funcționalitatea motorului de cautarea search
*     Testul "test_add_to_cart" a verificat funcționalitatea pagini unui produs și selectarea opțiuniilor dorite.
*     Testul "test_sort_by" a verificat funcționalitatea butonului de sortare
*     Testul "test_filter" a verificat funcționalitate a filtrului filtrând prin categorie și preț un produs.
*     Testul "test_change_language" verificat funcționalitatea modificările limbei din engleză în română.
*     Testul "test_next_page" a verificat funcționalitatea scroll-ul pagini și butonul next.
*     Testul "test_quick_view" a verificat funcționalitatea butonului Quick view pentru un produs.
Observații și rezultate:
* Nu am identificat bug-uri sau erori în timpul testării.
* Riscuri potențiale ar putea include probleme de performanță în cazul în care numărul de utilizatori simultani crește semnificativ.
  
Concluzie:
În urma testării efectuate, putem trage concluzia că aplicația PrestaShop se comportă conform așteptărilor și funcționalităților sale specifice. 



