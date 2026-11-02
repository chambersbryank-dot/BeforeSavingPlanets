# Dinosaur find pages. Same shape as the Smilodon page, plus a sourced ecosystem section.
# English and French are written here. Other languages keep the English with the review note.
import html, json

def _a(href, label):
    return f'<a href="{html.escape(href, quote=True)}" rel="noopener noreferrer">{html.escape(label)}</a>'

BROWN2017 = "https://www.cell.com/current-biology/fulltext/S0960-9822(17)30808-4"
BROWN2020 = "https://royalsocietypublishing.org/rsos/article/7/6/200305"
BROWN2020PMC = "https://pmc.ncbi.nlm.nih.gov/articles/PMC7353971/"
SERENO2007 = "https://doi.org/10.1371/journal.pone.0001230"
SERENO2005 = "https://public.websites.umich.edu/~wilsonja/JAW/Publications_files/Sereno%26Wilson2005.pdf"
ERICKSON = "https://doi.org/10.1080/02724634.1996.10011297"
PBDB_FELCH = "https://paleobiodb.org/classic/displayCollResults?collection_no=28366"
PBDB_BONE = "https://paleobiodb.org/classic/displayCollResults?collection_no=22648"
PBDB_LANCE = "https://paleobiodb.org/classic/displayCollResults?collection_no=46130"
PBDB_SAND = "https://paleobiodb.org/classic/displayCollResults?collection_no=49016"
PBDB_BRIGGS = "https://paleobiodb.org/classic/displayCollResults?collection_no=49529"
NHM_STEG = "https://www.nhm.ac.uk/discover/news/2016/may/dinosaur-eating-habit-insights-stegosaurus-stenops.html"
FILE_BOREAL = "https://commons.wikimedia.org/wiki/File:Borealopelta_markmitchelli_(TMP_2011.033.0001),_Royal_Tyrrell_Museum,_Drumheller,_Alberta,_2025-07-13.jpg"
FILE_NIGER = "https://commons.wikimedia.org/wiki/File:Nigersaurus_taqueti_skull.jpg"
FILE_TRI = "https://commons.wikimedia.org/wiki/File:Triceratops_skeleton_-_Ulster_Museum_2.JPG"
FILE_STEG = "https://commons.wikimedia.org/wiki/File:Stegosaurus_skeleton_at_American_Museum_of_Natural_History.jpg"

def _hero(prefix, spec, alt, credit_html, file_label, file_href):
    big, small = spec["big"], spec["small"]
    return (
        f'<section class="sm-hero"><img src="{prefix}{small}" srcset="{prefix}{small} {spec["sw"]}w, {prefix}{big} {spec["bw"]}w" '
        f'sizes="(min-width: 1100px) 2400px, 100vw" width="{spec["bw"]}" height="{spec["bh"]}" alt="{html.escape(alt)}" '
        f'fetchpriority="high" decoding="async"><div class="sm-hero-shade" aria-hidden="true"></div>'
        f'<div class="sm-hero-copy"><p class="sm-kicker">{spec["kicker"]}</p><h1>{spec["h1"]}</h1>'
        f'<p class="sm-lead">{spec["lead"]}</p><p class="sm-credit">{credit_html} {_a(file_href, file_label)}</p></div></section>'
    )

def dt_markup(prefix, lang, focus="", all_page=False):
    L="fr" if lang=="fr" else "en"
    full=""
    if focus and not all_page:
        label="Ouvrir la carte du temps profond" if lang=="fr" else "Open the full deep-time map"
        full=f'<p class="dt-full"><a href="Deep_Time.html#{html.escape(focus)}">{label}</a></p>'
    flag="1" if all_page else "0"
    return (f'<div class="dt" data-json="{prefix}assets/data/deep-time.json" data-tex="{prefix}assets/hero/paleo/" '
            f'data-prefix="{prefix}" data-lang="{L}" data-focus="{html.escape(focus)}" data-all="{flag}"></div>{full}')

def _map(prefix, h1, sites, aside_h, aside, lang, slug):
    if not sites:
        return f'<section><h2>{"Où sont les fossiles" if lang=="fr" else "Where the fossils are"}</h2>{aside}</section>'
    pins=[{"lat":s["lat"],"lng":s["lng"],"species":s["species"],"href":s["href"],"source":s["source"],
           "name":s["name"][lang],"note":s["note"][lang]} for s in sites]
    blob=json.dumps(pins, ensure_ascii=False).replace("<","\\u003c")
    icon=sites[0]["icon"]
    fr = lang=="fr"
    where = "Où sont les fossiles" if fr else "Where the fossils are"
    intro = ("Chaque icône est ce dinosaure, dessinée pour ce site. Elle est posée sur un lieu fossile d’aujourd’hui."
             if fr else
             "Each icon is this dinosaur, drawn for this site. It sits on a fossil locality as that place is today.")
    drift = ("Ces icônes marquent des fossiles sur la carte d’aujourd’hui. Quand l’animal vivait, les continents n’étaient pas à ces places."
             if fr else
             "These icons mark fossils on today’s map. When the animal lived, the continents were not in these places.")
    now_l = "Aujourd’hui" if fr else "Today"
    then_l = "À l’époque" if fr else "Then"
    group = "Carte d’aujourd’hui ou carte d’alors" if fr else "Today’s map or the map from then"
    return (f'<section><h2>{where}</h2><p>{intro}</p><p class="sm-drift">{drift}</p>'
            f'<div class="sm-when" role="group" aria-label="{html.escape(group)}">'
            f'<button type="button" data-when="now" aria-pressed="true">{now_l}</button>'
            f'<button type="button" data-when="then" aria-pressed="false">{then_l}</button></div>'
            f'<div class="sm-map-layout"><div class="sm-map-stack">'
            f'<div id="sm-now"><div id="sm-map" data-icon="{prefix}{icon}" role="region" aria-label="{html.escape(h1)}"></div></div>'
            f'<div id="sm-then" hidden>{dt_markup(prefix, lang, slug)}</div></div>'
            f'<aside class="sm-aside"><h3>{aside_h}</h3>{aside}</aside></div>'
            f'<script type="application/json" id="sm-sites">{blob}</script></section>')

def _page(lang, prefix, slug, spec):
    fr = lang=="fr"
    L = "fr" if fr else "en"
    note = "" if lang in ("en","fr") else '<p class="sm-note" role="note">TODO machine-draft translation: English for review.</p>'
    la = "" if lang in ("en","fr") else ' lang="en"'
    c = spec[L]
    file_label = "Page du fichier" if fr else "File page"
    hero = _hero(prefix, {**spec["img"], "kicker": c["kicker"], "h1": c["h1"], "lead": c["lead"]}, c["alt"], c["credit"], file_label, spec["file"])
    back = f'<p class="find-back"><a href="Dinosaurs.html">{"Tous les dinosaures" if fr else "All dinosaur finds"}</a> · <a href="Smilodon.html">Smilodon</a></p>'
    main = f'<main id="main">{hero}<div class="sm-wrap"{la}>{note}{c["body"]}{_map(prefix, c["h1"], spec["sites"], c["aside_h"], c["aside"], L, slug)}{back}</div></main>'
    return c["title"], c["desc"], main

# --- Borealopelta ---
def _boreal_en():
    return f'''
<p>Borealopelta markmitchelli is an armored dinosaur, a nodosaur, known from one skeleton. It is not a meat-eater. The skeleton is TMP 2011.033.0001.</p>
<h2>Timeline</h2>
<ul>
<li>The bones come from the Wabiskaw Member of the Clearwater Formation, at the Suncor Millennium Mine near Fort McMurray, Alberta. Brown, Henderson, Vinther, and others (2017) call that member Albian in the discovery section and Aptian in the locality line. Brown and others (2020) say ammonites, pollen, and foraminifera indicate an Early Albian age. This page uses Early Albian, and keeps both wordings.</li>
<li>The 2017 paper estimates a length of 5.5 m and a body mass of about 1,300 kg.</li>
</ul>
<h2>What we know</h2>
<ul>
<li>The skeleton keeps its three-dimensional shape, with skin, scales, and horn sheaths on the armor. It is on display at the Royal Tyrrell Museum in Drumheller. {_a(BROWN2017, "Brown, Henderson, Vinther, and others, 2017")}</li>
<li>Chemical tests found the signature of pheomelanin, a reddish-brown pigment. Melanosome shapes were not preserved. The back is darker than the belly. The paper reads that pattern as countershading. The large shoulder spine is pigmented in a way the authors tie to display, not only to armor.</li>
<li>A mass in the belly meets 14 of 16 checks for real stomach contents, a cololite. About 88% of it is leaf tissue. About 85% of that leaf fraction is leptosporangiate ferns. Cycad-like leaves are about 3%. Charcoal is about 6%. {_a(BROWN2020, "Brown and others, 2020")} {_a(BROWN2020PMC, "Same paper on PMC")}</li>
</ul>
<h2>What we don’t know yet</h2>
<ul>
<li>The Aptian and Albian labels in the 2017 paper do not match. The 2020 paper argues for Early Albian. The stage name is not settled by a single line.</li>
<li>The charcoal may mean the animal fed in a fern patch growing after a fire. The paper says “may.” It does not prove the animal sought out burns.</li>
<li>Countershading is an inference from where the dark film stops. The paper is clear that melanosome bodies were not found.</li>
</ul>
<h2>Its role in Earth’s ecosystem</h2>
<p>This animal ate plants, and the stomach shows which ones. It chose ferns and mostly skipped other plants that were in the surrounding rock. That is a herbivore shaping a fern-rich ground layer, not a high browser stripping trees. The charcoal is the paper’s evidence that fire and the plants that follow fire were part of that meal. {_a(BROWN2020, "Brown and others, 2020")}</p>
<p>The countershading, on an animal of about 1,300 kg that already carried armor, is the 2017 paper’s evidence that big predators still mattered. Living plant-eaters above about 1,000 kg usually do not wear camouflage, because adults are rarely killed. Borealopelta breaks that living pattern. The authors read it as predation pressure strong enough to favor hiding, even with armor. The shoulder spine, differently pigmented, is their candidate for a display signal to other Borealopelta, not only a weapon.</p>
<h2>Sources (3)</h2>
<ul>
<li>{_a(BROWN2017, "Brown, Henderson, Vinther, and others, 2017, Current Biology")}. The skeleton, the pigment, and the predator-pressure argument.</li>
<li>{_a(BROWN2020, "Brown and others, 2020, Royal Society Open Science")}. The stomach contents, the mine grid, and the Early Albian age.</li>
<li>{_a(FILE_BOREAL, "Wikimedia Commons — the hero photograph, CC BY-SA 4.0")}</li>
</ul>'''

def _boreal_fr():
    return f'''
<p>Borealopelta markmitchelli est un dinosaure cuirassé, un nodosaure, connu par un seul squelette. Ce n’est pas un carnivore. Le squelette est TMP 2011.033.0001.</p>
<h2>Chronologie</h2>
<ul>
<li>Les os viennent du membre de Wabiskaw, formation de Clearwater, à la mine Millennium de Suncor, près de Fort McMurray, en Alberta. Brown, Henderson, Vinther et autres (2017) appellent ce membre albien dans le récit de la découverte et aptien dans la ligne de localité. Brown et autres (2020) écrivent que les ammonites, le pollen et les foraminifères indiquent un âge albien précoce. Cette page retient l’Albien précoce et garde les deux formulations.</li>
<li>L’article de 2017 estime une longueur de 5,5 m et une masse d’environ 1 300 kg.</li>
</ul>
<h2>Ce que l’on sait</h2>
<ul>
<li>Le squelette garde son volume, avec la peau, les écailles et les étuis cornés de l’armure. Il est exposé au Royal Tyrrell Museum, à Drumheller. {_a(BROWN2017, "Brown, Henderson, Vinther et autres, 2017")}</li>
<li>Les analyses chimiques ont trouvé la signature de la phéomélanine, un pigment brun-roux. La forme des mélanosomes n’est pas conservée. Le dos est plus sombre que le ventre. L’article lit ce motif comme un contre-jour. La grande épine de l’épaule est pigmentée d’une façon que les auteurs lient à la parade, pas seulement à l’armure.</li>
<li>Une masse dans le ventre remplit 14 critères sur 16 pour de vrais contenus d’estomac, un cololite. Environ 88 % sont du tissu de feuille. Environ 85 % de cette part de feuilles sont des fougères leptosporangiées. Les feuilles de type cycas font environ 3 %. Le charbon de bois fait environ 6 %. {_a(BROWN2020, "Brown et autres, 2020")} {_a(BROWN2020PMC, "Le même article sur PMC")}</li>
</ul>
<h2>Ce que l’on ne sait pas encore</h2>
<ul>
<li>Les mots Aptien et Albien dans l’article de 2017 ne concordent pas. L’article de 2020 défend l’Albien précoce. Un seul étage n’est pas tranché par une seule ligne.</li>
<li>Le charbon de bois peut vouloir dire que l’animal mangeait dans une fougeraie après un feu. L’article dit « peut ». Il ne prouve pas que l’animal cherchait les brûlis.</li>
<li>Le contre-jour est une lecture de l’endroit où le film sombre s’arrête. L’article dit clairement que les mélanosomes eux-mêmes n’ont pas été trouvés.</li>
</ul>
<h2>Son rôle dans l’écosystème de la Terre</h2>
<p>Cet animal mangeait des plantes, et l’estomac montre lesquelles. Il choisissait les fougères et laissait de côté d’autres plantes présentes dans la roche autour. C’est un herbivore qui agit sur un tapis de fougères, pas un brouteur haut perché. Le charbon de bois est, dans l’article, le signe que le feu et les plantes qui suivent un feu entraient dans ce repas. {_a(BROWN2020, "Brown et autres, 2020")}</p>
<p>Le contre-jour, sur un animal d’environ 1 300 kg déjà couvert d’armure, est l’argument de 2017 : de grands prédateurs comptaient encore. Les herbivores vivants au-dessus d’environ 1 000 kg ne portent en général pas de camouflage, parce que les adultes sont rarement tués. Borealopelta rompt ce motif actuel. Les auteurs y lisent une pression de prédation assez forte pour favoriser le camouflage, même avec une armure. L’épine de l’épaule, pigmentée autrement, est leur candidate pour un signal vers d’autres Borealopelta, pas seulement une arme.</p>
<h2>Sources (3)</h2>
<ul>
<li>{_a(BROWN2017, "Brown, Henderson, Vinther et autres, 2017, Current Biology")}. Le squelette, le pigment et l’argument sur les prédateurs.</li>
<li>{_a(BROWN2020, "Brown et autres, 2020, Royal Society Open Science")}. Le contenu de l’estomac, le carroyage de la mine et l’âge albien précoce.</li>
<li>{_a(FILE_BOREAL, "Wikimedia Commons — la photo du bandeau, CC BY-SA 4.0")}</li>
</ul>'''

# --- Nigersaurus ---
def _niger_en():
    return f'''
<p>Nigersaurus taqueti is a sauropod, a long-necked plant-eater, from the Elrhaz Formation at Gadoufaoua in Niger. It is a rebbachisaurid. The skull is built to crop plants at the ground, not to reach a high crown.</p>
<h2>Timeline</h2>
<ul>
<li>Sereno and Wilson (2005) place it in the Early Cretaceous, Aptian to Albian, of the Elrhaz Formation.</li>
<li>Sereno and others (2007) reconstruct an adult about 9 m long, with a femur about 1 m long. That skeleton is several partial skeletons, scaled to one size. It is not one complete animal found in a single pose.</li>
</ul>
<h2>What we know</h2>
<ul>
<li>The holotype, MNN GDF512, is a skull and neck found together on about 1 m² of sandstone. Limb bones found farther away are not securely the same individual. {_a(SERENO2005, "Sereno and Wilson, 2005")}</li>
<li>The jaws hold tooth batteries at the front of the muzzle. One skull has more than 500 teeth if the replacement teeth are counted. A tooth could be replaced about once a month. The inner ear shows a habitual head posture with the muzzle aimed at the ground. {_a(SERENO2007, "Sereno and others, 2007")}</li>
<li>The paper defines ground-level browsing as cropping plants within one meter of the soil. In the Aptian and Albian that ground cover was ferns, horsetails, and other plants that were not grass. Grass is a later arrival.</li>
</ul>
<h2>What we don’t know yet</h2>
<ul>
<li>How many neck vertebrae a rebbachisaurid had. The 2007 paper says only eight neck vertebrae are known for the group in the comparison it discusses, and it still draws Nigersaurus with 13. The neck in the drawing is a reconstruction.</li>
<li>Whether every diplodocoid fed this way. The authors call widespread ground-level browsing a hypothesis that needs more teeth to test.</li>
<li>A body mass in kilograms. The paper says the mass was comparable to an elephant’s and does not print a number. This page does not invent one.</li>
</ul>
<h2>Its role in Earth’s ecosystem</h2>
<p>In a fauna with several sauropods, Nigersaurus took the lowest slice. A muzzle that faces the ground, a tooth battery at the front, and wear on the outer face of the teeth are the 2007 paper’s evidence that it gathered soft plants within a meter of the soil. That lowers the feeding band of the whole fauna: other sauropods could reach higher, and this one cropped the mat. {_a(SERENO2007, "Sereno and others, 2007")}</p>
<p>Sereno and Wilson (2005) also note that Cretaceous sauropods stayed diverse on southern continents while ornithischians with tooth batteries rose in the north. Nigersaurus is their southern example of a sauropod that evolved its own tooth battery. It was not a predator, and these papers do not name an animal that ate it.</p>
<h2>Sources (3)</h2>
<ul>
<li>{_a(SERENO2007, "Sereno, Wilson, Witmer, Whitlock, Maga, Ide, and Rowe, 2007, PLoS ONE")}</li>
<li>{_a(SERENO2005, "Sereno and Wilson, 2005, the tooth-battery chapter (PDF)")}. The Gadoufaoua coordinate and the holotype limits are here.</li>
<li>{_a(FILE_NIGER, "Wikimedia Commons — the hero figure, CC BY 2.5")}</li>
</ul>'''

def _niger_fr():
    return f'''
<p>Nigersaurus taqueti est un sauropode, un mangeur de plantes au long cou, de la formation d’Elrhaz à Gadoufaoua, au Niger. C’est un rebbachisauridé. Le crâne est fait pour couper des plantes au sol, pas pour atteindre une couronne haute.</p>
<h2>Chronologie</h2>
<ul>
<li>Sereno et Wilson (2005) le placent dans le Crétacé inférieur, de l’Aptien à l’Albien, formation d’Elrhaz.</li>
<li>Sereno et autres (2007) reconstruisent un adulte d’environ 9 m, avec un fémur d’environ 1 m. Ce squelette réunit plusieurs squelettes partiels, ramenés à une seule taille. Ce n’est pas un animal complet trouvé dans une seule pose.</li>
</ul>
<h2>Ce que l’on sait</h2>
<ul>
<li>L’holotype, MNN GDF512, est un crâne et un cou trouvés ensemble sur environ 1 m² de grès. Des os de membres trouvés plus loin ne sont pas sûrement le même individu. {_a(SERENO2005, "Sereno et Wilson, 2005")}</li>
<li>Les mâchoires portent des batteries de dents à l’avant du museau. Un crâne compte plus de 500 dents si l’on ajoute les dents de remplacement. Une dent pouvait être remplacée environ une fois par mois. L’oreille interne montre une posture habituelle avec le museau vers le sol. {_a(SERENO2007, "Sereno et autres, 2007")}</li>
<li>L’article définit le broutage au ras du sol comme la coupe de plantes à moins d’un mètre du sol. À l’Aptien et à l’Albien, ce couvert était fait de fougères, de prêles et d’autres plantes qui n’étaient pas de l’herbe. L’herbe arrive plus tard.</li>
</ul>
<h2>Ce que l’on ne sait pas encore</h2>
<ul>
<li>Combien de vertèbres du cou avait un rebbachisauridé. L’article de 2007 dit que seules huit vertèbres du cou sont connues pour le groupe dans la comparaison qu’il discute, et il dessine quand même Nigersaurus avec 13. Le cou du dessin est une reconstruction.</li>
<li>Si tous les diplodocoïdes mangeaient ainsi. Les auteurs présentent le broutage généralisé au ras du sol comme une hypothèse qui demande plus de dents pour être testée.</li>
<li>Une masse en kilogrammes. L’article dit une masse comparable à celle d’un éléphant et ne donne pas de chiffre. Cette page n’en invente pas.</li>
</ul>
<h2>Son rôle dans l’écosystème de la Terre</h2>
<p>Dans une faune à plusieurs sauropodes, Nigersaurus prenait la tranche la plus basse. Un museau tourné vers le sol, une batterie de dents à l’avant et une usure sur la face externe des dents sont les arguments de 2007 : il ramassait des plantes tendres à moins d’un mètre du sol. Cela abaisse la bande alimentaire de toute la faune. D’autres sauropodes pouvaient monter plus haut. Celui-ci coupait le tapis. {_a(SERENO2007, "Sereno et autres, 2007")}</p>
<p>Sereno et Wilson (2005) notent aussi que les sauropodes du Crétacé restent divers sur les continents du sud, tandis que les ornithischiens à batteries de dents montent au nord. Nigersaurus est leur exemple d’un sauropode du sud qui a évolué sa propre batterie. Ce n’était pas un prédateur, et ces articles ne nomment pas un animal qui le mangeait.</p>
<h2>Sources (3)</h2>
<ul>
<li>{_a(SERENO2007, "Sereno, Wilson, Witmer, Whitlock, Maga, Ide et Rowe, 2007, PLoS ONE")}</li>
<li>{_a(SERENO2005, "Sereno et Wilson, 2005, le chapitre sur la batterie dentaire (PDF)")}. La coordonnée de Gadoufaoua et les limites de l’holotype sont ici.</li>
<li>{_a(FILE_NIGER, "Wikimedia Commons — la figure du bandeau, CC BY 2.5")}</li>
</ul>'''

# --- Triceratops ---
def _tri_en():
    return f'''
<p>Triceratops is the three-horned plant-eater of the last part of the Cretaceous in western North America. The photograph is a mounted skeleton at the Ulster Museum in Belfast. The file page calls it Triceratops horridus. It does not say which quarry the bones came from, so this page does not invent one.</p>
<h2>Timeline</h2>
<ul>
<li>Erickson and Olson (1996) describe a Triceratops pelvis from the Late Maastrichtian Hell Creek Formation of east-central Montana. That is the end of the Cretaceous, in the same rock unit as Tyrannosaurus rex.</li>
</ul>
<h2>What we know</h2>
<ul>
<li>The pelvis is MOR 799, at the Museum of the Rockies in Bozeman. It carries 58 definite bite marks and 22 possible ones. Punctures reach 2.5 cm across and 3.7 cm deep. A cast of one deep bite matches an adult T. rex tooth, including the cutting edge. No other meat-eater known from the Hell Creek fauna was large enough, in that paper’s judgment, to do this. {_a(ERICKSON, "Erickson and Olson, 1996")}</li>
<li>At least 39 punctures are on the underside and the sides of the sacrum, so the pelvis was turned over before or during the biting. The first sacral vertebra is nearly bitten in half. About a sixth of the front of the left ilium was bitten away.</li>
</ul>
<h2>What we don’t know yet</h2>
<ul>
<li>Whether the tyrannosaur killed this Triceratops or fed on an animal that was already dead. The paper describes feeding. It does not show the moment of death.</li>
<li>Where the Ulster Museum mount was dug up. The file page does not say. This page does not guess a state or a quarry.</li>
<li>A GPS point for that bitten pelvis. The 1996 paper says east-central Montana and prints no coordinate. The pins on this map are other Triceratops horridus localities from the Paleobiology Database, not that bone.</li>
</ul>
<h2>Its role in Earth’s ecosystem</h2>
<p>The bite marks are a direct link in a food web. An adult Tyrannosaurus rex, or more than one, bit into this Triceratops pelvis hard enough to overturn it and to cut bone. Triceratops was not only a horned animal standing in a landscape. It was flesh in a T. rex meal, at least after death. {_a(ERICKSON, "Erickson and Olson, 1996")}</p>
<p>The paper does not count how often this happened, and it does not show Triceratops eating. The horns and the beak are visible on the Belfast mount. What plants those jaws cropped is not in the 1996 paper, so this page does not name a diet.</p>
<h2>Sources (5)</h2>
<ul>
<li>{_a(ERICKSON, "Erickson and Olson, 1996, Journal of Vertebrate Paleontology")}</li>
<li>{_a(PBDB_LANCE, "Paleobiology Database — Lance Creek collection 46130")}</li>
<li>{_a(PBDB_SAND, "Paleobiology Database — Sand Arroyo collection 49016")}</li>
<li>{_a(PBDB_BRIGGS, "Paleobiology Database — Briggsdale collection 49529")}</li>
<li>{_a(FILE_TRI, "Wikimedia Commons — the hero photograph, CC BY-SA 3.0")}</li>
</ul>'''

def _tri_fr():
    return f'''
<p>Triceratops est le mangeur de plantes à trois cornes de la fin du Crétacé dans l’ouest de l’Amérique du Nord. La photo est un squelette monté à l’Ulster Museum, à Belfast. La page du fichier l’appelle Triceratops horridus. Elle ne dit pas de quelle carrière viennent les os, donc cette page n’en invente pas.</p>
<h2>Chronologie</h2>
<ul>
<li>Erickson et Olson (1996) décrivent un bassin de Triceratops du Maastrichtien tardif, formation de Hell Creek, dans le centre-est du Montana. C’est la fin du Crétacé, dans la même unité que Tyrannosaurus rex.</li>
</ul>
<h2>Ce que l’on sait</h2>
<ul>
<li>Le bassin est MOR 799, au Museum of the Rockies, à Bozeman. Il porte 58 traces de morsure certaines et 22 possibles. Des perforations atteignent 2,5 cm de large et 3,7 cm de profondeur. Le moulage d’une morsure profonde correspond à une dent d’adulte de T. rex, tranchant compris. Aucun autre carnivore connu dans la faune de Hell Creek n’était assez grand, selon cet article, pour faire cela. {_a(ERICKSON, "Erickson et Olson, 1996")}</li>
<li>Au moins 39 perforations sont sous le sacrum et sur ses côtés, donc le bassin a été retourné avant ou pendant les morsures. La première vertèbre sacrée est presque coupée en deux. Environ un sixième de l’avant de l’ilion gauche a été emporté.</li>
</ul>
<h2>Ce que l’on ne sait pas encore</h2>
<ul>
<li>Si le tyrannosaure a tué ce Triceratops ou s’il a mangé un animal déjà mort. L’article décrit un repas. Il ne montre pas l’instant de la mort.</li>
<li>D’où vient le montage de l’Ulster Museum. La page du fichier ne le dit pas. Cette page ne devine ni un État ni une carrière.</li>
<li>Un point GPS pour ce bassin mordu. L’article de 1996 dit le centre-est du Montana et n’imprime pas de coordonnée. Les épingles de cette carte sont d’autres localités de Triceratops horridus dans la Paleobiology Database, pas cet os.</li>
</ul>
<h2>Son rôle dans l’écosystème de la Terre</h2>
<p>Les traces de morsure sont un lien direct dans un réseau alimentaire. Un Tyrannosaurus rex adulte, ou plusieurs, a mordu ce bassin de Triceratops assez fort pour le retourner et pour entamer l’os. Triceratops n’était pas seulement un animal à cornes dans un paysage. Il était de la chair dans un repas de T. rex, au moins après la mort. {_a(ERICKSON, "Erickson et Olson, 1996")}</p>
<p>L’article ne compte pas la fréquence, et il ne montre pas Triceratops en train de manger. Les cornes et le bec se voient sur le montage de Belfast. Les plantes que ces mâchoires coupaient ne sont pas dans l’article de 1996, donc cette page ne nomme pas un régime.</p>
<h2>Sources (5)</h2>
<ul>
<li>{_a(ERICKSON, "Erickson et Olson, 1996, Journal of Vertebrate Paleontology")}</li>
<li>{_a(PBDB_LANCE, "Paleobiology Database — collection Lance Creek 46130")}</li>
<li>{_a(PBDB_SAND, "Paleobiology Database — collection Sand Arroyo 49016")}</li>
<li>{_a(PBDB_BRIGGS, "Paleobiology Database — collection Briggsdale 49529")}</li>
<li>{_a(FILE_TRI, "Wikimedia Commons — la photo du bandeau, CC BY-SA 3.0")}</li>
</ul>'''

# --- Stegosaurus ---
def _steg_en():
    return f'''
<p>Stegosaurus stenops is a plated dinosaur from the Morrison Formation of the western United States. The photograph is a mount at the American Museum of Natural History in New York, with a smaller model in front of it. It is not the type skeleton, and the file page does not give a specimen number.</p>
<h2>Timeline</h2>
<ul>
<li>The Paleobiology Database records the type skeleton, USNM 4934, from Felch Quarry 1 at Garden Park, Colorado, in the Morrison Formation, and lists the age as Late Kimmeridgian. It cites Marsh, 1887, for the name Stegosaurus stenops. {_a(PBDB_FELCH, "Paleobiology Database — Felch Quarry 1")}</li>
</ul>
<h2>What we know</h2>
<ul>
<li>A 2016 study of the Natural History Museum in London’s Stegosaurus stenops skull, reported by that museum, found a bite about as strong as the bite of a sheep or a cow. The same account says the jaws could crop ferns and cycads, a wider menu than the more tender plants inferred for Plateosaurus. The London skull is not the New York mount in the photograph. {_a(NHM_STEG, "Natural History Museum — Stegosaurus feeding")}</li>
</ul>
<h2>What we don’t know yet</h2>
<ul>
<li>What the plates did. The sources used here are about the quarry and about feeding. They do not test display, defense, or heat. This page does not pick a job for the plates.</li>
<li>Which animal the New York mount is. The file page says Stegosaurus and does not say stenops or give a catalog number.</li>
<li>A coordinate printed by Marsh. The map points are Paleobiology Database locations for Felch Quarry 1 and Bone Cabin Quarry, not readings from the 1887 paper.</li>
</ul>
<h2>Its role in Earth’s ecosystem</h2>
<p>The London study is the feeding evidence. Stegosaurus stenops had a strong bite for a dinosaurian plant-eater and could take ferns and cycads, not only soft leaves. In the Morrison floodplains that is a mid-height to low plant-eater with a different bite from the other herbivores in the same computer comparison, Plateosaurus and Erlikosaurus. {_a(NHM_STEG, "Natural History Museum, London")}</p>
<p>The tail spikes are on the New York mount. These sources do not show a spike wound in another animal, so this page does not claim a predator that those spikes stopped.</p>
<h2>Sources (4)</h2>
<ul>
<li>{_a(PBDB_FELCH, "Paleobiology Database — Felch Quarry 1, Garden Park")}</li>
<li>{_a(PBDB_BONE, "Paleobiology Database — Bone Cabin Quarry")}</li>
<li>{_a(NHM_STEG, "Natural History Museum, London — what the Stegosaurus skull could bite")}</li>
<li>{_a(FILE_STEG, "Wikimedia Commons — the hero photograph, CC BY 4.0")}</li>
</ul>'''

def _steg_fr():
    return f'''
<p>Stegosaurus stenops est un dinosaure à plaques de la formation de Morrison, dans l’ouest des États-Unis. La photo est un montage à l’American Museum of Natural History, à New York, avec un modèle plus petit devant lui. Ce n’est pas le squelette type, et la page du fichier ne donne pas de numéro de spécimen.</p>
<h2>Chronologie</h2>
<ul>
<li>La Paleobiology Database enregistre le squelette type, USNM 4934, à Felch Quarry 1, Garden Park, Colorado, dans la formation de Morrison, et donne un âge kimméridgien tardif. Elle cite Marsh, 1887, pour le nom Stegosaurus stenops. {_a(PBDB_FELCH, "Paleobiology Database — Felch Quarry 1")}</li>
</ul>
<h2>Ce que l’on sait</h2>
<ul>
<li>Une étude de 2016 sur le crâne de Stegosaurus stenops du Natural History Museum de Londres, racontée par ce musée, a trouvé une morsure à peu près aussi forte que celle d’un mouton ou d’une vache. Le même récit dit que les mâchoires pouvaient couper des fougères et des cycas, un menu plus large que les plantes plus tendres inférées pour Plateosaurus. Le crâne de Londres n’est pas le montage de New York sur la photo. {_a(NHM_STEG, "Natural History Museum — l’alimentation de Stegosaurus")}</li>
</ul>
<h2>Ce que l’on ne sait pas encore</h2>
<ul>
<li>À quoi servaient les plaques. Les sources utilisées ici parlent de la carrière et de l’alimentation. Elles ne testent ni la parade, ni la défense, ni la chaleur. Cette page ne choisit pas un rôle pour les plaques.</li>
<li>Quel animal est le montage de New York. La page du fichier dit Stegosaurus et ne dit pas stenops, et elle ne donne pas de numéro.</li>
<li>Une coordonnée imprimée par Marsh. Les points de la carte sont des emplacements Paleobiology Database pour Felch Quarry 1 et Bone Cabin Quarry, pas des lectures de l’article de 1887.</li>
</ul>
<h2>Son rôle dans l’écosystème de la Terre</h2>
<p>L’étude de Londres est la preuve alimentaire. Stegosaurus stenops avait une morsure forte pour un dinosaure mangeur de plantes et pouvait prendre des fougères et des cycas, pas seulement des feuilles tendres. Dans les plaines de la Morrison, c’est un herbivore de hauteur moyenne à basse, avec une morsure différente des deux autres herbivores de la même comparaison par ordinateur, Plateosaurus et Erlikosaurus. {_a(NHM_STEG, "Natural History Museum, Londres")}</p>
<p>Les piques de la queue sont sur le montage de New York. Ces sources ne montrent pas une blessure de pique dans un autre animal, donc cette page ne nomme pas un prédateur que ces piques auraient arrêté.</p>
<h2>Sources (4)</h2>
<ul>
<li>{_a(PBDB_FELCH, "Paleobiology Database — Felch Quarry 1, Garden Park")}</li>
<li>{_a(PBDB_BONE, "Paleobiology Database — Bone Cabin Quarry")}</li>
<li>{_a(NHM_STEG, "Natural History Museum, Londres — ce que le crâne de Stegosaurus pouvait mordre")}</li>
<li>{_a(FILE_STEG, "Wikimedia Commons — la photo du bandeau, CC BY 4.0")}</li>
</ul>'''

FINDS = {
"Borealopelta": dict(
    file=FILE_BOREAL,
    img=dict(big="assets/finds/borealopelta-3840.webp", small="assets/finds/borealopelta-1600.webp", bw=3840, bh=2900, sw=1600),
    then=dict(mask="m120.webp",
              en="Then, 120 million years ago", fr="À l’époque, il y a 120 millions d’années",
              alt_en="PALEOMAP world about 120 million years ago, with the Borealopelta icon on the reconstructed site.",
              alt_fr="Monde PALEOMAP il y a environ 120 millions d’années, avec l’icône de Borealopelta sur le site reconstruit.",
              credit_en="Then view: Scotese PALEOMAP coastlines, the same set as the Dig Quest globe, via the GPlates Web Service (EarthByte). The icon was moved with that model to 120 million years ago, the nearest stored frame to the Early Albian. Not a new survey.",
              credit_fr="Vue d’alors : côtes PALEOMAP de Scotese, le même jeu que le globe du Dig Quest, via le service GPlates (EarthByte). L’icône a été déplacée avec ce modèle à 120 millions d’années, le cadre stocké le plus proche de l’Albien précoce. Pas un nouveau levé."),
    sites=[dict(lat=56.9801, lng=-111.3546, plat=56.8735, plon=-53.6183, species="Borealopelta markmitchelli", href=BROWN2020,
                source="Brown and others, 2020", icon="assets/finds/pin-borealopelta.svg",
                name={"en":"Suncor Millennium Mine, near Fort McMurray, Alberta","fr":"Mine Millennium de Suncor, près de Fort McMurray, Alberta"},
                note={"en":"Published grid: UTM zone 12, 478446 m E, 6315224 m N, WGS84. The decimal degrees are the conversion of that grid point, not a second survey. The fossil on display is at the Royal Tyrrell Museum in Drumheller.",
                      "fr":"Carroyage publié : UTM zone 12, 478446 m E, 6315224 m N, WGS84. Les degrés décimaux sont la conversion de ce point, pas un second levé. Le fossile exposé est au Royal Tyrrell Museum, à Drumheller."})],
    en=dict(title="Borealopelta", desc="An armored dinosaur from Alberta with skin, pigment, and a stomach full of ferns.",
            kicker="One skeleton, still in its skin", h1="Borealopelta", lead="An armored plant-eater with a fern meal still inside it.",
            alt="The fossil of Borealopelta markmitchelli, an armored dinosaur, on display against a pink museum wall.",
            credit="Borealopelta markmitchelli, TMP 2011.033.0001, at the Royal Tyrrell Museum, Drumheller. Chris Woodrich, CC BY-SA 4.0, via Wikimedia Commons. ShareAlike: remixes keep the same license. The original photograph is 4679 × 3533 pixels. This page serves it at 3840 and 1600 pixels wide.",
            aside_h="Also true", aside="<p>The display is in Drumheller. The pin is the mine, because that is the point the 2020 paper prints.</p>",
            body=_boreal_en()),
    fr=dict(title="Borealopelta", desc="Un dinosaure cuirassé d’Alberta, avec la peau, un pigment, et un estomac plein de fougères.",
            kicker="Un seul squelette, encore dans sa peau", h1="Borealopelta", lead="Un mangeur de plantes cuirassé, avec un repas de fougères encore à l’intérieur.",
            alt="Le fossile de Borealopelta markmitchelli, un dinosaure cuirassé, exposé contre un mur rose de musée.",
            credit="Borealopelta markmitchelli, TMP 2011.033.0001, au Royal Tyrrell Museum, à Drumheller. Chris Woodrich, CC BY-SA 4.0, via Wikimedia Commons. ShareAlike : les reprises gardent la même licence. La photo d’origine fait 4679 × 3533 pixels. Cette page la sert en 3840 et en 1600 pixels de large.",
            aside_h="Aussi vrai", aside="<p>L’exposition est à Drumheller. L’épingle est la mine, parce que c’est le point imprimé dans l’article de 2020.</p>",
            body=_boreal_fr()),
),
"Nigersaurus": dict(
    file=FILE_NIGER,
    img=dict(big="assets/finds/nigersaurus-3840.webp", small="assets/finds/nigersaurus-1600.webp", bw=2852, bh=3840, sw=1600),
    then=dict(mask="m120.webp",
              en="Then, 120 million years ago", fr="À l’époque, il y a 120 millions d’années",
              alt_en="PALEOMAP world about 120 million years ago, with the Nigersaurus icon on Gadoufaoua.",
              alt_fr="Monde PALEOMAP il y a environ 120 millions d’années, avec l’icône de Nigersaurus sur Gadoufaoua.",
              credit_en="Then view: Scotese PALEOMAP coastlines, the same set as the Dig Quest globe, via the GPlates Web Service (EarthByte). The icon was moved with that model to 120 million years ago, inside the Aptian–Albian span of this animal. Not a new survey.",
              credit_fr="Vue d’alors : côtes PALEOMAP de Scotese, le même jeu que le globe du Dig Quest, via le service GPlates (EarthByte). L’icône a été déplacée avec ce modèle à 120 millions d’années, dans l’intervalle Aptien–Albien de cet animal. Pas un nouveau levé."),
    sites=[dict(lat=16.45, lng=9.1333, plat=3.097, plon=4.6246, species="Nigersaurus taqueti", href=SERENO2005,
                source="Sereno and Wilson, 2005", icon="assets/finds/pin-nigersaurus.svg",
                name={"en":"Gadoufaoua, Ténéré, Niger","fr":"Gadoufaoua, Ténéré, Niger"},
                note={"en":"Sereno and Wilson (2005) print Gadoufaoua as 16°27′ N, 9°8′ E. The PDF shows a doubled prime on the longitude. This pin reads it as 9°8′ east (9.133° E), the reading that matches the Paleobiology Database figure of about 16.5° N, 9.2° E.",
                      "fr":"Sereno et Wilson (2005) impriment Gadoufaoua comme 16°27′ N, 9°8′ E. Le PDF montre un double prime sur la longitude. Cette épingle le lit comme 9°8′ est (9,133° E), la lecture qui rejoint le chiffre de la Paleobiology Database, environ 16,5° N, 9,2° E."})],
    en=dict(title="Nigersaurus", desc="A sauropod from Niger with a ground-facing muzzle and more than 500 teeth.",
            kicker="A lawnmower with a long neck", h1="Nigersaurus", lead="A plant-eater that cropped the ground, not the treetops.",
            alt="Scientific figure of the Nigersaurus taqueti skull, including drawings and a digital model with the muzzle aimed down.",
            credit="Figure of the skull and head posture of Nigersaurus taqueti from Sereno and others, 2007. CC BY 2.5, via Wikimedia Commons. This is a scientific figure, not a photograph of a mounted skeleton. The original file is 3540 × 4766 pixels. This page serves a 2852 × 3840 image and a 1600-pixel-wide image, without enlarging the file.",
            aside_h="One animal, many bones", aside="<p>The 9 m skeleton is a composite. Limb bones found away from the skull are not counted as the holotype.</p>",
            body=_niger_en()),
    fr=dict(title="Nigersaurus", desc="Un sauropode du Niger, au museau vers le sol et à plus de 500 dents.",
            kicker="Une tondeuse au long cou", h1="Nigersaurus", lead="Un mangeur de plantes qui coupait le sol, pas la cime des arbres.",
            alt="Figure scientifique du crâne de Nigersaurus taqueti, avec des dessins et un modèle numérique, le museau vers le bas.",
            credit="Figure du crâne et de la posture de la tête de Nigersaurus taqueti, Sereno et autres, 2007. CC BY 2.5, via Wikimedia Commons. C’est une figure scientifique, pas la photo d’un squelette monté. Le fichier d’origine fait 3540 × 4766 pixels. Cette page sert une image de 2852 × 3840 et une image de 1600 pixels de large, sans agrandir le fichier.",
            aside_h="Un animal, plusieurs os", aside="<p>Le squelette de 9 m est un composite. Les os de membres trouvés loin du crâne ne comptent pas dans l’holotype.</p>",
            body=_niger_fr()),
),
"Triceratops": dict(
    file=FILE_TRI,
    img=dict(big="assets/finds/triceratops-3840.webp", small="assets/finds/triceratops-1600.webp", bw=3840, bh=2880, sw=1600),
    then=dict(mask="m060.webp",
              en="Then, nearest map (60 million years ago)", fr="À l’époque, carte la plus proche (60 millions d’années)",
              alt_en="PALEOMAP world 60 million years ago, with Triceratops icons on the reconstructed sites.",
              alt_fr="Monde PALEOMAP il y a 60 millions d’années, avec les icônes de Triceratops sur les sites reconstruits.",
              credit_en="Then view: Scotese PALEOMAP coastlines, the same set as the Dig Quest globe, via the GPlates Web Service (EarthByte). Sixty million years ago is the nearest stored frame. Triceratops lived a few million years earlier, at the end of the Cretaceous. Not a new survey.",
              credit_fr="Vue d’alors : côtes PALEOMAP de Scotese, le même jeu que le globe du Dig Quest, via le service GPlates (EarthByte). Soixante millions d’années est le cadre stocké le plus proche. Triceratops vivait quelques millions d’années plus tôt, à la fin du Crétacé. Pas un nouveau levé."),
    sites=[
        dict(lat=43.2379, lng=-104.6084, plat=48.6076, plon=-83.7736, species="Triceratops horridus", href=PBDB_LANCE,
             source="Paleobiology Database — Lance Creek", icon="assets/finds/pin-triceratops.svg",
             name={"en":"Lance Creek, near Lightning Creek, Wyoming","fr":"Lance Creek, près de Lightning Creek, Wyoming"},
             note={"en":"Paleobiology Database location for a Triceratops horridus collection (46130), on today’s map. Not a coordinate from Erickson and Olson, 1996, and not the bitten pelvis.",
                   "fr":"Emplacement Paleobiology Database d’une collection de Triceratops horridus (46130), sur la carte d’aujourd’hui. Pas une coordonnée d’Erickson et Olson, 1996, et pas le bassin mordu."}),
        dict(lat=47.8396, lng=-106.1613, plat=53.3358, plon=-83.7282, species="Triceratops horridus", href=PBDB_SAND,
             source="Paleobiology Database — Sand Arroyo", icon="assets/finds/pin-triceratops.svg",
             name={"en":"Sand Arroyo / Prairie Elk Creek, Montana","fr":"Sand Arroyo / Prairie Elk Creek, Montana"},
             note={"en":"Paleobiology Database location for a Triceratops horridus collection (49016) in Hell Creek country. A database point, not a quarry stake printed in the 1996 paper.",
                   "fr":"Emplacement Paleobiology Database d’une collection de Triceratops horridus (49016), dans le pays de Hell Creek. Un point de base de données, pas un piquet de carrière imprimé en 1996."}),
        dict(lat=40.6700, lng=-104.3332, plat=46.0581, plon=-84.3175, species="Triceratops horridus", href=PBDB_BRIGGS,
             source="Paleobiology Database — Briggsdale", icon="assets/finds/pin-triceratops.svg",
             name={"en":"Two miles north of Briggsdale, Colorado","fr":"Trois kilomètres au nord de Briggsdale, Colorado"},
             note={"en":"Paleobiology Database location for a Late Maastrichtian Triceratops horridus collection (49529). A database point on today’s map.",
                   "fr":"Emplacement Paleobiology Database d’une collection de Triceratops horridus du Maastrichtien tardif (49529). Un point de base de données sur la carte d’aujourd’hui."}),
    ],
    en=dict(title="Triceratops", desc="A horned dinosaur from the end of the Cretaceous, and a meal for Tyrannosaurus.",
            kicker="Three horns, and a bitten pelvis", h1="Triceratops", lead="A plant-eater that ended up in a tyrannosaur’s meal.",
            alt="Mounted three-horned dinosaur skeleton in a glass case at the Ulster Museum.",
            credit="Mounted skeleton at the Ulster Museum, Belfast. The file page calls it Triceratops horridus. Bazonka, CC BY-SA 3.0, via Wikimedia Commons. ShareAlike: remixes keep the same license. The original photograph is 4320 × 3240 pixels. This page serves it at 3840 and 1600 pixels wide. The quarry is not named on the file page.",
            aside_h="Three fossil areas", aside=f"<p>Wyoming, Montana, and Colorado, as the Paleobiology Database locates Triceratops horridus today. The bitten pelvis has no printed coordinate. {_a(ERICKSON, 'Erickson and Olson, 1996')}</p>",
            body=_tri_en()),
    fr=dict(title="Triceratops", desc="Un dinosaure à cornes de la fin du Crétacé, et un repas pour Tyrannosaurus.",
            kicker="Trois cornes, et un bassin mordu", h1="Triceratops", lead="Un mangeur de plantes qui a fini dans un repas de tyrannosaure.",
            alt="Squelette monté d’un dinosaure à trois cornes, dans une vitrine de l’Ulster Museum.",
            credit="Squelette monté à l’Ulster Museum, à Belfast. La page du fichier l’appelle Triceratops horridus. Bazonka, CC BY-SA 3.0, via Wikimedia Commons. ShareAlike : les reprises gardent la même licence. La photo d’origine fait 4320 × 3240 pixels. Cette page la sert en 3840 et en 1600 pixels de large. La carrière n’est pas nommée sur la page du fichier.",
            aside_h="Trois régions fossiles", aside=f"<p>Wyoming, Montana et Colorado, là où la Paleobiology Database place Triceratops horridus aujourd’hui. Le bassin mordu n’a pas de coordonnée imprimée. {_a(ERICKSON, 'Erickson et Olson, 1996')}</p>",
            body=_tri_fr()),
),
"Stegosaurus": dict(
    file=FILE_STEG,
    img=dict(big="assets/finds/stegosaurus-3840.webp", small="assets/finds/stegosaurus-1600.webp", bw=3840, bh=2880, sw=1600),
    then=dict(mask="m160.webp",
              en="Then, 160 million years ago", fr="À l’époque, il y a 160 millions d’années",
              alt_en="PALEOMAP world about 160 million years ago, with Stegosaurus icons on the reconstructed quarries.",
              alt_fr="Monde PALEOMAP il y a environ 160 millions d’années, avec les icônes de Stegosaurus sur les carrières reconstruites.",
              credit_en="Then view: Scotese PALEOMAP coastlines, the same set as the Dig Quest globe, via the GPlates Web Service (EarthByte). The icons were moved with that model to 160 million years ago, the nearest stored frame to the Late Kimmeridgian. Not a new survey.",
              credit_fr="Vue d’alors : côtes PALEOMAP de Scotese, le même jeu que le globe du Dig Quest, via le service GPlates (EarthByte). Les icônes ont été déplacées avec ce modèle à 160 millions d’années, le cadre stocké le plus proche du Kimméridgien tardif. Pas un nouveau levé."),
    sites=[
        dict(lat=38.539501, lng=-105.224701, plat=32.6697, plon=-50.3395, species="Stegosaurus stenops", href=PBDB_FELCH,
             source="Paleobiology Database — Felch Quarry 1", icon="assets/finds/pin-stegosaurus.svg",
             name={"en":"Felch Quarry 1, Garden Park, Colorado","fr":"Felch Quarry 1, Garden Park, Colorado"},
             note={"en":"Paleobiology Database point for the type quarry of Stegosaurus stenops: 38.539501, −105.224701. Marsh’s 1887 paper, as cited there, does not print this coordinate. The photograph is a mount in New York, not this quarry.",
                   "fr":"Point de la Paleobiology Database pour la carrière type de Stegosaurus stenops : 38,539501, −105,224701. L’article de Marsh en 1887, cité là, n’imprime pas cette coordonnée. La photo est un montage à New York, pas cette carrière."}),
        dict(lat=42.017776, lng=-106.048615, plat=36.2042, plon=-50.3261, species="Stegosaurus stenops", href=PBDB_BONE,
             source="Paleobiology Database — Bone Cabin Quarry", icon="assets/finds/pin-stegosaurus.svg",
             name={"en":"Bone Cabin Quarry, Wyoming","fr":"Bone Cabin Quarry, Wyoming"},
             note={"en":"Paleobiology Database location for a Stegosaurus stenops collection at Bone Cabin Quarry (22648). A database point on today’s map, not a coordinate printed by Marsh.",
                   "fr":"Emplacement Paleobiology Database d’une collection de Stegosaurus stenops à Bone Cabin Quarry (22648). Un point de base de données sur la carte d’aujourd’hui, pas une coordonnée imprimée par Marsh."}),
    ],
    en=dict(title="Stegosaurus", desc="A plated dinosaur from the Morrison Formation, with a bite as strong as a cow’s.",
            kicker="Plates on the back, ferns in the bite", h1="Stegosaurus", lead="A Morrison plant-eater with a stronger bite than its skull suggests.",
            alt="A Stegosaurus skeleton on display at the American Museum of Natural History, with a smaller model in front.",
            credit="Stegosaurus mount at the American Museum of Natural History, New York, with a smaller model in front. Vicpeters, CC BY 4.0, via Wikimedia Commons. The original photograph is 5712 × 4284 pixels. This page serves it at 3840 and 1600 pixels wide. The file page does not give a specimen number.",
            aside_h="Photo and quarries", aside="<p>The pins are Garden Park and Bone Cabin, on today’s map. The skeleton in the hero is in New York.</p>",
            body=_steg_en()),
    fr=dict(title="Stegosaurus", desc="Un dinosaure à plaques de la formation de Morrison, avec une morsure aussi forte que celle d’une vache.",
            kicker="Des plaques sur le dos, des fougères dans la morsure", h1="Stegosaurus", lead="Un mangeur de plantes de la Morrison, avec une morsure plus forte que son crâne ne le laisse croire.",
            alt="Un squelette de Stegosaurus exposé à l’American Museum of Natural History, avec un modèle plus petit devant.",
            credit="Montage de Stegosaurus à l’American Museum of Natural History, à New York, avec un modèle plus petit devant. Vicpeters, CC BY 4.0, via Wikimedia Commons. La photo d’origine fait 5712 × 4284 pixels. Cette page la sert en 3840 et en 1600 pixels de large. La page du fichier ne donne pas de numéro de spécimen.",
            aside_h="Photo et carrières", aside="<p>Les épingles sont Garden Park et Bone Cabin, sur la carte d’aujourd’hui. Le squelette du bandeau est à New York.</p>",
            body=_steg_fr()),
),
}

FIND_SLUGS = ["Borealopelta", "Nigersaurus", "Triceratops", "Stegosaurus"]
NAV = {"en":"Dinosaurs","fr":"Dinosaures","es":"Dinosaurios","ar":"ديناصورات","it":"Dinosauri","he":"דינוזאורים"}
DEEP_NAV = {"en":"Deep time","fr":"Temps profond","es":"Tiempo profundo","ar":"الزمن العميق","it":"Tempo profondo","he":"זמן עמוק"}

USGS_AGE = "https://pubs.usgs.gov/gip/geotime/age.html"
NASA_230 = "https://science.nasa.gov/solar-system/solar-system-facts/"
NASA_250 = "https://imagine.gsfc.nasa.gov/science/featured_science/milkyway/"

def _time_intro(fr):
    if fr:
        line = "La Terre a enduré environ 4,5 milliards d’années et à peu près 20 tours autour du centre de la Voie lactée, et elle est encore d’un seul tenant."
        cite = ("Environ 4,5 milliards d’années arrondit l’âge de 4,54 milliards d’années de l’U.S. Geological Survey. "
                "NASA Science donne environ 230 millions d’années pour un tour de la Voie lactée. Une page plus ancienne de la NASA donne 250 millions d’années. "
                "À peu près 20 tours, c’est cet âge divisé par une année galactique dans cet intervalle.")
    else:
        line = "Earth has weathered about 4.5 billion years and roughly 20 trips around the center of the Milky Way, and it's still in one piece."
        cite = ("About 4.5 billion years rounds the U.S. Geological Survey age of 4.54 billion years. "
                "NASA Science gives about 230 million years for one trip around the Milky Way. An older NASA page gives 250 million years. "
                "Roughly 20 trips divides that age by a galactic year in that span.")
    links = " · ".join((
        _a(USGS_AGE, "USGS: Age of the Earth"),
        _a(NASA_230, "NASA Science: about 230 million years"),
        _a(NASA_250, "NASA: 250 million years"),
    ))
    return f'<p class="dt-intro">{line}</p><p class="dt-intro-src">{cite} {links}</p>'

def deep_time_page(lang, prefix=""):
    fr=lang=="fr"
    note="" if lang in ("en","fr") else '<p class="sm-note" role="note">TODO machine-draft translation: English for review.</p>'
    la="" if lang in ("en","fr") else ' lang="en"'
    if fr:
        title, desc = "Temps profond", "Les continents bougent du début du Cambrien à aujourd’hui. Les icônes ne sont là que pendant l’intervalle de chaque espèce."
        h1, lead = "Temps profond", "Faites défiler depuis 539 millions d’années, le début du Cambrien sur cette échelle, jusqu’à aujourd’hui. Le plus ancien est à gauche. Les côtes sont les images PALEOMAP du Dig Quest. Chaque icône suit sa plaque, et elle disparaît en dehors de l’intervalle cité. Le bandeau coloré suit les noms et les couleurs de la charte internationale. Des pastilles au-dessus du curseur gardent une catégorie, ou plusieurs. Le panneau dit qui vivait, et qui a disparu."
        back = "Retour aux dinosaures"
    else:
        title, desc = "Deep time", "Continents move from the start of the Cambrian to today. Icons show only during each species’ cited time span."
        h1, lead = "Deep time", "Scrub from 539 million years ago, the start of the Cambrian on this scale, to today. Oldest is on the left. The coastlines are the Dig Quest PALEOMAP images. Each icon rides its plate, and it disappears outside the cited span. The color band uses the international chart’s names and colors. Chips above the slider keep one category, or several. The panel says what lived, and what died out."
        back = "Back to the dinosaurs"
    links="".join(f'<a href="{s}.html">{s}</a>' for s in FIND_SLUGS)
    kicker = "Du Cambrien à aujourd’hui" if fr else "Cambrian to today"
    main=(f'<main id="main"><section class="sm-hero" style="min-height:34vh"><div class="sm-hero-shade" aria-hidden="true"></div>'
          f'<div class="sm-hero-copy"><p class="sm-kicker">{kicker}</p><h1>{h1}</h1><p class="sm-lead">{lead}</p></div></section>'
          f'<div class="sm-wrap"{la}>{note}{_time_intro(fr)}{dt_markup(prefix, lang, "", True)}'
          f'<p class="find-back"><a href="Dinosaurs.html">{back}</a> · {links}</p></div></main>')
    return title, desc, main

def find_page(slug, lang, prefix=""):
    return _page(lang, prefix, slug, FINDS[slug])

def has_map(slug):
    return bool(FINDS[slug]["sites"])

def hub_page(lang, prefix=""):
    fr = lang=="fr"
    note = "" if lang in ("en","fr") else '<p class="sm-note" role="note">TODO machine-draft translation: English for review.</p>'
    la = "" if lang in ("en","fr") else ' lang="en"'
    if fr:
        title, desc = "Dinosaures", "Quatre trouvailles, sur le modèle de la page Smilodon, avec le rôle de chacune dans son écosystème."
        h1, lead = "Dinosaures", "Les célèbres et ceux dont on parle peu. Chaque page a une image libre, une carte, ce que l’on sait, ce que l’on ne sait pas, une chronologie, un rôle dans l’écosystème, et les sources."
        love, rare = "Ceux que l’on aime", "Ceux dont on n’a pas entendu parler"
        later, why = "Pas encore sur le site", "Ce premier groupe tient en quatre pages, celles qui avaient une image libre assez grande et un lieu que l’on pouvait citer sans inventer un point."
    else:
        title, desc = "Dinosaurs", "Four finds, on the Smilodon page’s pattern, each with its role in an ecosystem."
        h1, lead = "Dinosaurs", "The ones we love, and the ones you have not heard of. Each page has a free image, a map, what we know, what we do not know yet, a timeline, a role in the ecosystem, and the sources."
        love, rare = "The dinosaurs we love", "The dinosaurs you’ve never heard of"
        later, why = "Not on the site yet", "This first set is four pages: the ones with a free image large enough to use, and a place that could be cited without inventing a dot."
    def card(slug, group):
        img=FINDS[slug]["img"]["small"]
        lead=html.escape(FINDS[slug]["fr" if fr else "en"]["lead"])
        return (f'<a class="find-card" href="{slug}.html"><img src="{prefix}{img}" alt="" width="640" height="240" loading="lazy">'
                f'<p class="find-k">{group}</p><h3>{slug}</h3><p>{lead}</p></a>')
    cards_love = card("Triceratops", love)+card("Stegosaurus", love)
    cards_rare = card("Borealopelta", rare)+card("Nigersaurus", rare)
    waiting = [
        ("Tyrannosaurus rex", "Many quarries, and it is easy to say more than the papers say. Next, not skipped."),
        ("Velociraptor", "The animal and the movie animal are easy to mix up. It needs its own careful page."),
        ("Brachiosaurus and Giraffatitan", "The famous Berlin skeleton is Giraffatitan, not Brachiosaurus. That page has to keep the two names apart."),
        ("Spinosaurus", "The body shape is still being revised. A short page would freeze a picture the papers have not finished."),
        ("Mononykus", "The American Museum mount is real, and the best free photo found is 2592 pixels wide, under the 3840-pixel bar used for this batch."),
        ("Yi qi", "One fossil, and how it flew is still argued. Deferred so the flight claim is not rushed."),
        ("Kosmoceratops", "The skull figure is free. Deferred so this batch stayed at four."),
        ("Halszkaraptor", "Deferred with the others. A later page has to deal with where the holotype was collected."),
    ]
    if fr:
        waiting = [
            ("Tyrannosaurus rex", "Beaucoup de carrières, et il est facile d’en dire plus que les articles. Ensuite, pas écarté."),
            ("Velociraptor", "L’animal et l’animal du film se mélangent vite. Il lui faut sa propre page, prudente."),
            ("Brachiosaurus et Giraffatitan", "Le célèbre squelette de Berlin est Giraffatitan, pas Brachiosaurus. La page doit garder les deux noms séparés."),
            ("Spinosaurus", "La forme du corps est encore en révision. Une page courte figerait une image que les articles n’ont pas finie."),
            ("Mononykus", "Le montage de l’American Museum est réel, et la meilleure photo libre trouvée fait 2592 pixels de large, sous la barre de 3840 pixels de ce groupe."),
            ("Yi qi", "Un seul fossile, et la façon de voler est encore discutée. Reporté pour ne pas bâcler le vol."),
            ("Kosmoceratops", "La figure du crâne est libre. Reporté pour que ce groupe reste à quatre."),
            ("Halszkaraptor", "Reporté avec les autres. Une page plus tard devra dire d’où vient l’holotype."),
        ]
    lis = "".join(f"<li><strong>{html.escape(n)}</strong> — {html.escape(w)}</li>" for n,w in waiting)
    kicker = "Le modèle est la page Smilodon" if fr else "The model is the Smilodon page"
    main = f'''<main id="main"><section class="sm-hero" style="min-height:42vh"><div class="sm-hero-shade" aria-hidden="true"></div><div class="sm-hero-copy"><p class="sm-kicker">{kicker}</p><h1>{h1}</h1><p class="sm-lead">{lead}</p></div></section>
<div class="sm-wrap"{la}>{note}<p><a href="Smilodon.html">{"La page Smilodon, le modèle" if fr else "The Smilodon page, the model"}</a> · <a href="Deep_Time.html">{"La carte du temps profond" if fr else "The deep-time map"}</a></p>
<h2>{love}</h2><div class="find-grid">{cards_love}</div>
<h2>{rare}</h2><div class="find-grid">{cards_rare}</div>
<h2>{later}</h2><p>{why}</p><ul class="find-wait">{lis}</ul></div></main>'''
    # The hub hero has no photograph. Do not fake one. The shade sits on the dark page background.
    return title, desc, main
