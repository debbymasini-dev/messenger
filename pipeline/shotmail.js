const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});const p=await b.newPage({viewport:{width:640,height:900},deviceScaleFactor:1.5});
for(const k of process.argv.slice(2)){await p.goto('file://'+(process.env.KIT_SP||'/tmp/kit')+'/kitassets/email/'+k+'.html',{waitUntil:'networkidle',timeout:60000}).catch(e=>console.log(k,e.message));await p.evaluate((src)=>{document.querySelectorAll('img[src*=giphy],img[src*=pinimg]').forEach(i=>i.src=src)},'file://'+(process.env.KIT_SP||'/tmp/kit')+'/assets/gif-'+k+'.jpg');await p.waitForTimeout(1500);
const bad=await p.evaluate(()=>[...document.images].filter(i=>!i.naturalWidth).map(i=>i.src));if(bad.length)console.log(k,'broken',bad);
await p.screenshot({path:''+(process.env.KIT_SP||'/tmp/kit')+'/news/newsletter-'+k+'.jpg',fullPage:true,type:'jpeg',quality:85});console.log('ok',k)}
await b.close()})();
