// Small micro-interactions for pixel UI
document.addEventListener('DOMContentLoaded', function(){
  document.querySelectorAll('.cta, .cta-outline').forEach(el=>{
    el.addEventListener('mousedown', ()=> el.classList.add('pixel-press'))
    el.addEventListener('mouseup', ()=> el.classList.remove('pixel-press'))
    el.addEventListener('mouseleave', ()=> el.classList.remove('pixel-press'))
  })

  // The mushroom image is centered and static; no scroll-based movement is applied.
})
