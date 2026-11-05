(function(){
  var needle=document.getElementById("dq-needle");
  var now=document.getElementById("dq-now");
  var eras=Array.prototype.slice.call(document.querySelectorAll("[data-era]"));
  if(!needle||!eras.length) return;
  var links=Array.prototype.slice.call(document.querySelectorAll(".dq-legend a"));
  function place(){
    var y=window.scrollY+Math.min(window.innerHeight*0.34, 240);
    var active=eras[0];
    for(var i=0;i<eras.length;i++){
      if(eras[i].offsetTop<=y) active=eras[i];
    }
    var top=active.offsetTop;
    var h=active.offsetHeight||1;
    var p=(y-top)/h;
    if(p<0) p=0;
    if(p>1) p=1;
    var start=+active.getAttribute("data-start");
    var end=+active.getAttribute("data-end");
    var pos=start+(end-start)*p;
    needle.style.insetInlineStart=(pos*100)+"%";
    var id=active.id;
    links.forEach(function(a){
      if(a.getAttribute("href")==="#"+id) a.setAttribute("aria-current","true");
      else a.removeAttribute("aria-current");
    });
    if(now) now.textContent=active.getAttribute("data-label")||"";
  }
  place();
  window.addEventListener("scroll", place, {passive:true});
  window.addEventListener("resize", place);
})();
