/* Deep-time map. Coastlines are the Dig Quest PALEOMAP frames.
   Icons follow PALEOMAP paths from the GPlates Web Service, baked in deep-time.json. */
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
    var readrow=document.createElement('div');
    readrow.className='dt-readrow';
    readrow.appendChild(play);
    readrow.appendChild(readout);
    var legend=document.createElement('ul');
    legend.className='dt-legend';
    species.forEach(function(s){
      var li=document.createElement('li');
      li.dataset.id=s.id;
      var prefix=root.getAttribute('data-prefix')||'';
      var span=lang==='fr'?s.spanFr:s.span;
      li.innerHTML='<img src="'+esc(prefix+s.icon)+'" alt="" width="28" height="32"><span><strong>'+esc(s.id)+'</strong> '+esc(span)+'</span>';
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
      d.textContent=lang==='fr'?e.fr:e.en;
      d.title=lang==='fr'?e.fr:e.en;
      eras.appendChild(d);
    });
    var key=document.createElement('div');
    key.className='dt-key';
    var keyLabel=lang==='fr'?'Périodes, de la plus ancienne à aujourd’hui':'Periods, oldest to today';
    key.setAttribute('aria-label', keyLabel);
    (pack.bands||[]).forEach(function(b){
      var name=lang==='fr'?b.fr:b.en;
      var d=document.createElement('button');
      d.type='button';
      d.className='dt-per';
      d.style.flex=String(b.older-b.younger);
      d.style.background=b.color;
      d.style.color=b.ink;
      d.dataset.en=b.en;
      d.innerHTML='<span class="dt-name">'+esc(name)+'</span><span class="dt-abbr">'+esc(b.short||name)+'</span>';
      d.title=name;
      d.setAttribute('aria-label', (lang==='fr'?'Aller au milieu du ':'Go to the middle of the ')+name);
      d.addEventListener('click', function(){ go((b.older+b.younger)/2); });
      periods.appendChild(d);
      var chip=document.createElement('button');
      chip.type='button';
      chip.dataset.en=b.en;
      chip.innerHTML='<i class="dt-swatch" style="background:'+esc(b.color)+'"></i><span>'+esc(name)+'</span>';
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
    died.className='dt-box';
    panel.appendChild(lived);
    panel.appendChild(died);
    root.appendChild(stage);
    root.appendChild(scale);
    root.appendChild(filters);
    root.appendChild(controls);
    root.appendChild(axis);
    root.appendChild(key);
    root.appendChild(readrow);
    root.appendChild(panel);
    root.appendChild(legend);
    root.appendChild(method);
    var colorNote=document.createElement('p');
    colorNote.className='dt-method';
    colorNote.textContent=pack.colorSource||'';
    root.appendChild(colorNote);
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
    function drawPins(){
      var prefix=root.getAttribute('data-prefix')||'';
      var html='';
      species.forEach(function(s){
        var on=age<=s.older && age>=s.younger && allowed(s.groups);
        s.sites.forEach(function(site){
          if(!on)return;
          var c=at(site.path, age);
          var x=(c[0]+180)/360*100;
          var y=(90-c[1])/180*100;
          var name=lang==='fr'?site.fr:site.en;
          html+='<span class="dt-pin" style="left:'+x.toFixed(2)+'%;top:'+y.toFixed(2)+'%" title="'+esc(name)+'"><img src="'+esc(prefix+s.icon)+'" alt="'+esc(s.id)+'" width="32" height="36"></span>';
        });
      });
      pinLayer.innerHTML=html;
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
      stage.setAttribute('aria-label', readout.textContent);
      var width=pack.fromMa||539;
      marker.style.left=((width-age)/width*100)+'%';
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
      showFrame();
      drawPins();
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
      var noneL=picked.all?(lang==='fr'?'Pas d’exemple sourcé sur cette carte pour cette période.':'No sourced example on this map for this period.'):(lang==='fr'?'Pas d’exemple sourcé sur cette carte pour cette période dans les catégories choisies.':'No sourced example on this map for this period in the selected categories.');
      var noneD=picked.all?(lang==='fr'?'Pas d’extinction de masse notée ici dans cette période.':'No mass extinction is listed here in this period.'):(lang==='fr'?'Pas d’extinction de masse notée ici pour ces catégories dans cette période.':'No mass extinction is listed here for these categories in this period.');
      var pool=(pack.life||[]).filter(function(x){return band && x.ma<=band.older && x.ma>=band.younger && allowed(x.groups)});
      pool.sort(function(a,b){
        var d=Math.abs(a.ma-age)-Math.abs(b.ma-age);
        if(d)return d;
        return String(a.name).localeCompare(String(b.name));
      });
      var shown=pool.slice(0,5);
      var dead=(pack.extinctions||[]).filter(function(x){
        if(!allowed(x.groups))return false;
        var home=homeBand(x);
        var inHome=!!(band && home && home.en===band.en);
        var near=Math.abs(x.ma-age)<=8;
        return inHome||near;
      });
      var cats=Object.keys(picked).filter(function(k){return picked[k]}).sort().join(',');
      var key=(band?band.en:'')+'|'+cats+'|'+shown.map(function(x){return x.name}).join(',')+'|'+dead.map(function(x){
        return x.name+':'+(Math.abs(x.ma-age)<=8?'1':'0');
      }).join(',');
      if(key===panelKey)return;
      panelKey=key;
      var html='<h3>'+esc(headL)+'</h3>';
      if(!shown.length) html+='<p>'+esc(noneL)+'</p>';
      else {
        var note='';
        if(pool.length>5) note=lang==='fr'?'Les cinq exemples les plus proches du curseur.':'The five examples closest to the slider.';
        else if(pool.length<3) note=lang==='fr'?('Cette carte n’a que '+pool.length+' exemple'+(pool.length>1?'s':'')+' sourcé'+(pool.length>1?'s':'')+' pour cette période.'):('This map has only '+pool.length+' sourced example'+(pool.length>1?'s':'')+' for this period.');
        if(note) html+='<p class="dt-note">'+esc(note)+'</p>';
        html+='<ul class="dt-life">';
        shown.forEach(function(x){
          var src=/^https?:/i.test(x.img)?x.img:(prefix+x.img);
          var name=lang==='fr'?x.nameFr:x.name;
          var blurb=lang==='fr'?x.blurbFr:x.blurb;
          var cite=lang==='fr'?(x.sourceFr||x.source):(x.source||'');
          var ext=/^https?:/i.test(x.sourceHref)?' rel="noopener noreferrer"':'';
          var lifeExt=/^https?:/i.test(x.href)?' rel="noopener noreferrer"':'';
          html+='<li><a class="dt-life-link" href="'+esc(x.href)+'"'+lifeExt+'><img src="'+esc(src)+'" alt="" width="84" height="84" decoding="async"><span><strong>'+esc(name)+'</strong> '+esc(blurb)+'</span></a>';
          if(cite&&x.sourceHref) html+='<p class="dt-src"><a href="'+esc(x.sourceHref)+'"'+ext+'>'+esc(cite)+'</a></p>';
          html+='</li>';
        });
        html+='</ul>';
      }
      lived.innerHTML=html;
      html='<h3>'+esc(headD)+'</h3>';
      if(!dead.length) html+='<p>'+esc(noneD)+'</p>';
      else dead.forEach(function(x){
        var name=lang==='fr'?x.nameFr:x.name;
        var cause=lang==='fr'?x.causeFr:x.cause;
        var src=lang==='fr'?x.sourceFr:x.source;
        var hot=Math.abs(x.ma-age)<=8;
        var ext=/^https?:/i.test(x.sourceHref)?' rel="noopener noreferrer"':'';
        html+='<article class="dt-ext'+(x.bigFive?' is-big':'')+(hot?' is-hot':'')+'"><p><strong>'+esc(name)+'</strong>'+(x.bigFive?(lang==='fr'?' · une des cinq grandes':' · one of the Big Five'):'')+'</p><p>'+esc(agoLine(x.ma))+'</p><p>'+esc(cause)+'</p><p><a href="'+esc(x.href)+'">'+(lang==='fr'?'Ouvrir la pièce':'Open the coin')+'</a> · <a href="'+esc(x.sourceHref)+'"'+ext+'>'+esc(src)+'</a></p></article>';
      });
      died.innerHTML=html;
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
    function go(ma){
      stop();
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
        age-=dt*18;
        if(age<=0){age=0;stop();apply();return}
        apply();
      }
      last=now;
      requestAnimationFrame(tick);
    }
    play.addEventListener('click', function(){
      if(reduce)return;
      if(playing){stop();return}
      if(age<0.5)age=pack.fromMa||539;
      playing=true;
      play.setAttribute('aria-pressed','true');
      play.textContent=pauseWord;
      last=null;
      requestAnimationFrame(tick);
    });
    slider.addEventListener('input', function(){
      stop();
      age=+slider.value;
      apply();
    });
    apply();
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
