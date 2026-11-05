(function(){
  var w=document.querySelector('.bsp-map');
  if(!w||!window.L)return;
  fetch(w.getAttribute('data-src')).then(function(r){return r.json()}).then(function(d){
    var m=L.map('wm',{worldCopyJump:true}).setView([20,10],2);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',{maxZoom:12,attribution:'&copy; OpenStreetMap contributors'}).addTo(m);
    var ui=d.ui||{},markers={},sites={};
    d.sites.forEach(function(s){
      var coin=s.teach&&s.specimen&&s.restoration;
      var marker=L.circleMarker([s.lat,s.lng],coin?{radius:10,color:'#f3e2a8',weight:2,fillColor:'#c9a227',fillOpacity:.95}:{radius:9,color:'#ffb347',fillColor:'#c8641c',fillOpacity:.85}).addTo(m);
      if(coin)marker.on('click',function(){openCoin(s)});
      else marker.bindPopup('<strong>'+esc(s.n)+'</strong><br><em>'+esc(d.pin)+'</em>',{maxWidth:340,minWidth:210});
      markers[s.n]=marker;
      sites[s.n]=s;
    });
    var modal,panel,body,lastFocus;
    function closeLabel(){
      var lang=(document.documentElement.lang||'en').slice(0,2);
      return {en:'Close',fr:'Fermer',es:'Cerrar',ar:'إغلاق',it:'Chiudi',he:'סגירה'}[lang]||'Close';
    }
    function lockPage(on){
      document.documentElement.classList.toggle('wm-coin-open',on);
      [document.getElementById('topnav'),document.getElementById('main'),document.querySelector('footer')].forEach(function(el){
        if(el)el.inert=on;
      });
    }
    function closeCoin(){
      if(!modal||modal.hidden)return;
      modal.hidden=true;
      body.innerHTML='';
      lockPage(false);
      if(lastFocus&&lastFocus.focus)lastFocus.focus();
    }
    function openNamed(name){
      var site=sites[name],marker=markers[name];
      if(!site||!marker)return;
      m.flyTo(marker.getLatLng(),Math.max(m.getZoom(),4),{duration:.6});
      openCoin(site,true);
    }
    function ensureModal(){
      if(modal)return;
      modal=document.createElement('div');
      modal.className='wm-coin-modal';
      modal.hidden=true;
      modal.innerHTML='<div class="wm-coin-backdrop" data-wm-close></div><div class="wm-coin-panel" role="dialog" aria-modal="true" aria-labelledby="wm-coin-title"><div class="wm-coin-bar"><button type="button" class="wm-coin-x" data-wm-close><span class="wm-coin-x-t"></span><span class="wm-coin-x-mark" aria-hidden="true">×</span></button></div><div class="wm-coin-body"></div></div>';
      document.body.appendChild(modal);
      panel=modal.querySelector('.wm-coin-panel');
      body=modal.querySelector('.wm-coin-body');
      modal.querySelector('.wm-coin-x-t').textContent=closeLabel();
      modal.addEventListener('click',function(e){if(e.target.closest('[data-wm-close]'))closeCoin()});
      document.addEventListener('keydown',function(e){
        if(!modal||modal.hidden)return;
        if(e.key==='Escape'){e.preventDefault();closeCoin();return}
        if(e.key!=='Tab')return;
        var nodes=focusables();
        if(!nodes.length){e.preventDefault();return}
        var first=nodes[0],last=nodes[nodes.length-1],active=document.activeElement;
        var inside=panel.contains(active);
        if(e.shiftKey){
          if(!inside||active===first){e.preventDefault();last.focus()}
        }else if(!inside||active===last){e.preventDefault();first.focus()}
      });
    }
    function openCoin(s,keepFocus){
      ensureModal();
      if(!keepFocus)lastFocus=document.activeElement;
      body.innerHTML=coinHtml(s,ui);
      var name=body.querySelector('.wm-coin-name');
      if(name)name.id='wm-coin-title';
      var btn=body.querySelector('[data-pair]');
      if(btn)btn.addEventListener('click',function(){openNamed(btn.getAttribute('data-pair'))});
      modal.hidden=false;
      panel.scrollTop=0;
      lockPage(true);
      body.querySelectorAll('img[data-fallback]').forEach(function(img){
        img.addEventListener('error',function(){
          var fallback=img.getAttribute('data-fallback');
          if(fallback&&img.getAttribute('src')!==fallback){img.setAttribute('src',fallback)}
        });
      });
      modal.querySelector('.wm-coin-x').focus();
    }
    function focusables(){
      return Array.prototype.filter.call(panel.querySelectorAll('button,a[href],input,select,textarea,[tabindex]'),function(el){
        return !el.disabled&&el.getAttribute('tabindex')!=='-1'&&el.offsetParent!==null;
      });
    }
    var b=document.querySelector('.bsp-mascot');
    if(b)b.addEventListener('click',function(){m.flyTo([62,-20],3)});
    try{
      var pin=new URLSearchParams(location.search).get('pin');
      if(pin&&sites[pin]) openCoin(sites[pin]);
    }catch(err){}
  }).catch(function(){});
  function esc(s){return String(s==null?'':s).replace(/[&<>"']/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]})}
  function https(u){return typeof u==='string'&&/^https:\/\//i.test(u)?u:''}
  function sitePage(u){
    if(typeof u!=='string'||u.indexOf('..')!==-1)return '';
    return /^(?:[A-Za-z0-9_-]+\/)*[A-Za-z0-9_-]+\.html$/.test(u)?u:'';
  }
  function hiRes(url){
    // Card pictures stay near 1080–1920 wide. A stored thumb below that is requested at 1920. Full files are not enlarged.
    return url.replace(/\/(\d+)px-([^/?#]+)$/i,function(_,w,name){
      return '/'+((parseInt(w,10)>=1920)?w:'1920')+'px-'+name;
    });
  }
  function looksLikeLife(img){
    if(!img||!img.src) return false;
    var low=[img.label,img.caption,img.alt,img.credit].join(' ').toLowerCase();
    if(/not a life restoration|not an artist|not a restoration|not a picture of the living|not a drawing|another fossil|another specimen/.test(low)) return false;
    return /life restoration|artist|illustration|\bdrawing\b|\bpainting\b|diorama|approximation|\bsculpture|\bmodel of\b|knight/.test(low);
  }
  function fig(img,fallback,hero){
    if(!img)return '';
    var label=img.label||fallback;
    var src=https(img.src),href=https(img.href),credit=esc(img.credit||'');
    if(href)credit='<a href="'+esc(href)+'" rel="noopener noreferrer">'+credit+'</a>';
    var media='';
    if(src){
      var big=hiRes(src);
      media='<img class="wm-coin-img" src="'+esc(big)+'" data-fallback="'+esc(src)+'" alt="'+esc(img.alt||label)+'" decoding="async"'+(hero?' fetchpriority="high"':' loading="lazy"')+'>';
    }
    var cap=img.caption?'<span class="wm-coin-cap">'+esc(img.caption)+'</span>':'';
    return '<figure class="wm-coin-fig'+(hero?' is-hero':' is-side')+'">'+media+'<figcaption><span class="wm-coin-k">'+esc(label)+'</span>'+cap+' '+credit+'</figcaption></figure>';
  }
  function row(dt,dd){return dd?'<dt>'+esc(dt)+'</dt><dd>'+esc(dd)+'</dd>':''}
  function coinHtml(s,ui){
    var t=s.teach||{},links=Array.isArray(s.learnMore)?s.learnMore:(s.learnMore?[s.learnMore]:[]);
    var more=links.map(function(x){var href=https(x&&x.href);return href?'<li><a href="'+esc(href)+'" rel="noopener noreferrer">'+esc((x&&x.label)||ui.learnMore||'Learn more')+'</a></li>':''}).join('');
    var readHref=sitePage(s.readMore&&s.readMore.href);
    var read=readHref?'<p class="wm-coin-read"><a href="'+esc(readHref)+'">'+esc((s.readMore&&s.readMore.label)||ui.readMore||'Read more')+'</a></p>':'';
    var pair=s.pairWith?'<p class="wm-coin-pair"><button type="button" class="wm-coin-pairbtn" data-pair="'+esc(s.pairWith)+'">'+esc(ui.seeAlso||'See also')+': '+esc(s.pairWith)+'</button></p>':'';
    var life=looksLikeLife(s.restoration);
    var leadImg=life?s.restoration:s.specimen;
    var leadLabel=life?(ui.restoration||'Life restoration'):(ui.specimen||'Specimen');
    var nextImg=life?s.specimen:s.restoration;
    var nextLabel=life?(ui.specimen||'Specimen'):(ui.restoration||'Life restoration');
    return '<article class="wm-coin" dir="auto"><p class="wm-coin-name">'+esc(s.n)+'</p>'+(s.era?'<p class="wm-coin-era">'+esc(s.era)+'</p>':'')+'<div class="wm-coin-layout"><div class="wm-coin-hero">'+fig(leadImg,leadLabel,true)+fig(nextImg,nextLabel,false)+'</div><div class="wm-coin-copy"><dl>'+row(ui.what||'What',t.what)+row(ui.when||'When it lived',t.when)+row(ui.where||'Where found',t.where)+row(ui.why||'Why it matters',t.why)+'</dl>'+read+pair+(more?'<p class="wm-coin-more">'+esc(ui.learnMore||'Learn more')+'</p><ul>'+more+'</ul>':'')+'</div></div></article>';
  }
})();
