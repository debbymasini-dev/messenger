import re, os, sys
from bs4 import BeautifulSoup, NavigableString, Tag
from PIL import Image, ImageEnhance

SP=os.environ.get('KIT_SP','/tmp/kit')+'/'
A=SP+'assets/'; OUT=SP+'kitassets/email/'; os.makedirs(OUT,exist_ok=True)
RAW='https://raw.githubusercontent.com/debbymasini-dev/messenger/kit-assets/'
src=open(SP+'render/render.js').read()
BLOBS=dict(re.findall(r"'([0-9a-f]{32})': '([^']+)'",src))
GIFURL={"2410": "https://i.pinimg.com/originals/fb/7c/43/fb7c434728119967ef133f4ffe475f95.gif", "0711": "https://i.pinimg.com/originals/c7/82/37/c78237962a7f4f0cd79d9f82b4872011.gif", "1411": "https://i.pinimg.com/originals/5a/1c/2f/5a1c2f41f5874c960f07cb88c515b811.gif", "1912": "https://i.pinimg.com/originals/f2/34/82/f234829dc1e2ef1eb4dd20cd3902b07f.gif", "1212": "https://i.pinimg.com/originals/81/a9/bd/81a9bdc6182e234fc18acdfc1e799a5d.gif", "1910": "https://i.pinimg.com/originals/b3/75/46/b375468136a88d8a53f6362c0f6555bb.gif"}
GIPHY={"0310": "YOM7mcEtcFzRqTpvPr", "0610": "emdBjSGSxHyVO", "1010": "d3Kq5w84bzlBLVDO", "1013": "3o7aTIGlhSo1bL8QUg", "2010": "t9xC86uywfQ1G", "2710": "oqwsns7qHCEi4", "0311": "3otPoCmoVM8gvKbAEo", "1011": "3og0IKMmOZE88Ankty", "1711": "Ma9YUiOM7bqZW", "0501": "6xE1FNcorRInS", "0512": "BM1rtI9t5TJB975bg1", "0112": "ukUZ5XHV92KDS", "0812": "d2ZaW7LrLwem8W0U", "1512": "K4Ov4XqbqUSf6", "2212": "l2YWq7orQMOvu5J3W", "2912": "ysFkRNpsekhC8phxbp"}

def P(s):
    d={}
    for part in (s or '').split(';'):
        if ':' in part:
            k,v=part.split(':',1); d[k.strip()]=v.strip()
    return d
def S(d): return '; '.join(f'{k}: {v}' for k,v in d.items())
def px(v): 
    m=re.match(r'(-?[\d.]+)px',v or ''); return float(m.group(1)) if m else None

def crop(fname, w, h, pos, bright, key, n):
    im=Image.open(A+fname).convert('RGB')
    W,H=im.size; r=w/h
    if W/H>r: cw,ch=H*r,H
    else: cw,ch=W,W/r
    px_,py_=[float(x.strip('%'))/100 for x in (pos or '50% 50%').split()[:2]]
    x0=(W-cw)*px_; y0=(H-ch)*py_
    im=im.crop((int(x0),int(y0),int(x0+cw),int(y0+ch)))
    tw=min(int(w*2), im.size[0]); im=im.resize((tw,int(tw/r)),Image.LANCZOS)
    if bright: im=ImageEnhance.Brightness(im).enhance(bright)
    name=f'{key}-img{n}.jpg'; im.save(OUT+name,quality=85,optimize=True); return RAW+'email/'+name

def build(key, path):
    html=open(path).read()
    helm=re.search(r'<helmet>([\s\S]*?)</helmet>',html).group(1)
    fontlink=re.search(r'<link href="(https://fonts.googleapis.com/css2[^"]+)"',helm).group(1)
    acol=re.search(r'a\{color:(#[0-9A-Fa-f]{6})',helm).group(1)
    body=html.split('<x-dc>')[1].split('</x-dc>')[0]
    body=re.sub(r'<helmet>[\s\S]*?</helmet>','',body)
    soup=BeautifulSoup(body,'html.parser')
    root=soup.find('div'); rs=P(root.get('style'))
    bg=rs.get('background','#000'); n=[0]
    # GIF box
    for img in soup.find_all('img'):
        if img.get('alt')=='GIF divertente della campagna':
            box=img.parent; bs=P(box.get('style'))
            still=Image.open(A+f'gif-{key}.jpg'); gw,gh=still.size
            w=int(min(520, 300*gw/gh, max(gw*1.2,300)))
            new=soup.new_tag('div'); new['style']=S({'margin':bs['margin'],'text-align':'center','background':bs.get('background','#000'),**({'border':bs['border']} if 'border' in bs else {}),**({'border-radius':bs['border-radius']} if 'border-radius' in bs else {}),**({'box-shadow':bs['box-shadow']} if 'box-shadow' in bs else {}),'padding':'10px 0','line-height':'0'})
            gsrc=GIFURL[key] if key in GIFURL else f'https://media.giphy.com/media/{GIPHY[key]}/giphy.gif' if key in GIPHY else RAW+f'gif/gif-{key}.gif'
            g=soup.new_tag('img',src=gsrc,alt='GIF',width=str(w))
            g['style']=f'width: {w}px; max-width: 100%; height: auto; display: inline-block; border: 0'
            new.append(g); box.replace_with(new)
    for img in soup.find_all('img'):
        s=P(img.get('style')); m=re.search(r'/_blob/([0-9a-f]{32})',img['src'] or '')
        if not m: continue
        f=BLOBS[m.group(1)]; w=px(s.get('width')); h=px(s.get('height'))
        if s.get('object-fit')=='cover':
            b=re.search(r'brightness\(([\d.]+)\)',s.get('filter',''))
            n[0]+=1
            img['src']=crop(f,w,h,s.get('object-position'),float(b.group(1)) if b else None,key,n[0])
        else:
            img['src']=RAW+(f if f.endswith('.png') else 'foto/'+f)
        ns={'width':f'{int(w)}px','max-width':'100%','height':'auto','display':'block','border':'0'}
        if 'margin' in s: ns['margin']=s['margin']
        img['width']=str(int(w)); img['style']=S(ns)
    # flex conversion
    for el in list(soup.find_all(True)):
        s=P(el.get('style'))
        if el.name!='img':
            s.pop('height',None)
            if s.get('margin-top')=='auto': s['margin-top']='30px'
            for k in ('box-sizing','position','overflow'): s.pop(k,None)
        if s.get('display')=='flex':
            d=s.pop('flex-direction','row'); ai=s.pop('align-items',None); jc=s.pop('justify-content',None); gap=s.pop('gap',None); s.pop('display')
            kids=[c for c in el.children if isinstance(c,Tag)]
            if d=='column':
                if ai=='center' or jc=='center': s.setdefault('text-align','center')
                if el.name=='a':
                    s['display']='block'; s.setdefault('padding','18px 14px'); s['text-align']='center'
                for i,c in enumerate(kids):
                    cs=P(c.get('style'))
                    if c.name in ('span','b'): cs['display']='block'
                    if c.name=='a' and el.name!='a' and 'display' not in cs: cs['display']='inline-block'
                    if c.name=='img' and (ai=='center'): cs['display']='inline-block'; 
                    if i>0 and gap:
                        if cs.get('margin') in ('0',None) : cs.pop('margin',None); cs['margin-top']=gap
                    c['style']=S(cs)
            else:
                t=soup.new_tag('table'); t['role']='presentation'; t['cellpadding']='0'; t['cellspacing']='0'; t['border']='0'
                if jc=='space-between': t['width']='100%'
                else: t['align']='center'
                tr=soup.new_tag('tr'); t.append(tr)
                for i,c in enumerate(kids):
                    td=soup.new_tag('td'); td['valign']='middle'
                    tds={}
                    if jc=='space-between': td['align']='left' if i==0 else 'right'
                    elif gap: tds['padding']=f'0 {int(px(gap)/2)}px'
                    if 'font-size' in s: tds['font-size']=s['font-size']
                    if 'font-weight' in s: tds['font-weight']=s['font-weight']
                    td['style']=S(tds); c.extract(); td.append(c); tr.append(td)
                for c in list(el.children):
                    if isinstance(c,NavigableString) and not c.strip(): c.extract()
                el.append(t)
        if el.name=='a':
            s.setdefault('color',acol)
        if el is not root: el['style']=S(s) if s else None
        if el.get('style') is None and el.has_attr('style'): del el['style']
    rs=P(root.get('style')); 
    for k in ('width','height','display','flex-direction','box-sizing'): rs.pop(k,None)
    rs['max-width']='600px'; rs['margin']='0 auto'
    root['style']=S(rs)
    out=str(soup)
    out=out.replace('Annulla iscrizione',f'<a href="*|UNSUB|*" style="color: inherit; text-decoration: underline">Annulla iscrizione</a>')
    doc=f'''<!doctype html>
<html lang="it"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>*|MC:SUBJECT|*</title>
<link href="{fontlink}" rel="stylesheet">
<style>body{{margin:0;padding:0;background:{bg}}} img{{max-width:100%}} a{{color:{acol}}} @media (max-width:620px){{.wrap{{width:100%!important}}}}</style>
</head><body style="margin:0;padding:0;background:{bg}">
<span style="display:none;max-height:0;overflow:hidden">*|MC_PREVIEW_TEXT|*</span>
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background:{bg}"><tr><td align="center">
<table role="presentation" class="wrap" width="600" cellpadding="0" cellspacing="0" border="0" style="width:600px;max-width:100%"><tr><td style="padding-bottom:24px">
{out}
</td></tr></table>
</td></tr></table>
</body></html>'''
    open(OUT+f'{key}.html','w').write(doc); print(key,len(doc))

import sys
if len(sys.argv)>1:
    for k in sys.argv[1:]: build(k,SP+f'kitall/project/k{k}-news.dc.html')
else:
    keys='1013 2010 2710 0311 1011 1711 2411 0112 0812 1512 2212 2912'.split()
    build('0610',SP+'kit0610/project/Newsletter.dc.html')
    for k in keys: build(k,SP+f'kitall/project/k{k}-news.dc.html')
