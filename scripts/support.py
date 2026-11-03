# "Support their work" blocks for BSP find pages + combined cross-site counts (Nov 2 2026).
# Data: /workspace/beforesavingplanets/support-links.csv. Donate only where vetted (audited / rated / public body).
import html
SP_DONATE, SP_VOL = 78, 227          # savingplanets.com Ways_to_Help totals (Saveworld build-ways-to-help.py)
ORGS = {
 "Smilodon": dict(org="La Brea Tar Pits (Natural History Museums of Los Angeles County)",
   donate="https://nhmlac.org/join-and-give/make-gift", vol="https://nhmlac.org/join-and-give/volunteers"),
 "Triceratops": dict(org="Ulster Museum (National Museums NI)",
   donate="https://www.ulstermuseum.org/join-support", vol="https://www.nationalmuseumsni.org/volunteer"),
 "Borealopelta": dict(org="Royal Tyrrell Museum of Palaeontology",
   donate="https://www.tyrrellmuseum.com/about/join_support", vol=""),
 "Stegosaurus": dict(org="American Museum of Natural History",
   donate="https://www.amnh.org/join-support/donate", vol="https://www.amnh.org/about/careers/volunteer"),
}
BSP_DONATE = sum(1 for o in ORGS.values() if o["donate"])
BSP_VOL = sum(1 for o in ORGS.values() if o["vol"])
T = {
 "en": dict(h="Support their work", p="This find is cared for by {org}. You can support them directly. Before Saving Planets is free and asks for nothing.", d="Donate", v="Volunteer",
            tot="Across Before Saving Planets and Saving Planets: {d} donation pages and {v} volunteer programs.", sp="More ways to help on Saving Planets", rule="Donate buttons only link to groups with audited finances, a recognized charity rating, or public (government or university) status."),
 "fr": dict(h="Soutenir leur travail", p="Cette découverte est conservée par {org}. Vous pouvez les soutenir directement. Before Saving Planets est gratuit et ne demande rien.", d="Faire un don", v="Bénévolat",
            tot="Sur Before Saving Planets et Saving Planets : {d} pages de dons et {v} programmes de bénévolat.", sp="Plus de façons d’aider sur Saving Planets", rule="Les boutons de don ne mènent qu’à des organismes aux comptes audités, notés par un évaluateur reconnu, ou publics (État ou université)."),
 "es": dict(h="Apoya su trabajo", p="Este hallazgo está al cuidado de {org}. Puedes apoyarlos directamente. Before Saving Planets es gratuito y no pide nada.", d="Donar", v="Voluntariado",
            tot="Entre Before Saving Planets y Saving Planets: {d} páginas de donación y {v} programas de voluntariado.", sp="Más formas de ayudar en Saving Planets", rule="Los botones de donar solo llevan a grupos con cuentas auditadas, una calificación benéfica reconocida o carácter público (gobierno o universidad)."),
 "it": dict(h="Sostieni il loro lavoro", p="Questo reperto è custodito da {org}. Puoi sostenerli direttamente. Before Saving Planets è gratuito e non chiede nulla.", d="Dona", v="Volontariato",
            tot="Tra Before Saving Planets e Saving Planets: {d} pagine di donazione e {v} programmi di volontariato.", sp="Altri modi per aiutare su Saving Planets", rule="I pulsanti Dona portano solo a enti con bilanci certificati, un rating benefico riconosciuto o natura pubblica (governo o università)."),
 "ar": dict(h="ادعم عملهم", p="تعتني بهذا الاكتشاف جهة {org}. يمكنك دعمها مباشرة. موقع Before Saving Planets مجاني ولا يطلب شيئًا.", d="تبرّع", v="تطوّع",
            tot="عبر Before Saving Planets وSaving Planets: {d} صفحة تبرع و{v} برنامج تطوع.", sp="طرق أخرى للمساعدة على Saving Planets", rule="أزرار التبرع تؤدي فقط إلى جهات ذات حسابات مدققة أو تقييم خيري معترف به أو صفة عامة (حكومة أو جامعة)."),
 "he": dict(h="תמכו בעבודתם", p="הממצא הזה נשמר בידי {org}. אפשר לתמוך בהם ישירות. Before Saving Planets חינמי ואינו מבקש דבר.", d="תרומה", v="התנדבות",
            tot="ב-Before Saving Planets וב-Saving Planets יחד: {d} דפי תרומה ו-{v} תוכניות התנדבות.", sp="עוד דרכים לעזור ב-Saving Planets", rule="כפתורי תרומה מובילים רק לגופים עם דוחות כספיים מבוקרים, דירוג צדקה מוכר או מעמד ציבורי (ממשלה או אוניברסיטה)."),
}
SP_HUBS = [("hub-ocean",{"en":"Oceans","fr":"Océans","es":"Océanos","it":"Oceani","ar":"المحيطات","he":"אוקיינוסים"}),
           ("hub-forests",{"en":"Forests","fr":"Forêts","es":"Bosques","it":"Foreste","ar":"الغابات","he":"יערות"}),
           ("hub-polar",{"en":"Polar","fr":"Pôles","es":"Polos","it":"Poli","ar":"القطبان","he":"קטבים"}),
           ("hub-lakes",{"en":"Lakes","fr":"Lacs","es":"Lagos","it":"Laghi","ar":"البحيرات","he":"אגמים"}),
           ("hub-rivers",{"en":"Rivers","fr":"Rivières","es":"Ríos","it":"Fiumi","ar":"الأنهار","he":"נהרות"})]
CSS = ('<style>.bsp-support{border:1px solid rgba(255,207,138,.35);border-radius:14px;padding:.9rem 1rem;margin:1.4rem 0;background:rgba(255,255,255,.05)}'
       '.bsp-support .bs-btns{display:flex;flex-wrap:wrap;gap:.5rem;margin:.6rem 0}.bsp-support .btn{display:inline-block;padding:.5rem 1rem;border-radius:999px;border:1px solid currentColor;text-decoration:none;font-weight:700;min-height:36px}'
       '.bsp-support .bs-don{background:#1b6e4b;border-color:#1b6e4b;color:#fff}.bsp-support small{display:block;opacity:.85}.bsp-support ul{display:flex;flex-wrap:wrap;gap:.3rem 1rem;list-style:none;padding:0}</style>')
def _sp(lang):
    return "https://www.savingplanets.com/" + ("" if lang=="en" else lang+"/") + "Ways_to_Help.html"
def totals(lang):
    return T[lang]["tot"].format(d=SP_DONATE+BSP_DONATE, v=SP_VOL+BSP_VOL)
def hubs(lang):
    return "<ul>" + "".join(f'<li><a href="{_sp(lang)}#{h}" rel="noopener">{n[lang]}</a></li>' for h,n in SP_HUBS) + "</ul>"
def block(slug, lang):
    o = ORGS.get(slug)
    if not o: return ""
    t = T[lang]; b = ""
    if o["donate"]: b += f'<a class="btn bs-don" href="{html.escape(o["donate"])}" target="_blank" rel="noopener">{t["d"]}</a>'
    if o["vol"]: b += f'<a class="btn" href="{html.escape(o["vol"])}" target="_blank" rel="noopener">{t["v"]}</a>'
    return (f'{CSS}<section class="bsp-support" id="support"><h2>{t["h"]}</h2><p>{t["p"].format(org=f"<span lang=\"en\">{html.escape(o["org"])}</span>")}</p>'
            f'<div class="bs-btns">{b}</div><p>{totals(lang)}</p><p><a href="{_sp(lang)}" rel="noopener">{t["sp"]}</a></p>{hubs(lang)}<small>{t["rule"]}</small></section>')
def help_section(lang, finds_label):
    t = T[lang]
    rows = "".join(f'<li><a href="{s}.html#support">{s}</a> — <span lang="en">{html.escape(o["org"])}</span></li>' for s,o in ORGS.items())
    return (f'{CSS}<div class="edu-wrap bsp-wrap"><section class="bsp-support"><h2>{t["h"]}</h2><p><b>{totals(lang)}</b></p><ul style="display:block">{rows}</ul>'
            f'<h3>{t["sp"]}</h3>{hubs(lang)}<small>{t["rule"]}</small></section></div>')
