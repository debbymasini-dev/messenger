#!/usr/bin/env python3
# Generates the 4 informative kits (k2410, k0711, k1411, k1912): post, storia, news.
import os
import os
SP = os.environ.get('KIT_SP','/tmp/kit') + '/kitall/project/'
B = lambda i: '/_blob/' + i
LET = B('f76aa4f097dce598a2692bd36380569a'); BOC = B('b6b849e87ef0993310e1ac51deaa6468'); SCA = B('d6906306ac53852834d3e32c9027e117')
IMG = {k: B(v) for k, v in {
 'gif2410': '1d066c7ae1eeb977fdc70c6e551115a5', 'gif0711': '9d9a0e522220ecec5d88f0787f41012c',
 'gif1411': 'add45a902504bf80c9ec361bda0d2998', 'gif1912': '273f6e53d4fc506b6d0a8c1d2bda1b3c',
 'cy1': '13f473410b88a075d10fd4da35a45cbf', 'cy2': '72fe780d184232d54a9a580a8d5ec86e', 'cy3': '20f3367a5ddac233917209a9f0d6ebcc',
 'el2': 'b543281472b96b85d84ec99bae2a4c0b', 'el3': '57766fce5b926478fea36f15a73fe58b',
 'fe0': 'f346d334f3d690e8a7745bb0e5463879', 'fe3': 'f6ecb57669f8fcad998d389b67eea51e',
 'gi1': '5693ccdb55439321f95dd0636531333b', 'gi2': '6dce3ad756d69eee202b825ede5ed592', 'gi3': 'b50429aa2da4b1055efa00753960b780',
 'pa1': 'b5150c377f6573ed50d549ddfc5d6d6c', 'pa2': '101ba5c6ac52bc1e64091b57ba8faf2c', 'pa3': '2d89934e19b73b6807f7144e24ba0f17', 'pa4': '1bbd25f6a5aaf914f8746146ddbc76d8'}.items()}
WA = 'https://wa.me/393314030216'
VIPL = 'https://chat.whatsapp.com/CsCcdqcW0O6FgpkYA94QEa?mode=gi_t'
ICONS = '''<div style="display: flex; gap: 20px; align-items: center">
<a href="https://www.instagram.com/__teenage_dirtbag__"><img src="/_blob/8fcf166f36a7b4281a58bff0342858da" alt="Instagram" style="width: 40px; height: 40px; display: block"></a>
<a href="https://www.facebook.com/share/1V3Xd1A6zq/"><img src="/_blob/edfc443f5fb2b7abda2c14c450834ce0" alt="Facebook" style="width: 40px; height: 40px; display: block"></a>
<a href="https://www.tiktok.com/@__teenagedirtbag__"><img src="/_blob/fbd97a11899d22f16c64e6c3f0450150" alt="TikTok" style="width: 40px; height: 40px; display: block"></a>
<a href="https://wa.me/393314030216"><img src="/_blob/52528d2838b82fcbae21aab60cdad752" alt="WhatsApp" style="width: 40px; height: 40px; display: block"></a>
<a href="mailto:info@teenagedirtbag.it"><img src="/_blob/17eb94dd26b7ba7e9725c327d67cf983" alt="Email" style="width: 40px; height: 40px; display: block"></a>
</div>'''

FONTS = {
 'zine': ('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Permanent+Marker&family=Special+Elite&display=swap', "'Special Elite',monospace", '#EDE7D8', '#111111'),
 'chrome': ('https://fonts.googleapis.com/css2?family=Chakra+Petch:ital,wght@0,400;0,600;0,700;1,400&family=Oswald:wght@500;700&display=swap', "'Chakra Petch',sans-serif", '#050510', '#ffffff'),
 'pink': ('https://fonts.googleapis.com/css2?family=Fredoka:wght@500;600;700&family=Dancing+Script:wght@700&family=Quicksand:wght@500;700&display=swap', "'Quicksand',sans-serif", '#FFF3F7', '#5A2A4A'),
}
ACOL = {'zine': ('#ffffff', '#C6FF00', '#B026FF', '#FF2E88'), 'chrome': ('#ffffff', '#C9CDD4', '#00E5FF', '#C9CDD4'), 'pink': ('#ffffff', '#FFE1ED', '#B026FF', '#F0508C')}

def page(title, style, body, w, h, news=False):
    link, ff, bg, col = FONTS[style]
    a, ah = (ACOL[style][2], ACOL[style][3]) if news else (ACOL[style][0], ACOL[style][1])
    return f'''<!doctype html>
<html lang="it">
<head>
<meta charset="utf-8">
<title>{title}</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="{link}" rel="stylesheet">
<style>
body{{margin:0;background:{bg};font-family:{ff};color:{col}}}
a{{color:{a};text-decoration:none}}a:hover{{color:{ah}}}
</style>
</helmet>
{body}
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":{w},"height":{h}}}}}'>
class Component extends DCLogic {{
renderVals() {{ return {{}}; }}
}}
</script>
</body>
</html>
'''

def save(name, html):
    open(SP + name, 'w').write(html); print('wrote', name)

# ---------------- ZINE (patchwork, cybersigilism) ----------------
ZBG = "background: #EDE7D8; background-image: repeating-linear-gradient(90deg, rgba(17,17,17,0.03) 0px, rgba(17,17,17,0.03) 1px, transparent 1px, transparent 5px); font-family: 'Special Elite', monospace; color: #111111"

def zine_visual(k, H, i1, a1, p1, i2, a2, p2, kick, t1, t2, sub, btn, url):
    st = H == 1920
    s = dict(hdr=300 if st else 190, lx=80, ly=60 if st else 18, lw=250 if st else 210, lh=181 if st else 152,
             bx=800 if st else 840, by=50 if st else 12, bw=200 if st else 160,
             fx=90 if st else 110, fy=330 if st else 214, fw=900 if st else 860, fh=760 if st else 580,
             iw=433 if st else 415, ih=736 if st else 560)
    kt, tt, sut, bt, sc = (1106, 1180, 1428, 1484, 1624) if st else (806, 866, 1080, 1124, 1256)
    return f'''<div style="width: 1080px; height: {H}px; position: relative; overflow: hidden; {ZBG}">
<div style="position: absolute; left: 0; top: 0; width: 1080px; height: {s['hdr']}px; background: #111111"></div>
<img src="{LET}" alt="Teenage Dirtbag" style="position: absolute; left: 80px; top: {s['ly']}px; width: {s['lw']}px; height: {s['lh']}px">
<img src="{BOC}" alt="Logo bocca Teenage Dirtbag" style="position: absolute; left: {s['bx']}px; top: {s['by']}px; width: {s['bw']}px; height: {s['bw']}px; filter: drop-shadow(0 0 20px rgba(176,38,255,0.7))">
<div style="position: absolute; left: {s['fx']}px; top: {s['fy']}px; width: {s['fw']}px; height: {s['fh']}px; transform: rotate(-1.5deg); background: #111111; padding: {12 if st else 10}px; box-sizing: border-box; box-shadow: {10 if st else 8}px {10 if st else 8}px 0 #B026FF">
<div style="display: flex; gap: 10px"><img src="{IMG[i1]}" alt="{a1}" style="width: {s['iw']}px; height: {s['ih']}px; object-fit: cover; object-position: {p1}; display: block"><img src="{IMG[i2]}" alt="{a2}" style="width: {s['iw']}px; height: {s['ih']}px; object-fit: cover; object-position: {p2}; display: block"></div>
</div>
<div style="position: absolute; left: {870 if st else 860}px; top: {318 if st else 200}px; width: {160 if st else 150}px; height: {38 if st else 36}px; background: rgba(198,255,0,0.85); transform: rotate(18deg)"></div>
<div style="position: absolute; left: {60 if st else 84}px; top: {1062 if st else 770}px; width: {160 if st else 150}px; height: {38 if st else 36}px; background: rgba(255,46,136,0.85); transform: rotate(12deg)"></div>
<div style="position: absolute; left: {100 if st else 110}px; top: {kt}px; font-family: 'Permanent Marker', cursive; font-size: {48 if st else 42}px; color: #FF2E88; transform: rotate(-3deg)">{kick}</div>
<div style="position: absolute; left: 80px; top: {tt}px; width: 920px; font-family: 'Bebas Neue', sans-serif; font-size: {132 if st else 108}px; line-height: 0.88; color: #111111; transform: rotate(-1.5deg)">{t1}<br><span style="color: #B026FF; -webkit-text-stroke: 2px #ffffff; text-shadow: 5px 5px 0 #111111">{t2}</span></div>
<div style="position: absolute; left: 80px; top: {sut}px; width: 920px; font-size: {27 if st else 24}px">{sub}</div>
<a href="{url}" style="position: absolute; left: 80px; top: {bt}px; width: 920px; height: {112 if st else 104}px; box-sizing: border-box; background: #B026FF; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 2px; color: #ffffff; box-shadow: 6px 6px 0 #111111; transform: rotate(-0.8deg)">
<span style="font-family: 'Bebas Neue', sans-serif; font-size: {60 if st else 56}px; letter-spacing: 2px; line-height: 1">SCOPRI DI PIÙ</span>
<span style="font-size: {22 if st else 21}px">{btn}</span>
</a>
<img src="{SCA}" alt="Scalapay - paga a rate" style="position: absolute; left: 445px; top: {sc}px; width: 190px; height: 60px">
</div>'''

def zpair(i1, a1, p1, i2, a2, p2, cred, rot='-1deg', sh='#B026FF'):
    return f'''<div style="margin: 24px 40px 0 40px; background: #111111; padding: 10px; transform: rotate({rot}); box-shadow: 6px 6px 0 {sh}"><div style="display: flex; gap: 10px"><img src="{IMG[i1]}" alt="{a1}" style="width: 245px; height: 305px; object-fit: cover; object-position: {p1}; display: block"><img src="{IMG[i2]}" alt="{a2}" style="width: 245px; height: 305px; object-fit: cover; object-position: {p2}; display: block"></div><div style="margin-top: 8px; font-size: 11px; color: #EDE7D8; text-align: center">{cred}</div></div>'''

def zp(t, b):
    return f'<p style="margin: 0; font-size: 15px; line-height: 1.55"><b style="color: #C6FF00">{t}</b><br>{b}</p>'

def zine_news(title, kick, t1, t2, intro, top_pair, pts1, mid_pair, mid_cap, pts2, tip, gifcap, cta_sub, credits, bye):
    return f'''<div style="width: 600px; height: 3300px; box-sizing: border-box; background: #EDE7D8; font-family: 'Special Elite', monospace; color: #111111; display: flex; flex-direction: column">
<div style="display: flex; justify-content: space-between; align-items: center; padding: 22px 32px; background: #111111">
<img src="{LET}" alt="Teenage Dirtbag" style="width: 150px; height: 108px">
<img src="{BOC}" alt="Logo bocca" style="width: 108px; height: 108px; filter: drop-shadow(0 0 14px rgba(176,38,255,0.7))">
</div>
{top_pair}
<div style="padding: 30px 40px 0 40px; display: flex; flex-direction: column; gap: 12px">
<div style="font-family: 'Permanent Marker', cursive; font-size: 26px; color: #FF2E88; transform: rotate(-2deg)">{kick}</div>
<div style="font-family: 'Bebas Neue', sans-serif; font-size: 64px; line-height: 0.9">{t1} <span style="color: #B026FF">{t2}</span></div>
<p style="margin: 6px 0 0 0; font-size: 16px; line-height: 1.6">{intro}</p>
</div>
<div style="margin: 24px 40px 0 40px; padding: 22px; background: #111111; color: #EDE7D8; display: flex; flex-direction: column; gap: 16px; transform: rotate(0.5deg)">
{''.join(zp(*x) for x in pts1)}
</div>
{mid_pair}
<div style="margin: 10px 40px 0 40px; text-align: center; font-family: 'Permanent Marker', cursive; font-size: 16px; color: #B026FF">{mid_cap}</div>
<div style="margin: 24px 40px 0 40px; padding: 22px; background: #111111; color: #EDE7D8; display: flex; flex-direction: column; gap: 16px; transform: rotate(-0.5deg)">
{''.join(zp(*x) for x in pts2)}
</div>
<div style="margin: 24px 40px 0 40px; padding: 18px 20px; border: 2px solid #111111; background: #ffffff; font-size: 14px; line-height: 1.55; transform: rotate(-0.4deg)"><b style="color: #B026FF">🖤 IL CONSIGLIO DI FILIPPO</b><br>«{tip}»<br>👉 seguilo su Instagram: <a href="https://www.instagram.com/sfregio_lttr/">@sfregio_lttr</a></div>
<div style="margin: 24px 40px 0 40px; height: 260px; background: #111111; box-shadow: 5px 5px 0 #B026FF; overflow: hidden; position: relative; display: flex; align-items: center; justify-content: center"><img src="{IMG['gif' + title]}" alt="GIF divertente della campagna" style="max-width: 100%; max-height: 100%; object-fit: contain; display: block"><div style="position: absolute; right: 10px; bottom: 10px; background: #B026FF; color: #ffffff; font-size: 12px; font-weight: 700; letter-spacing: 1px; padding: 5px 12px; border-radius: 999px">▶ ANIMATA NELLA MAIL</div></div>
<div style="margin: 10px 40px 0 40px; text-align: center; font-family: 'Permanent Marker', cursive; font-size: 17px; color: #B026FF">{gifcap}</div>
<a href="{WA}" style="margin: 26px 40px 0 40px; height: 92px; background: #B026FF; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 2px; color: #ffffff; text-decoration: none; box-shadow: 5px 5px 0 #111111; transform: rotate(-0.6deg)">
<span style="font-family: 'Bebas Neue', sans-serif; font-size: 38px; letter-spacing: 1px; line-height: 1">📲 CHIEDICI INFO</span>
<span style="font-size: 14px">{cta_sub}</span>
</a>
<div style="margin: 26px 40px 0 40px; padding: 22px; background: #000000; border: 2px solid #25D366; display: flex; flex-direction: column; align-items: center; gap: 10px; text-align: center; color: #ffffff">
<div style="font-family: 'Bebas Neue', sans-serif; font-size: 30px; letter-spacing: 1px">🎁 GRUPPO TEENAGE VIP</div>
<div style="font-size: 14px; color: #EDE7D8">SOLO LÌ vengono pubblicate le OFFERTE e i LAST MINUTE</div>
<a href="{VIPL}" style="padding: 12px 26px; border-radius: 999px; background: #25D366; color: #000000; font-weight: 700; font-size: 15px; text-decoration: none">UNISCITI AL GRUPPO VIP</a>
</div>
<div style="margin-top: auto; padding: 28px 40px 32px 40px; display: flex; flex-direction: column; align-items: center; gap: 14px; background: #111111; color: #EDE7D8">
<div style="font-size: 16px">{bye}</div>
{ICONS}
<img src="{SCA}" alt="Scalapay - paga a rate" style="width: 170px; height: 54px">
<div style="font-size: 12px; text-align: center">📍 Via Giardini 86, Pavullo nel Frignano (MO)<br>{credits}<br>© Teenage Dirtbag Tattoo Studio · Annulla iscrizione</div>
</div>
</div>'''

# ---- 24/10 Patchwork ----
U2410 = 'https://eepurl.com/yBSe01vk7f'
args = ('pa4', 'Manica patchwork traditional, pin di FatCatCollectiveCo', '50% 40%', 'pa2', 'Braccio con pezzi fine line staccati, pin di selftattoocom', '50% 45%',
        'patchwork 🧩', 'TANTI PICCOLI', 'UN SOLO RACCONTO')
save('k2410-post.dc.html', page('Patchwork · grafica WhatsApp', 'zine', zine_visual('2410', 1350, *args, 'come si riempie un braccio un pezzo alla volta ✂️', 'le regole del patchwork fatto bene ✨', U2410), 1080, 1350))
save('k2410-storia.dc.html', page('Patchwork · storia IG', 'zine', zine_visual('2410', 1920, *args, 'un braccio, tanti pezzi, zero caos ✂️', 'le regole del patchwork fatto bene ✨', U2410), 1080, 1920))
save('k2410-news.dc.html', page('Patchwork · newsletter', 'zine', zine_news('2410', 'come si riempie un braccio 🧩', 'PATCHWORK:', 'TANTI PICCOLI, NESSUN PROGETTO UNICO',
    "Il patchwork è il modo in cui oggi si riempie un braccio: non un disegno unico, ma <b>tanti pezzi separati che convivono</b>. Sembra la cosa più libera del mondo. In realtà è quella che va <b>pianificata di più</b>. ✂️",
    zpair('pa4', 'Manica patchwork traditional', '50% 40%', 'pa2', 'Braccio con pezzi fine line staccati', '50% 45%', 'foto: Pinterest · FatCatCollectiveCo · selftattoocom').replace('margin: 24px 40px 0 40px', 'margin: 30px 40px 0 40px'),
    [('🧩 I PEZZI GRANDI SULLA PELLE PIATTA', 'Vanno dove la pelle è piatta e si vede: bicipite esterno, avambraccio esterno, interno dell’avambraccio. I piccoli riempiono gli spazi fra quelli.'),
     ('🌬️ IL VUOTO FA PARTE DEL DISEGNO', 'La pelle libera non è spazio sprecato: è quella che fa respirare tutto il resto.'),
     ('🧵 IL FILO È IL LINGUAGGIO, NON IL SOGGETTO', 'Solo nero e grigio, oppure un solo stile, oppure una famiglia di soggetti. Spessore delle linee, ombreggiatura e scala si tengono allineati.')],
    zpair('pa1', 'Avambraccio con pezzi diversi nello stesso linguaggio', '50% 50%', 'pa3', 'Manica patchwork affollata, il caso da evitare', '50% 35%', 'foto: Pinterest · nicetattooideas · tattoovibeblog', '0.8deg', '#FF2E88'),
    'a sinistra: pezzi diversi, stesso linguaggio ✅ · a destra: spazio finito, il caso da evitare 🚫',
    [('✨ I RIEMPITIVI SERVONO', 'Stelle e puntini nel traditional, dotwork e piccoli accenti nel fine line: collegano senza coprire.'),
     ('🚫 L’ERRORE NUMERO UNO', 'Affollare i primi tre pezzi. Dopo non si può più scegliere dove mettere il quarto.'),
     ('🗣️ DILLO ALL’ARTISTA CHE VUOI CONTINUARE', 'Se lo sa, ti posiziona il pezzo di oggi pensando a quello dell’anno prossimo. Non è un progetto da una seduta: cresce per mesi o anni, ed è il suo bello.')],
    'Portami due o tre immagini di quello che ti piace e dimmi dove vuoi arrivare, anche se è vago. Il primo tatuaggio di una manica patchwork lo metto in un punto diverso se so che ne arriveranno altri cinque.',
    'la mia manica al sesto pezzo: È VIVA! ⚡🧟',
    'raccontaci la tua manica, la pensiamo insieme 🧩',
    'Foto: Pinterest · FatCatCollectiveCo, selftattoocom, nicetattooideas, tattoovibeblog · GIF: Pinterest · iiris_siempre (Frankenstein, 1931)',
    '🧩 Ci vediamo in studio 💜'), 600, 3300, news=True))

# ---- 19/12 Cybersigilism ----
U1912 = 'https://eepurl.com/yfg_Q0gDls'
args = ('cy3', 'Schiena con tatuaggio cybersigilism, pin di fcfsrevenge', '50% 40%', 'cy2', 'Flash ornamentale cybersigilism, pin di v1sam0r3', '50% 45%',
        'cybersigilism ⛓️', 'IL TRIBALE', 'IN VERSIONE ALIENA')
save('k1912-post.dc.html', page('Cybersigilism · grafica WhatsApp', 'zine', zine_visual('1912', 1350, *args, 'spine, simmetrie e linee finissime: cosa sapere prima 🖤', 'da dove nasce e come si porta ✨', U1912), 1080, 1350))
save('k1912-storia.dc.html', page('Cybersigilism · storia IG', 'zine', zine_visual('1912', 1920, *args, 'spine, simmetrie, linee finissime 🖤', 'da dove nasce e come si porta ✨', U1912), 1080, 1920))
save('k1912-news.dc.html', page('Cybersigilism · newsletter', 'zine', zine_news('1912', 'spine, simmetrie, linee finissime ⛓️', 'CYBERSIGILISM:', 'IL TRIBALE TORNATO IN VERSIONE ALIENA',
    "Spine, rami, simmetrie che sembrano antenne. Il <b>cybersigilism</b> è il neo-tribale degli anni Ottanta passato dentro il cyberpunk e risputato fuori in <b>nero finissimo</b>. 🖤",
    zpair('cy3', 'Schiena con tatuaggio cybersigilism', '50% 40%', 'cy2', 'Flash ornamentale cybersigilism', '50% 45%', 'foto: Pinterest · fcfsrevenge · v1sam0r3').replace('margin: 24px 40px 0 40px', 'margin: 30px 40px 0 40px'),
    [('🔮 IL NOME VIENE DAI SIGILLI', 'I simboli magici: forme intricate che sembrano voler dire qualcosa, da lì l’aria da misticismo digitale. Dall’altra parte c’è il Y2K: cromature, farfalle, filo spinato. Stesso immaginario, disegnato con la precisione di oggi.'),
     ('🖋️ FINE LINE + BLACKWORK', 'Solo nero, niente colore, linee che si assottigliano fino a sparire in punta.'),
     ('🪞 FUNZIONA PER SIMMETRIA', 'Sterno, colonna, nuca e avambraccio sono i posti dove la forma si legge per intero.')],
    zpair('cy1', 'Tatuaggio cybersigilism sulla schiena', '50% 30%', 'cy2', 'Dettaglio del flash cybersigilism', '50% 15%', 'foto: Pinterest · melinameilia · v1sam0r3', '0.8deg', '#FF2E88'),
    'il legame col neo-tribale si vede: è la stessa silhouette, riletta ⛓️',
    [('⚠️ È UNO STILE CHE NON PERDONA', 'Con linee così sottili la mano si vede tutta. Chiedi di vedere lavori guariti da mesi, non le foto appena fatte.'),
     ('📏 TROPPO PICCOLO NON REGGE', 'Le punte si chiudono e dopo qualche anno diventa una macchia. Meglio un pezzo giusto di misura che tre micro.'),
     ('🌐 NON È NATO IERI', 'E non da un solo artista: le fonti si contraddicono su chi l’ha cominciato, fra neo-tribale, scena di New York e il termine sigilism coniato nel 2023. Diffida di chi te lo racconta come una moda appena uscita.')],
    'Qui conta la misura prima del disegno. Dimmi dove lo vuoi e ti dico quanto deve essere grande per restare leggibile fra dieci anni: poi lo disegniamo su quella misura, non il contrario.',
    'io dopo aver scelto il mio pezzo in cybersigilism 🤖',
    'dicci dove lo vuoi, ti diciamo la misura giusta ⛓️',
    'Foto: Pinterest · fcfsrevenge, v1sam0r3, melinameilia · GIF: Pinterest · edrlml (Ghost in the Shell, 1995)',
    '⛓️ Ci vediamo in studio 💜'), 600, 3300, news=True))

# ---------------- CHROME (primo gioiello) ----------------
U0711 = 'https://eepurl.com/hBDeVcyH50'
def chrome_visual(H):
    st = H == 1920
    ph = 1300 if st else 1000
    ty = 1150 if st else 760; by = 1560 if st else 1090; sc = 1720 if st else 1222
    return f'''<div style="width: 1080px; height: {H}px; position: relative; overflow: hidden; background: #050510; font-family: 'Chakra Petch', sans-serif; color: #ffffff">
<img src="{IMG['gi1']}" alt="Septum e labret in titanio, pin di birthrightadornment" style="position: absolute; left: 0; top: 0; width: 1080px; height: {ph}px; object-fit: cover; object-position: 50% 55%">
<div style="position: absolute; left: 0; top: 0; width: 1080px; height: {300 if st else 230}px; background: linear-gradient(180deg, #050510 0%, rgba(5,5,16,0.8) 55%, rgba(5,5,16,0) 100%)"></div>
<div style="position: absolute; left: 0; top: {ph - 420}px; width: 1080px; height: 420px; background: linear-gradient(0deg, #050510 0%, rgba(5,5,16,0.85) 45%, rgba(5,5,16,0) 100%)"></div>
<img src="{LET}" alt="Teenage Dirtbag" style="position: absolute; left: 80px; top: {60 if st else 26}px; width: {250 if st else 220}px; height: {181 if st else 159}px">
<img src="{BOC}" alt="Logo bocca Teenage Dirtbag" style="position: absolute; left: {800 if st else 830}px; top: {50 if st else 16}px; width: {200 if st else 170}px; height: {200 if st else 170}px; filter: drop-shadow(0 0 22px rgba(176,38,255,0.75))">
<div style="position: absolute; left: 80px; top: {ty}px; width: 920px; display: flex; flex-direction: column; align-items: center; gap: 8px; text-align: center">
<div style="font-weight: 600; font-size: {28 if st else 26}px; letter-spacing: 8px; color: #00E5FF">PIERCING · LA GUIDA</div>
<div style="font-family: 'Oswald', sans-serif; font-weight: 700; font-size: {96 if st else 84}px; line-height: 1; letter-spacing: 1px; color: #C9CDD4; text-shadow: 0 2px 0 #ffffff, 0 0 24px rgba(176,38,255,0.45)">IL PRIMO <span style="color: #B026FF; -webkit-text-stroke: 3px #ffffff">GIOIELLO</span></div>
<div style="font-family: 'Oswald', sans-serif; font-weight: 700; font-size: {56 if st else 50}px; letter-spacing: 3px; color: #ffffff">SI SCEGLIE PER GUARIRE</div>
<div style="font-style: italic; font-size: {28 if st else 26}px; color: #ffffff; opacity: 0.85">titanio implant-grade · i consigli di Rebecca @beb_piercing</div>
</div>
<a href="{U0711}" style="position: absolute; left: 80px; top: {by}px; width: 920px; height: {112 if st else 104}px; box-sizing: border-box; border-radius: 26px; background: #B026FF; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 2px; color: #ffffff; box-shadow: 0 0 30px rgba(176,38,255,0.45)">
<span style="font-family: 'Oswald', sans-serif; font-weight: 700; font-size: {48 if st else 44}px; letter-spacing: 2px; line-height: 1.05">SCOPRI DI PIÙ</span>
<span style="font-style: italic; font-size: 22px">cosa mettere nel foro nuovo, e perché ✨</span>
</a>
<img src="{SCA}" alt="Scalapay - paga a rate" style="position: absolute; left: 445px; top: {sc}px; width: 190px; height: 60px">
</div>'''
save('k0711-post.dc.html', page('Primo gioiello · grafica WhatsApp', 'chrome', chrome_visual(1350), 1080, 1350))
save('k0711-storia.dc.html', page('Primo gioiello · storia IG', 'chrome', chrome_visual(1920), 1080, 1920))

def cp(t, b):
    return f'<p style="margin: 0; font-size: 16px; line-height: 1.55"><b style="color: #00E5FF">{t}</b><br>{b}</p>'
def cimg(i, alt, h, pos, cap):
    return f'''<img src="{IMG[i]}" alt="{alt}" style="width: 520px; height: {h}px; object-fit: cover; object-position: {pos}; margin: 24px 40px 0 40px; border-radius: 14px">
<div style="margin: 8px 40px 0 40px; text-align: center; font-size: 13px; color: #C9CDD4">{cap}</div>'''
news0711 = f'''<div style="width: 600px; height: 3300px; box-sizing: border-box; background: #050510; font-family: 'Chakra Petch', sans-serif; color: #ffffff; display: flex; flex-direction: column">
<div style="display: flex; justify-content: space-between; align-items: center; padding: 24px 32px">
<img src="{LET}" alt="Teenage Dirtbag" style="width: 150px; height: 108px">
<img src="{BOC}" alt="Logo bocca" style="width: 112px; height: 112px; filter: drop-shadow(0 0 16px rgba(176,38,255,0.7))">
</div>
<img src="{IMG['gi1']}" alt="Septum e labret in titanio implant-grade" style="width: 600px; height: 480px; object-fit: cover; object-position: 50% 55%">
<div style="padding: 34px 40px 0 40px; display: flex; flex-direction: column; gap: 14px">
<div style="font-size: 15px; font-weight: 600; letter-spacing: 6px; color: #00E5FF">PIERCING · LA GUIDA</div>
<div style="font-family: 'Oswald', sans-serif; font-weight: 700; font-size: 46px; line-height: 1.02; color: #B026FF; text-shadow: -1px -1px 0 #ffffff, 1px -1px 0 #ffffff, -1px 1px 0 #ffffff, 1px 1px 0 #ffffff">IL PRIMO GIOIELLO SI SCEGLIE PER GUARIRE, NON PER LO SPECCHIO</div>
<p style="margin: 0; font-size: 17px; line-height: 1.6; color: #C9CDD4">Il gioiello che ti mettiamo il giorno del piercing <b style="color: #ffffff">non è quello che porterai per sempre</b>. È quello che ti fa guarire: sono due oggetti diversi e si scelgono con due criteri diversi. ✨</p>
</div>
<div style="margin: 24px 40px 0 40px; padding: 24px; border: 1px solid #B026FF; border-radius: 14px; background: #2A1440; display: flex; flex-direction: column; gap: 16px">
{cp('🔩 TITANIO IMPLANT-GRADE, O ORO MASSICCIO', 'Adatto al corpo, punto. I metalli di composizione sconosciuta sono la prima causa di irritazione che vediamo in studio.')}
{cp('📏 PIÙ LUNGO DEL NECESSARIO', 'Il primo gioiello ha spazio in più, perché il gonfiore ne ha bisogno. Sembra sproporzionato ed è giusto così: si accorcia dopo.')}
{cp('🙅 NON SI TOCCA E NON SI GIRA', 'Mai con le mani non lavate. Girarlo non serve a niente: rompe solo il canale che si sta formando.')}
</div>
{cimg('gi2', 'Clicker in titanio, dorato e argento', 380, '50% 50%', 'clicker in titanio: liscio, leggero, senza nichel · foto Pinterest · tjjquality')}
<div style="margin: 24px 40px 0 40px; padding: 24px; border: 1px solid #B026FF; border-radius: 14px; background: #2A1440; display: flex; flex-direction: column; gap: 16px">
{cp('⏳ NON SI CAMBIA PRIMA CHE SIA PRONTO', 'Il lobo guarisce in fretta, cartilagine e ombelico molto più lentamente, e non si va a occhio.')}
{cp('🗓️ I PROGETTI SULL’ORECCHIO SI DISTANZIANO', 'Tre fori insieme vogliono dire tre guarigioni insieme, sullo stesso lato su cui dormi. Per l’ombelico contano la cintura dei jeans, la palestra e come ti giri nel sonno.')}
{cp('🚨 QUANDO CHIAMARCI SUBITO', 'Dolore che aumenta, calore, secrezioni strane o gonfiore che non scende. Non si aspetta: si viene a far vedere.')}
</div>
{cimg('gi3', 'Ragazza con piercing al viso', 340, '50% 35%', 'il gioiello definitivo arriva dopo, a foro guarito 💎 · foto Pinterest · ashleypiercingjewelry')}
<div style="margin: 24px 40px 0 40px; padding: 18px 20px; border: 2px solid #00E5FF; border-radius: 14px; font-size: 15px; line-height: 1.55; box-shadow: 0 0 22px rgba(0,229,255,0.2)"><b style="color: #00E5FF">💎 IL CONSIGLIO DI REBECCA</b><br>«Quando torni per il cambio, vieni senza fretta. Il gioiello definitivo lo scegliamo guardando il foro guarito, non il catalogo.»<br>👉 seguila su Instagram: <a href="https://www.instagram.com/beb_piercing/">@beb_piercing</a></div>
<div style="margin: 24px 40px 0 40px; height: 260px; background: #000000; border: 1px solid #B026FF; border-radius: 14px; overflow: hidden; position: relative; display: flex; align-items: center; justify-content: center"><img src="{IMG['gif0711']}" alt="GIF divertente della campagna" style="max-width: 100%; max-height: 100%; object-fit: contain; display: block"><div style="position: absolute; right: 10px; bottom: 10px; background: #B026FF; color: #ffffff; font-size: 12px; font-weight: 700; letter-spacing: 1px; padding: 5px 12px; border-radius: 999px">▶ ANIMATA NELLA MAIL</div></div>
<div style="margin: 10px 40px 0 40px; text-align: center; font-style: italic; font-size: 16px; color: #C9CDD4">io che controllo se il foro è guarito per cambiare gioiello 👀</div>
<a href="{WA}" style="margin: 26px 40px 0 40px; height: 96px; border-radius: 20px; background: #B026FF; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 2px; color: #ffffff; text-decoration: none; box-shadow: 0 0 26px rgba(176,38,255,0.45)">
<span style="font-family: 'Oswald', sans-serif; font-weight: 700; font-size: 34px; letter-spacing: 2px; line-height: 1.05">📲 CHIEDICI INFO</span>
<span style="font-style: italic; font-size: 15px">dubbi sul tuo foro nuovo? scrivici ✨</span>
</a>
<div style="margin: 26px 40px 0 40px; padding: 22px; background: #000000; border: 2px solid #25D366; border-radius: 14px; display: flex; flex-direction: column; align-items: center; gap: 10px; text-align: center">
<div style="font-family: 'Oswald', sans-serif; font-weight: 700; font-size: 24px; letter-spacing: 2px">🎁 GRUPPO TEENAGE VIP</div>
<div style="font-size: 15px; color: #C9CDD4">SOLO LÌ vengono pubblicate le OFFERTE e i LAST MINUTE</div>
<a href="{VIPL}" style="padding: 12px 26px; border-radius: 999px; background: #25D366; color: #000000; font-weight: 700; font-size: 16px; text-decoration: none">UNISCITI AL GRUPPO VIP</a>
</div>
<div style="margin-top: auto; padding: 28px 40px 32px 40px; display: flex; flex-direction: column; align-items: center; gap: 14px; border-top: 1px solid #2A1440">
<div style="font-size: 16px">💎 Ci vediamo in studio 💜</div>
{ICONS}
<img src="{SCA}" alt="Scalapay - paga a rate" style="width: 170px; height: 54px">
<div style="font-size: 12px; color: #C9CDD4; text-align: center">📍 Via Giardini 86, Pavullo nel Frignano (MO)<br>Foto: Pinterest · birthrightadornment, tjjquality, ashleypiercingjewelry · GIF: Pinterest · michaelabakeov (Colazione da Tiffany, 1961)<br>© Teenage Dirtbag Tattoo Studio · Annulla iscrizione</div>
</div>
</div>'''
save('k0711-news.dc.html', page('Primo gioiello · newsletter', 'chrome', news0711, 600, 3300, news=True))

# ---------------- PINK (eyeliner permanente) ----------------
U1411 = 'https://eepurl.com/5L0Lskl1cH'
SPARK = '''<div style="position: absolute; left: 40px; top: {a}px; font-size: 40px; color: #FF9CC4; opacity: .6">♡</div>
<div style="position: absolute; left: 1020px; top: {b}px; font-size: 34px; color: #E9B8FF; opacity: .7">✦</div>
<div style="position: absolute; left: 30px; top: {c}px; font-size: 30px; color: #E9B8FF; opacity: .7">✦</div>
<div style="position: absolute; left: 1024px; top: {d}px; font-size: 38px; color: #FF9CC4; opacity: .6">♡</div>
<div style="position: absolute; left: 480px; top: 60px; font-size: 44px; color: #FF9CC4; opacity: .55">♡</div>
<div style="position: absolute; left: 600px; top: 200px; font-size: 28px; color: #E9B8FF; opacity: .7">✦</div>'''
def frame(i, alt, x, y, w, h, pos='50% 50%', r=36):
    return f'''<div style="position: absolute; left: {x}px; top: {y}px; width: {w}px; height: {h}px; border-radius: {r}px; border: 10px solid #ffffff; box-shadow: 0 16px 40px rgba(240,80,140,.25); overflow: hidden; box-sizing: border-box">
<img src="{IMG[i]}" alt="{alt}" style="width: {w-20}px; height: {h-20}px; object-fit: cover; object-position: {pos}; display: block">
</div>'''
def pill(x, y, w, t, fs=24):
    return f'<div style="position: absolute; left: {x}px; top: {y}px; width: {w}px; text-align: center"><span style="display: inline-block; background: rgba(255,255,255,.94); border-radius: 999px; padding: 6px 20px; font-weight: 600; font-size: {fs}px">{t}</span></div>'
def pink_visual(H):
    st = H == 1920
    o = 130 if st else 0
    E = 210 if st else 0; e = E // 2  # vertical offset for the story
    box_y = 838 + o + E
    return f'''<div style="width: 1080px; height: {H}px; position: relative; overflow: hidden; background: linear-gradient(180deg,#FFE1ED 0%,#FFF4F8 50%,#FFE6F0 100%); font-family: 'Fredoka', sans-serif; color: #5A2A4A">
{SPARK.format(a=300 + o, b=180 + o, c=760 + o, d=820 + o)}
<img src="{LET}" alt="Teenage Dirtbag" style="position: absolute; left: 80px; top: {34 + (40 if st else 0)}px; width: 300px; height: 217px">
<div style="position: absolute; left: 742px; top: {14 + (40 if st else 0)}px; width: 258px; height: 258px; border-radius: 50%; background: radial-gradient(circle,rgba(255,156,196,.55) 0%,rgba(255,156,196,0) 70%)"></div>
<img src="{BOC}" alt="Logo bocca Teenage Dirtbag" style="position: absolute; left: 752px; top: {24 + (40 if st else 0)}px; width: 240px; height: 240px">
{frame('fe0', 'Eyeliner permanente sfumato, lavoro di Federica', 80, 276 + o, 500, 536 + E, '50% 30%', 40)}
{frame('fe3', 'Eyeliner permanente definito, lavoro di Federica', 600, 276 + o, 400, 260 + e, '50% 40%')}
{frame('el2', 'Pigmenti per trucco permanente', 600, 552 + o + e, 400, 260 + e, '50% 30%')}
{pill(100, 740 + o + E, 460, '👁️ sfumato', 28)}
{pill(610, 472 + o + e, 380, '✨ definito')}
{pill(610, 748 + o + E, 380, '🎨 pigmenti')}
<div style="position: absolute; left: 80px; top: {box_y}px; width: 920px; height: 400px; border-radius: 48px; background: rgba(255,255,255,.95); border: 4px solid #FFB3CF; box-shadow: 0 14px 40px rgba(240,80,140,.18); box-sizing: border-box"></div>
<div style="position: absolute; left: 80px; width: 920px; top: {box_y + 18}px; text-align: center; font-weight: 700; font-size: 112px; line-height: 1; color: #B026FF; text-shadow: 0 6px 0 #FFD1E3">EYELINER 💗</div>
<div style="position: absolute; left: 80px; width: 920px; top: {box_y + 134}px; text-align: center; font-family: 'Dancing Script', cursive; font-weight: 700; font-size: 50px; color: #F0508C">permanente: cosa sapere prima</div>
<div style="position: absolute; left: 80px; width: 920px; top: {box_y + 204}px; text-align: center; font-family: 'Quicksand', sans-serif; font-weight: 700; font-size: 28px; line-height: 1; color: #B0577F">i consigli di Federica · @favalorofederica_pmu 🌸</div>
<a href="{U1411}" style="position: absolute; left: 140px; top: {box_y + 268}px; width: 800px; height: 104px; border-radius: 999px; background: #B026FF; box-shadow: 0 8px 0 #8A16D0; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 4px; color: #ffffff">
<span style="font-weight: 600; font-size: 40px; line-height: 1; letter-spacing: 1px">SCOPRI DI PIÙ</span>
<span style="font-family: 'Quicksand', sans-serif; font-weight: 700; font-size: 22px">stili, durata e guarigione, spiegati semplice 💕</span>
</a>
<img src="{SCA}" alt="Scalapay - paga a rate" style="position: absolute; left: 445px; top: {box_y + 418}px; width: 190px; height: 60px">
{'' if not st else SPARK.format(a=1500, b=1560, c=1680, d=1750).split(chr(10))[0]}
</div>'''
save('k1411-post.dc.html', page('Eyeliner permanente · grafica WhatsApp', 'pink', pink_visual(1350), 1080, 1350))
save('k1411-storia.dc.html', page('Eyeliner permanente · storia IG', 'pink', pink_visual(1920), 1080, 1920))

def pp(t, b):
    return f'<p style="margin: 0; font-size: 16px; line-height: 1.55"><b style="color: #F0508C">{t}</b><br>{b}</p>'
BOX = 'margin: 26px 40px 0 40px; padding: 24px; background: #ffffff; border: 3px solid #FFB3CF; border-radius: 24px; display: flex; flex-direction: column; gap: 16px'
news1411 = f'''<div style="width: 600px; height: 3500px; box-sizing: border-box; background: #FFF3F7; font-family: 'Quicksand', sans-serif; color: #5A2A4A; display: flex; flex-direction: column">
<div style="display: flex; justify-content: space-between; align-items: center; padding: 24px 32px">
<img src="{LET}" alt="Teenage Dirtbag" style="width: 150px; height: 108px">
<img src="{BOC}" alt="Logo bocca" style="width: 112px; height: 112px">
</div>
<div style="padding: 10px 40px 0 40px; display: flex; flex-direction: column; align-items: center; gap: 6px; text-align: center">
<div style="font-family: 'Fredoka', sans-serif; font-size: 15px; font-weight: 600; letter-spacing: 5px; color: #F0508C">💗 TRUCCO PERMANENTE · PMU 💗</div>
<div style="font-family: 'Fredoka', sans-serif; font-weight: 700; font-size: 76px; line-height: 1; color: #B026FF; text-shadow: 0 5px 0 #FFD1E3">EYELINER</div>
<div style="font-family: 'Dancing Script', cursive; font-weight: 700; font-size: 34px; line-height: 1.1; color: #F0508C">permanente: cosa sapere prima di dire sì</div>
</div>
<img src="{IMG['fe0']}" alt="Eyeliner permanente sfumato, lavoro di Federica" style="width: 520px; height: 420px; object-fit: cover; object-position: 50% 30%; margin: 24px 40px 0 40px; border-radius: 24px">
<div style="margin: 8px 40px 0 40px; text-align: center; font-size: 14px; font-weight: 700; color: #B0577F">eyeliner sfumato di Federica: morbido come un ombretto 👁️</div>
<div style="padding: 26px 40px 0 40px; display: flex; flex-direction: column; gap: 14px">
<p style="margin: 0; font-size: 17px; line-height: 1.65">Non è un tatuaggio per sempre e non è il trucco che devi struccare ogni sera. Sta nel mezzo: <b>pigmento sulla linea delle ciglia che sbiadisce piano</b>. 🌸</p>
</div>
<div style="{BOX}">
{pp('🖊️ TRE STILI, NON UNO', 'Linea sottile che infoltisce la rima e quasi non si vede, tratto classico definito, versione sfumata effetto ombretto morbido.')}
{pp('☀️ IL VERO MOTIVO È LA MATTINA', 'Niente mano ferma alle sette, niente che cola con il caldo, la palestra o l’umidità. E aiuta chi ha la pelle sensibile o allergie ai cosmetici, perché toglie il contatto quotidiano con i prodotti.')}
{pp('⏳ QUANTO DURA', 'In genere qualche anno, ma cambia molto da persona a persona: pelle grassa, sole e ricambio cellulare lo accorciano. Le tonalità chiare sbiadiscono prima del nero.')}
</div>
<div style="margin: 26px 40px 0 40px; display: flex; gap: 10px">
<img src="{IMG['fe3']}" alt="Eyeliner definito, lavoro di Federica" style="width: 255px; height: 220px; object-fit: cover; object-position: 50% 40%; border-radius: 18px">
<img src="{IMG['el2']}" alt="Pigmenti per trucco permanente" style="width: 255px; height: 220px; object-fit: cover; object-position: 50% 30%; border-radius: 18px">
</div>
<div style="margin: 8px 40px 0 40px; text-align: center; font-size: 14px; font-weight: 700; color: #B0577F">tratto definito ✨ · i pigmenti, scelti sul tuo incarnato 🎨</div>
<div style="{BOX}">
{pp('💬 IL RITOCCO QUASI SEMPRE SERVE', 'A qualche settimana di distanza. La domanda da fare in consulenza è una: il ritocco è compreso nel prezzo?')}
{pp('🪞 PRIMA SI DISEGNA CON LA MATITA', 'E lo si guarda insieme allo specchio: se non ti piace, si rifà lì.')}
{pp('👓 LENTI E OCCHI SENSIBILI', 'Lenti a contatto fuori prima della seduta, e si rimettono solo a guarigione finita. Occhi secchi, allergie o problemi di vista: prima si sente l’oculista.')}
</div>
<div style="margin: 26px 40px 0 40px; padding: 24px; background: #FFE1ED; border-radius: 24px; display: flex; flex-direction: column; gap: 10px">
<div style="font-family: 'Fredoka', sans-serif; font-weight: 600; font-size: 24px; color: #B026FF; text-align: center">LA GUARIGIONE GIORNO PER GIORNO 🌷</div>
<p style="margin: 0; font-size: 16px; line-height: 1.55">💧 <b>Primi giorni:</b> più intenso del risultato finale, con un gonfiorino sulla rima.</p>
<p style="margin: 0; font-size: 16px; line-height: 1.55">🤏 <b>Poi:</b> crosticine sottili. Non si toccano e non si grattano: cadono da sole.</p>
<p style="margin: 0; font-size: 16px; line-height: 1.55">😮 <b>Secondo o terzo giorno:</b> sembra troppo scuro. È normale, schiarisce mentre le croste vanno via.</p>
<p style="margin: 0; font-size: 16px; line-height: 1.55">🌸 <b>Alla fine:</b> il colore vero si vede solo a pelle stabilizzata.</p>
</div>
<img src="{IMG['el3']}" alt="Still life di pigmenti per permanente" style="width: 520px; height: 300px; object-fit: cover; object-position: 50% 45%; margin: 26px 40px 0 40px; border-radius: 24px">
<div style="margin: 26px 40px 0 40px; padding: 22px 24px; background: #ffffff; border: 3px solid #FFB3CF; border-radius: 24px; font-size: 16px; line-height: 1.55; text-align: center"><b style="color: #B026FF; font-family: 'Fredoka', sans-serif; font-size: 22px">IL CONSIGLIO DI FEDERICA 💕</b><br>«Non guardare l’eyeliner il terzo giorno e non giudicarlo. Guardalo a guarigione finita: è un altro trucco.»<br><a href="https://www.instagram.com/favalorofederica_pmu/" style="display: inline-block; margin-top: 12px; padding: 10px 22px; border-radius: 999px; background: #FFE1ED; color: #B026FF; font-weight: 700">✨ guarda i suoi lavori: @favalorofederica_pmu</a></div>
<div style="margin: 26px 40px 0 40px; height: 270px; background: #ffffff; border: 3px solid #FFB3CF; border-radius: 24px; overflow: hidden; position: relative; display: flex; align-items: center; justify-content: center"><img src="{IMG['gif1411']}" alt="GIF divertente della campagna" style="max-width: 100%; max-height: 100%; object-fit: contain; display: block"><div style="position: absolute; right: 10px; bottom: 10px; background: #B026FF; color: #ffffff; font-size: 12px; font-weight: 700; letter-spacing: 1px; padding: 5px 12px; border-radius: 999px">▶ ANIMATA NELLA MAIL</div></div>
<div style="margin: 10px 40px 0 40px; text-align: center; font-family: 'Dancing Script', cursive; font-weight: 700; font-size: 24px; color: #F0508C">io col mio eyeliner a guarigione finita: regina d’Egitto 👑</div>
<a href="{WA}" style="margin: 28px 40px 0 40px; height: 100px; border-radius: 999px; background: #B026FF; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 4px; color: #ffffff; text-decoration: none">
<span style="font-family: 'Fredoka', sans-serif; font-weight: 600; font-size: 26px; letter-spacing: .5px; white-space: nowrap">📲 CHIEDICI INFO</span>
<span style="font-size: 15px; font-weight: 700">ti rispondiamo con calma, zero impegno 💕</span>
</a>
<div style="margin: 14px 40px 0 40px; text-align: center; font-size: 15px; font-weight: 700; color: #B0577F">💳 e se decidi di farlo, puoi pagare anche a rate con Scalapay</div>
<div style="margin: 26px 40px 0 40px; padding: 18px 22px; border-top: 2px dotted #FFB3CF; border-bottom: 2px dotted #FFB3CF; font-size: 15px; line-height: 1.55; text-align: center">✍️ I tatuaggi di casa portano la firma di <b>Filippo</b>, il nostro resident: seguilo su Instagram — <a href="https://www.instagram.com/sfregio_lttr/">@sfregio_lttr</a> 🖤</div>
<div style="margin: 26px 40px 0 40px; padding: 22px; background: #ffffff; border: 3px solid #25D366; border-radius: 24px; display: flex; flex-direction: column; align-items: center; gap: 10px; text-align: center">
<div style="font-family: 'Fredoka', sans-serif; font-weight: 600; font-size: 24px; letter-spacing: 1px; color: #5A2A4A">🎁 GRUPPO TEENAGE VIP</div>
<div style="font-size: 15px; font-weight: 700">SOLO LÌ vengono pubblicate le OFFERTE e i LAST MINUTE</div>
<a href="{VIPL}" style="padding: 12px 26px; border-radius: 999px; background: #25D366; color: #ffffff; font-weight: 700; font-size: 16px; text-decoration: none">UNISCITI AL GRUPPO VIP</a>
</div>
<div style="margin-top: auto; padding: 28px 40px 32px 40px; display: flex; flex-direction: column; align-items: center; gap: 14px; border-top: 2px solid #FFD1E3">
<div style="font-size: 16px; font-weight: 700">Ti aspettiamo in studio 💜</div>
{ICONS}
<img src="{SCA}" alt="Scalapay - paga a rate" style="width: 170px; height: 54px">
<div style="font-size: 12px; text-align: center; color: #B0577F">📍 Via Giardini 86, Pavullo nel Frignano (MO)<br>Foto: lavori di Federica · @favalorofederica_pmu · Pinterest · Rpbeauty_, daryakostrova · GIF: Pinterest · breeannaquiroz (Cleopatra, 1963)<br>© Teenage Dirtbag Tattoo Studio · Annulla iscrizione</div>
</div>
</div>'''
save('k1411-news.dc.html', page('Eyeliner permanente · newsletter', 'pink', news1411, 600, 3500, news=True))
