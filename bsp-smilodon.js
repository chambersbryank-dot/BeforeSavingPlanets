(function(){
  var el=document.getElementById('sm-map');
  if(!el||!window.L)return;
  var sites=JSON.parse(document.getElementById('sm-sites').textContent);
  var map=L.map(el,{scrollWheelZoom:false,worldCopyJump:true}).setView([8,-70],2);
  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',{maxZoom:12,attribution:'&copy; OpenStreetMap contributors'}).addTo(map);
  var icon=L.divIcon({
    className:'sm-pin',
    html:'<img src="'+el.getAttribute('data-icon')+'" alt="" width="42" height="48">',
    iconSize:[42,48],
    iconAnchor:[21,44],
    popupAnchor:[0,-36]
  });
  function esc(s){return String(s==null?'':s).replace(/[&<>"']/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]})}
  sites.forEach(function(s){
    var html='<strong>'+esc(s.name)+'</strong><p>'+esc(s.species)+'</p><p>'+esc(s.note)+'</p><p><a href="'+esc(s.href)+'" rel="noopener noreferrer">'+esc(s.source)+'</a></p>';
    L.marker([s.lat,s.lng],{icon:icon,title:s.name}).addTo(map).bindPopup(html,{maxWidth:280});
  });
})();
