// Renders Claude Design artboards (.dc.html) to JPG with local assets and fonts.
const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');

const SP = process.env.KIT_SP || '/tmp/kit';
const A = SP + '/assets/';
const FS = SP + '/render/node_modules/@fontsource/';
const blobs = {
'50072525f00f756537f049d460af3ff9': 'nt1.jpg',
'da65d05274479955d930a12c3f8236e3': 'nt3.jpg',
'78f06bf5a11d63d8eb2a13600e4097c2': 'nt4.jpg',
'0ff7d2199d0191cabbec9009c808ce57': 'nt5.jpg',
'd709d137b9d456ce9b6761526e9c5613': 're1.jpg',
'98871a55ece02e471745ff8a30398a89': 're2.jpg',
'c6352e9e53042db52798d1a6e87916dc': 're3.jpg',
'b395586dc81319132f9cc6551dd20c1c': 'fe1.jpg',
'602130b340b5e60e958ee5ba13884dfa': 'fe2.jpg',
'996b301116a56d2791f67214c8633f00': 'fe3.jpg',
'd8b2de66bef2db271bb1d79afc679cad': 'gif-0602.jpg',
'72e87334530a108d857cd70435e1b5ba': 'gif-0902.jpg',
'de96167b446e781a6758b02b8a712ec3': 'gif-1102.jpg',

  // kit gennaio 2027 (09/01-21/01)
  '5b75a9718de2d227896e521073e958d5': 'k27-se1.jpg',
  '1ac0b93705b41f102e3f93b540af66bc': 'k27-se2.jpg',
  'bda6bd038e93ec2e68e852a6fb711993': 'k27-se3.jpg',
  '60ea5c63d4dc7863c6c3f5c70cb37261': 'k27-ag1.jpg',
  '398c879cc66189eacff000705f4163d8': 'k27-ag2.jpg',
  '7da7a891719984ec2b5d86620c5c765a': 'k27-ag3.jpg',
  'd3979d2842390780590c3e0bdb14de8f': 'k27-ag4.jpg',
  '25bf07407ae5548cafa68a21548a6b64': 'k27-lb1.jpg',
  '5a3ad50d47904e1fd9aa239a5330f0f6': 'k27-lb2.jpg',
  '46d754350d76bec3dc36e15b528a9fd1': 'k27-lb3.jpg',
  'a9dde570d7f7a9fd646455d0fb5bd3eb': 'k27-br1.jpg',
  '73269d00c8a1a56d12d105b430050d33': 'k27-br2.jpg',
  '6318105911869b73a54316f6d4f39ae8': 'k27-br3.jpg',
  '81f04a96c13c8bc0a0625ccd536b3362': 'k27-tr1.jpg',
  'f9add7bc1015219b70af8d453580db06': 'k27-tr2.jpg',
  '935f25aadfe61d2c8081de86c9bac346': 'k27-tr3.jpg',
  '963e0099b3a4f46f15f4c0fa4907366a': 'k27-tr4.jpg',
  '6c0f59809dd36fba8c633969c76ae6f9': 'k27-dw1.jpg',
  '3eda06fc2cbc405bee52c24f1ae1f534': 'k27-dw2.jpg',
  '48cadde224b78b9cbec5b8d33868ddb4': 'k27-dw3.jpg',
  'df7a7454ef515524ad47092bff3ffc32': 'k27-dw4.jpg',
  'ae46856809d57a907bfe20df1c0f23c9': 'gif-0901.jpg',
  '73ab2b65a277ab8c0cb00af6099f66a0': 'gif-1201.jpg',
  'bac494605876471ac1c11c6d7d55be06': 'gif-1401.jpg',
  '0534ba937ca567bfeaf8202844ab184e': 'gif-1601.jpg',
  '8e2ffb16d5c48fe06a1af85411739b85': 'gif-1901.jpg',
  '924824e08e83c6f5b2b7a187b3badb31': 'gif-2101.jpg',
  // kit informativi 24/10 07/11 14/11 19/12
  '1d066c7ae1eeb977fdc70c6e551115a5': 'gif-2410.jpg',
  '9d9a0e522220ecec5d88f0787f41012c': 'gif-0711.jpg',
  'add45a902504bf80c9ec361bda0d2998': 'gif-1411.jpg',
  '273f6e53d4fc506b6d0a8c1d2bda1b3c': 'gif-1912.jpg',
  '13f473410b88a075d10fd4da35a45cbf': 'k4-cy1.jpg',
  '72fe780d184232d54a9a580a8d5ec86e': 'k4-cy2.jpg',
  '20f3367a5ddac233917209a9f0d6ebcc': 'k4-cy3.jpg',
  'b543281472b96b85d84ec99bae2a4c0b': 'k4-el2.jpg',
  '57766fce5b926478fea36f15a73fe58b': 'k4-el3.jpg',
  'f346d334f3d690e8a7745bb0e5463879': 'k4-fe0.jpg',
  'f6ecb57669f8fcad998d389b67eea51e': 'k4-fe3.jpg',
  '5693ccdb55439321f95dd0636531333b': 'k4-gi1.jpg',
  '6dce3ad756d69eee202b825ede5ed592': 'k4-gi2.jpg',
  'b50429aa2da4b1055efa00753960b780': 'k4-gi3.jpg',
  'b5150c377f6573ed50d549ddfc5d6d6c': 'k4-pa1.jpg',
  '101ba5c6ac52bc1e64091b57ba8faf2c': 'k4-pa2.jpg',
  '2d89934e19b73b6807f7144e24ba0f17': 'k4-pa3.jpg',
  '1bbd25f6a5aaf914f8746146ddbc76d8': 'k4-pa4.jpg',
  '7324518154d4025dee8325f56ed0ea09': 'pmu-e4.jpg', '2b7312ac623e52b82741744020069875': 'pmu-l7.jpg', 'b3eaf7b2ad05d10da2dc1be77bfe1320': 'pmu-b18a.jpg', 'b421976ba1dbaba3f875f9c89b663a58': 'pmu-b20.jpg', '6b1cc5223932c83c544e334fdd9830fa': 'pmu-l1.jpg', '69e12e8acfb4d04b25ea6dec8ae0d276': 'gif-1910.jpg',
 "3afddef70e720d2ca552c86410c4dd19":"bw-post.jpg","bc564730f4212b63c045e5b9bd7c5765":"bw-storia.jpg",
 "3ee642f7174009ddcaaac34c52855983":"bw-post.jpg","459a475d4f95671e3d4fd433bb501261":"bw-storia.jpg","9ebd45574344a051825e22f514b63005":"fl-post.jpg","24727bb41775c3a9e628f475952274fc":"fl-storia.jpg",
  '641ad3ef3c51dc9d36137c1120ea27e1': 'orazio-blackwork.jpg', 'b6bd3dee9d5fd4495ffab7d4dfbf7f5a': 'marica-fiori.jpg', '8fcf166f36a7b4281a58bff0342858da': 'ico-instagram.png', 'edfc443f5fb2b7abda2c14c450834ce0': 'ico-facebook.png', 'fbd97a11899d22f16c64e6c3f0450150': 'ico-tiktok.png', '52528d2838b82fcbae21aab60cdad752': 'ico-whatsapp.png', '17eb94dd26b7ba7e9725c327d67cf983': 'ico-email.png', 'fb49d2baeff671834c48c1f103ca1aa4': 'sq-b6.jpg', '16e77f47658c7de237129e8187b476f1': 'sq-b11.jpg', '7847eaf680e182730b32b9934d568fa7': 'sq-f2.jpg', 'e9bd369e429daade53fa0c6d13a13d62': 'sq-f19.jpg', '8ab9b1240f9117d849ac7194f9849b1e': 'gif-0512.jpg', '08401e44348bd43b8498396be8a90a03': 'gif-1212.jpg',
  '71c7387b4bf08c7dd42c67b035aef5d8': 'lele-post.jpg', '74828867409965b76246ae1a67ec2aba': 'lele-storia.jpg', '8d0d59fe73f088fdcb36190a16ec489d': 'lele-news1.jpg', '6f3c2ae7e045050fae2a6b4f07531c4a': 'lele-news2.jpg', '0c7c37b2410659a9a14fb7a8a3100fe7': 'gif-1710.jpg',
  '5064dde9662a205486f4a5e941bf9d6f': 'po2-post.jpg', '18a9747c091cd861cde2691e5824f8e6': 'po2-storia.jpg', 'ecbe97b4f8a828cfc1fe3e710172c258': 'po2-news.jpg',
  '236b03a73b4bfb6991b57674fbcd05c2': 'po-post.jpg', '2f74058a4fe09492482e743ae192a9d8': 'po-storia.jpg', '8ec3466d9a166d1e3404344700a3ec2e': 'po-news.jpg',
  'e969f7c9fc51cfb5bcdef143a8d9a6cd': 'td10-hero.jpg', '3ca8edc1739f4b7281497fc3ad63e1e1': 'gif-2411.jpg',
  'e01cc44b470fa806e831df19984dae12': 'gift.jpg', 'dbd57bfdde5bb23cc9d273af1d0545a9': 'gio-bg.jpg', 'd7800a5e6f67ff2d21a76d1238abd26d': 'gio-news.jpg', '6d0b23d9df3a90c94dc171adb057f152': 'tr-dark-news.jpg', 'c76c5c6636f176f450c896fc96bf5be7': 'tr-dark-post.jpg', '604a7ba53b0981b57082f5737e022ae9': 'tr-fine-news.jpg', 'dfd9170dcb32ce8d022bc79bef438d9b': 'tr-fine-post.jpg', 'c3d3774c7d6a57a80804514a1be8ed96': 'xmas-news.jpg', '5f57a0fe98c9904060c06a935db1dd5f': 'xmas-post.jpg', 'c1fde77e923c4ddbd957a8003a16ce6e': 'xmas-storia.jpg', '440cd2ec9329cdbc4db2dfffdb85db45': 'y2k-news.jpg', '0c7759ef121380ad67bbe84ed265f036': 'y2k-post.jpg', '230230c47d4a93f049a7526ee95c8a23': 'y2k-storia.jpg',
  '485b2bb9514ded580b9f21a2514352ae': 'reb-ear-post.jpg', '69d8774dc57d9edef1fa2dc595b75535': 'reb-ear-storia.jpg', '74c83b8be102ace6b1ed3c7c06f5ad5f': 'reb-ear-news.jpg',
  '943c5d84ab0ece1051cfb6981046566a': 'reb-ear.jpg',
  '3d81de9c197bc1a9496e4c90ea0a3032': 'banchetto.jpg', '9ec301afd99f9f488a989e338e3c9972': 'lele-lavoro.jpg', '5f45bd9a4e2da4100d54dc36ad193882': 'fil-lettering.jpg', '7438d8d2d4ccff2e8cdd37243fd73ca7': 'fil-tower.jpg',
  'f2a60dd6ef2457b260c2a982749daefc': 'fed-labbra.jpg', '108bad2c8a9e0ac07421749904b51033': 'fed-sopracciglia.jpg',
  '147bc88d32d96136ae8ed0074166a1de': 'hw-orazio.jpg', 'd2cfbaa87165dc69d446ce48aaaccf0c': 'hw-marica-ragno.jpg', '826b7a3aeb4fce87b36393eab4017cde': 'hw-marica-serpente.jpg',
  'fc30243ad06551575c5124d535fe59e9': 'cu-ozan-prima.jpg', '3db89b5dde51e3577c93e53156f58979': 'cu-ozan-dopo.jpg', '652c78d23df5d68de77484fa39d4378a': 'cu-yau.jpg', '12cf720f19b5bdcd2afe608c98eba239': 'cu-gatto.jpg',
  '1eae0213dfb0c257a9d3d47d63905f34': 'gif-0610.jpg',
  '6c4fd7069937fb4de44fd92cba40dc06': 'gif-1010.jpg', '36858f29c794f1ae7cde17061158db6e': 'gif-1013.jpg', '28d7692b544b2d5b127bb775243282ba': 'gif-2010.jpg', 'ce0e4a6e46c9dfc6d7123f74a77cc7bd': 'gif-2710.jpg', 'd509d271616504cb007c576cd03bee12': 'gif-0311.jpg', '5484ad163ef3e7c248853bb8e0238810': 'gif-1011.jpg', '420798558288109cff8fe5a1754d2bb0': 'gif-1711.jpg', '740160b344468cf19c98847921384fff': 'gif-0501.jpg', 'abff0f0eb330c0d904dd5655b84e741a': 'gif-0112.jpg', 'c2309180d5702c0fb8927d1bfe5fa854': 'gif-0812.jpg', '230d113bb650d1be9a70e5c7cbf1a805': 'gif-1512.jpg', '158b7c7b78c0c8aef1ec7b60753777ad': 'gif-2212.jpg', 'd0778096fc732458dacb916e59c3b1ba': 'gif-2912.jpg',
  '0a382204d21d7eec7bd10ba6898725ec': 'w-cu4a.jpg', '5744c47799b7c9c739ed580cb314835d': 'w-cu4b.jpg', 'f8a97294773791872c98aa307eb6ea7e': 'w-cu5a.jpg', '940dbde3e81db93707c7a8eccaf1f788': 'w-cu5b.jpg', 'defd86c44acc1608acec3a2baf894371': 'w-hw1.jpg', 'c9fe5a1fb404dd451c57fe16904f285e': 'w-hw3.jpg', '9b8c3dae9416deda8414f5896aae49a5': 'w-pmu1.jpg', 'ee176dd3cf0d48431bab15bf5fdba822': 'w-pmu3.jpg', '1fc017d435c20e70907f3ea38718ec2a': 'w-ses1.jpg', 'd6fbc435b2954c3bcb67424d2fc99a36': 'w-ses2.jpg', '9b459aaa741ec68b10addbb5d716bb95': 'w-st1.jpg', '670d76ec14996100683eeb8c0d682df2': 'w-st2.jpg', '8368fab5cdb77adae2bbfa192ddb3476': 'w-tr1.jpg', '87dd3ca30a7e406a16d24371b3b989ac': 'w-tr2.jpg',
  // kit 06/10 canvas
  '2a98858cff42fe925be0c7bdc29155c7': 'lettering.png', 'a94d7b3956b581eaf5b73ddff4ee655a': 'bocca.png',
  'f3cd49c68485af8337dc61f392d4d841': 'scalapay.png', '59c945d90d9ab8bf8e41cce7fc52f4cf': 'po_bocca.jpg',
  'a6872ba281edd91d9bd3843125dcbe8d': 'po_gioielli.jpg',
  // kit ottobre-dicembre canvas
  'f76aa4f097dce598a2692bd36380569a': 'lettering.png', 'b6b849e87ef0993310e1ac51deaa6468': 'bocca.png',
  'd6906306ac53852834d3e32c9027e117': 'scalapay.png', '5c1d56a13564a9424fe7903d9cf40a43': 'pmu.jpg',
  '394778564320a3f00c8531d38cde20fc': 'halloween.jpg', '9a33a1e907cdd82f15de95e344a924c0': 'cover.jpg',
  'd981d7fb09068026c3c06ce7dcfcb3aa': 'sicurezza.jpg', '29b5cc538ac65d41b28209700b35c55f': 'fineline.jpg',
  'f310a0fa65609f1bbf165164fe4a584c': 'orecchio.jpg', 'b400767276f32a300a239f4cbbc01853': 'y2k.jpg',
  'd49fcb31eb8fc91211adfe9cb9a12fe1': 'bangles.jpg', 'e073d3a1b607ad90abf21dbc96c057a3': 'giftcard.jpg',
  'a2b6a0c0ed246d8d8f2d2e3bafabd39a': 'braccio.jpg', '14c775062ebde8e49e48d1fdb7fd2ae0': 'studio.jpg',
  'da68bf2463018340e2d7b181859e0aa2': 'trend.jpg',
  '16b00bd6325edb41cf0e4f2dcc6222f2': 'pd1.jpg', '291ea9a019946be88c7a057f858a9ce9': 'pd2.jpg',
  'a354c7b665b65eac54ba6ca31cc5de60': 'pd3.jpg', '29da3d9ce83c94bdf8553fd96e8166a8': 'pd4.jpg',
  '97a3c16cd582fea3ee026b6334798c2a': 'pd5.jpg', '7127f117ec547b856942f30309c7fe2a': 'rebecca-logo.png',
  '73fee0b4a43e887b2072043315e7528d': 'bocca.png', '8dd51a9d9d4e91eeb1c4c60606fa8bd0': 'scalapay.png',
  'f2f93cc14c9f4a9fa705ab577bbed10f': 'lettering.png',
  '7cea92f6ba00af11f6cbf21de2d5aff7': 'autunno.jpg', '49c6a1f34c5173573e4c83d1d590af35': 'gif-0310.jpg', 'bbadaae17076f8d89a2f873c133ba194': 'autunno-zoom.jpg', '8c215c483ca8cb003e403b37cc62e4dd': 'castello.jpg', '844a95ffecf314e3cc737a8a1d9af42e': 'gif-1010.jpg', '4caa0dc42decfd005863c8707c1feb42': 'dk-chetcuti.jpg', '67a7f3c6a5229d2dba02789f71eef4ba': 'dk-wesson.jpg', '219590c8db6c7b94e212b9326e3afba4': 'dk-maffeo.jpg', 'aee5dcf86a5bb7af400bcfadddaba3fe': 'dk-acker.jpg',
  '931ec41f05989e6037609bfbf0cf0feb': 'gif-1013.jpg',
  '1e72bad12f74f6b95772025d956e5349': 'gif-2010.jpg',
  '1e618efd02ea480b126f6d307ce0dca5': 'gif-2710.jpg',
  '96e058478eb8134dd779912272937275': 'gif-0311.jpg',
  '461dca8f0ba2521f228188bc06547400': 'gif-1011.jpg',
  '5d6c2468805ec1c75ef1b739ba0f032f': 'gif-1711.jpg',
  'edef71362a99e0aaf8f49e1de2a4009d': 'gif-2411.jpg',
  '4af67caf75464b293d82828fd2b286a2': 'gif-0112.jpg',
  'eceb32d4483b0d1e6b5e4c119c0d1b5f': 'gif-0812.jpg',
  'fe206f1c869bba02abf70aea28d40ec3': 'gif-1512.jpg',
  '29ca82c3b6bf2efa07f9d8121c4b5507': 'gif-2212.jpg',
  '3ba36647d9ac823a0063cec20426604e': 'gif-2912.jpg',
  'b41e31e6ed19fb942b3cef0373a030f9': 'gif-0610.jpg',
};
const ff = (fam, file, w, style = 'normal') =>
  `@font-face{font-family:'${fam}';font-style:${style};font-weight:${w};src:url('file://${FS}${file}') format('woff2');}`;
const fonts = [
  ff('Oswald', 'oswald/files/oswald-latin-500-normal.woff2', 500),
  ff('Oswald', 'oswald/files/oswald-latin-700-normal.woff2', 700),
  ff('Chakra Petch', 'chakra-petch/files/chakra-petch-latin-400-normal.woff2', 400),
  ff('Chakra Petch', 'chakra-petch/files/chakra-petch-latin-400-italic.woff2', 400, 'italic'),
  ff('Chakra Petch', 'chakra-petch/files/chakra-petch-latin-600-normal.woff2', 600),
  ff('Chakra Petch', 'chakra-petch/files/chakra-petch-latin-700-normal.woff2', 700),
  ff('Bebas Neue', 'bebas-neue/files/bebas-neue-latin-400-normal.woff2', 400),
  ff('Permanent Marker', 'permanent-marker/files/permanent-marker-latin-400-normal.woff2', 400),
  ff('Special Elite', 'special-elite/files/special-elite-latin-400-normal.woff2', 400),
  ff('League Gothic', 'league-gothic/files/league-gothic-latin-400-normal.woff2', 400),
  ff('Cinzel', 'cinzel/files/cinzel-latin-400-normal.woff2', 400),
  ff('Cinzel', 'cinzel/files/cinzel-latin-700-normal.woff2', 700),
  ff('Cormorant Garamond', 'cormorant-garamond/files/cormorant-garamond-latin-400-italic.woff2', 400, 'italic'),
  ff('Cormorant Garamond', 'cormorant-garamond/files/cormorant-garamond-latin-600-italic.woff2', 600, 'italic'),
  ff('Fredoka', 'fredoka/files/fredoka-latin-500-normal.woff2', 500),
  ff('Fredoka', 'fredoka/files/fredoka-latin-600-normal.woff2', 600),
  ff('Fredoka', 'fredoka/files/fredoka-latin-700-normal.woff2', 700),
  ff('Dancing Script', 'dancing-script/files/dancing-script-latin-700-normal.woff2', 700),
  ff('Quicksand', 'quicksand/files/quicksand-latin-500-normal.woff2', 500),
  ff('Quicksand', 'quicksand/files/quicksand-latin-700-normal.woff2', 700),
].join('\n');
const TW = (process.env.KIT_TW || SP + '/render/node_modules/@twemoji/svg') + '/';
const twText = (t) => t.replace(/\p{Extended_Pictographic}\uFE0F?(\u200D\p{Extended_Pictographic}\uFE0F?)*/gu, (m) => {
  if (m === '\u2661' || m === '\u2726' || m === '\u00a9') return m;
  const cps = [...m].map(c => c.codePointAt(0)).filter(c => c !== 0xfe0f).map(c => c.toString(16));
  let f = TW + cps.join('-') + '.svg';
  if (!fs.existsSync(f)) f = TW + [...m].map(c => c.codePointAt(0).toString(16)).join('-') + '.svg';
  if (!fs.existsSync(f)) return m;
  return `<img src="file://${f}" style="height:1em;width:1em;vertical-align:-0.12em;display:inline-block;margin:0 .05em">`;
});
const twify = (h) => h.split(/(<[^>]+>)/).map(x => x.startsWith('<') ? x : twText(x)).join('');

function toHtml(src) {
  let body = src.split('<x-dc>')[1].split('</x-dc>')[0];
  body = body.replace(/<helmet>[\s\S]*?<\/helmet>/, (h) => h.replace(/<link[^>]*>/g, '').replace(/<\/?helmet>/g, ''));
  body = body.replace(/\/_blob\/([0-9a-f]{32})/g, (m, id) => 'file://' + A + blobs[id]);
  body = twify(body);
  return `<!doctype html><html><head><meta charset="utf-8"><style>${fonts}
*{-webkit-font-smoothing:antialiased} body{margin:0}</style></head><body>${body}</body></html>`;
}

(async () => {
  const jobs = JSON.parse(fs.readFileSync(process.argv[2], 'utf8')); // [{src,out,w,h}]
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium', args: ['--allow-file-access-from-files'] });
  const page = await browser.newPage();
  for (const j of jobs) {
    const tmp = path.join(SP, 'render', 'tmp.html');
    fs.writeFileSync(tmp, toHtml(fs.readFileSync(j.src, 'utf8')));
    await page.setViewportSize({ width: j.w, height: j.h });
    await page.goto('file://' + tmp, { waitUntil: 'load' });
    await page.evaluate(() => document.fonts.ready);
    await page.waitForTimeout(300);
    await page.screenshot({ path: j.out, type: 'jpeg', quality: 90, clip: { x: 0, y: 0, width: j.w, height: j.h } });
    console.log('ok', j.out);
  }
  await browser.close();
})();
