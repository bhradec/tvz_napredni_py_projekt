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
U slučaju da wheel nije instaliran:    
```pip install wheel```  

## Opis datoteka

| DATOTEKA            | OPIS                                                        |
|---------------------|-------------------------------------------------------------|
| hf_message_gui.py   | Grafičko sučelje programa napravljeno korištenjem tkintera. |
| find_message.py     | Program za pronalazak skrivenih poruka u slikama.           |
| hide_message.py     | Program za sakrivanje poruka u slikama.                     |
| display_pixels.py   | Program za ispis RGB vrijednosti po retcima.                |

## Korištenje

Pokretanje GUI-a:  
```hf_message_gui.py```  

Pronalazak skrivene poruke:  
```find_message.py source_image.png```  

Sakrivanje poruke:  
```hide_message.py "tekst" dest_image.png```  

## Autori

Antonio Jurešić i Bruno Hradec,  
2020.