const header=document.querySelector('.site-header');
const toggle=document.querySelector('.menu-toggle');
const nav=document.querySelector('.primary-nav');

document.getElementById('year').textContent=new Date().getFullYear();

window.addEventListener('scroll',()=>{
  header.classList.toggle('scrolled',window.scrollY>8);
},{passive:true});

toggle?.addEventListener('click',()=>{
  const open=toggle.getAttribute('aria-expanded')==='true';
  toggle.setAttribute('aria-expanded',String(!open));
  nav.classList.toggle('open',!open);
});

if(nav&&!nav.querySelector('a[href="#gallery"]')){
  const galleryLink=document.createElement('a');
  galleryLink.href='#gallery';
  galleryLink.textContent='Gallery';
  const processLink=nav.querySelector('a[href="#process"]');
  nav.insertBefore(galleryLink,processLink||nav.lastElementChild);
}

const services=document.querySelector('#services');
if(services&&!document.querySelector('#gallery')){
  const gallery=document.createElement('section');
  gallery.className='section gallery-section';
  gallery.id='gallery';
  gallery.innerHTML=`
    <div class="container">
      <div class="section-heading centered">
        <p class="eyebrow">Residential before &amp; after inspiration</p>
        <h2>See how resurfacing can transform residential concrete.</h2>
        <p>Explore twelve residential-only visual examples across driveways, patios, pool decks, sidewalks, walkways, front entries, and steps.</p>
      </div>
      <div class="gallery-rows">
        <figure class="gallery-row"><img src="images/gallery/gallery-row-1.svg" alt="Four illustrative residential before and after concrete resurfacing examples including driveway, patio, pool deck and sidewalk" loading="lazy"><figcaption>Driveways · Patios · Pool decks · Sidewalks</figcaption></figure>
        <figure class="gallery-row"><img src="images/gallery/gallery-row-2.svg" alt="Four illustrative residential before and after concrete resurfacing examples including front entry, steps, stamped patio and driveway" loading="lazy"><figcaption>Front entries · Steps · Stamped patios · Driveways</figcaption></figure>
        <figure class="gallery-row"><img src="images/gallery/gallery-row-3.svg" alt="Four additional illustrative residential before and after concrete resurfacing examples including walkway, pool deck, patio and front step" loading="lazy"><figcaption>Walkways · Pool decks · Patios · Front steps</figcaption></figure>
      </div>
      <p class="gallery-disclaimer">Illustrative residential transformation examples shown for design inspiration. Finished appearance varies by slab condition, selected system, texture, and color. These should be replaced with verified Dakota residential project photography as completed work becomes available.</p>
      <div class="gallery-cta"><a class="button" href="#estimate">Get a Free Concrete Assessment</a></div>
    </div>`;
  services.insertAdjacentElement('afterend',gallery);

  const style=document.createElement('style');
  style.textContent=`
    .gallery-section{background:#f7f4ed}.gallery-rows{display:grid;gap:30px}.gallery-row{margin:0;overflow:hidden;border:1px solid rgba(20,34,30,.12);border-radius:24px;background:#0e1110;box-shadow:0 16px 45px rgba(20,34,30,.10)}.gallery-row img{display:block;width:100%;height:auto}.gallery-row figcaption{padding:16px 20px;color:#f1d28a;font:800 .9rem Manrope,sans-serif;letter-spacing:.04em;text-align:center}.gallery-disclaimer{max-width:900px;margin:32px auto 0;color:var(--muted);font-size:.8rem;text-align:center}.gallery-cta{display:flex;justify-content:center;margin-top:28px}@media(max-width:700px){.gallery-rows{gap:18px}.gallery-row{border-radius:16px}.gallery-row figcaption{padding:12px 14px;font-size:.75rem}.gallery-disclaimer{font-size:.74rem}}`;
  document.head.appendChild(style);
}

nav?.querySelectorAll('a').forEach(link=>{
  link.addEventListener('click',()=>{
    nav.classList.remove('open');
    toggle?.setAttribute('aria-expanded','false');
  });
});
