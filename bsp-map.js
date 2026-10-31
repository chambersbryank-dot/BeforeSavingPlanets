(function(){
  var w=document.querySelector('.bsp-map');
  if(!w||!window.L)return;
  fetch(w.getAttribute('data-src')).then(function(r){return r.json()}).then(function(d){
    var m=L.map('wm',{worldCopyJump:true}).setView([20,10],2);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',{maxZoom:12,attribution:'&copy; OpenStreetMap contributors'}).addTo(m);
    var ui=d.ui||{};
    d.sites.forEach(function(s){
      var coin=s.teach&&s.specimen&&s.restoration;
      L.circleMarker([s.lat,s.lng],coin?{radius:10,color:'#f3e2a8',weight:2,fillColor:'#c9a227',fillOpacity:.95}:{radius:9,color:'#ffb347',fillColor:'#c8641c',fillOpacity:.85}).addTo(m).bindPopup(coin?coinHtml(s,ui):'<strong>'+esc(s.n)+'</strong><br><em>'+esc(d.pin)+'</em>',{maxWidth:340,minWidth:coin?280:210,className:coin?'wm-coin-pop':''});
    });
    var b=document.querySelector('.bsp-mascot');
    if(b)b.addEventListener('click',function(){m.flyTo([62,-20],3)});
  }).catch(function(){});
  function esc(s){return String(s==null?'':s).replace(/[&<>"']/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]})}
  function https(u){return typeof u==='string'&&/^https:\/\//i.test(u)?u:''}
  function fig(img,label){
    if(!img)return '';
    var src=https(img.src),href=https(img.href),credit=esc(img.credit||'');
    if(href)credit='<a href="'+esc(href)+'" rel="noopener noreferrer">'+credit+'</a>';
    var media=src?'<img class="wm-coin-img" src="'+esc(src)+'" alt="'+esc(img.alt||label)+'" width="118" height="118" loading="lazy">':'';
    return '<figure class="wm-coin-fig">'+media+'<figcaption><span class="wm-coin-k">'+esc(label)+'</span> '+credit+'</figcaption></figure>';
  }
  function row(dt,dd){return dd?'<dt>'+esc(dt)+'</dt><dd>'+esc(dd)+'</dd>':''}
  function coinHtml(s,ui){
    var t=s.teach||{},links=Array.isArray(s.learnMore)?s.learnMore:(s.learnMore?[s.learnMore]:[]);
    var more=links.map(function(x){var href=https(x&&x.href);return href?'<li><a href="'+esc(href)+'" rel="noopener noreferrer">'+esc((x&&x.label)||ui.learnMore||'Learn more')+'</a></li>':''}).join('');
    return '<article class="wm-coin"><div class="wm-coins">'+fig(s.specimen,ui.specimen||'Specimen')+fig(s.restoration,ui.restoration||'Life restoration')+'</div><p class="wm-coin-name">'+esc(s.n)+'</p>'+(s.era?'<p class="wm-coin-era">'+esc(s.era)+'</p>':'')+'<dl>'+row(ui.what||'What',t.what)+row(ui.when||'When it lived',t.when)+row(ui.where||'Where found',t.where)+row(ui.why||'Why it matters',t.why)+'</dl>'+(more?'<p class="wm-coin-more">'+esc(ui.learnMore||'Learn more')+'</p><ul>'+more+'</ul>':'')+'</article>';
  }
})();
