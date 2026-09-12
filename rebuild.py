from pathlib import Path
p=Path('/tmp/corefix/script.js')
s=p.read_text()
start=s.index('function renderModel(part){')
end=s.index('\n\nconst answers=', start)
render=r'''function renderModel(part){
 const d=document.getElementById('detailModel'); if(!d) return;
 const titles={case:'PC CASE',motherboard:'MOTHERBOARD',cpu:'CPU',gpu:'GPU',ram:'RAM',storage:'NVMe SSD',cooling:'COOLING',psu:'POWER SUPPLY',monitor:'MONITOR',keyboard:'KEYBOARD',mouse:'MOUSE'};
 const label=titles[part]||'COMPONENT';
 const drawings={
  case:`<g><rect x="170" y="45" width="180" height="310" rx="12"/><rect class="glass" x="188" y="64" width="144" height="270" rx="8"/><circle cx="260" cy="112" r="30"/><circle cx="260" cy="200" r="30"/><circle cx="260" cy="288" r="30"/><rect class="blue" x="205" y="176" width="110" height="12" rx="6"/></g>`,
  motherboard:`<g><rect class="board" x="80" y="80" width="340" height="240" rx="12"/><rect x="205" y="140" width="90" height="90" rx="5"/><rect class="blue" x="110" y="110" width="18" height="170"/><rect class="blue" x="145" y="110" width="18" height="170"/><path d="M305 115h80v55h-80zm0 75h80v90h-80z" fill="none"/><circle cx="145" cy="145" r="8"/><circle cx="145" cy="175" r="8"/><circle cx="145" cy="205" r="8"/></g>`,
  cpu:`<g><rect x="125" y="80" width="270" height="270" rx="16"/><rect class="blue" x="175" y="130" width="170" height="170" rx="10"/><path d="M150 60v40m55-40v40m55-40v40m55-40v40M150 330v40m55-40v40m55-40v40m55-40v40M105 105h40M105 160h40M105 215h40M105 270h40M375 105h40M375 160h40M375 215h40M375 270h40"/></g>`,
  gpu:`<g><rect x="55" y="125" width="410" height="145" rx="14"/><circle cx="160" cy="198" r="48"/><circle cx="260" cy="198" r="48"/><circle cx="360" cy="198" r="48"/><path class="blue-stroke" d="M85 150h350"/><rect class="purple" x="120" y="252" width="280" height="8" rx="4"/></g>`,
  ram:`<g><rect class="blue" x="145" y="45" width="60" height="330" rx="6"/><rect class="blue" x="275" y="45" width="60" height="330" rx="6"/><path d="M155 75h40m-40 38h40m-40 38h40m-40 38h40m-40 38h40m-40 38h40m-40 38h40M285 75h40m-40 38h40m-40 38h40m-40 38h40m-40 38h40m-40 38h40m-40 38h40"/><rect x="115" y="360" width="250" height="18" rx="4"/></g>`,
  storage:`<g><rect x="65" y="145" width="370" height="115" rx="12"/><rect class="blue" x="120" y="175" width="120" height="20" rx="4"/><circle cx="360" cy="202" r="12"/><path d="M100 235h300"/></g>`,
  cooling:`<g><circle cx="260" cy="205" r="135"/><circle class="blue" cx="260" cy="205" r="32"/>${Array.from({length:8},(_,i)=>{let a=i*Math.PI/4,x=260+Math.cos(a)*75,y=205+Math.sin(a)*75;return `<rect x="${x-9}" y="${y-42}" width="18" height="84" rx="9" transform="rotate(${i*45} ${x} ${y})"/>`}).join('')}</g>`,
  psu:`<g><rect x="65" y="105" width="390" height="205" rx="14"/><circle cx="190" cy="205" r="70"/><circle class="blue" cx="190" cy="205" r="12"/><rect class="blue" x="345" y="145" width="55" height="120" rx="5"/><path d="M355 160h35m-35 25h35m-35 25h35m-35 25h35"/></g>`,
  monitor:`<g><rect x="55" y="65" width="410" height="245" rx="12"/><rect class="blue" x="82" y="92" width="356" height="190" rx="5"/><rect x="238" y="310" width="34" height="70"/><path d="M165 395h180"/></g>`,
  keyboard:`<g><rect x="45" y="105" width="430" height="220" rx="18"/><g class="keys">${Array.from({length:45},(_,i)=>{let row=Math.floor(i/15),col=i%15;return `<rect x="70" y="130" width="21" height="22" rx="3" transform="translate(${col*25} ${row*45})"/>`}).join('')}</g><rect x="155" y="265" width="190" height="25" rx="6"/></g>`,
  mouse:`<g><path d="M260 55c-70 0-105 55-105 130v80c0 80 35 120 105 120s105-40 105-120v-80c0-75-35-130-105-130z"/><path class="blue-stroke" d="M260 60v110"/><rect class="blue" x="248" y="92" width="24" height="55" rx="12"/></g>`
 };
 d.innerHTML=`<svg class="component-svg" viewBox="0 0 520 420" role="img" aria-label="${label}"><defs><filter id="glow"><feGaussianBlur stdDeviation="7" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter><linearGradient id="metal" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#24313c"/><stop offset="1" stop-color="#080d12"/></linearGradient></defs><ellipse cx="260" cy="385" rx="175" ry="18" fill="#36a9ff" opacity=".08"/><g filter="url(#glow)" fill="url(#metal)" stroke="#607587" stroke-width="3" stroke-linejoin="round">${drawings[part]||drawings.case}</g><text x="260" y="410" text-anchor="middle" fill="#7890a2" font-family="monospace" font-size="10" letter-spacing="3">${label}</text></svg>`;
}

const answers={'''
# preserve answers onward but replace the old duplicate const marker through init simulator
s=s[:start]+render+s[end+2:]  # leaves const answers
# remove old simulator block starting comment after show call
marker='/* CORE v4 — interactive 3D computer simulation */'
if marker in s:
    a=s.index(marker)
    s=s[:a]
# append dependency-free simulator
sim=r'''

/* CORE v6 — dependency-free interactive computer lab. No WebGL, CDN or external libraries required. */
(function initComputerLab(){
 const root=document.getElementById('pcSimulator'); if(!root) return;
 root.innerHTML=`<canvas id="coreSimCanvas" aria-label="Interactive computer simulation"></canvas>`;
 const canvas=document.getElementById('coreSimCanvas'),ctx=canvas.getContext('2d');
 const statusEl=document.getElementById('simStatus'),selectionEl=document.getElementById('simSelection'),tooltip=document.getElementById('simTooltip');
 const powerBtn=document.getElementById('powerBtn'),powerLabel=document.getElementById('powerLabel'),loadSlider=document.getElementById('loadSlider'),loadValue=document.getElementById('loadValue');
 const cpuRead=document.getElementById('cpuRead'),gpuRead=document.getElementById('gpuRead'),ramRead=document.getElementById('ramRead'),tempRead=document.getElementById('tempRead');
 let powered=false,airflow=true,labels=true,exploded=false,load=35,rot=0,zoom=1,dragging=false,lastX=0,time=0,hover='';
 const parts=[
  {id:'Motherboard',x:0,y:0,w:270,h:210,c:'#153c2a'}, {id:'CPU',x:-35,y:-68,w:70,h:58,c:'#aab6bd'},
  {id:'Cooling',x:-35,y:-102,w:82,h:32,c:'#87949d'}, {id:'GPU',x:5,y:18,w:255,h:48,c:'#17212a'},
  {id:'RAM',x:-112,y:-68,w:25,h:100,c:'#31b7ff'}, {id:'RAM',x:-80,y:-68,w:25,h:100,c:'#31b7ff'},
  {id:'Storage',x:100,y:75,w:100,h:32,c:'#121a21'}, {id:'Power Supply',x:-115,y:83,w:230,h:65,c:'#0a0e12'}
 ];
 function resize(){const r=root.getBoundingClientRect(),dpr=Math.min(devicePixelRatio||1,2);canvas.width=Math.max(1,r.width*dpr);canvas.height=Math.max(1,r.height*dpr);canvas.style.width=r.width+'px';canvas.style.height=r.height+'px';ctx.setTransform(dpr,0,0,dpr,0,0)}
 function project(x,y,z){const c=canvas.clientWidth/2,cy=canvas.clientHeight/2+25; const a=rot,xx=x*Math.cos(a)-z*Math.sin(a),zz=x*Math.sin(a)+z*Math.cos(a); return [c+xx*zoom,cy-y*zoom+zz*.28*zoom]}
 function roundRect(x,y,w,h,r){ctx.beginPath();ctx.roundRect(x,y,w,h,r);}
 function drawBox(p,ox=0,oy=0,oz=0){const [x,y]=project(p.x+ox,p.y+oy,oz); const w=p.w*zoom,h=p.h*zoom;ctx.save();ctx.translate(x,y);ctx.fillStyle=p.c;ctx.strokeStyle='#506474';ctx.lineWidth=1.5;roundRect(-w/2,-h/2,w,h,7);ctx.fill();ctx.stroke();ctx.restore()}
 function draw(){time+=.016;const w=canvas.clientWidth,h=canvas.clientHeight;ctx.clearRect(0,0,w,h);
  const grad=ctx.createRadialGradient(w*.5,h*.45,20,w*.5,h*.45,Math.max(w,h)*.55);grad.addColorStop(0,'rgba(54,169,255,.11)');grad.addColorStop(1,'rgba(0,0,0,0)');ctx.fillStyle=grad;ctx.fillRect(0,0,w,h);
  ctx.save();ctx.translate(w/2,h*.83);ctx.scale(zoom,zoom);ctx.fillStyle='#071019';ctx.strokeStyle='#1d4b67';ctx.lineWidth=1;ctx.beginPath();ctx.ellipse(0,0,235,48,0,0,Math.PI*2);ctx.fill();ctx.stroke();ctx.restore();
  const sep=exploded?1:0; parts.forEach((p,i)=>{let ox=0,oy=0;if(sep){ox=p.id==='GPU'?45:p.id==='Power Supply'?-45:p.id==='RAM'?(-15+i*4):p.id==='Cooling'?-10:0;oy=p.id==='CPU'?-35:p.id==='Cooling'?-50:p.id==='Storage'?35:0;} drawBox(p,ox,oy,0)});
  // case outline
  const [cx,cy]=project(0,55,0);ctx.save();ctx.translate(cx,cy);ctx.rotate(rot*.25);ctx.strokeStyle='#718594';ctx.lineWidth=2;ctx.fillStyle='rgba(10,17,24,.28)';roundRect(-165,-205,330,410,14);ctx.fill();ctx.stroke();ctx.strokeStyle='rgba(54,169,255,.35)';roundRect(-148,-188,296,376,10);ctx.stroke();ctx.restore();
  // fans + lights
  for(let i=0;i<3;i++){const [fx,fy]=project(0,150-i*100,3);ctx.save();ctx.translate(fx,fy);ctx.rotate(powered?time*(1.5+load/60):0);ctx.strokeStyle=powered?'#36a9ff':'#50606c';ctx.lineWidth=5;ctx.beginPath();ctx.arc(0,0,34*zoom,0,Math.PI*2);ctx.stroke();for(let j=0;j<6;j++){ctx.rotate(Math.PI/3);ctx.beginPath();ctx.moveTo(0,0);ctx.quadraticCurveTo(20*zoom,-8*zoom,30*zoom,0);ctx.stroke()}ctx.restore()}
  if(powered){ctx.fillStyle='#36a9ff';ctx.shadowBlur=15;ctx.shadowColor='#36a9ff';ctx.beginPath();ctx.arc(w/2+150*zoom,h*.5,5,0,Math.PI*2);ctx.fill();ctx.shadowBlur=0}
  if(airflow&&powered){for(let i=0;i<18;i++){let yy=((time*(35+load*.3)+i*43)%360)-180;let [ax,ay]=project(-205,yy,5);ctx.fillStyle='rgba(78,230,255,.7)';ctx.beginPath();ctx.arc(ax,ay,2.2,0,Math.PI*2);ctx.fill()}}
  if(labels){ctx.font='10px monospace';ctx.fillStyle='#a9dfff';[['CPU',-260,-70],['GPU',250,15],['RAM',-255,-10],['SSD',245,85],['COOLING',-270,-120],['PSU',240,135]].forEach(([t,x,y])=>{const [lx,ly]=project(x,y,4);ctx.fillText(t,lx,ly)})}
  requestAnimationFrame(draw);
 }
 function update(){load=+loadSlider.value;loadValue.textContent=load+'%';cpuRead.textContent=(powered?Math.round(load*.92):0)+'%';gpuRead.textContent=(powered?Math.round(load*.82):0)+'%';ramRead.textContent=(4.2+load*.055).toFixed(1)+' GB';tempRead.textContent=(powered?Math.round(27+load*.48):27)+'°C';statusEl.textContent=powered?'SYSTEM ONLINE · SIMULATING':'SYSTEM OFFLINE';powerLabel.textContent=powered?'ONLINE':'OFFLINE';powerBtn.querySelector('span').textContent=powered?'POWER OFF':'POWER ON';powerBtn.classList.toggle('on',powered)}
 function select(name){hover=name;selectionEl.textContent=name.toUpperCase();const key=name.toLowerCase().replace(' ','');const card=document.querySelector(`[data-part="${key}"]`);if(card) card.classList.add('selected')}
 function hit(x,y){const w=canvas.clientWidth,h=canvas.clientHeight;const dx=x-w/2,dy=y-(h*.5);if(Math.abs(dx)<140&&dy>-120&&dy<20)return 'CPU';if(Math.abs(dx)<150&&dy>-20&&dy<70)return 'GPU';if(dx<-70&&dx>-160&&dy>-130&&dy<20)return 'RAM';if(dx>50&&dy>50)return 'Storage';if(dy>75)return 'Power Supply';return 'Motherboard'}
 canvas.addEventListener('pointerdown',e=>{dragging=true;lastX=e.clientX;canvas.setPointerCapture(e.pointerId)});
 canvas.addEventListener('pointerup',()=>dragging=false);canvas.addEventListener('pointercancel',()=>dragging=false);
 canvas.addEventListener('pointermove',e=>{const r=canvas.getBoundingClientRect(),x=e.clientX-r.left,y=e.clientY-r.top;if(dragging)rot+=(e.clientX-lastX)*.008;lastX=e.clientX;hover=hit(x,y);tooltip.textContent=hover;tooltip.style.opacity='1';tooltip.style.left=(x+15)+'px';tooltip.style.top=(y+15)+'px';});
 canvas.addEventListener('pointerleave',()=>tooltip.style.opacity='0');
 canvas.addEventListener('click',e=>{if(Math.abs(e.clientX-lastX)<4){const r=canvas.getBoundingClientRect();select(hit(e.clientX-r.left,e.clientY-r.top))}});
 canvas.addEventListener('wheel',e=>{e.preventDefault();zoom=Math.max(.72,Math.min(1.35,zoom*(e.deltaY<0?1.08:.92)))},{passive:false});
 powerBtn.addEventListener('click',()=>{powered=!powered;update()});loadSlider.addEventListener('input',update);
 document.getElementById('explodeBtn').addEventListener('click',e=>{exploded=!exploded;e.currentTarget.textContent=exploded?'COMPACT VIEW':'EXPLODE VIEW'});
 document.getElementById('airBtn').addEventListener('click',e=>{airflow=!airflow;e.currentTarget.textContent=airflow?'AIRFLOW ON':'AIRFLOW OFF'});
 document.getElementById('labelsBtn').addEventListener('click',e=>{labels=!labels;e.currentTarget.textContent=labels?'LABELS ON':'LABELS OFF'});
 document.getElementById('resetBtn').addEventListener('click',()=>{rot=0;zoom=1;exploded=false;document.getElementById('explodeBtn').textContent='EXPLODE VIEW'});
 window.addEventListener('resize',resize);resize();update();draw();
})();
'''
s=s+sim
p.write_text(s)
