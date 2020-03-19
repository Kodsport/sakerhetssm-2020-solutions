# Boot2root: Knowit 2 - User

- **Skapare:** Knowit (Fredrik Ljung)
- **Poäng:** 200
- **Antal lösningar:** 7

## Beskrivning

David hade inte tänkt på att en utomstående skulle få tillgång till servern.
Se om du kan hitta någon känslig information för att komma åt nästa flagga.

## Flagga

SSM{knowit_2_wE_4rE_8_pe0pl3_w0rk1ng_w1tH_p3nte5t1ng_0n_A_daIly_Bas1S!}

## Lösning

När man nu har ett shell (från knowit 1) så kan man navigera runt i filsystemet.
Går man till `/var/www` hittar man `/wordpress` och i `wp-config.php` finns lösenordet till användaren david.

Nu kan man antingen ssh:a in som david eller köra `su - david` och skriva in lösenordet.

