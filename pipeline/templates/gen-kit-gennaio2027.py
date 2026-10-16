#!/usr/bin/env python3
# Kit informativi gennaio 2027: 0901 septum, 1201 lip blush, 1401 traditional, 1601 dotwork, 1901 ago vs pistola, 2101 sopracciglia.
import os
SP = os.environ['KIT_SP'] + '/kitall/project/'
os.makedirs(SP, exist_ok=True)
src = open(os.environ['KIT_SP'] + '/kitassets/pipeline/templates/gen-kit-esempio.py').read()
exec(src.split('# ---- 24/10 Patchwork ----')[0].replace("SP = os.environ.get('KIT_SP','/tmp/kit') + '/kitall/project/'", ''))
SP = os.environ['KIT_SP'] + '/kitall/project/'
_l = src.split('\n')
def _block(start, end):
    a = next(i for i, x in enumerate(_l) if x.startswith(start)); b = next(i for i, x in enumerate(_l) if i > a and x.startswith(end))
    return '\n'.join(_l[a:b])
exec(_block('def cp(', 'news0711 ='))
exec(_block("SPARK = '''", 'def pink_visual('))
exec(_block('def pp(', 'news1411 ='))
def save(name, html):
    open(SP + name, 'w').write(html); print('wrote', name)

IMG.update({k: B(v) for k, v in {
 'se1': '5b75a9718de2d227896e521073e958d5', 'se2': '1ac0b93705b41f102e3f93b540af66bc', 'se3': 'bda6bd038e93ec2e68e852a6fb711993',
 'ag1': '60ea5c63d4dc7863c6c3f5c70cb37261', 'ag2': '398c879cc66189eacff000705f4163d8', 'ag3': '7da7a891719984ec2b5d86620c5c765a', 'ag4': 'd3979d2842390780590c3e0bdb14de8f',
 'lb1': '25bf07407ae5548cafa68a21548a6b64', 'lb2': '5a3ad50d47904e1fd9aa239a5330f0f6', 'lb3': '46d754350d76bec3dc36e15b528a9fd1',
 'br1': 'a9dde570d7f7a9fd646455d0fb5bd3eb', 'br2': '73269d00c8a1a56d12d105b430050d33', 'br3': '6318105911869b73a54316f6d4f39ae8',
 'tr1': '81f04a96c13c8bc0a0625ccd536b3362', 'tr2': 'f9add7bc1015219b70af8d453580db06', 'tr3': '935f25aadfe61d2c8081de86c9bac346', 'tr4': '963e0099b3a4f46f15f4c0fa4907366a',
 'dw1': '6c0f59809dd36fba8c633969c76ae6f9', 'dw2': '3eda06fc2cbc405bee52c24f1ae1f534', 'dw3': '48cadde224b78b9cbec5b8d33868ddb4', 'dw4': 'df7a7454ef515524ad47092bff3ffc32',
 'gif0901': 'ae46856809d57a907bfe20df1c0f23c9', 'gif1201': '73ab2b65a277ab8c0cb00af6099f66a0', 'gif1401': 'bac494605876471ac1c11c6d7d55be06',
 'gif1601': '0534ba937ca567bfeaf8202844ab184e', 'gif1901': '8e2ffb16d5c48fe06a1af85411739b85', 'gif2101': '924824e08e83c6f5b2b7a187b3badb31'}.items()})

REB_BOX = '<b style="color: #B026FF">💜 IL CONSIGLIO DI REBECCA</b><br>«{tip}»<br>👉 seguila su Instagram: <a href="https://www.instagram.com/beb_piercing/">@beb_piercing</a>'

# ============ ZINE: 1401 traditional (tattoo) ============
U1401 = 'https://eepurl.com/umT3u_DINr'
args = ('tr1', 'Foglio flash traditional con aquila, nave, ancora e pantera', '50% 50%', 'tr2', 'Pantera traditional sul braccio', '85% 35%',
        'traditional americano ⚓', 'BOLD', 'WILL HOLD')
save('k1401-post.dc.html', page('Traditional · grafica WhatsApp', 'zine', zine_visual('1401', 1350, *args, 'linea spessa, pochi colori pieni: perché non passa mai ⚓', 'la storia dello stile nato nei porti 🦅', U1401), 1080, 1350))
save('k1401-storia.dc.html', page('Traditional · storia IG', 'zine', zine_visual('1401', 1920, *args, 'linea spessa, colori pieni, zero tempo ⚓', 'la storia dello stile nato nei porti 🦅', U1401), 1080, 1920))
save('k1401-news.dc.html', page('Traditional · newsletter', 'zine', zine_news('1401', 'lo stile nato nei porti ⚓', 'BOLD WILL HOLD:', 'IL TRADITIONAL NON PASSA MAI',
    "Linea spessa, pochi colori pieni, soggetti che riconosci da lontano. Il <b>traditional americano</b> è nato tra porti e marinai ed è ancora lo stile che <b>invecchia meglio sulla pelle</b>. ⚓",
    zpair('tr1', 'Foglio flash traditional', '50% 50%', 'tr2', 'Pantera traditional sul braccio', '85% 35%', 'foto: Pinterest').replace('margin: 24px 40px 0 40px', 'margin: 30px 40px 0 40px'),
    [('⚓ NATO NEI PORTI', 'Nel Novecento i tatuatori di porto disegnavano i <b>flash</b>: fogli di soggetti pronti da scegliere sul muro. Il nome più famoso è <b>Sailor Jerry</b>, a Honolulu.'),
     ('🖤 LINEA SPESSA = DURA NEL TEMPO', 'Il motto è <b>bold will hold</b>: contorni pieni e neri che tra vent’anni si leggono ancora, anche quando la pelle cambia.'),
     ('🎨 POCHI COLORI, MA PIENI', 'Rosso, giallo, verde e nero, stesi pieni. Niente sfumature infinite: il colore si vede da lontano.')],
    zpair('tr3', 'Rondine traditional sulla mano', '50% 50%', 'tr4', 'Testa di pantera traditional', '50% 40%', 'foto: Pinterest', '0.8deg', '#FF2E88'),
    'la rondine per tornare a casa, la pantera per la grinta 🐦🐆',
    [('🐦 I SOGGETTI HANNO UN SIGNIFICATO', 'La rondine per il ritorno a casa, l’ancora per la stabilità, poi la rosa, il pugnale, la pantera. Puoi scegliere il classico o farlo tuo.'),
     ('🧩 PERFETTO PER IL PATCHWORK', 'Pezzi piccoli e leggibili che stanno bene vicini: è lo stile ideale per riempire un braccio un tatuaggio alla volta.'),
     ('📏 LA MISURA CONTA', 'Il traditional vive di contrasto: se lo stringi troppo, i neri si chiudono e il disegno si impasta.')],
    'Nel traditional conta la leggibilità: scegli una misura che si legga da un metro di distanza. Più piccolo non vuol dire più elegante, vuol dire più confuso tra qualche anno.',
    'io che esco dallo studio con la mia prima ancora ⚓💪',
    'hai già in mente il tuo soggetto? scrivici 🖤',
    'Foto: Pinterest · GIF: Pinterest (Popeye)',
    '⚓ Ci vediamo in studio 💜'), 600, 3300, news=True))

# ============ ZINE: 1901 ago vs pistola (piercing, solo Rebecca) ============
U1901 = 'https://eepurl.com/WvM018q0CS'
args = ('ag1', 'Orecchio con helix e conch fatti ad ago da Rebecca', '50% 40%', 'ag2', 'Helix in titanio fatto ad ago', '50% 35%',
        'piercing fatto bene 💉', 'PISTOLA NO,', 'AGO SÌ')
nv = lambda H, k, b: zine_visual('1901', H, *args, k, b, U1901)
save('k1901-post.dc.html', page('Ago vs pistola · grafica WhatsApp', 'zine', nv(1350, 'perché in studio si buca solo con l’ago 💉', 'cosa cambia davvero per il tuo foro ✨'), 1080, 1350))
save('k1901-storia.dc.html', page('Ago vs pistola · storia IG', 'zine', nv(1920, 'in studio si buca solo con l’ago 💉', 'cosa cambia davvero per il tuo foro ✨'), 1080, 1920))
n1901 = zine_news('1901', 'come si fa davvero un piercing 💉', 'PISTOLA NO,', 'AGO SÌ',
    "Il buco “al volo” fatto con la pistola sembra la stessa cosa di un piercing fatto in studio. <b>Non lo è</b>: cambiano lo strumento, il gioiello e soprattutto la <b>guarigione</b>. 🖤",
    zpair('ag1', 'Orecchio con helix e conch fatti ad ago', '50% 40%', 'ag2', 'Helix in titanio', '50% 35%', 'lavori di Rebecca · @beb_piercing').replace('margin: 24px 40px 0 40px', 'margin: 30px 40px 0 40px'),
    [('💉 L’AGO TAGLIA, LA PISTOLA SPINGE', 'L’ago cavo apre un canale pulito. La pistola spinge l’orecchino a forza attraverso il tessuto: più trauma, guarigione più lunga e più capricciosa.'),
     ('🧼 MONOUSO E STERILE', 'In studio ago e gioiello sono sterili e monouso, aperti davanti a te. La pistola ha parti in plastica che non si sterilizzano come si deve.'),
     ('🦻 CARTILAGINE: MAI CON LA PISTOLA', 'Elice, trago, conch: sulla cartilagine la pistola è la scelta peggiore. Si fa con l’ago, sempre.')],
    zpair('ag3', 'Lobo e helix con gioielli in titanio', '50% 40%', 'ag4', 'Orecchio curato con più fori', '50% 35%', 'lavori di Rebecca · @beb_piercing', '0.8deg', '#FF2E88'),
    'fori posizionati sulla tua anatomia, non dove arriva lo strumento 📍',
    [('🔩 IL GIOIELLO GIUSTO', 'L’orecchino della pistola è corto e stringe quando arriva il gonfiore. In studio si parte con titanio implant-grade e lo spazio giusto.'),
     ('📍 IL PUNTO SI SCEGLIE', 'Con l’ago il foro si posiziona sulla tua anatomia: conta per l’estetica e per guarire bene.'),
     ('🔁 GIÀ FATTO CON LA PISTOLA?', 'Nessun dramma: passa in studio, controlliamo foro e gioiello e, se serve, lo sistemiamo.')],
    'TIP',
    'io quando mi propongono la pistola per l’elice ✂️😶',
    'hai un foro fatto con la pistola che ti dà noia? scrivici ✨',
    'Foto: lavori di Rebecca · @beb_piercing · GIF: Pinterest (Edward mani di forbice, 1990)',
    '💉 Ci vediamo in studio 💜')
tip_old = n1901.split('<b style="color: #B026FF">🖤 IL CONSIGLIO DI FILIPPO</b>')[1].split('</div>')[0]
n1901 = n1901.replace('<b style="color: #B026FF">🖤 IL CONSIGLIO DI FILIPPO</b>' + tip_old,
    REB_BOX.format(tip='Prima di bucare chiedi sempre di vedere ago e gioiello aperti davanti a te: è un tuo diritto, e chi lavora bene è contento di mostrarteli.'))
save('k1901-news.dc.html', page('Ago vs pistola · newsletter', 'zine', n1901, 600, 3300, news=True))

# ============ CHROME: 0901 septum (Rebecca) e 1601 dotwork (Filippo) ============
def chrome_visual2(H, hero, alt, pos, kick, t1, t2, t3, sub, url, btn):
    st = H == 1920
    ph = 1300 if st else 1000
    ty = 1150 if st else 760; by = 1560 if st else 1090; sc = 1720 if st else 1222
    return f'''<div style="width: 1080px; height: {H}px; position: relative; overflow: hidden; background: #050510; font-family: 'Chakra Petch', sans-serif; color: #ffffff">
<img src="{IMG[hero]}" alt="{alt}" style="position: absolute; left: 0; top: 0; width: 1080px; height: {ph}px; object-fit: cover; object-position: {pos}">
<div style="position: absolute; left: 0; top: 0; width: 1080px; height: {300 if st else 230}px; background: linear-gradient(180deg, #050510 0%, rgba(5,5,16,0.8) 55%, rgba(5,5,16,0) 100%)"></div>
<div style="position: absolute; left: 0; top: {ph - 420}px; width: 1080px; height: 420px; background: linear-gradient(0deg, #050510 0%, rgba(5,5,16,0.85) 45%, rgba(5,5,16,0) 100%)"></div>
<img src="{LET}" alt="Teenage Dirtbag" style="position: absolute; left: 80px; top: {60 if st else 26}px; width: {250 if st else 220}px; height: {181 if st else 159}px">
<img src="{BOC}" alt="Logo bocca Teenage Dirtbag" style="position: absolute; left: {800 if st else 830}px; top: {50 if st else 16}px; width: {200 if st else 170}px; height: {200 if st else 170}px; filter: drop-shadow(0 0 22px rgba(176,38,255,0.75))">
<div style="position: absolute; left: 80px; top: {ty}px; width: 920px; display: flex; flex-direction: column; align-items: center; gap: 8px; text-align: center">
<div style="font-weight: 600; font-size: {28 if st else 26}px; letter-spacing: 8px; color: #00E5FF">{kick}</div>
<div style="font-family: 'Oswald', sans-serif; font-weight: 700; font-size: {96 if st else 84}px; line-height: 1; letter-spacing: 1px; color: #C9CDD4; text-shadow: 0 2px 0 #ffffff, 0 0 24px rgba(176,38,255,0.45)">{t1} <span style="color: #B026FF; -webkit-text-stroke: 3px #ffffff">{t2}</span></div>
<div style="font-family: 'Oswald', sans-serif; font-weight: 700; font-size: {56 if st else 50}px; letter-spacing: 3px; color: #ffffff">{t3}</div>
<div style="font-style: italic; font-size: {28 if st else 26}px; color: #ffffff; opacity: 0.85">{sub}</div>
</div>
<a href="{url}" style="position: absolute; left: 80px; top: {by}px; width: 920px; height: {112 if st else 104}px; box-sizing: border-box; border-radius: 26px; background: #B026FF; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 2px; color: #ffffff; box-shadow: 0 0 30px rgba(176,38,255,0.45)">
<span style="font-family: 'Oswald', sans-serif; font-weight: 700; font-size: {48 if st else 44}px; letter-spacing: 2px; line-height: 1.05">SCOPRI DI PIÙ</span>
<span style="font-style: italic; font-size: 22px">{btn}</span>
</a>
<img src="{SCA}" alt="Scalapay - paga a rate" style="position: absolute; left: 445px; top: {sc}px; width: 190px; height: 60px">
</div>'''

def cbox(items):
    return '<div style="margin: 24px 40px 0 40px; padding: 24px; border: 1px solid #B026FF; border-radius: 14px; background: #2A1440; display: flex; flex-direction: column; gap: 16px">\n' + '\n'.join(cp(*x) for x in items) + '\n</div>'

def chrome_news(key, hero, hero_alt, hero_pos, kick, title, intro, pts1, im2, pts2, im3, tipbox, gifcap, cta_sub, credits, bye, extra=''):
    return f'''<div style="width: 600px; height: 3300px; box-sizing: border-box; background: #050510; font-family: 'Chakra Petch', sans-serif; color: #ffffff; display: flex; flex-direction: column">
<div style="display: flex; justify-content: space-between; align-items: center; padding: 24px 32px">
<img src="{LET}" alt="Teenage Dirtbag" style="width: 150px; height: 108px">
<img src="{BOC}" alt="Logo bocca" style="width: 112px; height: 112px; filter: drop-shadow(0 0 16px rgba(176,38,255,0.7))">
</div>
<img src="{IMG[hero]}" alt="{hero_alt}" style="width: 600px; height: 480px; object-fit: cover; object-position: {hero_pos}">
<div style="padding: 34px 40px 0 40px; display: flex; flex-direction: column; gap: 14px">
<div style="font-size: 15px; font-weight: 600; letter-spacing: 6px; color: #00E5FF">{kick}</div>
<div style="font-family: 'Oswald', sans-serif; font-weight: 700; font-size: 46px; line-height: 1.02; color: #B026FF; text-shadow: -1px -1px 0 #ffffff, 1px -1px 0 #ffffff, -1px 1px 0 #ffffff, 1px 1px 0 #ffffff">{title}</div>
<p style="margin: 0; font-size: 17px; line-height: 1.6; color: #C9CDD4">{intro}</p>
</div>
{cbox(pts1)}
{cimg(*im2)}
{cbox(pts2)}
{cimg(*im3)}
<div style="margin: 24px 40px 0 40px; padding: 18px 20px; border: 2px solid #00E5FF; border-radius: 14px; font-size: 15px; line-height: 1.55; box-shadow: 0 0 22px rgba(0,229,255,0.2)">{tipbox}</div>
<div style="margin: 24px 40px 0 40px; height: 260px; background: #000000; border: 1px solid #B026FF; border-radius: 14px; overflow: hidden; position: relative; display: flex; align-items: center; justify-content: center"><img src="{IMG['gif' + key]}" alt="GIF divertente della campagna" style="max-width: 100%; max-height: 100%; object-fit: contain; display: block"><div style="position: absolute; right: 10px; bottom: 10px; background: #B026FF; color: #ffffff; font-size: 12px; font-weight: 700; letter-spacing: 1px; padding: 5px 12px; border-radius: 999px">▶ ANIMATA NELLA MAIL</div></div>
<div style="margin: 10px 40px 0 40px; text-align: center; font-style: italic; font-size: 16px; color: #C9CDD4">{gifcap}</div>
<a href="{WA}" style="margin: 26px 40px 0 40px; height: 96px; border-radius: 20px; background: #B026FF; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 2px; color: #ffffff; text-decoration: none; box-shadow: 0 0 26px rgba(176,38,255,0.45)">
<span style="font-family: 'Oswald', sans-serif; font-weight: 700; font-size: 34px; letter-spacing: 2px; line-height: 1.05">📲 CHIEDICI INFO</span>
<span style="font-style: italic; font-size: 15px">{cta_sub}</span>
</a>
{extra}
<div style="margin: 26px 40px 0 40px; padding: 22px; background: #000000; border: 2px solid #25D366; border-radius: 14px; display: flex; flex-direction: column; align-items: center; gap: 10px; text-align: center">
<div style="font-family: 'Oswald', sans-serif; font-weight: 700; font-size: 24px; letter-spacing: 2px">🎁 GRUPPO TEENAGE VIP</div>
<div style="font-size: 15px; color: #C9CDD4">SOLO LÌ vengono pubblicate le OFFERTE e i LAST MINUTE</div>
<a href="{VIPL}" style="padding: 12px 26px; border-radius: 999px; background: #25D366; color: #000000; font-weight: 700; font-size: 16px; text-decoration: none">UNISCITI AL GRUPPO VIP</a>
</div>
<div style="margin-top: auto; padding: 28px 40px 32px 40px; display: flex; flex-direction: column; align-items: center; gap: 14px; border-top: 1px solid #2A1440">
<div style="font-size: 16px">{bye}</div>
{ICONS}
<img src="{SCA}" alt="Scalapay - paga a rate" style="width: 170px; height: 54px">
<div style="font-size: 12px; color: #C9CDD4; text-align: center">📍 Via Giardini 86, Pavullo nel Frignano (MO)<br>{credits}<br>© Teenage Dirtbag Tattoo Studio · Annulla iscrizione</div>
</div>
</div>'''

U0901 = 'https://eepurl.com/Cv6XO4d5I8'
v = lambda H: chrome_visual2(H, 'se1', 'Septum e labret in titanio, lavoro di Rebecca', '50% 40%', 'PIERCING · LA GUIDA', 'IL', 'SEPTUM', 'SPARISCE QUANDO VUOI TU',
                              'si gira all’insù · i consigli di Rebecca @beb_piercing', U0901, 'il piercing più discreto che ci sia ✨')
save('k0901-post.dc.html', page('Septum · grafica WhatsApp', 'chrome', v(1350), 1080, 1350))
save('k0901-storia.dc.html', page('Septum · storia IG', 'chrome', v(1920), 1080, 1920))
save('k0901-news.dc.html', page('Septum · newsletter', 'chrome', chrome_news('0901', 'se1', 'Septum a ferro di cavallo in titanio', '50% 40%', 'PIERCING · LA GUIDA',
    'SEPTUM: IL PIERCING CHE SPARISCE QUANDO VUOI TU',
    'Sembra il più audace di tutti, invece è <b style="color: #ffffff">uno dei più discreti</b>: con il gioiello giusto lo giri all’insù e nessuno lo vede. A patto di farlo nel punto giusto. ✨',
    [('🎯 IL PUNTO GIUSTO NON È LA CARTILAGINE', 'Si passa nel “sweet spot”, il sottile strato di pelle tra la cartilagine e la punta del naso. Fatto lì è più veloce e più tranquillo; storto o troppo in alto, fa male e guarisce male.'),
     ('🔄 SI GIRA ALL’INSÙ', 'Con un ferro di cavallo lo nascondi dentro la narice in un attimo: colloquio, pranzo dai nonni, foto per i documenti. Nelle prime settimane però si lascia stare.'),
     ('🔩 IL PRIMO GIOIELLO', 'Titanio implant-grade, con spazio per il gonfiore. Anelli chiusi e gioielli “da vetrina” arrivano dopo, a foro guarito.')],
    ('se2', 'Septum e labret in titanio', 380, '50% 40%', 'ferro di cavallo in titanio: liscio, leggero, senza nichel · lavoro di Rebecca'),
    [('🤧 RAFFREDDORE E SCIARPE', 'D’inverno il nemico è il fazzoletto: soffia piano e senza tirare. Occhio alle sciarpe di lana che si impigliano.'),
     ('⏳ QUANTO CI METTE', 'Le prime settimane sono le più delicate, la guarigione completa richiede qualche mese. Il cambio gioiello si fa in studio, non a casa.'),
     ('🚨 QUANDO CHIAMARCI', 'Dolore che aumenta, calore, gonfiore che non scende o secrezioni strane: non si aspetta, si viene a farlo vedere.')],
    ('se3', 'Septum visto di fronte', 340, '50% 35%', 'di fronte si vede appena: è il suo bello 💎 · lavoro di Rebecca'),
    '<b style="color: #00E5FF">💎 IL CONSIGLIO DI REBECCA</b><br>«Il septum perfetto parte dalla posizione: prima di forare guardiamo insieme il tuo naso allo specchio, poi decidiamo.»<br>👉 seguila su Instagram: <a href="https://www.instagram.com/beb_piercing/">@beb_piercing</a>',
    'io che giro il septum all’insù prima del colloquio 👀',
    'dubbi sul septum? scrivici ✨',
    'Foto: lavori di Rebecca · @beb_piercing · GIF: Pinterest (Il quinto elemento, 1997)',
    '💎 Ci vediamo in studio 💜'), 600, 3300, news=True))

U1601 = 'https://eepurl.com/Erc8xTZLTz'
v = lambda H: chrome_visual2(H, 'dw1', 'Mandala in dotwork sul braccio', '50% 45%', 'TATTOO · LO STILE', 'UN', 'PUNTINO', 'ALLA VOLTA',
                              'dotwork e ornamentale · il consiglio di Filippo @sfregio_lttr', U1601, 'mandala, geometrie e ombre fatte di punti 🔘')
save('k1601-post.dc.html', page('Dotwork · grafica WhatsApp', 'chrome', v(1350), 1080, 1350))
save('k1601-storia.dc.html', page('Dotwork · storia IG', 'chrome', v(1920), 1080, 1920))
save('k1601-news.dc.html', page('Dotwork · newsletter', 'chrome', chrome_news('1601', 'dw1', 'Mandala in dotwork sul braccio', '50% 45%', 'TATTOO · LO STILE',
    'DOTWORK: IL TATUAGGIO FATTO UN PUNTINO ALLA VOLTA',
    'Niente sfumature tirate: qui l’ombra nasce da <b style="color: #ffffff">migliaia di punti</b>, più fitti dove serve il buio e più radi dove serve la luce. È lo stile di mandala, geometrie e ornamenti che seguono il corpo. ✨',
    [('🔘 COS’È, IN DUE RIGHE', 'Il dotwork costruisce chiaroscuri con i punti invece che con le linee o le sfumature piene. L’effetto è morbido, quasi da incisione.'),
     ('🌀 ORNAMENTALE E GEOMETRICO', 'Mandala, motivi sacri, pizzi, pattern ripetuti: disegni simmetrici pensati per incorniciare una parte del corpo.'),
     ('🧭 SEGUE IL CORPO', 'Sterno, schiena, avambraccio, mano: l’ornamentale funziona quando segue la forma del muscolo. Per questo si disegna sulla persona, non solo sul foglio.')],
    ('dw4', 'Mandala in dotwork sulla mano', 380, '60% 50%', 'la mano: punti fitti per il buio, radi per la luce · foto Pinterest'),
    [('⏳ È LENTO, E VA BENE COSÌ', 'Ogni sfumatura è fatta punto per punto: le sedute sono più lunghe e i pezzi grandi si dividono in più appuntamenti.'),
     ('🌗 DA GUARITO È PIÙ MORBIDO', 'Appena fatto sembra tutto definitissimo, poi i punti si assestano e l’effetto diventa più vellutato. È il risultato giusto.'),
     ('📐 LA SIMMETRIA SI PROVA PRIMA', 'Su sterno e schiena basta un centimetro storto e si vede: lo stencil si prova e si riposiziona finché non è dritto con te in piedi.')],
    ('dw2', 'Ornamentale sullo sterno', 340, '50% 50%', 'ornamentale sotto il seno: segue la curva, non la combatte 🖤 · foto Pinterest'),
    '<b style="color: #00E5FF">🖤 IL CONSIGLIO DI FILIPPO</b><br>«Con l’ornamentale non scegliere solo il disegno: scegli la zona. Il pezzo giusto nel posto sbagliato perde metà della sua forza.»<br>👉 seguilo su Instagram: <a href="https://www.instagram.com/sfregio_lttr/">@sfregio_lttr</a>',
    'io che schivo i puntini come i proiettili 🕶️',
    'hai una zona in mente? scrivici 🖤',
    'Foto: Pinterest · GIF: Pinterest (Matrix, 1999)',
    '🔘 Ci vediamo in studio 💜'), 600, 3300, news=True))

# ============ PINK: 1201 lip blush, 2101 sopracciglia (Federica) ============
def pink_visual2(H, i0, a0, p0, i1, a1, p1, i2, a2, p2, l0, l1, l2, big, script, sub, url, btn, big_fs=112):
    st = H == 1920
    o = 130 if st else 0
    E = 210 if st else 0; e = E // 2
    box_y = 838 + o + E
    return f'''<div style="width: 1080px; height: {H}px; position: relative; overflow: hidden; background: linear-gradient(180deg,#FFE1ED 0%,#FFF4F8 50%,#FFE6F0 100%); font-family: 'Fredoka', sans-serif; color: #5A2A4A">
{SPARK.format(a=300 + o, b=180 + o, c=760 + o, d=820 + o)}
<img src="{LET}" alt="Teenage Dirtbag" style="position: absolute; left: 80px; top: {34 + (40 if st else 0)}px; width: 300px; height: 217px">
<div style="position: absolute; left: 742px; top: {14 + (40 if st else 0)}px; width: 258px; height: 258px; border-radius: 50%; background: radial-gradient(circle,rgba(255,156,196,.55) 0%,rgba(255,156,196,0) 70%)"></div>
<img src="{BOC}" alt="Logo bocca Teenage Dirtbag" style="position: absolute; left: 752px; top: {24 + (40 if st else 0)}px; width: 240px; height: 240px">
{frame(i0, a0, 80, 276 + o, 500, 536 + E, p0, 40)}
{frame(i1, a1, 600, 276 + o, 400, 260 + e, p1)}
{frame(i2, a2, 600, 552 + o + e, 400, 260 + e, p2)}
{pill(100, 740 + o + E, 460, l0, 28)}
{pill(610, 472 + o + e, 380, l1)}
{pill(610, 748 + o + E, 380, l2)}
<div style="position: absolute; left: 80px; top: {box_y}px; width: 920px; height: 400px; border-radius: 48px; background: rgba(255,255,255,.95); border: 4px solid #FFB3CF; box-shadow: 0 14px 40px rgba(240,80,140,.18); box-sizing: border-box"></div>
<div style="position: absolute; left: 80px; width: 920px; top: {box_y + 18}px; text-align: center; font-weight: 700; font-size: {big_fs}px; line-height: 1; color: #B026FF; text-shadow: 0 6px 0 #FFD1E3">{big}</div>
<div style="position: absolute; left: 80px; width: 920px; top: {box_y + 134}px; text-align: center; font-family: 'Dancing Script', cursive; font-weight: 700; font-size: 50px; color: #F0508C">{script}</div>
<div style="position: absolute; left: 80px; width: 920px; top: {box_y + 204}px; text-align: center; font-family: 'Quicksand', sans-serif; font-weight: 700; font-size: 28px; line-height: 1; color: #B0577F">{sub}</div>
<a href="{url}" style="position: absolute; left: 140px; top: {box_y + 268}px; width: 800px; height: 104px; border-radius: 999px; background: #B026FF; box-shadow: 0 8px 0 #8A16D0; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 4px; color: #ffffff">
<span style="font-weight: 600; font-size: 40px; line-height: 1; letter-spacing: 1px">SCOPRI DI PIÙ</span>
<span style="font-family: 'Quicksand', sans-serif; font-weight: 700; font-size: 22px">{btn}</span>
</a>
<img src="{SCA}" alt="Scalapay - paga a rate" style="position: absolute; left: 445px; top: {box_y + 418}px; width: 190px; height: 60px">
{'' if not st else SPARK.format(a=1500, b=1560, c=1680, d=1750).split(chr(10))[0]}
</div>'''

def pink_news(key, big, script, hero, hero_alt, hero_pos, hero_cap, intro, pts1, pair, pair_cap, pts2, heal, tip, gifcap, credits):
    return f'''<div style="width: 600px; height: 3300px; box-sizing: border-box; background: #FFF3F7; font-family: 'Quicksand', sans-serif; color: #5A2A4A; display: flex; flex-direction: column">
<div style="display: flex; justify-content: space-between; align-items: center; padding: 24px 32px">
<img src="{LET}" alt="Teenage Dirtbag" style="width: 150px; height: 108px">
<img src="{BOC}" alt="Logo bocca" style="width: 112px; height: 112px">
</div>
<div style="padding: 10px 40px 0 40px; display: flex; flex-direction: column; align-items: center; gap: 6px; text-align: center">
<div style="font-family: 'Fredoka', sans-serif; font-size: 15px; font-weight: 600; letter-spacing: 5px; color: #F0508C">💗 TRUCCO PERMANENTE · PMU 💗</div>
<div style="font-family: 'Fredoka', sans-serif; font-weight: 700; font-size: 76px; line-height: 1; color: #B026FF; text-shadow: 0 5px 0 #FFD1E3">{big}</div>
<div style="font-family: 'Dancing Script', cursive; font-weight: 700; font-size: 34px; line-height: 1.1; color: #F0508C">{script}</div>
</div>
<img src="{IMG[hero]}" alt="{hero_alt}" style="width: 520px; height: 420px; object-fit: cover; object-position: {hero_pos}; margin: 24px 40px 0 40px; border-radius: 24px">
<div style="margin: 8px 40px 0 40px; text-align: center; font-size: 14px; font-weight: 700; color: #B0577F">{hero_cap}</div>
<div style="padding: 26px 40px 0 40px; display: flex; flex-direction: column; gap: 14px">
<p style="margin: 0; font-size: 17px; line-height: 1.65">{intro}</p>
</div>
<div style="{BOX}">
{''.join(pp(*x) for x in pts1)}
</div>
<div style="margin: 26px 40px 0 40px; display: flex; gap: 10px">
<img src="{IMG[pair[0]]}" alt="{pair[1]}" style="width: 255px; height: 220px; object-fit: cover; object-position: {pair[2]}; border-radius: 18px">
<img src="{IMG[pair[3]]}" alt="{pair[4]}" style="width: 255px; height: 220px; object-fit: cover; object-position: {pair[5]}; border-radius: 18px">
</div>
<div style="margin: 8px 40px 0 40px; text-align: center; font-size: 14px; font-weight: 700; color: #B0577F">{pair_cap}</div>
<div style="{BOX}">
{''.join(pp(*x) for x in pts2)}
</div>
<div style="margin: 26px 40px 0 40px; padding: 24px; background: #FFE1ED; border-radius: 24px; display: flex; flex-direction: column; gap: 10px">
<div style="font-family: 'Fredoka', sans-serif; font-weight: 600; font-size: 24px; color: #B026FF; text-align: center">LA GUARIGIONE GIORNO PER GIORNO 🌷</div>
{''.join(f'<p style="margin: 0; font-size: 16px; line-height: 1.55">{e} <b>{t}</b> {b}</p>' for e, t, b in heal)}
</div>
<div style="margin: 26px 40px 0 40px; padding: 22px 24px; background: #ffffff; border: 3px solid #FFB3CF; border-radius: 24px; font-size: 16px; line-height: 1.55; text-align: center"><b style="color: #B026FF; font-family: 'Fredoka', sans-serif; font-size: 22px">IL CONSIGLIO DI FEDERICA 💕</b><br>«{tip}»<br><a href="https://www.instagram.com/favalorofederica_pmu/" style="display: inline-block; margin-top: 12px; padding: 10px 22px; border-radius: 999px; background: #FFE1ED; color: #B026FF; font-weight: 700">✨ guarda i suoi lavori: @favalorofederica_pmu</a></div>
<div style="margin: 26px 40px 0 40px; height: 270px; background: #ffffff; border: 3px solid #FFB3CF; border-radius: 24px; overflow: hidden; position: relative; display: flex; align-items: center; justify-content: center"><img src="{IMG['gif' + key]}" alt="GIF divertente della campagna" style="max-width: 100%; max-height: 100%; object-fit: contain; display: block"><div style="position: absolute; right: 10px; bottom: 10px; background: #B026FF; color: #ffffff; font-size: 12px; font-weight: 700; letter-spacing: 1px; padding: 5px 12px; border-radius: 999px">▶ ANIMATA NELLA MAIL</div></div>
<div style="margin: 10px 40px 0 40px; text-align: center; font-family: 'Dancing Script', cursive; font-weight: 700; font-size: 24px; color: #F0508C">{gifcap}</div>
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
<div style="font-size: 12px; text-align: center; color: #B0577F">📍 Via Giardini 86, Pavullo nel Frignano (MO)<br>{credits}<br>© Teenage Dirtbag Tattoo Studio · Annulla iscrizione</div>
</div>
</div>'''

U1201 = 'https://eepurl.com/0IcIBv6Tc9'
v = lambda H: pink_visual2(H, 'lb1', 'Lip blush rosso acceso, lavoro di Federica', '50% 50%', 'lb2', 'Lip blush nude, lavoro di Federica', '50% 55%', 'lb3', 'Lip blush prima e dopo, lavoro di Federica', '50% 50%',
                            '💋 acceso', '🌸 nude', '✨ prima / dopo', 'LIP BLUSH 💋', 'il colore che si sveglia con te', 'i lavori di Federica · @favalorofederica_pmu 🌸', U1201, 'colori, durata e guarigione, spiegati semplice 💕')
save('k1201-post.dc.html', page('Lip blush · grafica WhatsApp', 'pink', v(1350), 1080, 1350))
save('k1201-storia.dc.html', page('Lip blush · storia IG', 'pink', v(1920), 1080, 1920))
save('k1201-news.dc.html', page('Lip blush · newsletter', 'pink', pink_news('1201', 'LIP BLUSH', 'il colore delle labbra che si sveglia con te', 'lb1', 'Lip blush rosso acceso, lavoro di Federica', '50% 50%',
    'lip blush acceso di Federica: colore pieno, contorno pulito 💋',
    'Non è un rossetto tatuato e non cambia la forma della tua bocca: è una <b>velatura di pigmento</b> che ravviva il colore naturale e definisce il contorno. 🌸',
    [('🎨 IL COLORE SI SCEGLIE INSIEME', 'Dal nude rosato al corallo più acceso: il pigmento si sceglie sul tuo incarnato e sul colore naturale delle tue labbra.'),
     ('✏️ PRIMA SI DISEGNA', 'Il contorno si prova con la matita e si guarda allo specchio insieme. Si parte solo quando ti piace.'),
     ('☕ IL MOTIVO VERO', 'Un colore che resta dopo il caffè, la palestra e la mascherina, senza ritoccare il rossetto ogni ora.')],
    ('lb2', 'Lip blush nude', '50% 55%', 'lb3', 'Lip blush prima e dopo', '50% 50%'),
    'nude morbido 🌸 · prima e dopo: la differenza è nel contorno ✨',
    [('⏳ QUANTO DURA', 'In genere qualche anno, ma dipende dalla pelle e dalle abitudini. Dopo qualche settimana di solito si fa un ritocco: chiedi in consulenza se è compreso.'),
     ('💬 DILLO IN CONSULENZA', 'Se ti è mai venuto l’herpes sulle labbra o hai allergie, dillo prima: Federica ti spiega come organizzarti.'),
     ('🧴 DOPO, POCO E BENE', 'Labbra pulite e la crema che ti viene indicata. Niente scrub, niente rossetti finché non è guarito.')],
    [('💧', 'Primi giorni:', 'colore molto intenso e un po’ di gonfiore.'),
     ('🤏', 'Poi:', 'pellicine sottili. Non si strappano: vanno via da sole.'),
     ('👻', 'Dopo:', 'sembra quasi sparito. È la fase “fantasma”, è normale.'),
     ('🌸', 'Alla fine:', 'il colore vero torna a pelle stabilizzata.')],
    'Nei primi giorni il colore ti sembrerà troppo, poi quasi sparito. Aspetta la fine della guarigione prima di giudicare: è lì che vedi il tuo lip blush.',
    'io che mi sveglio con le labbra già pronte 💋',
    'Foto: lavori di Federica · @favalorofederica_pmu · GIF: Pinterest (Clueless, 1995)'), 600, 3300, news=True))

U2101 = 'https://eepurl.com/NY4KS9BU17'
v = lambda H: pink_visual2(H, 'br1', 'Sopracciglia effetto polvere, lavoro di Federica', '50% 35%', 'br2', 'Sopracciglia definite, lavoro di Federica', '50% 40%', 'br3', 'Sopracciglia naturali, lavoro di Federica', '50% 30%',
                            '☁️ effetto polvere', '✍️ definite', '🤎 naturali', 'SOPRACCIGLIA', 'pelo a pelo o effetto polvere?', 'i lavori di Federica · @favalorofederica_pmu 🌸', U2101, 'la tecnica giusta per la tua pelle 💕', big_fs=96)
save('k2101-post.dc.html', page('Sopracciglia · grafica WhatsApp', 'pink', v(1350), 1080, 1350))
save('k2101-storia.dc.html', page('Sopracciglia · storia IG', 'pink', v(1920), 1080, 1920))
save('k2101-news.dc.html', page('Sopracciglia · newsletter', 'pink', pink_news('2101', 'SOPRACCIGLIA', 'pelo a pelo o effetto polvere?', 'br1', 'Sopracciglia effetto polvere, lavoro di Federica', '50% 35%',
    'effetto polvere di Federica: morbido come una matita 🤎',
    'Le sopracciglia permanenti non sono tutte uguali: c’è chi vuole <b>peletti disegnati uno a uno</b> e chi un <b>effetto matita morbido</b>. La tecnica giusta la decide la tua pelle, non la moda. 🌸',
    [('✍️ PELO A PELO', 'Tratti sottili che imitano i peli veri: perfetto per chi ha sopracciglia rade in alcuni punti e vuole un risultato naturalissimo.'),
     ('☁️ EFFETTO POLVERE', 'Una sfumatura morbida fatta a puntini, come una matita o un ombretto. In genere dura di più e funziona bene anche sulle pelli più grasse.'),
     ('💞 IL MIX', 'Peletti davanti e sfumatura verso la coda: naturalezza e definizione insieme.')],
    ('br2', 'Sopracciglia definite', '50% 40%', 'br3', 'Sopracciglia naturali', '50% 30%'),
    'più definite ✨ · più naturali 🤎 · la scelta è tua',
    [('🪞 PRIMA SI DISEGNA', 'La forma si studia sul tuo viso con matita e misure, e si parte solo quando ti piace allo specchio.'),
     ('⏳ QUANTO DURA', 'Qualche anno, ma cambia con pelle, sole e skincare. Di solito dopo qualche settimana c’è il ritocco: chiedi in consulenza se è compreso.'),
     ('🧴 SKINCARE ATTENTA', 'Acidi, retinolo e scrub sulla zona schiariscono il pigmento prima del tempo: dillo in consulenza cosa usi.')],
    [('💧', 'Primi giorni:', 'più scure e definite del risultato finale.'),
     ('🤏', 'Poi:', 'pellicine sottili che non si grattano.'),
     ('😮', 'Dopo:', 'sembrano schiarite troppo: è la fase normale.'),
     ('🌸', 'Alla fine:', 'il colore vero si vede a pelle stabilizzata.')],
    'Non portarmi solo la foto delle sopracciglia che ti piacciono: portami anche quella delle tue senza trucco. Partiamo da lì.',
    'io che alzo il sopracciglio, perfetto anche al risveglio 💅',
    'Foto: lavori di Federica · @favalorofederica_pmu · GIF: Pinterest (Il diavolo veste Prada, 2006)'), 600, 3300, news=True))
