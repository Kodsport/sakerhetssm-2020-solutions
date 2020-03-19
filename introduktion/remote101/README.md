# Introduktion: Remote 101

- **Skapare:** Mattias Grenfeldt
- **Poäng:** 10
- **Antal lösningar:** ???

## Beskrivning

En stor del av all dagens kommunikation på internet sker via protokollet TCP, Transmission Control Protocol. För att kommunicera via TCP behöver man två datorer, en som lyssnar och en som ansluter. När man väl har startat en anslutning mellan två datorer kan de prata fritt fram och tillbaka med varandra. I många av utmaningarna i tävlingen ber vi er ansluta till en ip och en port. Se exemplet nedan. IP:n berättar vilken annan dator vi vill ansluta till och porten säger vilket program på den andra datorn vi vill prata med. 

På i stort sätt alla linuxsystem finns verktyget netcat. (Om du inte har ett linuxsystem så läs beskrivningen för Elf 101.) Man kan använda netcat genom kommandot nc. Netcat kan användas för att skapa en TCP-koppling direkt till en IP och port för att kunna kommunicera över internet. Testa att ansluta till IP:n och porten nedan. Vem vet, du kanske får en flaggan. :o

IP : port
35.228.52.143 : 4321

Kommando: nc <ip> <port>

## Flagga

`SSM{congratz!_you_can_now_build_an_internet!}`

## Lösning

Kör kommandot `nc 35.228.52.143 4321`
