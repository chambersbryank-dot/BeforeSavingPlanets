/* Deep Time. The full page (data-all=1) is a timeline and a what-lived list.
   It does not draw the paleomap or a what-died-out panel.
   Species "then" views still use the flat PALEOMAP frames and the baked paths. */
(function(){
  var reduce=window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  function esc(s){return String(s==null?'':s).replace(/[&<>"']/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]})}
  function pad(n){n=Math.round(n);return (n<10?'00':n<100?'0':'')+n}
  function frame(ma){
    var q=Math.round(ma/20)*20;
    if(q<0)q=0;
    if(q>540)q=540;
    return 'm'+pad(q)+'.webp';
  }
  function pair(ma){
    var lo=Math.floor(ma/20)*20;
    var hi=lo+20;
    if(lo<0)lo=0;
    if(hi>540)hi=540;
    var t=hi===lo?0:(ma-lo)/(hi-lo);
    return {lo:lo,hi:hi,t:t};
  }
  function at(path, ma){
    var keys=Object.keys(path).map(Number).sort(function(a,b){return a-b});
    var lo=keys[0], hi=keys[keys.length-1];
    for(var i=0;i<keys.length;i++){
      if(keys[i]<=ma)lo=keys[i];
      if(keys[i]>=ma){hi=keys[i];break}
    }
    var a=path[String(lo)], b=path[String(hi)];
    if(!b||lo===hi)return a;
    var u=(ma-lo)/(hi-lo);
    var d=b[0]-a[0];
    if(d>180)d-=360;
    if(d<-180)d+=360;
    return [a[0]+d*u, a[1]+(b[1]-a[1])*u];
  }
  function period(list, ma){
    var best=null, span=1e9;
    for(var i=0;i<list.length;i++){
      var p=list[i];
      if(ma<=p.older && ma>=p.younger){
        var w=p.older-p.younger;
        if(w<span){span=w;best=p}
      }
    }
    return best;
  }
  function boot(root, pack){
    var lang=root.getAttribute('data-lang')==='fr'?'fr':'en';
    var fullPage=root.getAttribute('data-all')==='1';
    var focus=root.getAttribute('data-focus')||'';
    var jump=null;
    if(!focus && root.getAttribute('data-all')==='1' && location.hash){
      var id=decodeURIComponent(location.hash.slice(1));
      jump=pack.species.filter(function(s){return s.id===id})[0]||null;
    }
    var species=pack.species.filter(function(s){return !focus||s.id===focus});
    var tex=root.getAttribute('data-tex');
    var stage=document.createElement('div');
    stage.className='dt-stage';
    var imgA=document.createElement('img');
    var imgB=document.createElement('img');
    imgA.alt=''; imgB.alt='';
    imgA.width=640; imgA.height=320; imgB.width=640; imgB.height=320;
    stage.appendChild(imgA); stage.appendChild(imgB);
    var pinLayer=document.createElement('div');
    pinLayer.className='dt-pins';
    stage.appendChild(pinLayer);
    var controls=document.createElement('div');
    controls.className='dt-controls';
    var play=document.createElement('button');
    play.type='button';
    play.className='dt-play';
    var playWord=lang==='fr'?'Lecture':'Play';
    var pauseWord=lang==='fr'?'Pause':'Pause';
    play.textContent=playWord;
    play.setAttribute('aria-pressed','false');
    if(reduce)play.hidden=true;
    var slider=document.createElement('input');
    slider.type='range';
    slider.className='dt-slider';
    var spanMa=pack.fromMa||539;
    slider.min='0'; slider.max=String(spanMa); slider.step='1';
    var start=spanMa;
    var sp0=focus?species[0]:jump;
    if(sp0)start=Math.round((sp0.older+sp0.younger)/2);
    slider.value=String(start);
    slider.setAttribute('aria-label', lang==='fr'?'Millions d’années avant aujourd’hui, le plus ancien à gauche':'Millions of years ago, oldest on the left');
    controls.appendChild(slider);
    var readout=document.createElement('p');
    readout.className='dt-readout';
    readout.setAttribute('aria-live','polite');
    var dock=document.createElement('div');
    dock.className='dt-dock';
    var speedLabel=document.createElement('label');
    speedLabel.className='dt-speed';
    speedLabel.appendChild(document.createTextNode(lang==='fr'?'Vitesse':'Speed'));
    var speed=document.createElement('select');
    speed.className='dt-speed-select';
    speed.setAttribute('aria-label', lang==='fr'?'Vitesse de lecture':'Playback speed');
    var rates=[
      {v:'2', en:'Slow', fr:'Lent'},
      {v:'6', en:'Medium', fr:'Moyen'},
      {v:'12', en:'Fast', fr:'Rapide'},
      {v:'24', en:'Fastest', fr:'Très rapide'}
    ];
    rates.forEach(function(r){
      var opt=document.createElement('option');
      opt.value=r.v;
      opt.textContent=lang==='fr'?r.fr:r.en;
      if(r.v==='2')opt.selected=true;
      speed.appendChild(opt);
    });
    speedLabel.appendChild(speed);
    dock.appendChild(play);
    dock.appendChild(speedLabel);
    dock.appendChild(readout);
    stage.appendChild(dock);
    var maPerSec=2;
    var legend=document.createElement('ul');
    legend.className='dt-legend';
    species.forEach(function(s){
      var li=document.createElement('li');
      li.dataset.id=s.id;
      var prefix=root.getAttribute('data-prefix')||'';
      var span=lang==='fr'?s.spanFr:s.span;
      var cite=lang==='fr'?(s.sourceFr||s.source):(s.source||'');
      var citeLink=s.sourceHref?' <a href="'+esc(s.sourceHref)+'" rel="noopener noreferrer">'+esc(cite)+'</a>':'';
      li.innerHTML='<img src="'+esc(prefix+s.icon)+'" alt="" width="28" height="32"><span><strong>'+esc(s.id)+'</strong> '+esc(span)+citeLink+'</span>';
      legend.appendChild(li);
    });
    var method=document.createElement('p');
    method.className='dt-method';
    method.textContent=lang==='fr'?pack.methodFr:pack.method;
    var scale=document.createElement('div');
    scale.className='dt-scale';
    var eras=document.createElement('div');
    eras.className='dt-eras';
    var periods=document.createElement('div');
    periods.className='dt-periods';
    var marker=document.createElement('div');
    marker.className='dt-now';
    (pack.eras||[]).forEach(function(e){
      var d=document.createElement('div');
      d.style.flex=String(e.older-e.younger);
      d.dataset.older=String(e.older);
      d.dataset.younger=String(e.younger);
      d.textContent=lang==='fr'?e.fr:e.en;
      d.title=lang==='fr'?e.fr:e.en;
      eras.appendChild(d);
    });
    var key=document.createElement('div');
    key.className='dt-key';
    var keyLabel=lang==='fr'?'Périodes, de la plus ancienne à aujourd’hui':'Periods, oldest to today';
    key.setAttribute('aria-label', keyLabel);
    function gem(){
      return '<svg class="dt-gem" viewBox="0 0 24 24" width="16" height="16" aria-hidden="true"><path d="M12 1.4 3.8 8.6 12 22.4 20.2 8.6z"/><path class="dt-gem-shine" d="M12 1.4 7.6 8.6h8.8z"/></svg>';
    }
    function tone(b){
      if(b.younger>=251.9) return 'dt-tone-paleo';
      if(b.older<=66.05) return 'dt-tone-ceno';
      return 'dt-tone-meso';
    }
    (pack.bands||[]).forEach(function(b){
      var name=lang==='fr'?b.fr:b.en;
      var d=document.createElement('button');
      d.type='button';
      d.className='dt-per '+tone(b);
      d.style.flex=String(b.older-b.younger);
      d.dataset.en=b.en;
      d.innerHTML=gem()+'<span class="dt-name">'+esc(name)+'</span><span class="dt-abbr">'+esc(b.short||name)+'</span>';
      d.title=name;
      d.setAttribute('aria-label', (lang==='fr'?'Aller au milieu du ':'Go to the middle of the ')+name);
      d.addEventListener('click', function(){ go((b.older+b.younger)/2); });
      periods.appendChild(d);
      var chip=document.createElement('button');
      chip.type='button';
      chip.dataset.en=b.en;
      chip.innerHTML=gem()+'<span>'+esc(name)+'</span>';
      chip.setAttribute('aria-label', (lang==='fr'?'Aller au milieu du ':'Go to the middle of the ')+name);
      chip.addEventListener('click', function(){ go((b.older+b.younger)/2); });
      key.appendChild(chip);
    });
    var filters=document.createElement('div');
    filters.className='dt-filters';
    filters.setAttribute('role','group');
    filters.setAttribute('aria-label', lang==='fr'?'Catégories du vivant':'Categories of life');
    var chipDefs=[
      {id:'all', en:'All', fr:'Tout'},
      {id:'dinosaurs', en:'Dinosaurs', fr:'Dinosaures'},
      {id:'marine', en:'Marine life', fr:'Vie marine'},
      {id:'flying', en:'Flying', fr:'En vol'},
      {id:'mammals', en:'Mammals', fr:'Mammifères'},
      {id:'plants', en:'Plants', fr:'Plantes'},
      {id:'invertebrates', en:'Insects and invertebrates', fr:'Insectes et invertébrés'},
      {id:'humans', en:'Early humans', fr:'Premiers humains'}
    ];
    var picked={all:true};
    chipDefs.forEach(function(def){
      var b=document.createElement('button');
      b.type='button';
      b.className='dt-chip';
      b.dataset.cat=def.id;
      b.textContent=lang==='fr'?def.fr:def.en;
      b.setAttribute('aria-pressed', def.id==='all'?'true':'false');
      b.addEventListener('click', function(){ toggleCat(def.id); });
      filters.appendChild(b);
    });
    var axis=document.createElement('p');
    axis.className='dt-axis';
    axis.textContent=lang==='fr'?'Le plus ancien à gauche, aujourd’hui à droite.':'Oldest on the left, today on the right.';
    scale.appendChild(eras);
    scale.appendChild(periods);
    scale.appendChild(marker);
    var panel=document.createElement('div');
    panel.className='dt-panel';
    var lived=document.createElement('section');
    lived.className='dt-box';
    var died=document.createElement('section');
    died.className='dt-box'+(fullPage?' dt-died':'');
    if(!fullPage){
      panel.appendChild(lived);
      panel.appendChild(died);
    }
    var coast=document.createElement('p');
    coast.className='dt-coast';
    var gplates='https://gws.gplates.org/reconstruct/reconstruct_points/';
    coast.innerHTML=(lang==='fr'
      ? 'Côtes : cadres PALEOMAP de Scotese, ceux du Dig Quest, 640 × 320 pixels, non agrandis. '
      : 'Coastlines: Scotese PALEOMAP frames from the Dig Quest globe, 640 × 320 pixels, not enlarged. ')
      + '<a href="'+gplates+'" rel="noopener noreferrer">'+(lang==='fr'?'Service GPlates, modèle PALEOMAP':'GPlates Web Service, model PALEOMAP')+'</a>';
    var cast=document.createElement('div');
    cast.className='dt-cast';
    cast.setAttribute('role','list');
    var learn=document.createElement('aside');
    learn.className='dt-learn';
    learn.hidden=true;
    if(fullPage){
      controls.insertBefore(readout, controls.firstChild);
      controls.insertBefore(speedLabel, controls.firstChild);
      controls.insertBefore(play, controls.firstChild);
      root.appendChild(controls);
    }else{
      root.appendChild(stage);
      root.appendChild(coast);
    }
    root.appendChild(scale);
    root.appendChild(cast);
    root.appendChild(learn);
    root.appendChild(filters);
    if(!fullPage) root.appendChild(controls);
    root.appendChild(axis);
    root.appendChild(key);
    if(fullPage) root.appendChild(lived);
    else {
      root.appendChild(panel);
      root.appendChild(legend);
      root.appendChild(method);
    }
    if(!fullPage){
      var colorNote=document.createElement('p');
      colorNote.className='dt-method';
      colorNote.textContent=lang==='fr'
        ? 'Le bandeau utilise trois tons d’eau cristalline, un par ère. Les âges viennent de l’échelle de la Paleobiology Database.'
        : 'The bar uses three crystal-water tones, one for each era. Ages come from the Paleobiology Database timescale.';
      root.appendChild(colorNote);
    }
    var sourceList=document.createElement('section');
    sourceList.className='dt-sources';
    root.appendChild(sourceList);
    function pushSrc(bucket, href, label){
      if(!href||!/^https:\/\//i.test(href))return;
      if(bucket.some(function(x){return x.href===href}))return;
      bucket.push({href:href, label:label||href});
    }
    function fillSources(){
      var bucket=[];
      (pack.life||[]).forEach(function(x){
        pushSrc(bucket, x.sourceHref, lang==='fr'?(x.sourceFr||x.source):x.source);
        pushSrc(bucket, x.sourceHref2, lang==='fr'?(x.source2Fr||x.source2):x.source2);
        pushSrc(bucket, x.imageHref, (lang==='fr'?'Image, ':'Image, ')+(lang==='fr'?x.nameFr:x.name));
      });
      (pack.extinctions||[]).forEach(function(x){
        pushSrc(bucket, x.sourceHref, lang==='fr'?(x.sourceFr||x.source):x.source);
        pushSrc(bucket, x.sourceHref2, lang==='fr'?(x.source2Fr||x.source2):x.source2);
      });
      (pack.species||[]).forEach(function(s){
        pushSrc(bucket, s.sourceHref, lang==='fr'?(s.sourceFr||s.source):s.source);
        pushSrc(bucket, s.sourceHref2, s.sourceHref2);
        (s.sites||[]).forEach(function(site){
          pushSrc(bucket, site.sourceHref, lang==='fr'?(site.sourceFr||site.source):site.source);
          pushSrc(bucket, site.paleoHref, lang==='fr'?(site.paleoSourceFr||site.paleoSource):site.paleoSource);
        });
      });
      (pack.bands||[]).concat(pack.eras||[]).forEach(function(row){
        pushSrc(bucket, row.sourceHref, lang==='fr'?(row.sourceFr||row.source):row.source);
        pushSrc(bucket, row.colorHref, lang==='fr'?'Couleurs CGMW 2022':'CGMW 2022 colors');
      });
      var h=lang==='fr'?('Sources ('+bucket.length+')'):('Sources ('+bucket.length+')');
      var html='<details><summary>'+esc(h)+'</summary><ul>';
      bucket.forEach(function(x){
        html+='<li><a href="'+esc(x.href)+'" rel="noopener noreferrer">'+esc(x.label)+'</a></li>';
      });
      html+='</ul></details>';
      sourceList.innerHTML=html;
    }
    fillSources();
    var age=+slider.value;
    var playing=false;
    var last=null;
    var cache={};
    function load(name, cb){
      if(cache[name]){cb(cache[name]);return}
      var img=new Image();
      img.onload=function(){cache[name]=img;cb(img)};
      img.onerror=function(){cb(null)};
      img.src=tex+name;
    }
    function showFrame(){
      var a,b,t;
      if(reduce){
        a=frame(age); b=a; t=0;
      }else{
        var p=pair(age);
        a=frame(p.lo); b=frame(p.hi); t=p.t;
      }
      load(a, function(){ if(imgA.getAttribute('src')!==tex+a)imgA.src=tex+a; });
      load(b, function(){ if(imgB.getAttribute('src')!==tex+b)imgB.src=tex+b; });
      imgA.style.opacity='1';
      imgB.style.opacity=String(t);
    }
    var pinNodes={};
    var castKey='';
    var learnPick=null;
    function diedNear(ma){
      var best=null, dist=1e9;
      (pack.extinctions||[]).forEach(function(x){
        if(!allowed(x.groups))return;
        var d=Math.abs(x.ma-ma);
        if(d<=12 && d<dist){dist=d;best=x}
      });
      return best;
    }
    function showLearn(item){
      learnPick=item;
      var livedK=lang==='fr'?'Qui vivait':'What lived';
      var diedK=lang==='fr'?'Qui a disparu':'What died out';
      var none=lang==='fr'?'Pas d’extinction de masse marquée à cet arrêt.':'No mass extinction is marked at this stop.';
      var dead=diedNear(item.ma);
      var diedTxt=dead?(lang==='fr'?dead.nameFr:dead.name)+' — '+(lang==='fr'?dead.causeFr:dead.cause):none;
      learn.hidden=false;
      learn.innerHTML='<p class="dt-learn-k">'+esc(livedK)+'</p><p><strong>'+esc(item.name)+'</strong> '+esc(item.text)+'</p>'+(fullPage?'':'<p class="dt-learn-k">'+esc(diedK)+'</p><p>'+esc(diedTxt)+'</p>');
    }
    function drawPins(){
      var prefix=root.getAttribute('data-prefix')||'';
      var keep={};
      species.forEach(function(s){
        var on=age<=s.older && age>=s.younger && allowed(s.groups);
        if(!on)return;
        s.sites.forEach(function(site, idx){
          var key=s.id+'|'+idx;
          keep[key]=1;
          var c=at(site.path, age);
          var x=(c[0]+180)/360*100;
          var y=(90-c[1])/180*100;
          var name=lang==='fr'?site.fr:site.en;
          var btn=pinNodes[key];
          if(!btn){
            btn=document.createElement('button');
            btn.type='button';
            btn.className='dt-pin dt-reveal';
            btn.innerHTML=gem()+'<img src="'+esc(prefix+s.icon)+'" alt="'+esc(s.id)+'" width="32" height="36">';
            btn.addEventListener('click', function(){
              stop();
              showLearn({
                ma:(s.older+s.younger)/2,
                name:s.id,
                text:lang==='fr'
                  ? (s.id+' est sur la carte pendant l’intervalle cité, et suit sa plaque.')
                  : (s.id+' is on the map through its cited span, riding its plate.')
              });
            });
            pinLayer.appendChild(btn);
            pinNodes[key]=btn;
          }
          btn.style.left=x.toFixed(2)+'%';
          btn.style.top=y.toFixed(2)+'%';
          btn.title=name;
        });
      });
      Object.keys(pinNodes).forEach(function(k){
        if(!keep[k]){ pinNodes[k].remove(); delete pinNodes[k]; }
      });
    }
    function drawCast(){
      var band=inPeriod(age);
      var pool=(pack.life||[]).filter(function(x){return band && x.ma<=band.older && x.ma>=band.younger && allowed(x.groups)});
      pool.sort(function(a,b){return a.ma-b.ma});
      var shown=pool.slice(0,8);
      var key=shown.map(function(x){return x.name}).join('|')+'|'+(learnPick?learnPick.name:'');
      if(key===castKey)return;
      castKey=key;
      cast.innerHTML='';
      shown.forEach(function(x){
        var name=lang==='fr'?x.nameFr:x.name;
        var b=document.createElement('button');
        b.type='button';
        b.className='dt-cast-btn dt-reveal'+(learnPick&&learnPick.name===name?' is-on':'');
        b.innerHTML=gem()+'<span>'+esc(name)+'</span>';
        b.setAttribute('aria-label', name);
        b.addEventListener('click', function(){
          stop();
          age=x.ma;
          showLearn({ma:x.ma, name:name, text:lang==='fr'?x.blurbFr:x.blurb});
          castKey='';
          apply();
        });
        cast.appendChild(b);
      });
    }
    function apply(){
      if(age<0)age=0;
      var cap=pack.fromMa||539;
      if(age>cap)age=cap;
      slider.value=String(Math.round(age));
      var p=period(pack.periods, age);
      var label=p?(lang==='fr'?p.fr:p.en):'';
      var when=age<0.5?(lang==='fr'?'Aujourd’hui':'Today'):(lang==='fr'?('Il y a '+Math.round(age)+' millions d’années'):(Math.round(age)+' million years ago'));
      readout.textContent=label?when+' · '+label:when;
      slider.setAttribute('aria-valuetext', readout.textContent);
      if(!fullPage) stage.setAttribute('aria-label', readout.textContent);
      var width=pack.fromMa||539;
      marker.style.left=((width-age)/width*100)+'%';
      [].forEach.call(eras.children, function(el){
        var on=age<=+el.dataset.older && age>=+el.dataset.younger;
        el.classList.toggle('is-on', on);
      });
      var bandNow=inPeriod(age);
      [].forEach.call(periods.children, function(el){
        var on=!!(bandNow&&el.dataset.en===bandNow.en);
        el.classList.toggle('is-on', on);
        el.setAttribute('aria-current', on?'true':'false');
      });
      [].forEach.call(key.children, function(el){
        var on=!!(bandNow&&el.dataset.en===bandNow.en);
        el.classList.toggle('is-on', on);
        el.setAttribute('aria-current', on?'true':'false');
      });
      [].forEach.call(legend.children, function(el){
        var sp=species.filter(function(s){return s.id===el.dataset.id})[0];
        el.hidden=!(sp&&allowed(sp.groups));
      });
      fillPanel();
      if(!fullPage){
        showFrame();
        drawPins();
      }
      drawCast();
    }
    function inPeriod(ma){
      var stage=period(pack.periods, ma);
      var probe=ma;
      if(stage && stage.older>stage.younger) probe=(stage.older+stage.younger)/2;
      var best=null, span=1e9;
      (pack.bands||[]).forEach(function(b){
        if(probe<=b.older && probe>=b.younger && (b.older-b.younger)<span){span=b.older-b.younger;best=b}
      });
      if(best) return best;
      (pack.bands||[]).forEach(function(b){
        if(ma<=b.older && ma>=b.younger && (b.older-b.younger)<span){span=b.older-b.younger;best=b}
      });
      return best;
    }
    var panelKey='';
    function homeBand(x){
      var best=null, score=1e9;
      (pack.bands||[]).forEach(function(b){
        var inside=x.ma<=b.older+0.05 && x.ma>=b.younger-0.05;
        var justAfter=x.ma<b.younger && (b.younger-x.ma)<=0.25;
        if(!inside && !justAfter)return;
        var d=Math.abs(x.ma-b.younger);
        if(d<score){score=d;best=b}
      });
      return best;
    }
    function agoLine(ma){
      var n=Math.round(ma*10)/10;
      var s=(Math.abs(n-Math.round(n))<0.05)?String(Math.round(n)):String(Math.round(n*10)/10);
      if(lang==='fr')return 'Il y a environ '+s.replace('.',',')+' millions d’années.';
      return 'About '+s+' million years ago.';
    }
    function fillPanel(){
      var prefix=root.getAttribute('data-prefix')||'';
      var band=inPeriod(age);
      var headL=lang==='fr'?'Qui vivait':'What lived';
      var headD=lang==='fr'?'Qui a disparu':'What died out';
      var noneL=fullPage
        ?(picked.all?(lang==='fr'?'Pas d’exemple sourcé pour cette période.':'No sourced example for this period.'):(lang==='fr'?'Pas d’exemple sourcé pour cette période dans les catégories choisies.':'No sourced example for this period in the selected categories.'))
        :(picked.all?(lang==='fr'?'Pas d’exemple sourcé sur cette carte pour cette période.':'No sourced example on this map for this period.'):(lang==='fr'?'Pas d’exemple sourcé sur cette carte pour cette période dans les catégories choisies.':'No sourced example on this map for this period in the selected categories.'));
      var noneD=picked.all?(lang==='fr'?'Pas d’extinction de masse notée ici dans cette période.':'No mass extinction is listed here in this period.'):(lang==='fr'?'Pas d’extinction de masse notée ici pour ces catégories dans cette période.':'No mass extinction is listed here for these categories in this period.');
      var pool=(pack.life||[]).filter(function(x){return band && x.ma<=band.older && x.ma>=band.younger && allowed(x.groups)});
      pool.sort(function(a,b){
        if(a.ma!==b.ma)return b.ma-a.ma;
        return String(a.name).localeCompare(String(b.name));
      });
      var shown=pool.slice(0,5);
      var dead=(pack.extinctions||[]).filter(function(x){
        if(!allowed(x.groups))return false;
        var home=homeBand(x);
        return !!(band && home && home.en===band.en);
      });
      var cats=Object.keys(picked).filter(function(k){return picked[k]}).sort().join(',');
      var key=(band?band.en:'')+'|'+cats+'|'+shown.map(function(x){return x.name}).join(',')+'|'+dead.map(function(x){return x.name}).join(',');
      if(key===panelKey)return;
      panelKey=key;
      var html='<h3>'+esc(headL)+'</h3>';
      if(!shown.length) html+='<p>'+esc(noneL)+'</p>';
      else {
        var note='';
        if(pool.length>5) note=lang==='fr'?'Cinq exemples de cette période.':'Five examples from this period.';
        else if(pool.length<3) note=fullPage
          ?(lang==='fr'?('Cette période n’a que '+pool.length+' exemple'+(pool.length>1?'s':'')+' sourcé'+(pool.length>1?'s':'')+'.'):('This period has only '+pool.length+' sourced example'+(pool.length>1?'s':'')+'.'))
          :(lang==='fr'?('Cette carte n’a que '+pool.length+' exemple'+(pool.length>1?'s':'')+' sourcé'+(pool.length>1?'s':'')+' pour cette période.'):('This map has only '+pool.length+' sourced example'+(pool.length>1?'s':'')+' for this period.'));
        if(note) html+='<p class="dt-note">'+esc(note)+'</p>';
        html+='<ul class="dt-life">';
        shown.forEach(function(x){
          var name=lang==='fr'?x.nameFr:x.name;
          var blurb=lang==='fr'?x.blurbFr:x.blurb;
          var cite=lang==='fr'?(x.sourceFr||x.source):(x.source||'');
          var ext=/^https?:/i.test(x.sourceHref)?' rel="noopener noreferrer"':'';
          var lifeExt=/^https?:/i.test(x.href)?' rel="noopener noreferrer"':'';
          html+='<li><a class="dt-life-link" href="'+esc(x.href)+'"'+lifeExt+'>'+lifePicture(x, prefix)+'<span><strong>'+esc(name)+'</strong> '+esc(blurb)+'</span></a>';
          if(!fullPage){
            if(cite&&x.sourceHref) html+='<p class="dt-src"><a href="'+esc(x.sourceHref)+'"'+ext+'>'+esc(cite)+'</a></p>';
            if(x.sourceHref2) html+='<p class="dt-src"><a href="'+esc(x.sourceHref2)+'" rel="noopener noreferrer">'+esc(lang==='fr'?(x.source2Fr||x.source2||x.sourceHref2):(x.source2||x.sourceHref2))+'</a></p>';
            if(!x.lifeImg && x.imageHref){
              var cap=lang==='fr'?(x.imageCreditFr||x.imageCredit||''):(x.imageCredit||'');
              html+='<p class="dt-src">'+esc(cap)+' <a href="'+esc(x.imageHref)+'" rel="noopener noreferrer">'+(lang==='fr'?'Page du fichier':'File page')+'</a></p>';
            }
          }
          if(x.lifeImg&&x.lifeHref){
            var lifeCap=lang==='fr'?(x.lifeCreditFr||x.lifeCredit||''):(x.lifeCredit||'');
            var lifeWord=lang==='fr'?'Reconstitution':'Life restoration';
            var fossilWord=lang==='fr'?'Fossile':'Fossil';
            html+='<p class="dt-src">'+esc(lifeWord)+'. '+esc(lifeCap)+' <a href="'+esc(x.lifeHref)+'" rel="noopener noreferrer">'+(lang==='fr'?'Page du fichier':'File page')+'</a></p>';
            if(x.imageHref){
              var fossilCap=lang==='fr'?(x.imageCreditFr||x.imageCredit||''):(x.imageCredit||'');
              html+='<p class="dt-src">'+esc(fossilWord)+'. '+esc(fossilCap)+' <a href="'+esc(x.imageHref)+'" rel="noopener noreferrer">'+(lang==='fr'?'Page du fichier':'File page')+'</a></p>';
            }
          }
          html+='</li>';
        });
        html+='</ul>';
      }
      lived.innerHTML=html;
      if(fullPage) return;
      html='<h3>'+esc(headD)+'</h3>';
      if(!dead.length) html+='<p>'+esc(noneD)+'</p>';
      else dead.forEach(function(x){
        var name=lang==='fr'?x.nameFr:x.name;
        var cause=lang==='fr'?x.causeFr:x.cause;
        var src=lang==='fr'?x.sourceFr:x.source;
        var hot=Math.abs(x.ma-age)<=8;
        var ext=/^https?:/i.test(x.sourceHref)?' rel="noopener noreferrer"':'';
        var openWord=/^https?:/i.test(x.href)?(lang==='fr'?'Ouvrir la source':'Open the source'):(lang==='fr'?'Ouvrir la pièce':'Open the coin');
        var more=x.sourceHref2?' · <a href="'+esc(x.sourceHref2)+'" rel="noopener noreferrer">'+esc(lang==='fr'?(x.source2Fr||x.source2):(x.source2||''))+'</a>':'';
        html+='<article class="dt-ext'+(x.bigFive?' is-big':'')+(hot?' is-hot':'')+'"><p><strong>'+esc(name)+'</strong>'+(x.bigFive?(lang==='fr'?' · une des cinq grandes':' · one of the Big Five'):'')+'</p><p>'+esc(agoLine(x.ma))+'</p><p>'+esc(cause)+'</p>'+(fullPage?'':'<p><a href="'+esc(x.href)+'"'+(/^https?:/i.test(x.href)?' rel="noopener noreferrer"':'')+'>'+openWord+'</a> · <a href="'+esc(x.sourceHref)+'"'+ext+'>'+esc(src)+'</a>'+more+'</p>')+'</article>';
      });
      died.innerHTML=html;
    }
    function lifePicture(x, prefix){
      function path(p){return p?(/^https?:/i.test(p)?p:(prefix+p)):'';}
      function shot(webp, avif, w, h){
        var html='<picture>';
        if(avif) html+='<source type="image/avif" src="'+esc(avif)+'">';
        html+='<img src="'+esc(webp)+'" alt="" width="'+(w||128)+'" height="'+(h||128)+'" loading="lazy" decoding="async"></picture>';
        return html;
      }
      var fossil=shot(path(x.imgSm||x.img), path(x.imgAvifSm||x.imgAvif), x.picSmW||x.picW, x.picH);
      if(!x.lifeImg) return fossil;
      var life=shot(path(x.lifeImgSm||x.lifeImg), "", x.lifeSmW||x.lifeW, x.lifeSmH||x.lifeH);
      return '<span class="dt-life-pics">'+life+fossil+'</span>';
    }
    function allowed(groups){
      if(picked.all)return true;
      var want=Object.keys(picked).filter(function(k){return picked[k]&&k!=='all'});
      if(!want.length)return true;
      groups=groups||[];
      for(var i=0;i<want.length;i++) if(groups.indexOf(want[i])!==-1) return true;
      return false;
    }
    function paintChips(){
      [].forEach.call(filters.children, function(b){
        var on=!!picked[b.dataset.cat];
        b.classList.toggle('is-on', on);
        b.setAttribute('aria-pressed', on?'true':'false');
      });
    }
    function toggleCat(id){
      if(id==='all'){
        picked={all:true};
      }else{
        picked.all=false;
        picked[id]=!picked[id];
        var any=chipDefs.some(function(def){return def.id!=='all'&&picked[def.id]});
        if(!any)picked={all:true};
      }
      paintChips();
      panelKey='';
      apply();
    }
    paintChips();
    function clearLearn(){
      learnPick=null;
      learn.hidden=true;
      castKey='';
    }
    function go(ma){
      stop();
      clearLearn();
      age=ma;
      apply();
    }
    function stop(){
      playing=false;
      play.setAttribute('aria-pressed','false');
      play.textContent=playWord;
      last=null;
    }
    function tick(now){
      if(!playing)return;
      var box=root.closest('#sm-then');
      if(box && box.hidden){stop();return}
      if(last!=null){
        var dt=Math.min(0.05,(now-last)/1000);
        age-=dt*maPerSec;
        if(age<=0){age=0;stop();apply();return}
        apply();
      }
      last=now;
      requestAnimationFrame(tick);
    }
    speed.addEventListener('change', function(){
      var n=+speed.value;
      if(n>0)maPerSec=n;
    });
    play.addEventListener('click', function(){
      if(reduce)return;
      if(playing){stop();return}
      clearLearn();
      if(age<0.5)age=pack.fromMa||539;
      playing=true;
      play.setAttribute('aria-pressed','true');
      play.textContent=pauseWord;
      last=null;
      requestAnimationFrame(tick);
    });
    slider.addEventListener('input', function(){
      stop();
      clearLearn();
      age=+slider.value;
      apply();
    });
    apply();
    if(!reduce && root.getAttribute('data-all')==='1'){
      playing=true;
      play.setAttribute('aria-pressed','true');
      play.textContent=pauseWord;
      last=null;
      requestAnimationFrame(tick);
    }
  }
  function start(){
    var nodes=[].slice.call(document.querySelectorAll('.dt'));
    if(!nodes.length)return;
    var url=nodes[0].getAttribute('data-json');
    fetch(url).then(function(r){return r.json()}).then(function(pack){
      nodes.forEach(function(n){boot(n, pack)});
    }).catch(function(){});
  }
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded', start);
  else start();
})();
