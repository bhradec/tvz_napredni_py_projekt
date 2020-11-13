# Projekt iz predmeta Napredno programiranje u jeziku Python

Svrha projekta je izrada jednostavnog programa za digitalnu 
steganografiju korištenjem slika. Program može čitati skrivene
poruke iz slika i upisivati skrivene poruke u slike.

## Dependency

Za ispravan rad potrebni su sljedeći paketi:  
<ol>
    <li>PIL (Pillow)</li>
    <li>numpy</li>
</ol>  

Moguće ih je instalirati na slijedeći način:  
```pip install Pillow```  
```pip install numpy```  
U slučaju pogreške ako wheel nije instaliran:    
```pip install wheel```  

## Opis datoteka

| DATOTEKA            | OPIS                                                        |
|---------------------|-------------------------------------------------------------|
| message_find_gui.py | Grafičko sučelje programa napravljeno korištenjem tkintera. |
| message_find.py     | Program za pronalazak skrivenih poruka u slikama.           |
| message_hide.py     | Program za sakrivanje poruka u slikama.                     |

## Korištenje

Pokretanje GUI-a:  
```message_find_gui.py```  

Pronalazak skrivene poruke:  
```message_find.py source_image.png```  

Sakrivanje poruke:  
```message_hide.py "tekst" dest_image.png```  

## Autori

Antonio Jurešić i Bruno Hradec,  
2020.