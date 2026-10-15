# Pipeline kit informativi — Teenage Dirtbag

Procedura usata dall'attività settimanale "3 kit informativi" (lunedì mattina) e da chiunque debba produrre un kit a mano.
Riguarda SOLO lo studio Teenage Dirtbag (tattoo e piercing, Via Giardini 86, Pavullo nel Frignano). Mai citare @gipsydeb, il bot Telegram o l'attività da modella.

## 0. Setup di una sessione nuova

```bash
export KIT_SP=/tmp/kit            # cartella di lavoro
mkdir -p $KIT_SP/{render,email,assets,kitall/project,news,out}
git clone -b kit-assets https://github.com/debbymasini-dev/messenger $KIT_SP/kitassets
cp $KIT_SP/kitassets/pipeline/{render.js,shotmail.js,package.json} $KIT_SP/render/
cp $KIT_SP/kitassets/pipeline/build.py $KIT_SP/email/
cd $KIT_SP/render && npm install          # font @fontsource + @twemoji/svg + playwright
# asset di base: loghi, icone, foto e still GIF già usati
cp $KIT_SP/kitassets/*.png $KIT_SP/kitassets/foto/* $KIT_SP/kitassets/gif/*.jpg $KIT_SP/assets/ 2>/dev/null
```
Chromium: `executablePath:'/opt/pw-browsers/chromium'` (già nello script). Non lanciare `playwright install`.
Gli emoji a colori non escono in Chromium headless: render.js li sostituisce con le SVG twemoji (non toccare).

## 1. Calendario e slot

- Uscite dei kit informativi: **martedì, giovedì e sabato alle 10:00 ora italiana** (08:00Z con ora legale, 09:00Z con ora solare; nel 2027 l'ora legale va dal 28/03 al 31/10).
- Si parte da **gennaio 2027** e si va avanti: ogni settimana di calendario si riempie con 3 kit (uno per slot), partendo dalla prima settimana che non è ancora piena.
- Prima di scegliere le date leggi:
  - registro `1ZaP-36ZVJ16opt6h56A8O7UhJl3ROMOrVASNsmI1-uI` (Google Sheet, colonne Data invio / Tema / Campaign ID / grafica WA / storia IG / script / note);
  - campagne Mailchimp con status `schedule` e `save` (us4, `https://us4.api.mailchimp.com/3.0/campaigns`);
  - Google Calendar della titolare per guest, piercing day, eventi, chiusure.
- **Guest ed eventi hanno la precedenza**: se uno slot (o il giorno prima/dopo) è occupato da guest, evento, piercing day, festività o chiusura, il kit informativo salta a uno slot libero successivo. Mai due newsletter lo stesso giorno.
- Il martedì 05/01/2027 è già occupato da "Y2K revival" (984e22fc28).

## 2. Temi e fonti

- Fonti giovani e attive (ottobre 2026): iglatattoo.com, lifestyleblog.it, Skinwalker Studio, Tribu Piercings, Onyx Academy (PMU), Tattoo History Atlas, The Daily Beast, Tattoo Life, Scene360 + **Pinterest** (fonte fissa per foto e GIF).
- Temi vari: tatuaggio (stili, trend, cura), piercing, trucco permanente. Niente doppioni: controlla i temi già a registro e già usciti.
- Un kit informativo NON è un annuncio: niente date sulle grafiche, niente PRENOTA ORA. CTA grafiche = **SCOPRI DI PIÙ** → archive_url (eepurl) della newsletter. CTA in newsletter = **CHIEDICI INFO** → https://wa.me/393314030216.
- Profili da linkare nel box consiglio: tatuaggi → Filippo @sfregio_lttr; piercing → Rebecca @beb_piercing (nei kit piercing NON si invita Filippo); trucco permanente → Federica @favalorofederica_pmu (+ riga piccola su Filippo come nel kit 19/10).
- Il consiglio del collaboratore va scritto come consiglio pratico coerente con l'articolo; mai inventare fatti sul collaboratore.

## 3. Estetiche (si alternano)

- **Zine acid punk**: carta #EDE7D8, inchiostro #111111, viola #B026FF, acido #C6FF00, rosa #FF2E88. Bebas Neue + Permanent Marker + Special Elite. Template: `templates/k2410-*`, `templates/k1010-*`.
- **Chrome cyber**: #050510, #B026FF, cromo #C9CDD4, ciano #00E5FF, #2A1440. Oswald + Chakra Petch. Template: `templates/k0711-*`, `templates/k1710-*`.
- **Cute rosa** (SOLO trucco permanente, target femminile, niente elementi dark, emoji e decori rosa rassicuranti): #FFF3F7, #B026FF, #F0508C, #FFB3CF, prugna #5A2A4A. Fredoka + Dancing Script + Quicksand. Template: `templates/k1411-*`, `templates/k1910-*`.
- Ogni kit = grafica WA 1080×1350 (`kDDMM-post`), storia IG 1080×1920 (`kDDMM-storia`), newsletter 600px (`kDDMM-news`). `templates/gen-kit-esempio.py` genera tutti e 3 i formati per 4 kit: copialo e cambia contenuti e immagini.
- Sempre: lettering e bocca veri (blob f76aa4f097dce598a2692bd36380569a e b6b849e87ef0993310e1ac51deaa6468), Scalapay (d6906306ac53852834d3e32c9027e117), nel footer della newsletter le 5 icone social (blob 8fcf166f…, edfc443f…, fbd97a11…, 52528d28…, 17eb94dd…), box GRUPPO TEENAGE VIP, indirizzo, crediti e "Annulla iscrizione".

## 4. Foto e GIF

- Almeno 3 foto per newsletter + 1 GIF unica (meglio un frame di film cult) che non sia già stata usata (controlla `GIFURL`/`GIPHY` in build.py).
- Pinterest si raggiunge dal Browser pane del computer di Gipsy (`mcp__remote-devices__Claude_Browser__*`), loggato come debbymasini2077. Dal container pinimg è bloccato.
  - Ricerca: `fetch('/resource/BaseSearchResource/get/?source_url=…&data={"options":{"query":q,"scope":"pins","page_size":50},"context":{}}')` con header `X-Requested-With: XMLHttpRequest`, `X-Pinterest-PWS-Handler: www/search/[scope].js`.
  - Dati pin (autore per i crediti): `/resource/PinResource/get/?source_url=/pin/ID/&data={"options":{"id":ID,"field_set_key":"detailed"},"context":{}}` con handler `www/pin/[id].js` → `pinner.username`, `images.orig.url`.
  - Scaricare: nel browser `fetch(url)` → canvas → `toDataURL('image/jpeg',.88)` e restituisci `ID=k;W=;H=;C=;P=;<base64>;PAD`; massimo 2 immagini per chiamata. L'output finisce in un file tool-results: decodifica separando su `ID=` e togliendo i caratteri non base64.
  - GIF: cerca `"<film> gif"`, tieni solo `images.orig.url` che finisce in `.gif`, < 3 MB, senza watermark o sottotitoli. Nella mail la GIF va linkata dall'URL pinimg (aggiungi la chiave in `GIFURL` di build.py) e lo still del primo frame va salvato in `assets/gif-DDMM.jpg`.
- Taglia via scritte e loghi delle foto (crop). Crediti dei pin SOLO nel footer della newsletter, mai su WA/storia.
- Se il Browser pane non risponde (computer spento o app chiusa): NON programmare kit senza foto. Prepara temi, testi e date, segnali a registro "FOTO DA PRENDERE" e avvisa Gipsy.

## 5. Tela Claude Design

- Tela principale: https://claude.ai/artifact/6XoX4eRy58fsZYSjuUAfKW.
- Prima di pubblicare leggi SEMPRE `project/canvas.json` della tela (Artifact read, path `project/canvas.json`) e fai il merge: aggiungi board, pagina `pDDMM` (nome "DD/MM · Tema"), nota `tDDMM` e voci di `order`. Non togliere niente di esistente.
- Le foto si caricano come asset della tela (Artifact publish con `asset: true` e `file_paths`, file sotto la cartella di lavoro): l'id restituito è il blob da usare in `/_blob/<id>`. Aggiungi ogni nuovo id in `const blobs = {` di render.js con la forma `'id': 'file.jpg',` (apici singoli, build.py legge solo quelli) e copia il file in `$KIT_SP/assets/`.
- Pubblica con `root=$KIT_SP/kitall`, `file_path=$KIT_SP/kitall/project/canvas.json` e la mappa `files` dei nuovi `project/kDDMM-*.dc.html`.

## 6. Render, repo, newsletter

1. Render JPG: `cd $KIT_SP/render && node render.js jobs.json` con `[{src,out,w,h}]` (post 1080×1350, storia 1080×1920). Guarda le JPG prima di andare avanti.
2. Mailchimp — crea la campagna replicando quella guida: `POST /campaigns/3d0d60dac0/actions/replicate`, poi `PATCH /campaigns/{id}` con `settings.title`, `subject_line` (emoji + titolo), `preview_text`, `from_name: "Teenage Dirtbag"`, `reply_to: hello@teenagedirtbag.shop`. Leggi `archive_url` (eepurl) e mettilo nel pulsante SCOPRI DI PIÙ di post e storia, poi rifai il render.
3. Email: `cd $KIT_SP/email && python3 build.py DDMM` → `kitassets/email/DDMM.html` (+ immagini ritagliate).
4. Repo: copia `kDDMM-post.jpg`, `kDDMM-storia.jpg` nella radice di `kitassets`, le foto in `foto/`, poi commit e `git push origin HEAD:kit-assets`. Messaggio commit con in fondo le righe di attribuzione richieste.
5. Import HTML: Zapier MailchimpCLIAPI `mailchimp_import_campaign_html_from_urls`, pairs `ID|https://raw.githack.com/debbymasini-dev/messenger/<COMMIT>/email/DDMM.html`.
6. Programma: `POST /campaigns/{id}/actions/schedule` con `{"schedule_time":"AAAA-MM-GGT08:00:00+00:00"}` (09:00Z con ora solare).
7. Anteprima: `node shotmail.js DDMM` (dopo il push) → `$KIT_SP/news/newsletter-DDMM.jpg`.
8. Registro: aggiungi una riga per kit (Data, Tema, Campaign ID, URL raw della JPG WA e storia fissati al commit, script doc se creato, Note con "NEWSLETTER PROGRAMMATA", estetica, fonte, crediti, eepurl per lo sticker della storia IG). Append: `values/A1:G1:append?valueInputOption=RAW&insertDataOption=INSERT_ROWS`.

Chiamate Mailchimp via Zapier: `_zap_raw_request` con tool_name `mailchimp_make_api_get_request` / `mailchimp_make_api_mutating_request`, URL assoluto `https://us4.api.mailchimp.com/3.0/…`, `fail_on_errors: false`.
