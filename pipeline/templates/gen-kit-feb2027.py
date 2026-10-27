#!/usr/bin/env python3
# Genera i 3 kit informativi di febbraio 2027: k0602 (neo traditional, zine),
# k0902 (helix, chrome), k1102 (durata PMU, pink). Post, storia, news.
import os
SP = os.environ.get('KIT_SP', '/tmp/kit') + '/kitall/project/'
B = lambda i: '/_blob/' + i
LET = B('f76aa4f097dce598a2692bd36380569a'); BOC = B('b6b849e87ef0993310e1ac51deaa6468'); SCA = B('d6906306ac53852834d3e32c9027e117')
IMG = {k: B(v) for k, v in {
 'gif0602': 'd8b2de66bef2db271bb1d79afc679cad', 'gif0902': '72e87334530a108d857cd70435e1b5ba', 'gif1102': 'de96167b446e781a6758b02b8a712ec3',
 'nt1': '50072525f00f756537f049d460af3ff9', 'nt3': 'da65d05274479955d930a12c3f8236e3', 'nt4': '78f06bf5a11d63d8eb2a13600e4097c2', 'nt5': '0ff7d2199d0191cabbec9009c808ce57',
 're1': 'd709d137b9d456ce9b6761526e9c5613', 're2': '98871a55ece02e471745ff8a30398a89', 're3': 'c6352e9e53042db52798d1a6e87916dc',
 'fe1': 'b395586dc81319132f9cc6551dd20c1c', 'fe2': '602130b340b5e60e958ee5ba13884dfa', 'fe3': '996b301116a56d2791f67214c8633f00'}.items()}
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

# ================= ZINE · 06/02 NEO TRADITIONAL =================
ZBG = "background: #EDE7D8; background-image: repeating-linear-gradient(90deg, rgba(17,17,17,0.03) 0px, rgba(17,17,17,0.03) 1px, transparent 1px, transparent 5px); font-family: 'Special Elite', monospace; color: #111111"

def zine_visual(k, H, i1, a1, p1, i2, a2, p2, kick, t1, t2, sub, btn, url):
    st = H == 1920
    s = dict(hdr=300 if st else 190, ly=60 if st else 18, lw=250 if st else 210, lh=181 if st else 152,
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

def zine_news(key, kick, t1, t2, intro, top_pair, pts1, mid_pair, mid_cap, pts2, tip, gifcap, cta_sub, credits, bye):
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
<div style="margin: 24px 40px 0 40px; height: 260px; background: #111111; box-shadow: 5px 5px 0 #B026FF; overflow: hidden; position: relative; display: flex; align-items: center; justify-content: center"><img src="{IMG['gif' + key]}" alt="GIF divertente della campagna" style="max-width: 100%; max-height: 100%; object-fit: contain; display: block"><div style="position: absolute; right: 10px; bottom: 10px; background: #B026FF; color: #ffffff; font-size: 12px; font-weight: 700; letter-spacing: 1px; padding: 5px 12px; border-radius: 999px">▶ ANIMATA NELLA MAIL</div></div>
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

U0602 = 'https://eepurl.com/1A8RWXILwD'
args = ('nt1', 'Cuore medaglione neo traditional su avambraccio, pin di bacchusdani', '50% 42%', 'nt5', 'Fiore neo traditional azzurro e rosa, pin di jayquellin87', '50% 50%',
        'neo traditional 🌹', 'IL CLASSICO CHE', 'NON INVECCHIA MAI')
save('k0602-post.dc.html', page('Neo traditional · grafica WhatsApp', 'zine', zine_visual('0602', 1350, *args, 'linee decise, colori pieni, soggetti d’epoca rivisti ✒️', 'lo stile spiegato bene ✨', U0602), 1080, 1350))
save('k0602-storia.dc.html', page('Neo traditional · storia IG', 'zine', zine_visual('0602', 1920, *args, 'linee decise, colori pieni, zero nostalgia ✒️', 'lo stile spiegato bene ✨', U0602), 1080, 1920))
save('k0602-news.dc.html', page('Neo traditional · newsletter', 'zine', zine_news('0602', 'il vecchio stile, rifatto nuovo 🌹', 'NEO TRADITIONAL:', 'IL CLASSICO CHE NON INVECCHIA MAI',
    "Rose, cuori, pugnali e pantere: i soggetti sono quelli di cent’anni fa. Ma il <b>neo traditional</b> li ridisegna con più dettaglio, più profondità e una tavolozza che il vecchio old school si sognava. ✍️",
    zpair('nt1', 'Cuore medaglione neo traditional', '50% 42%', 'nt5', 'Fiore neo traditional', '50% 50%', 'foto: Pinterest · bacchusdani · jayquellin87').replace('margin: 24px 40px 0 40px', 'margin: 30px 40px 0 40px'),
    [('🖤 LE LINEE RESTANO GROSSE', 'È il DNA del traditional: contorni decisi che tengono il tatuaggio leggibile per decenni. Il neo trad li tiene, e ci costruisce dentro.'),
     ('🎨 LA TAVOLOZZA SI ALLARGA', 'Dai 5-6 colori piatti dell’old school a sfumature, passaggi di tono e ombre morbide: più vicino all’illustrazione che al flash da bancone.'),
     ('🌹 SOGGETTI D’EPOCA, OCCHI NUOVI', 'Rose, animali, cuori, chiavi e medaglioni: il repertorio classico reinterpretato con gusto di oggi, senza fare il verso al passato.')],
    zpair('nt4', 'Flash traditional classico con corvo e teschio', '50% 40%', 'nt3', 'Fiammifero neo traditional colorato', '50% 45%', 'foto: Pinterest · krstenzel · amothcy', '0.8deg', '#FF2E88'),
    'a sinistra il traditional da cui nasce · a destra dove è arrivato 🔥',
    [('💪 PERCHÉ INVECCHIA BENE', 'Linee forti e colori saturi reggono il tempo meglio di qualsiasi micro: fra dieci anni si legge ancora come il primo giorno.'),
     ('📐 VUOLE IL SUO SPAZIO', 'Le ombreggiature ricche chiedono qualche centimetro in più: su un braccio o una gamba il neo trad canta, in miniatura soffoca.'),
     ('🧭 COME SI RICONOSCE UN BUON NEO TRAD', 'Guarda i lavori guariti: contorni ancora netti, colori che non si sono mangiati fra loro, composizione che si legge da lontano.')],
    'Porta il soggetto, non il disegno finito: il neo traditional dà il meglio quando l’artista può comporre. Una rosa la disegno su di te, non sul telefono.',
    'io che scelgo il neo trad: twist vincente 🕺',
    'raccontaci il soggetto che hai in testa 🌹',
    'Fonte: iNKPPL Magazine · Foto: Pinterest · bacchusdani, jayquellin87, krstenzel, amothcy · GIF: Pinterest · pasquale6071 (Pulp Fiction, 1994)',
    '🌹 Ci vediamo in studio 💜'), 600, 3300, news=True))

# ================= CHROME · 09/02 HELIX =================
U0902 = 'https://eepurl.com/qR3RCgAur6'
def chrome_visual(H):
    st = H == 1920
    ph = 1300 if st else 1000
    ty = 1150 if st else 760; by = 1560 if st else 1090; sc = 1720 if st else 1222
    return f'''<div style="width: 1080px; height: {H}px; position: relative; overflow: hidden; background: #050510; font-family: 'Chakra Petch', sans-serif; color: #ffffff">
<img src="{IMG['re1']}" alt="Helix e stack di piercing alla cartilagine, lavoro di Rebecca" style="position: absolute; left: 0; top: 0; width: 1080px; height: {ph}px; object-fit: cover; object-position: 60% 30%">
<div style="position: absolute; left: 0; top: 0; width: 1080px; height: {300 if st else 230}px; background: linear-gradient(180deg, #050510 0%, rgba(5,5,16,0.8) 55%, rgba(5,5,16,0) 100%)"></div>
<div style="position: absolute; left: 0; top: {ph - 420}px; width: 1080px; height: 420px; background: linear-gradient(0deg, #050510 0%, rgba(5,5,16,0.85) 45%, rgba(5,5,16,0) 100%)"></div>
<img src="{LET}" alt="Teenage Dirtbag" style="position: absolute; left: 80px; top: {60 if st else 26}px; width: {250 if st else 220}px; height: {181 if st else 159}px">
<img src="{BOC}" alt="Logo bocca Teenage Dirtbag" style="position: absolute; left: {800 if st else 830}px; top: {50 if st else 16}px; width: {200 if st else 170}px; height: {200 if st else 170}px; filter: drop-shadow(0 0 22px rgba(176,38,255,0.75))">
<div style="position: absolute; left: 80px; top: {ty}px; width: 920px; display: flex; flex-direction: column; align-items: center; gap: 8px; text-align: center">
<div style="font-weight: 600; font-size: {28 if st else 26}px; letter-spacing: 8px; color: #00E5FF">PIERCING · LA GUIDA</div>
<div style="font-family: 'Oswald', sans-serif; font-weight: 700; font-size: {96 if st else 84}px; line-height: 1; letter-spacing: 1px; color: #C9CDD4; text-shadow: 0 2px 0 #ffffff, 0 0 24px rgba(176,38,255,0.45)">HELIX: <span style="color: #B026FF; -webkit-text-stroke: 3px #ffffff">LA VERITÀ</span></div>
<div style="font-family: 'Oswald', sans-serif; font-weight: 700; font-size: {56 if st else 50}px; letter-spacing: 3px; color: #ffffff">SULLA GUARIGIONE</div>
<div style="font-style: italic; font-size: {28 if st else 26}px; color: #ffffff; opacity: 0.85">6-12 mesi, sì · i consigli di Rebecca @beb_piercing</div>
</div>
<a href="{U0902}" style="position: absolute; left: 80px; top: {by}px; width: 920px; height: {112 if st else 104}px; box-sizing: border-box; border-radius: 26px; background: #B026FF; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 2px; color: #ffffff; box-shadow: 0 0 30px rgba(176,38,255,0.45)">
<span style="font-family: 'Oswald', sans-serif; font-weight: 700; font-size: {48 if st else 44}px; letter-spacing: 2px; line-height: 1.05">SCOPRI DI PIÙ</span>
<span style="font-style: italic; font-size: 22px">fasi, errori da evitare e downsize ✨</span>
</a>
<img src="{SCA}" alt="Scalapay - paga a rate" style="position: absolute; left: 445px; top: {sc}px; width: 190px; height: 60px">
</div>'''
save('k0902-post.dc.html', page('Helix · grafica WhatsApp', 'chrome', chrome_visual(1350), 1080, 1350))
save('k0902-storia.dc.html', page('Helix · storia IG', 'chrome', chrome_visual(1920), 1080, 1920))

def cp(t, b):
    return f'<p style="margin: 0; font-size: 16px; line-height: 1.55"><b style="color: #00E5FF">{t}</b><br>{b}</p>'
def cimg(i, alt, h, pos, cap):
    return f'''<img src="{IMG[i]}" alt="{alt}" style="width: 520px; height: {h}px; object-fit: cover; object-position: {pos}; margin: 24px 40px 0 40px; border-radius: 14px">
<div style="margin: 8px 40px 0 40px; text-align: center; font-size: 13px; color: #C9CDD4">{cap}</div>'''
news0902 = f'''<div style="width: 600px; height: 3300px; box-sizing: border-box; background: #050510; font-family: 'Chakra Petch', sans-serif; color: #ffffff; display: flex; flex-direction: column">
<div style="display: flex; justify-content: space-between; align-items: center; padding: 24px 32px">
<img src="{LET}" alt="Teenage Dirtbag" style="width: 150px; height: 108px">
<img src="{BOC}" alt="Logo bocca" style="width: 112px; height: 112px; filter: drop-shadow(0 0 16px rgba(176,38,255,0.7))">
</div>
<img src="{IMG['re1']}" alt="Helix e stack alla cartilagine, lavoro di Rebecca" style="width: 600px; height: 480px; object-fit: cover; object-position: 60% 25%">
<div style="padding: 34px 40px 0 40px; display: flex; flex-direction: column; gap: 14px">
<div style="font-size: 15px; font-weight: 600; letter-spacing: 6px; color: #00E5FF">PIERCING · LA GUIDA</div>
<div style="font-family: 'Oswald', sans-serif; font-weight: 700; font-size: 46px; line-height: 1.02; color: #B026FF; text-shadow: -1px -1px 0 #ffffff, 1px -1px 0 #ffffff, -1px 1px 0 #ffffff, 1px 1px 0 #ffffff">HELIX: LA VERITÀ SULLA GUARIGIONE</div>
<p style="margin: 0; font-size: 17px; line-height: 1.6; color: #C9CDD4">È il piercing alla cartilagine più chiesto in studio. E la domanda è sempre la stessa: quanto ci mette a guarire? Risposta onesta: <b style="color: #ffffff">da 6 a 12 mesi</b>. Ma con le mosse giuste vive benissimo da subito. ⚡</p>
</div>
<div style="margin: 24px 40px 0 40px; padding: 24px; border: 1px solid #B026FF; border-radius: 14px; background: #2A1440; display: flex; flex-direction: column; gap: 16px">
{cp('🗓️ LE QUATTRO FASI', 'Prima settimana: caldo, rosso, sensibile — tutto normale. Settimane 2-8: la pelle fuori si chiude e si fanno le crosticine di linfa. Mesi 2-5: sembra guarito, ma dentro la cartilagine lavora ancora. Dal sesto mese in poi: guarito davvero.')}
{cp('📏 IL DOWNSIZE NON SI SALTA', 'Fra la sesta e l’ottava settimana la barretta va accorciata: quella montata il primo giorno è più lunga apposta per il gonfiore. Tenerla mesi significa agganci, urti e piercing storto.')}
{cp('🔩 TITANIO IMPLANT-GRADE', 'O oro massiccio. I metalli misteriosi da bancarella sono la prima causa delle irritazioni che vediamo arrivare in studio.')}
</div>
{cimg('re2', 'Orecchio con helix e lobi curati, lavoro di Rebecca', 380, '50% 40%', 'helix + lobi: ogni foro ha i suoi tempi · lavoro di Rebecca')}
<div style="margin: 24px 40px 0 40px; padding: 24px; border: 1px solid #B026FF; border-radius: 14px; background: #2A1440; display: flex; flex-direction: column; gap: 16px">
{cp('😴 L’ERRORE N°1: DORMIRCI SOPRA', 'La pressione del cuscino è la causa principale di bump e fori storti. Lato opposto, o cuscino con il buco: funziona.')}
{cp('🧼 LA CURA È NOIOSA MA CORTA', 'Soluzione salina sterile due volte al giorno, asciugare bene, mani lontane. Le crosticine cadono da sole: strapparle riapre tutto.')}
{cp('🚨 NORMALE VS NO', 'Prurito e sensibilità che va e viene: normale. Pallina rossa che cresce, gonfiore che ingloba il gioiello, dolore in aumento: si viene a far vedere, subito.')}
</div>
{cimg('re3', 'Stack di orecchini su lobo e cartilagine, lavoro di Rebecca', 340, '50% 35%', 'il progetto orecchio si costruisce un foro alla volta 💎 · lavoro di Rebecca')}
<div style="margin: 24px 40px 0 40px; padding: 18px 20px; border: 2px solid #00E5FF; border-radius: 14px; font-size: 15px; line-height: 1.55; box-shadow: 0 0 22px rgba(0,229,255,0.2)"><b style="color: #00E5FF">💎 IL CONSIGLIO DI REBECCA</b><br>«L’helix non si giudica a occhio: sembra guarito mesi prima di esserlo davvero. Prima di cambiare gioiello passa da me, il controllo è gratis e ti eviti di ricominciare da capo.»<br>👉 seguila su Instagram: <a href="https://www.instagram.com/beb_piercing/">@beb_piercing</a></div>
<div style="margin: 24px 40px 0 40px; height: 260px; background: #000000; border: 1px solid #B026FF; border-radius: 14px; overflow: hidden; position: relative; display: flex; align-items: center; justify-content: center"><img src="{IMG['gif0902']}" alt="GIF divertente della campagna" style="max-width: 100%; max-height: 100%; object-fit: contain; display: block"><div style="position: absolute; right: 10px; bottom: 10px; background: #B026FF; color: #ffffff; font-size: 12px; font-weight: 700; letter-spacing: 1px; padding: 5px 12px; border-radius: 999px">▶ ANIMATA NELLA MAIL</div></div>
<div style="margin: 10px 40px 0 40px; text-align: center; font-style: italic; font-size: 16px; color: #C9CDD4">le orecchie più famose della galassia approvano 🖖</div>
<a href="{WA}" style="margin: 26px 40px 0 40px; height: 96px; border-radius: 20px; background: #B026FF; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 2px; color: #ffffff; text-decoration: none; box-shadow: 0 0 26px rgba(176,38,255,0.45)">
<span style="font-family: 'Oswald', sans-serif; font-weight: 700; font-size: 34px; letter-spacing: 2px; line-height: 1.05">📲 CHIEDICI INFO</span>
<span style="font-style: italic; font-size: 15px">dubbi sul tuo helix? scrivici ✨</span>
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
<div style="font-size: 12px; color: #C9CDD4; text-align: center">📍 Via Giardini 86, Pavullo nel Frignano (MO)<br>Fonte: The Curated Lobe · Foto: lavori di Rebecca · @beb_piercing · GIF: Pinterest · janiebellbraddo (Star Trek, 1966)<br>© Teenage Dirtbag Tattoo Studio · Annulla iscrizione</div>
</div>
</div>'''
save('k0902-news.dc.html', page('Helix · newsletter', 'chrome', news0902, 600, 3300, news=True))

# ================= PINK · 11/02 DURATA PMU =================
U1102 = 'https://eepurl.com/cmLIqJMtWs'
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
    E = 210 if st else 0; e = E // 2
    box_y = 838 + o + E
    return f'''<div style="width: 1080px; height: {H}px; position: relative; overflow: hidden; background: linear-gradient(180deg,#FFE1ED 0%,#FFF4F8 50%,#FFE6F0 100%); font-family: 'Fredoka', sans-serif; color: #5A2A4A">
{SPARK.format(a=300 + o, b=180 + o, c=760 + o, d=820 + o)}
<img src="{LET}" alt="Teenage Dirtbag" style="position: absolute; left: 80px; top: {34 + (40 if st else 0)}px; width: 300px; height: 217px">
<div style="position: absolute; left: 742px; top: {14 + (40 if st else 0)}px; width: 258px; height: 258px; border-radius: 50%; background: radial-gradient(circle,rgba(255,156,196,.55) 0%,rgba(255,156,196,0) 70%)"></div>
<img src="{BOC}" alt="Logo bocca Teenage Dirtbag" style="position: absolute; left: 752px; top: {24 + (40 if st else 0)}px; width: 240px; height: 240px">
{frame('fe1', 'Lip blush guarito, lavoro di Federica', 80, 276 + o, 500, 536 + E, '50% 85%', 40)}
{frame('fe2', 'Sopracciglia in trucco permanente, lavoro di Federica', 600, 276 + o, 400, 260 + e, '50% 45%')}
{frame('fe3', 'Federica al lavoro su un trucco permanente', 600, 552 + o + e, 400, 260 + e, '50% 30%')}
{pill(100, 740 + o + E, 460, '💋 labbra', 28)}
{pill(610, 472 + o + e, 380, '✨ sopracciglia')}
{pill(610, 748 + o + E, 380, '🖊️ il ritocco')}
<div style="position: absolute; left: 80px; top: {box_y}px; width: 920px; height: 400px; border-radius: 48px; background: rgba(255,255,255,.95); border: 4px solid #FFB3CF; box-shadow: 0 14px 40px rgba(240,80,140,.18); box-sizing: border-box"></div>
<div style="position: absolute; left: 80px; width: 920px; top: {box_y + 18}px; text-align: center; font-weight: 700; font-size: 100px; line-height: 1; color: #B026FF; text-shadow: 0 6px 0 #FFD1E3">QUANTO DURA? 💗</div>
<div style="position: absolute; left: 80px; width: 920px; top: {box_y + 134}px; text-align: center; font-family: 'Dancing Script', cursive; font-weight: 700; font-size: 50px; color: #F0508C">il trucco permanente, spiegato semplice</div>
<div style="position: absolute; left: 80px; width: 920px; top: {box_y + 204}px; text-align: center; font-family: 'Quicksand', sans-serif; font-weight: 700; font-size: 28px; line-height: 1; color: #B0577F">i consigli di Federica · @favalorofederica_pmu 🌸</div>
<a href="{U1102}" style="position: absolute; left: 140px; top: {box_y + 268}px; width: 800px; height: 104px; border-radius: 999px; background: #B026FF; box-shadow: 0 8px 0 #8A16D0; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 4px; color: #ffffff">
<span style="font-weight: 600; font-size: 40px; line-height: 1; letter-spacing: 1px">SCOPRI DI PIÙ</span>
<span style="font-family: 'Quicksand', sans-serif; font-weight: 700; font-size: 22px">durata, sbiadimento e ritocchi: tutte le risposte 💕</span>
</a>
<img src="{SCA}" alt="Scalapay - paga a rate" style="position: absolute; left: 445px; top: {box_y + 418}px; width: 190px; height: 60px">
</div>'''
save('k1102-post.dc.html', page('Durata trucco permanente · grafica WhatsApp', 'pink', pink_visual(1350), 1080, 1350))
save('k1102-storia.dc.html', page('Durata trucco permanente · storia IG', 'pink', pink_visual(1920), 1080, 1920))

def pp(t, b):
    return f'<p style="margin: 0; font-size: 16px; line-height: 1.55"><b style="color: #F0508C">{t}</b><br>{b}</p>'
BOX = 'margin: 26px 40px 0 40px; padding: 24px; background: #ffffff; border: 3px solid #FFB3CF; border-radius: 24px; display: flex; flex-direction: column; gap: 16px'
news1102 = f'''<div style="width: 600px; height: 3500px; box-sizing: border-box; background: #FFF3F7; font-family: 'Quicksand', sans-serif; color: #5A2A4A; display: flex; flex-direction: column">
<div style="display: flex; justify-content: space-between; align-items: center; padding: 24px 32px">
<img src="{LET}" alt="Teenage Dirtbag" style="width: 150px; height: 108px">
<img src="{BOC}" alt="Logo bocca" style="width: 112px; height: 112px">
</div>
<div style="padding: 10px 40px 0 40px; display: flex; flex-direction: column; align-items: center; gap: 6px; text-align: center">
<div style="font-family: 'Fredoka', sans-serif; font-size: 15px; font-weight: 600; letter-spacing: 5px; color: #F0508C">💗 TRUCCO PERMANENTE · PMU 💗</div>
<div style="font-family: 'Fredoka', sans-serif; font-weight: 700; font-size: 66px; line-height: 1; color: #B026FF; text-shadow: 0 5px 0 #FFD1E3">QUANTO DURA?</div>
<div style="font-family: 'Dancing Script', cursive; font-weight: 700; font-size: 34px; line-height: 1.1; color: #F0508C">la domanda che ci fate tutte, con la risposta vera</div>
</div>
<img src="{IMG['fe1']}" alt="Lip blush guarito, lavoro di Federica" style="width: 520px; height: 420px; object-fit: cover; object-position: 50% 80%; margin: 24px 40px 0 40px; border-radius: 24px">
<div style="margin: 8px 40px 0 40px; text-align: center; font-size: 14px; font-weight: 700; color: #B0577F">lip blush di Federica: il colore che ti svegli addosso 💋</div>
<div style="padding: 26px 40px 0 40px; display: flex; flex-direction: column; gap: 14px">
<p style="margin: 0; font-size: 17px; line-height: 1.65">La risposta corta: <b>circa 2 anni</b>. La risposta vera: dipende da te. Il trucco permanente è <b>duraturo ma non definitivo</b> — e questa è la sua forza, non un difetto. 🌸</p>
</div>
<div style="{BOX}">
{pp('⏳ PERCHÉ SBIADISCE (ED È GIUSTO COSÌ)', 'I pigmenti sono bioriassorbibili: il corpo li smaltisce piano piano. Niente sopracciglia blu fra dieci anni, niente colore che vira: svanisce con grazia.')}
{pp('☀️ COSA LO ACCORCIA', 'Sole senza protezione, pelle grassa, acidi ed esfolianti in skincare, ricambio cellulare veloce. Le tonalità chiare se ne vanno prima delle scure.')}
{pp('💋 LE LABBRA FANNO STORIA A SÉ', 'Il colore appena fatto è intenso, poi schiarisce già nei primi giorni e si assesta su un effetto naturale. Non è sbiadito: è guarito.')}
</div>
<div style="margin: 26px 40px 0 40px; display: flex; gap: 10px">
<img src="{IMG['fe2']}" alt="Sopracciglia in trucco permanente, lavoro di Federica" style="width: 255px; height: 220px; object-fit: cover; object-position: 50% 45%; border-radius: 18px">
<img src="{IMG['fe3']}" alt="Federica al lavoro", style="width: 255px; height: 220px; object-fit: cover; object-position: 50% 30%; border-radius: 18px">
</div>
<div style="margin: 8px 40px 0 40px; text-align: center; font-size: 14px; font-weight: 700; color: #B0577F">sopracciglia pelo a pelo ✨ · Federica all’opera 🖊️</div>
<div style="{BOX}">
{pp('🗓️ IL RITOCCO È PARTE DEL GIOCO', 'Un refresh ogni 6-12 mesi tiene il colore vivo e la forma precisa. Costa una frazione del lavoro iniziale e si prenota in un messaggio.')}
{pp('🧴 FARLO DURARE DI PIÙ SI PUÒ', 'SPF sulla zona trattata tutto l’anno, niente acidi e scrub sopra il pigmento, crema post-trattamento finché la pelle guarisce.')}
{pp('🙅 LE CROSTICINE NON SI TOCCANO', 'Nei primi giorni il colore sembra troppo intenso e poi spellicola: cade tutto da solo. Chi gratta si porta via anche il pigmento.')}
</div>
<div style="margin: 26px 40px 0 40px; padding: 24px; background: #FFE1ED; border-radius: 24px; display: flex; flex-direction: column; gap: 10px">
<div style="font-family: 'Fredoka', sans-serif; font-weight: 600; font-size: 24px; color: #B026FF; text-align: center">IL CALENDARIO DEL COLORE 🌷</div>
<p style="margin: 0; font-size: 16px; line-height: 1.55">💧 <b>Giorni 1-7:</b> colore intenso, poi spellicola e schiarisce. Tutto previsto.</p>
<p style="margin: 0; font-size: 16px; line-height: 1.55">🌸 <b>Primo mese:</b> il pigmento si assesta e mostra il tono vero.</p>
<p style="margin: 0; font-size: 16px; line-height: 1.55">✨ <b>6-12 mesi:</b> finestra ideale per il ritocco che lo riporta al massimo.</p>
<p style="margin: 0; font-size: 16px; line-height: 1.55">💗 <b>~2 anni:</b> sbiadito con grazia: puoi rifarlo, cambiarlo o lasciarlo andare.</p>
</div>
<div style="margin: 26px 40px 0 40px; padding: 22px 24px; background: #ffffff; border: 3px solid #FFB3CF; border-radius: 24px; font-size: 16px; line-height: 1.55; text-align: center"><b style="color: #B026FF; font-family: 'Fredoka', sans-serif; font-size: 22px">IL CONSIGLIO DI FEDERICA 💕</b><br>«Il trucco permanente non si giudica il terzo giorno e nemmeno al terzo mese: si coccola. SPF e niente scrub sopra, e il ritocco annuale te lo tiene come appena fatto.»<br><a href="https://www.instagram.com/favalorofederica_pmu/" style="display: inline-block; margin-top: 12px; padding: 10px 22px; border-radius: 999px; background: #FFE1ED; color: #B026FF; font-weight: 700">✨ guarda i suoi lavori: @favalorofederica_pmu</a></div>
<div style="margin: 26px 40px 0 40px; height: 270px; background: #ffffff; border: 3px solid #FFB3CF; border-radius: 24px; overflow: hidden; position: relative; display: flex; align-items: center; justify-content: center"><img src="{IMG['gif1102']}" alt="GIF divertente della campagna" style="max-width: 100%; max-height: 100%; object-fit: contain; display: block"><div style="position: absolute; right: 10px; bottom: 10px; background: #B026FF; color: #ffffff; font-size: 12px; font-weight: 700; letter-spacing: 1px; padding: 5px 12px; border-radius: 999px">▶ ANIMATA NELLA MAIL</div></div>
<div style="margin: 10px 40px 0 40px; text-align: center; font-family: 'Dancing Script', cursive; font-weight: 700; font-size: 24px; color: #F0508C">io che mi sveglio già truccata: energia Elle Woods 💅</div>
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
<div style="font-size: 12px; text-align: center; color: #B0577F">📍 Via Giardini 86, Pavullo nel Frignano (MO)<br>Fonte: DiLei Bellezza · Foto: lavori di Federica · @favalorofederica_pmu · GIF: Pinterest · lizzy9441 (La rivincita delle bionde, 2001)<br>© Teenage Dirtbag Tattoo Studio · Annulla iscrizione</div>
</div>
</div>'''
save('k1102-news.dc.html', page('Durata trucco permanente · newsletter', 'pink', news1102, 600, 3500, news=True))
print('DONE')
