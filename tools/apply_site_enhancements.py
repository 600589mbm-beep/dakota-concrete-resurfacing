from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"

if not DIST.is_dir():
    raise RuntimeError("dist directory missing; run the site generator first")

VALUE_SECTION = '''
<section aria-labelledby="value-title" class="section homeowner-value-section">
  <div class="container">
    <div class="section-heading value-heading">
      <div><p class="eyebrow">A better homeowner experience</p><h2 id="value-title">A clearer path from worn concrete to the right next step.</h2></div>
      <p>The strongest projects begin with useful information—not pressure. Start with the slab, understand the options, and decide what makes sense for the property.</p>
    </div>
    <div class="value-grid">
      <article><span>01</span><h3>Condition first</h3><p>Look at cracks, movement, scaling, drainage, moisture and previous coatings before choosing a finish.</p></article>
      <article><span>02</span><h3>System fit</h3><p>Match the resurfacing approach to how the driveway, patio, pool deck, walkway or entry is actually used.</p></article>
      <article><span>03</span><h3>Finish direction</h3><p>Compare texture, tone, traction and maintenance priorities so the surface fits the home—not just a sample board.</p></article>
      <article><span>04</span><h3>Honest next step</h3><p>Know when resurfacing is worth evaluating and when settlement, heaving or base failure may point toward replacement.</p></article>
    </div>
    <div class="project-snapshot"><strong>Helpful project snapshot</strong><span>Surface type</span><span>City</span><span>Approximate size</span><span>Wide photos</span><span>Close-up damage photos</span></div>
  </div>
</section>
'''

FIT_SECTION = '''
<section aria-labelledby="fit-title" class="section fit-check-section" id="fit-check">
  <div class="container fit-check-layout">
    <div class="fit-check-copy">
      <p class="eyebrow light">Quick project-fit check</p>
      <h2 id="fit-title">What best describes your concrete?</h2>
      <p>Choose the closest condition for a practical starting point. This tool is general guidance, not a substitute for an on-site slab assessment.</p>
      <div class="fit-options" role="group" aria-label="Choose the condition that best describes your concrete">
        <button class="fit-option" data-result="surface" type="button"><strong>Surface wear</strong><span>Fading, scaling, staining or an outdated finish</span></button>
        <button class="fit-option" data-result="cracks" type="button"><strong>Minor cracks + wear</strong><span>Small cracks that appear stable, plus cosmetic damage</span></button>
        <button class="fit-option" data-result="movement" type="button"><strong>Movement or settlement</strong><span>Heaving, sinking, separated sections or active cracks</span></button>
        <button class="fit-option" data-result="unsure" type="button"><strong>I am not sure</strong><span>The slab has several conditions or is difficult to evaluate</span></button>
      </div>
    </div>
    <aside class="fit-result" aria-live="polite" aria-atomic="true">
      <span class="fit-result-label">Your starting point</span>
      <h3 id="fit-result-title">Select a concrete condition.</h3>
      <p id="fit-result-copy">You will receive a plain-language next step and a list of details worth photographing or noting.</p>
      <ul id="fit-result-list"><li>Take one wide photo of the full surface.</li><li>Take close photos of damage or prior coatings.</li><li>Note drainage, movement and approximate dimensions.</li></ul>
      <a class="button button-gold" href="#estimate">Open the assessment checklist</a>
    </aside>
  </div>
</section>
'''

MOBILE_BAR_HOME = '''
<div class="mobile-action-bar" aria-label="Quick actions">
  <a href="#fit-check"><span>Project fit</span><strong>Check my concrete</strong></a>
  <a href="#estimate"><span>Next step</span><strong>Assessment checklist</strong></a>
</div>
'''

MOBILE_BAR_INNER = '''
<div class="mobile-action-bar" aria-label="Quick actions">
  <a href="index.html#fit-check"><span>Project fit</span><strong>Check my concrete</strong></a>
  <a href="index.html#estimate"><span>Next step</span><strong>Assessment checklist</strong></a>
</div>
'''

CSS_APPEND = r'''
/* Conversion and homeowner-experience enhancements */
:focus-visible{outline:3px solid var(--gold);outline-offset:4px}.homeowner-value-section{background:linear-gradient(180deg,#fff,#f7f8f5)}.value-heading{display:grid;grid-template-columns:1.1fr .9fr;gap:72px;align-items:end}.value-heading>p{margin:0;color:var(--muted);font-size:1.04rem}.value-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:16px}.value-grid article{position:relative;min-height:265px;padding:30px;border:1px solid var(--line);border-radius:22px;background:#fff;box-shadow:0 12px 35px rgba(20,34,30,.05);overflow:hidden}.value-grid article:after{content:"";position:absolute;width:120px;height:120px;right:-42px;bottom:-54px;border-radius:50%;background:var(--mint);opacity:.65}.value-grid article>span{display:inline-grid;place-items:center;width:42px;height:42px;border-radius:50%;background:var(--forest);color:#fff;font-weight:900}.value-grid h3{margin:28px 0 10px;font-size:1.28rem}.value-grid p{position:relative;z-index:1;margin:0;color:var(--muted);font-size:.91rem}.project-snapshot{display:flex;flex-wrap:wrap;align-items:center;gap:10px;margin-top:24px;padding:18px 20px;border:1px solid var(--line);border-radius:16px;background:var(--cream)}.project-snapshot strong{margin-right:8px;color:var(--forest)}.project-snapshot span{padding:8px 11px;border-radius:999px;background:#fff;color:var(--muted);font-size:.8rem;font-weight:800}.fit-check-section{position:relative;overflow:hidden;background:linear-gradient(135deg,#0b211b,#173f35);color:#fff}.fit-check-section:before{content:"";position:absolute;width:520px;height:520px;right:-180px;top:-220px;border-radius:50%;background:radial-gradient(circle,rgba(209,164,81,.28),transparent 68%)}.fit-check-layout{position:relative;display:grid;grid-template-columns:1.05fr .95fr;gap:70px;align-items:start}.fit-check-copy h2{margin:0;font-size:clamp(2.5rem,4.6vw,4.8rem)}.fit-check-copy>p:not(.eyebrow){max-width:700px;color:#c9d8d2}.fit-options{display:grid;grid-template-columns:repeat(2,1fr);gap:12px;margin-top:30px}.fit-option{display:grid;gap:5px;min-height:120px;padding:19px;border:1px solid rgba(255,255,255,.19);border-radius:16px;background:rgba(255,255,255,.06);color:#fff;text-align:left;cursor:pointer;transition:.2s}.fit-option:hover,.fit-option.is-active{transform:translateY(-2px);border-color:var(--gold);background:rgba(209,164,81,.14)}.fit-option strong{font:800 1rem Manrope,sans-serif}.fit-option span{color:#c5d4cf;font-size:.82rem}.fit-result{position:sticky;top:120px;padding:34px;border:1px solid rgba(255,255,255,.16);border-radius:26px;background:#fff;color:var(--ink);box-shadow:0 30px 75px rgba(0,0,0,.23)}.fit-result-label{display:inline-block;padding:7px 10px;border-radius:999px;background:var(--mint);color:var(--forest);font-size:.72rem;font-weight:900;letter-spacing:.12em;text-transform:uppercase}.fit-result h3{margin:24px 0 12px;font-size:clamp(1.7rem,3vw,2.5rem)}.fit-result p,.fit-result li{color:var(--muted)}.fit-result ul{padding-left:20px;margin:22px 0 28px}.fit-result li{margin:8px 0}.fit-result .button{width:100%}.mobile-action-bar{display:none}.reveal-ready{opacity:0;transform:translateY(24px);transition:opacity .65s ease,transform .65s ease}.reveal-ready.is-visible{opacity:1;transform:none}.service-card h3 a{color:inherit}.service-card:not(.service-card-large) .card-link{color:var(--forest2)!important}.service-card:not(.service-card-large):hover{border-color:rgba(30,75,63,.35)}
@media(max-width:1000px){.value-heading,.fit-check-layout{grid-template-columns:1fr;gap:46px}.value-grid{grid-template-columns:repeat(2,1fr)}.fit-result{position:relative;top:auto}}
@media(max-width:700px){body{padding-bottom:72px}.value-grid,.fit-options{grid-template-columns:1fr}.value-grid article{min-height:auto}.project-snapshot{align-items:flex-start}.fit-option{min-height:105px}.fit-result{padding:25px}.mobile-action-bar{position:fixed;z-index:200;left:10px;right:10px;bottom:10px;display:grid;grid-template-columns:1fr 1fr;overflow:hidden;border:1px solid rgba(255,255,255,.18);border-radius:17px;background:rgba(8,26,21,.96);box-shadow:0 14px 45px rgba(0,0,0,.3);backdrop-filter:blur(16px)}.mobile-action-bar a{display:grid;gap:1px;padding:11px 13px;color:#fff}.mobile-action-bar a+a{border-left:1px solid rgba(255,255,255,.14);background:var(--gold);color:#17211e}.mobile-action-bar span{font-size:.65rem;font-weight:800;letter-spacing:.09em;text-transform:uppercase;opacity:.75}.mobile-action-bar strong{font-size:.78rem}.mobile-action-bar.is-hidden{transform:translateY(120%);opacity:0}.footer-bottom{padding-bottom:18px}}
@media(prefers-reduced-motion:reduce){.reveal-ready{opacity:1;transform:none}.fit-option:hover{transform:none}}
'''

JS_APPEND = r'''

// Homeowner project-fit tool and progressive visual enhancements.
const fitContent={
  surface:{title:'Resurfacing may be worth evaluating.',copy:'Surface-level wear on an otherwise stable slab is the type of condition commonly considered for resurfacing, staining or sealing.',items:['Photograph scaling, stains and worn areas in daylight.','Note whether any sections rock, sink or collect water.','Record prior paint, coating or sealer if known.']},
  cracks:{title:'A closer crack assessment is the right next step.',copy:'Some small, stable cracks can be prepared, but crack type and movement matter. No responsible finish can promise that an active crack will never return.',items:['Photograph the full crack and a close-up with a size reference.','Note whether the crack changes seasonally or has widened.','Check both sides for height difference or movement.']},
  movement:{title:'Replacement may deserve priority.',copy:'Heaving, settlement, displaced sections and ongoing movement can indicate a base or structural issue that a surface finish will not correct.',items:['Photograph height differences and separated sections.','Note trip hazards, drainage problems and nearby downspouts.','Ask for a condition-based recommendation before selecting finishes.']},
  unsure:{title:'Start with an organized condition review.',copy:'Mixed symptoms are common. A useful review separates appearance concerns from movement, drainage and structural issues.',items:['Take wide photos from multiple angles.','Add close-ups of every different type of damage.','Write down what changed, when it appeared and where water travels.']}
};
const fitButtons=document.querySelectorAll('.fit-option');
const fitTitle=document.getElementById('fit-result-title');
const fitCopy=document.getElementById('fit-result-copy');
const fitList=document.getElementById('fit-result-list');
fitButtons.forEach(button=>button.addEventListener('click',()=>{
  const result=fitContent[button.dataset.result];
  if(!result||!fitTitle||!fitCopy||!fitList)return;
  fitButtons.forEach(item=>item.classList.remove('is-active'));
  button.classList.add('is-active');
  fitTitle.textContent=result.title;
  fitCopy.textContent=result.copy;
  fitList.innerHTML=result.items.map(item=>`<li>${item}</li>`).join('');
}));

if(!window.matchMedia('(prefers-reduced-motion: reduce)').matches&&'IntersectionObserver'in window){
  const revealTargets=document.querySelectorAll('.value-grid article,.service-card,.photo-card,.why-grid article,.expertise-points article,.fit-result');
  revealTargets.forEach(target=>target.classList.add('reveal-ready'));
  const revealObserver=new IntersectionObserver(entries=>entries.forEach(entry=>{
    if(entry.isIntersecting){entry.target.classList.add('is-visible');revealObserver.unobserve(entry.target)}
  }),{threshold:.12});
  revealTargets.forEach(target=>revealObserver.observe(target));
}

const mobileBar=document.querySelector('.mobile-action-bar');
const estimateSection=document.getElementById('estimate');
if(mobileBar&&estimateSection&&'IntersectionObserver'in window){
  const barObserver=new IntersectionObserver(entries=>entries.forEach(entry=>mobileBar.classList.toggle('is-hidden',entry.isIntersecting)),{threshold:.15});
  barObserver.observe(estimateSection);
}
'''

index_path = DIST / "index.html"
index = index_path.read_text(encoding="utf-8")

index = index.replace('<a href="#services">Services</a>', '<a href="#services">Services</a>\n<a href="#fit-check">Project Fit</a>', 1)
index = index.replace('<div class="hero-actions"><a class="button button-gold" href="#estimate">Request a Free Assessment</a><a class="button button-ghost" href="#gallery">See Real Photo Inspiration</a></div>', '<div class="hero-actions"><a class="button button-gold" href="#fit-check">Check My Concrete</a><a class="button button-ghost" href="#services">Explore Residential Services</a></div>', 1)
index = index.replace('<section class="section intro-section" id="services">', VALUE_SECTION + '\n<section class="section intro-section" id="services">', 1)
index = index.replace('<article class="service-card"><span>06</span><h3>Crack Repair, Staining &amp; Sealing</h3><p>Prepare problem areas and add color or protection based on the needs of the slab.</p></article>', '<article class="service-card"><span>06</span><h3><a href="concrete-resurfacing-guide.html">Crack Repair, Staining &amp; Sealing</a></h3><p>Prepare problem areas and add color or protection based on the needs of the slab.</p><a class="card-link" href="concrete-resurfacing-guide.html">Read the homeowner guide →</a></article>', 1)
index = index.replace('<section aria-labelledby="faq-title" class="section faq-section" id="faq">', FIT_SECTION + '\n<section aria-labelledby="faq-title" class="section faq-section" id="faq">', 1)
index = index.replace('</body>', MOBILE_BAR_HOME + '\n</body>', 1)
index = index.replace('Free Estimate', 'Assessment Prep').replace('Free estimate', 'Assessment prep')
index_path.write_text(index, encoding="utf-8")

for html_path in DIST.glob("*.html"):
    if html_path.name in {"index.html", "404.html"}:
        continue
    text = html_path.read_text(encoding="utf-8")
    text = text.replace('Free Estimate', 'Assessment Prep').replace('Free estimate', 'Assessment prep')
    if 'mobile-action-bar' not in text and '</body>' in text:
        text = text.replace('</body>', MOBILE_BAR_INNER + '\n</body>', 1)
    html_path.write_text(text, encoding="utf-8")

styles_path = DIST / "styles.css"
styles = styles_path.read_text(encoding="utf-8")
if "/* Conversion and homeowner-experience enhancements */" not in styles:
    styles_path.write_text(styles + CSS_APPEND, encoding="utf-8")

script_path = DIST / "script.js"
script = script_path.read_text(encoding="utf-8")
if "const fitContent=" not in script:
    script_path.write_text(script + JS_APPEND, encoding="utf-8")

required_markers = {
    "index.html": ["id=\"fit-check\"", "homeowner-value-section", "mobile-action-bar", "Check My Concrete"],
    "styles.css": ["fit-check-section", "mobile-action-bar", "reveal-ready"],
    "script.js": ["const fitContent=", "IntersectionObserver", "fit-option"],
}
for filename, markers in required_markers.items():
    content = (DIST / filename).read_text(encoding="utf-8")
    missing = [marker for marker in markers if marker not in content]
    if missing:
        raise RuntimeError(f"Enhancement markers missing from {filename}: {', '.join(missing)}")

print("Applied conversion and homeowner-experience enhancements")
