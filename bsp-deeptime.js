/* Deep-time map. Coastlines are the Dig Quest PALEOMAP frames.
   Icons follow PALEOMAP paths from the GPlates Web Service, baked in deep-time.json. */
(function(){
  var reduce=window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  function esc(s){return String(s==null?'':s).replace(/[&<>"']/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]})}
  function pad(n){n=Math.round(n);return (n<10?'00':n<100?'0':'')+n}
  function frame(ma){
    var q=Math.round(ma/20)*20;
    if(q<0)q=0;
    if(q>260)q=260;
    return 'm'+pad(q)+'.webp';
  }
  function pair(ma){
    var lo=Math.floor(ma/20)*20;
    var hi=lo+20;
    if(lo<0)lo=0;
    if(hi>260)hi=260;
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
    slider.min='0'; slider.max='250'; slider.step='1';
    var start=250;
    var sp0=focus?species[0]:jump;
    if(sp0)start=Math.round((sp0.older+sp0.younger)/2);
    slider.value=String(start);
    slider.setAttribute('aria-label', lang==='fr'?'Millions d’années avant aujourd’hui':'Millions of years ago');
    controls.appendChild(play);
    controls.appendChild(slider);
    var readout=document.createElement('p');
    readout.className='dt-readout';
    readout.setAttribute('aria-live','polite');
    var legend=document.createElement('ul');
    legend.className='dt-legend';
    species.forEach(function(s){
      var li=document.createElement('li');
      var prefix=root.getAttribute('data-prefix')||'';
      var span=lang==='fr'?s.spanFr:s.span;
      li.innerHTML='<img src="'+esc(prefix+s.icon)+'" alt="" width="28" height="32"><span><strong>'+esc(s.id)+'</strong> '+esc(span)+'</span>';
      legend.appendChild(li);
    });
    var method=document.createElement('p');
    method.className='dt-method';
    method.textContent=lang==='fr'?pack.methodFr:pack.method;
    root.appendChild(stage);
    root.appendChild(controls);
    root.appendChild(readout);
    root.appendChild(legend);
    root.appendChild(method);
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
        var on=age<=s.older && age>=s.younger;
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
      if(age>250)age=250;
      slider.value=String(Math.round(age));
      var p=period(pack.periods, age);
      var label=p?(lang==='fr'?p.fr:p.en):'';
      var when=age<0.5?(lang==='fr'?'Aujourd’hui':'Today'):(lang==='fr'?('Il y a '+Math.round(age)+' millions d’années'):(Math.round(age)+' million years ago'));
      readout.textContent=label?when+' · '+label:when;
      slider.setAttribute('aria-valuetext', readout.textContent);
      stage.setAttribute('aria-label', readout.textContent);
      showFrame();
      drawPins();
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
        age-=dt*10;
        if(age<=0){age=0;stop();apply();return}
        apply();
      }
      last=now;
      requestAnimationFrame(tick);
    }
    play.addEventListener('click', function(){
      if(reduce)return;
      if(playing){stop();return}
      if(age<0.5)age=250;
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
