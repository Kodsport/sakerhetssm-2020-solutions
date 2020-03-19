# Misc: Vackra filer

- **Skapare:** Mattias Grenfeldt
- **Poäng:** 100
- **Antal lösningar:** ???

## Beskrivning

Har du någonsin sett såna vackra filer? 

SSHa till X.X.X.X på port 2222 och läs flaggan. Använd användaren ctf och lösenordet hunter2.

## Flagga

SSM{Vem_tyckte_NBSP_i_filnamn_var_en_bra_ide}

## Lösning

Man möts av ett shell som är väldigt begränsat. De flesta kommandona ger "permission denied" om man försöker köra dem. Men vi har `ls` och `cat`. 

När vi använder ls så ser vi att det finns en massa filer med något konstigt mellanslag i filnamnet. Det visar sig att det inte är ett vanligt mellanslag så det kan vara svårt att använda cat för att se vad filerna innehåller. Dock kan vi använda `cat *` för att se innehållet i alla filer i mappen på en gång. Då får vi följande:


```
HEJ HAR FINNS INGEN FLAGGA ATT HITTA. LETA NAGON ANNANSTANS.
HEJ HAR FINNS INGEN FLAGGA ATT HITTA. LETA NAGON ANNANSTANS.
HEJ HAR FINNS INGEN FLAGGA ATT HITTA. LETA NAGON ANNANSTANS.
HEJ HAR FINNS INGEN FLAGGA ATT HITTA. LETA NAGON ANNANSTANS.
HEJ HAR FINNS INGEN FLAGGA ATT HITTA. LETA NAGON ANNANSTANS.
HEJ HAR FINNS INGEN FLAGGA ATT HITTA. LETA NAGON ANNANSTANS.
HEJ HAR FINNS INGEN FLAGGA ATT HITTA. LETA NAGON ANNANSTANS.
HEJ HAR FINNS INGEN FLAGGA ATT HITTA. LETA NAGON ANNANSTANS.
HEJ HAR FINNS INGEN FLAGGA ATT HITTA. LETA NAGON ANNANSTANS.
HEJ HAR FINNS INGEN FLAGGA ATT HITTA. LETA NAGON ANNANSTANS.
HEJ HAR FINNS INGEN FLAGGA ATT HITTA. LETA NAGON ANNANSTANS.
HEJ HAR FINNS INGEN FLAGGA ATT HITTA. LETA NAGON ANNANSTANS.
HEJ HAR FINNS INGEN FLAGGA ATT HITTA. LETA NAGON ANNANSTANS.
HEJ HAR FINNS INGEN FLAGGA ATT HITTA. LETA NAGON ANNANSTANS.
HEJ HAR FINNS INGEN FLAGGA ATT HITTA. LETA NAGON ANNANSTANS.
HEJ HAR FINNS INGEN FLAGGA ATT HITTA. LETA NAGON ANNANSTANS.
HEJ HAR FINNS INGEN FLAGGA ATT HITTA. LETA NAGON ANNANSTANS. 
```

Nope, här fanns ingen flagga. Om vi använder `ls -la` kan vi se filstorleken för de individuella filerna. Vi ser att alla har samma filstorlek: `107 bytes`. Vi kan också se att det som printades från `cat` bara var 60 bytes på varje rad. Vi inser då att filerna innehåller något gömt som inte printas. 

Vi undersöke lite hur man kan använda `cat` för att printa alla tecken, även dem som inte vanligtvis syns. Genom att titta i `man cat` komer vi fram till att man kan använda `cat -v` för att visa specialtecken. Vi använder då `cat -v *` och får fram flaggan.

```
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa^MHEJ HAR FINNS INGEN FLAGGA ATT HITTA. LETA NAGON ANNANSTANS.
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa^MHEJ HAR FINNS INGEN FLAGGA ATT HITTA. LETA NAGON ANNANSTANS.
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa^MHEJ HAR FINNS INGEN FLAGGA ATT HITTA. LETA NAGON ANNANSTANS.
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa^MHEJ HAR FINNS INGEN FLAGGA ATT HITTA. LETA NAGON ANNANSTANS.
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa^MHEJ HAR FINNS INGEN FLAGGA ATT HITTA. LETA NAGON ANNANSTANS.
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa^MHEJ HAR FINNS INGEN FLAGGA ATT HITTA. LETA NAGON ANNANSTANS.
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa^MHEJ HAR FINNS INGEN FLAGGA ATT HITTA. LETA NAGON ANNANSTANS.
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa^MHEJ HAR FINNS INGEN FLAGGA ATT HITTA. LETA NAGON ANNANSTANS.
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa^MHEJ HAR FINNS INGEN FLAGGA ATT HITTA. LETA NAGON ANNANSTANS.
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa^MHEJ HAR FINNS INGEN FLAGGA ATT HITTA. LETA NAGON ANNANSTANS.
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa^MHEJ HAR FINNS INGEN FLAGGA ATT HITTA. LETA NAGON ANNANSTANS.
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa^MHEJ HAR FINNS INGEN FLAGGA ATT HITTA. LETA NAGON ANNANSTANS.
SSM{Vem_tyckte_NBSP_i_filnamn_var_en_bra_ide}^MHEJ HAR FINNS INGEN FLAGGA ATT HITTA. LETA NAGON ANNANSTANS.
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa^MHEJ HAR FINNS INGEN FLAGGA ATT HITTA. LETA NAGON ANNANSTANS.
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa^MHEJ HAR FINNS INGEN FLAGGA ATT HITTA. LETA NAGON ANNANSTANS.
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa^MHEJ HAR FINNS INGEN FLAGGA ATT HITTA. LETA NAGON ANNANSTANS.
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa^MHEJ HAR FINNS INGEN FLAGGA ATT HITTA. LETA NAGON ANNANSTANS.
```

