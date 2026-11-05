(function(){
  var GROUP_LABELS={
    en:{bar:"Map interests",dietBar:"Diet, across land, sea, and air",all:"All diets",carnivore:"Carnivore",herbivore:"Herbivore",omnivore:"Omnivore",land:"Land dinosaurs",sea:"Marine life",air:"In the air",ice:"Ice Age giants",reef:"Ancient reefs",fins:"From fins to feet",family:"Our family tree",change:"When the world changed",quest:"Dig Quest homes",questGo:"Open Dig Quest",
      carnivoreEmph:"Carnivores on land, in the sea, and in the air. Hell Creek in Montana for Tyrannosaurus rex. Alberta and Utah for other hunters. Solnhofen and Jehol for flyers. Cleveland, the Jurassic Coast story, and Egypt for ocean hunters.",
      herbivoreEmph:"Herbivores are the plant-eaters: horned and long-necked dinosaurs in Alberta and Utah, and Ice Age plant-eaters from Texas to Patagonia. This map’s sea and air pins are hunters, not plant-eaters.",
      omnivoreEmph:"Omnivores ate both. Ornithomimids at Dinosaur Provincial Park are the dinosaur example. Our species at Jebel Irhoud in Morocco is the later one. No sea or air pin on this map is labeled an omnivore.",
      landEmph:"Carnivores and omnivores both belong here. Tyrannosaurus rex hunted in the Hell Creek rocks of east-central Montana in the last few million years before 66 million years ago. At Dinosaur Provincial Park, 75 to 77 million years ago, Gorgosaurus was the hunter and ornithomimids ate a mixed diet. Raptors were hunters too, in Mongolia and in Montana and Wyoming, and the movie animal is not those fossils.",
      seaEmph:"Ocean giants and other marine hunters: armored fish, ichthyosaurs, mosasaurs, and early whales.",
      airEmph:"Pterosaurs, feathered dinosaurs, and Archaeopteryx. Solnhofen and the Jehol rocks are the pins."},
    fr:{bar:"Intérêts de la carte",dietBar:"Régime, sur terre, en mer et dans les airs",all:"Tous les régimes",carnivore:"Carnivore",herbivore:"Herbivore",omnivore:"Omnivore",land:"Dinosaures terrestres",sea:"Vie marine",air:"Dans les airs",ice:"Géants de l’ère glaciaire",reef:"Récifs anciens",fins:"Des nageoires aux pattes",family:"Notre arbre",change:"Quand le monde a changé",quest:"Maisons du Dig Quest",questGo:"Ouvrir Dig Quest",
      carnivoreEmph:"Des carnivores sur terre, en mer et dans les airs. Hell Creek au Montana pour Tyrannosaurus rex. L’Alberta et l’Utah pour d’autres chasseurs. Solnhofen et le Jehol pour le vol. Cleveland, l’histoire de la côte jurassique, et l’Égypte pour les chasseurs des océans.",
      herbivoreEmph:"Les herbivores mangeaient des plantes : dinosaures à cornes et à long cou en Alberta et dans l’Utah, et des géants de l’ère glaciaire du Texas à la Patagonie. Les repères marins et aériens de cette carte sont des chasseurs.",
      omnivoreEmph:"Les omnivores mangeaient les deux. Les ornithomimidés de Dinosaur Provincial Park sont l’exemple dinosaurien. Notre espèce à Jebel Irhoud, au Maroc, est l’exemple plus récent. Aucun repère marin ou aérien n’est étiqueté omnivore.",
      landEmph:"Carnivores et omnivores comptent tous les deux. Tyrannosaurus rex chassait dans les roches de Hell Creek, dans le centre-est du Montana, dans les derniers millions d’années avant il y a 66 millions d’années. À Dinosaur Provincial Park, il y a 75 à 77 millions d’années, Gorgosaurus était le chasseur et les ornithomimidés avaient un régime mixte. Les raptors chassaient aussi, en Mongolie et au Montana et au Wyoming, et l’animal du film n’est pas ces fossiles.",
      seaEmph:"Géants des océans et autres chasseurs marins : poissons cuirassés, ichtyosaures, mosasaures et baleines anciennes.",
      airEmph:"Ptérosaures, dinosaures à plumes et Archaeopteryx. Les repères sont Solnhofen et les roches du Jehol."},
    es:{bar:"Intereses del mapa",dietBar:"Dieta, en tierra, mar y aire",all:"Todas las dietas",carnivore:"Carnívoro",herbivore:"Herbívoro",omnivore:"Omnívoro",land:"Dinosaurios en tierra",sea:"Vida marina",air:"En el aire",ice:"Gigantes de la Edad de Hielo",reef:"Arrecifes antiguos",fins:"De las aletas a los pies",family:"Nuestro árbol",change:"Cuando el mundo cambió",quest:"Casas de Dig Quest",questGo:"Abrir Dig Quest",
      carnivoreEmph:"Carnívoros en tierra, en el mar y en el aire. Hell Creek en Montana para Tyrannosaurus rex. Alberta y Utah para otros cazadores. Solnhofen y Jehol para el vuelo. Cleveland y Egipto para cazadores del océano.",
      herbivoreEmph:"Los herbívoros comían plantas: dinosaurios con cuernos y cuello largo en Alberta y Utah, y gigantes de la Edad de Hielo de Texas a la Patagonia. Las marcas de mar y aire en este mapa son cazadores.",
      omnivoreEmph:"Los omnívoros comían las dos cosas. Los ornitomímidos de Dinosaur Provincial Park son el ejemplo dinosaurio. Nuestra especie en Jebel Irhoud, Marruecos, es el ejemplo más reciente.",
      landEmph:"Carnívoros y omnívoros cuentan los dos. Tyrannosaurus rex cazaba en las rocas de Hell Creek, en el centro-este de Montana, en los últimos millones de años antes de hace 66 millones de años. En Dinosaur Provincial Park, hace 75 a 77 millones de años, Gorgosaurus era el cazador y los ornitomímidos comían una dieta mixta.",
      seaEmph:"Gigantes del océano y otros cazadores marinos: peces acorazados, ictiosaurios, mosasaurios y ballenas antiguas.",
      airEmph:"Pterosaurios, dinosaurios con plumas y Archaeopteryx. Las marcas son Solnhofen y las rocas de Jehol."},
    it:{bar:"Interessi della mappa",dietBar:"Dieta, su terra, mare e aria",all:"Tutte le diete",carnivore:"Carnivoro",herbivore:"Erbivoro",omnivore:"Onnivoro",land:"Dinosauri di terra",sea:"Vita marina",air:"In aria",ice:"Giganti dell’era glaciale",reef:"Scogliere antiche",fins:"Dalle pinne ai piedi",family:"Il nostro albero",change:"Quando il mondo cambiò",quest:"Case di Dig Quest",questGo:"Apri Dig Quest",
      carnivoreEmph:"Carnivori a terra, in mare e in aria. Hell Creek in Montana per Tyrannosaurus rex. Alberta e Utah per altri cacciatori. Solnhofen e Jehol per il volo. Cleveland ed Egitto per i cacciatori dell’oceano.",
      herbivoreEmph:"Gli erbivori mangiavano piante: dinosauri cornuti e dal collo lungo in Alberta e nello Utah, e giganti dell’era glaciale dal Texas alla Patagonia. I segnaposto di mare e aria su questa mappa sono cacciatori.",
      omnivoreEmph:"Gli onnivori mangiavano entrambi. Gli ornitomimidi di Dinosaur Provincial Park sono l’esempio dinosauro. La nostra specie a Jebel Irhoud, in Marocco, è l’esempio più recente.",
      landEmph:"Carnivori e onnivori contano entrambi. Tyrannosaurus rex cacciava nelle rocce di Hell Creek, nel Montana centro-orientale, negli ultimi milioni di anni prima di 66 milioni di anni fa. A Dinosaur Provincial Park, da 75 a 77 milioni di anni fa, Gorgosaurus era il cacciatore e gli ornitomimidi avevano una dieta mista.",
      seaEmph:"Giganti dell’oceano e altri cacciatori marini: pesci corazzati, ittiosauri, mosasauri e balene antiche.",
      airEmph:"Pterosauri, dinosauri piumati e Archaeopteryx. I segnaposto sono Solnhofen e le rocce di Jehol."},
    ar:{bar:"اهتمامات الخريطة",dietBar:"الغذاء، في البر والبحر والهواء",all:"كل الغذاء",carnivore:"لاحم",herbivore:"عاشب",omnivore:"قارِت",land:"ديناصورات اليابسة",sea:"حياة البحر",air:"في الهواء",ice:"عمالقة العصر الجليدي",reef:"شعاب قديمة",fins:"من الزعانف إلى الأقدام",family:"شجرتنا",change:"حين تغيّر العالم",quest:"بيوت Dig Quest",questGo:"افتح Dig Quest",
      carnivoreEmph:"لاحمات في البر والبحر والهواء. هيل كريك في مونتانا لتيرانوصور. ألبرتا ويوتا لصيادين آخرين. سولنهوفن وجيهول للطيران. كليفلاند ومصر لصيادي المحيط.",
      herbivoreEmph:"العواشب أكلت النبات: ديناصورات ذات قرون ورقاب طويلة في ألبرتا ويوتا، وعمالقة العصر الجليدي من تكساس إلى باتاغونيا. دبابيس البحر والهواء في هذه الخريطة صيادون.",
      omnivoreEmph:"القوارت أكلت الاثنين. الأورنيثوميميات في منتزه الديناصورات هي مثال الديناصور. نوعنا في جبل إيغود بالمغرب هو المثال الأحدث.",
      landEmph:"آكلات اللحم وآكلات كل شيء معًا. اصطاد تيرانوصور في صخور هيل كريك في شرق وسط مونتانا في آخر ملايين السنين قبل 66 مليون سنة. في منتزه الديناصورات، قبل 75 إلى 77 مليون سنة، كان غورغوصور الصياد وكانت الأورنيثوميميات تأكل غذاءً مختلطًا.",
      seaEmph:"عمالقة المحيط وصيادون بحريون آخرون: أسماك مدرعة، وإكثيوصورات، وموزاصورات، وحيتان قديمة.",
      airEmph:"تيروسورات، وديناصورات ذات ريش، وأركيوبتركس. الدبابيس هي سولنهوفن وصخور جيهول."},
    he:{bar:"תחומי עניין במפה",dietBar:"תפריט, ביבשה בים ובאוויר",all:"כל התפריטים",carnivore:"טורף",herbivore:"אוכל-צמחים",omnivore:"אוכל-כול",land:"דינוזאורים ביבשה",sea:"חיים בים",air:"באוויר",ice:"ענקי עידן הקרח",reef:"שוניות עתיקות",fins:"מסנפירים לרגליים",family:"העץ שלנו",change:"כשהעולם השתנה",quest:"הבתים של Dig Quest",questGo:"פתיחת Dig Quest",
      carnivoreEmph:"טורפים ביבשה, בים ובאוויר. הל קריק במונטנה לטירנוזאורוס רקס. אלברטה ויוטה לציידים אחרים. זולנהופן וג׳הול לתעופה. קליבלנד ומצרים לציידי אוקיינוס.",
      herbivoreEmph:"אוכלי הצמחים: דינוזאורים בעלי קרניים וצוואר ארוך באלברטה וביוטה, וענקי עידן הקרח מטקסס עד פטגוניה. נעצי הים והאוויר במפה הזו הם ציידים.",
      omnivoreEmph:"אוכלי-הכול אכלו גם וגם. האורניתּומימידים בפארק הדינוזאורים הם הדוגמה של הדינוזאור. המין שלנו בג׳בל אירחוד במרוקו הוא הדוגמה המאוחרת.",
      landEmph:"טורפים ואוכלי-כול שניהם כאן. טירנוזאורוס רקס צד בסלעי הל קריק במזרח-מרכז מונטנה במיליוני השנים האחרונות לפני 66 מיליון שנים. בפארק הדינוזאורים, לפני 75 עד 77 מיליון שנים, גורגוזאורוס היה הצייד והאורניתּומימידים אכלו תפריט מעורב.",
      seaEmph:"ענקי אוקיינוס וציידים ימיים אחרים: דגים משוריינים, איכתיוזאורים, מוזאזאורים ולווייתנים קדומים.",
      airEmph:"פטרוזאורים, דינוזאורים עם נוצות וארכאופטריקס. הנעצים הם זולנהופן וסלעי ג׳הול."}
  };
  var w=document.querySelector('.bsp-map');
  if(!w||!window.L)return;
  fetch(w.getAttribute('data-src')).then(function(r){return r.json()}).then(function(d){
    var m=L.map('wm',{worldCopyJump:true}).setView([20,10],2);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',{maxZoom:12,attribution:'&copy; OpenStreetMap contributors'}).addTo(m);
    var ui=d.ui||{},markers={},sites={};
    d.sites.forEach(function(s){
      var coin=s.teach&&s.specimen&&s.restoration;
      var marker=L.circleMarker([s.lat,s.lng],coin?{radius:10,color:'#f3e2a8',weight:2,fillColor:'#c9a227',fillOpacity:.95}:{radius:9,color:'#ffb347',fillColor:'#c8641c',fillOpacity:.85});
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
      body.querySelectorAll('video[data-hd]').forEach(function(v){
        if(matchMedia('(prefers-reduced-motion: reduce)').matches)return;
        var big=matchMedia('(min-width: 1100px)').matches;
        var m=document.createElement('source');
        m.type='video/mp4';
        m.src=big?v.dataset.hd:v.dataset.sd;
        v.appendChild(m);
        v.preload='auto';
        v.autoplay=true;
        v.load();
        var p=v.play();
        if(p&&p.catch)p.catch(function(){});
      });
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
    var shown=[];
    function showNames(names){
      shown.forEach(function(marker){m.removeLayer(marker)});
      shown=[];
      var bounds=[];
      (names||[]).forEach(function(name){
        var marker=markers[name];
        if(!marker)return;
        marker.addTo(m);
        shown.push(marker);
        bounds.push(marker.getLatLng());
      });
      if(bounds.length)m.fitBounds(bounds,{padding:[24,24],maxZoom:5});
    }
    function mountGroups(pack){
      var lang=(document.documentElement.lang||'en').slice(0,2);
      var label=GROUP_LABELS[lang]||GROUP_LABELS.en;
      var screen=document.querySelector('.wm-screen');
      var stage=document.querySelector('.wm-stage');
      if(!screen||!stage||!pack)return;
      var bar=document.createElement('div');
      bar.className='wm-groups';
      bar.setAttribute('role','toolbar');
      bar.setAttribute('aria-label',label.bar);
      var diets=document.createElement('div');
      diets.className='wm-groups wm-diets';
      diets.setAttribute('role','toolbar');
      diets.setAttribute('aria-label',label.dietBar);
      var emph=document.createElement('p');
      emph.className='wm-emph';
      var questNames={};
      var group='land', diet='all';
      Object.keys(pack.quest||{}).forEach(function(k){(pack.quest[k]||[]).forEach(function(n){questNames[n]=k})});
      function namesFor(id){
        if(id==='quest')return [];
        var list=(pack.groups&&pack.groups[id])||[];
        if(diet==='all')return list;
        var allowed={};
        ((pack.diets&&pack.diets[diet])||[]).forEach(function(n){allowed[n]=1});
        var pool=['land','sea','air'];
        if(pool.indexOf(id)!==-1){
          var span=[];
          pool.forEach(function(lane){((pack.groups&&pack.groups[lane])||[]).forEach(function(n){if(allowed[n]&&span.indexOf(n)===-1)span.push(n)})});
          return span;
        }
        return list.filter(function(n){return allowed[n]});
      }
      function paint(){
        bar.querySelectorAll('button').forEach(function(b){b.setAttribute('aria-pressed',b.getAttribute('data-group')===group?'true':'false')});
        diets.querySelectorAll('button').forEach(function(b){b.setAttribute('aria-pressed',b.getAttribute('data-diet')===diet?'true':'false')});
        if(group==='quest'){
          showNames([]);
          emph.innerHTML='<a href="Quest.html#homes">'+label.questGo+'</a>';
          return;
        }
        showNames(namesFor(group));
        emph.textContent=(diet!=='all'&&label[diet+'Emph'])||label[group+'Emph']||'';
      }
      function press(id){group=id;paint();}
      (pack.order||[]).forEach(function(id){
        var b=document.createElement('button');
        b.type='button';
        b.setAttribute('data-group',id);
        b.textContent=label[id]||id;
        if((pack.top||[]).indexOf(id)!==-1)b.className='is-top';
        b.addEventListener('click',function(){press(id)});
        bar.appendChild(b);
      });
      var qb=document.createElement('button');
      qb.type='button';
      qb.setAttribute('data-group','quest');
      qb.textContent=label.quest;
      qb.addEventListener('click',function(){press('quest')});
      bar.appendChild(qb);
      ['all','carnivore','herbivore','omnivore'].forEach(function(id){
        var b=document.createElement('button');
        b.type='button';
        b.setAttribute('data-diet',id);
        b.textContent=label[id]||id;
        b.addEventListener('click',function(){diet=id;paint()});
        diets.appendChild(b);
      });
      screen.insertBefore(emph,stage);
      screen.insertBefore(diets,emph);
      screen.insertBefore(bar,diets);
      var pin='';
      try{pin=new URLSearchParams(location.search).get('pin')||''}catch(err){}
      if(pin&&sites[pin]){
        var home=questNames[pin];
        var groupId=(pack.order||[]).filter(function(id){return (pack.groups[id]||[]).indexOf(pin)!==-1})[0];
        if(groupId)press(groupId);
        else if(home)press('quest');
        if(markers[pin]){markers[pin].addTo(m);shown.push(markers[pin]);m.setView(markers[pin].getLatLng(),4)}
        openCoin(sites[pin]);
      }else press('land');
    }
    var src=w.getAttribute('data-src')||'';
    var rel=src.indexOf('../')===0?'../':'';
    var base=src.replace(/fossil-map\.[a-z]+\.json$/,'');
    Promise.all([
      fetch(base+'map-groups.json').then(function(r){return r.json()}),
      fetch(base+'creature-heroes.json').then(function(r){return r.json()}).catch(function(){return {sites:{}}})
    ]).then(function(pair){
      var heroes=(pair[1]&&pair[1].sites)||{};
      Object.keys(heroes).forEach(function(name){
        var h=heroes[name];
        if(!sites[name]||!sites[name].specimen||!h)return;
        sites[name].specimen.video={poster:rel+(h.poster||''),hd:rel+h.hd,sd:rel+(h.sd||h.hd)};
        if(h.alt)sites[name].specimen.alt=h.alt;
      });
      mountGroups(pair[0]);
    }).catch(function(){
      showNames(Object.keys(markers));
    });
  }).catch(function(){});
  function esc(s){return String(s==null?'':s).replace(/[&<>"']/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]})}
  function https(u){return typeof u==='string'&&/^https:\/\//i.test(u)?u:''}
  function sitePage(u){
    if(typeof u!=='string'||u.indexOf('..')!==-1)return '';
    return /^(?:[A-Za-z0-9_-]+\/)*[A-Za-z0-9_-]+\.html$/.test(u)?u:'';
  }
  function hiRes(url){
    return url.replace(/\/(\d+)px-([^/?#]+)$/i,function(_,w,name){
      return '/'+((parseInt(w,10)>=1920)?w:'1920')+'px-'+name;
    });
  }
  function fig(img,fallback,hero){
    if(!img)return '';
    var label=img.label||fallback;
    var src=https(img.src),href=https(img.href),credit=esc(img.credit||'');
    if(href)credit='<a href="'+esc(href)+'" rel="noopener noreferrer">'+credit+'</a>';
    var media='';
    if(hero&&img.video&&img.video.hd){
      var v=img.video;
      media='<video class="wm-coin-img wm-coin-video" muted playsinline preload="none" poster="'+esc(v.poster||'')+'" width="1920" height="1080" aria-label="'+esc(img.alt||label)+'" data-hd="'+esc(v.hd)+'" data-sd="'+esc(v.sd||v.hd)+'"></video>';
    }else if(src){
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
    return '<article class="wm-coin" dir="auto"><p class="wm-coin-name">'+esc(s.n)+'</p>'+(s.era?'<p class="wm-coin-era">'+esc(s.era)+'</p>':'')+'<div class="wm-coin-layout"><div class="wm-coin-hero">'+fig(s.specimen,ui.specimen||'Specimen',true)+fig(s.restoration,ui.restoration||'Life restoration',false)+'</div><div class="wm-coin-copy"><dl>'+row(ui.what||'What',t.what)+row(ui.when||'When it lived',t.when)+row(ui.where||'Where found',t.where)+row(ui.why||'Why it matters',t.why)+'</dl>'+read+pair+(more?'<p class="wm-coin-more">'+esc(ui.learnMore||'Learn more')+'</p><ul>'+more+'</ul>':'')+'</div></div></article>';
  }
})();
