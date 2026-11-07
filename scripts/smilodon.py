# Saber-toothed cat page. English and French are written for this page.
# Spanish, Arabic, Italian, and Hebrew keep the English text with the site's review note.
import html, json

# The video behind the title is built from these two files, not the museum photograph.
SKEL = "https://commons.wikimedia.org/wiki/File:Smilodon_californicus_Bovard_(sabertooth)_skeleton_(white_background).jpg"
DRAW = "https://commons.wikimedia.org/wiki/File:Smilodon_fatalis_Sergiodlarosa_with_a_white_background.png"
CC_BY_SA = "https://creativecommons.org/licenses/by-sa/3.0/"
TIGERS = "https://tarpits.org/stories/smilodon-saber-tooths-and-tigersoh-my"
FLMNH = "https://www.floridamuseum.ufl.edu/florida-vertebrate-fossils/species/smilodon-fatalis/"
DIET = "https://pmc.ncbi.nlm.nih.gov/articles/PMC12506855/"
KURTEN = "https://doi.org/10.1080/02724634.1990.10011804"
TALARA = "https://doi.org/10.1016/j.palaeo.2024.112032"
SEYMOUR = "https://sedici.unlp.edu.ar/handle/10915/16766"
PAMPA = "https://doi.org/10.1016/j.palaeo.2016.02.017"
TARPITS = "https://tarpits.org/"
LAGOA = "https://www.lagoasanta.mg.gov.br/turismo-cultura-o-que-conhecer/pre-historia-e-lund"

# Talara study-area point from Cruz, Lindsey, and others, 2024:
# 4°38′38.92″ S, 81°8′9.47″ W.
SITES = [
 dict(lat=34.063, lng=-118.356, species="Smilodon fatalis",
      href=FLMNH, source="Florida Museum of Natural History — Smilodon fatalis",
      name={"en":"La Brea Tar Pits, Los Angeles, California","fr":"Les puits de bitume de La Brea, Los Angeles, Californie"},
      note={"en":"Same point as the World Map coin (34.063, −118.356). The Florida Museum says more than 2,000 skulls of Smilodon fatalis come from these pits.",
            "fr":"Le même point que la pièce de la carte du monde (34,063, −118,356). Le musée de Floride écrit que plus de 2 000 crânes de Smilodon fatalis viennent de ces puits."}),
 dict(lat=-4.6441, lng=-81.1360, species="Smilodon fatalis",
      href=TALARA, source="Cruz, Lindsey, and others, 2024",
      name={"en":"Talara tar seeps, Piura, Peru","fr":"Les suintements de goudron de Talara, Piura, Pérou"},
      note={"en":"Published study-area point: 4°38′38.92″ S, 81°8′9.47″ W. Seymour (2010) counted a minimum of 20 Smilodon fatalis. The 2024 paper reports dates of about 14,500 to 17,000 years before present.",
            "fr":"Point publié pour la zone d’étude : 4°38′38,92″ S, 81°8′9,47″ O. Seymour (2010) a compté au minimum 20 Smilodon fatalis. L’article de 2024 donne environ 14 500 à 17 000 ans avant le présent."}),
 dict(lat=-19.63, lng=-43.89, species="Smilodon populator",
      href=LAGOA, source="Lagoa Santa — Peter Lund and the caves",
      name={"en":"Lagoa Santa caves, Minas Gerais, Brazil","fr":"Les grottes de Lagoa Santa, Minas Gerais, Brésil"},
      note={"en":"Same cave-region point as the World Map coin. Peter Lund named Smilodon populator from these caves. The skeleton on that coin is a cast in Georgia, USA, not a bone from the cave.",
            "fr":"Le même point de région que la pièce de la carte du monde. Peter Lund a nommé Smilodon populator à partir de ces grottes. Le squelette de cette pièce est un moulage en Géorgie, aux États-Unis, pas un os de la grotte."}),
]

def _p(text):
    return f"<p>{text}</p>"

def _a(href, label):
    return f'<a href="{html.escape(href, quote=True)}" rel="noopener noreferrer">{html.escape(label)}</a>'

COMPARE = {
    'en': '<section class="sm-vs" id="smilodon-vs-you"><h2>Smilodon vs. you</h2><figure><picture><source type="image/webp" srcset="@@/assets/smilodon/smilodon-vs-woman-v4-800.webp 800w, @@/assets/smilodon/smilodon-vs-woman-v4-1400.webp 1400w" sizes="(max-width: 940px) 100vw, 900px"><img class="sm-vs-img" src="@@/assets/smilodon/smilodon-vs-woman-v4-1400.jpg" width="1400" height="1090" loading="lazy" decoding="async" alt="To scale: the Smilodon fatalis restoration, 100 cm tall at the shoulder and about 175 cm long plus a 35 cm tail, standing next to a woman 165 cm (5 ft 5 in) tall. The cat’s shoulder comes up to about her waist."></picture><figcaption>To scale: the Smilodon fatalis restoration, 100 cm tall at the shoulder and about 175 cm long plus a 35 cm tail, standing next to a woman 165 cm (5 ft 5 in) tall. The cat’s shoulder comes up to about her waist.<p class="sm-vs-credit">Created by the Founder and SI. Smilodon: <a href="https://commons.wikimedia.org/wiki/File:Smilodon_fatalis_Sergiodlarosa_with_a_white_background.png" rel="noopener noreferrer">Sergio De La Rosa</a>, <a href="https://creativecommons.org/licenses/by-sa/3.0/" rel="noopener noreferrer">CC BY-SA 3.0</a>, via Wikimedia Commons. Woman figure: Created by the Founder and SI, shown with her permission. Image licensed <a href="https://creativecommons.org/licenses/by-sa/3.0/" rel="noopener noreferrer">CC BY-SA 3.0</a>.</p></figcaption></figure><ul><li><strong>Weight:</strong> <em>S. fatalis</em> weighed about 160–280 kg (350–620 lb). That is about 2 to 3 grown men. The biggest species, <em>S. populator</em>, weighed about 220–360 kg, up to about 4 grown men.</li><li><strong>Height:</strong> its back stood about 100 cm (39 in) high at the shoulder, around waist height on most adults.</li><li><strong>Length:</strong> from nose to rump it was about 175 cm, a little longer than the 165 cm woman in the picture is tall, plus a short tail of about 35 cm (14 in).</li><li><strong>Teeth:</strong> each saber tooth was up to 18 cm (7 in) long, about as long as a pencil.</li><li><strong>Bite:</strong> the gap between the saber tips, about 17 cm (6.7 in), was similar to a tiger’s. Its jaws opened at a wider angle than a lion’s.</li><li><strong>The woman:</strong> she is 165 cm (5 ft 5 in) tall.</li></ul><p class="sm-vs-src">Sources for this comparison: <a href="https://pubmed.ncbi.nlm.nih.gov/16235255/" rel="noopener noreferrer">Christiansen and Harris, 2005, Journal of Morphology — body size of Smilodon</a> <a href="https://ielc.libguides.com/sdzg/factsheets/extinctsaber-toothedcat/characteristics" rel="noopener noreferrer">San Diego Zoo Wildlife Alliance Library — Extinct saber-toothed cat fact sheet</a> <a href="https://museum.state.il.us/exhibits/larson/smilodon.html" rel="noopener noreferrer">Illinois State Museum — Smilodon</a> <a href="https://anatomypubs.onlinelibrary.wiley.com/doi/10.1002/ar.25529" rel="noopener noreferrer">The Anatomical Record, 2024 — saber-tooth gape</a></p></section>',
    'fr': '<section class="sm-vs" id="smilodon-vs-you"><h2>Smilodon contre toi</h2><figure><picture><source type="image/webp" srcset="@@/assets/smilodon/smilodon-vs-woman-v4-800.webp 800w, @@/assets/smilodon/smilodon-vs-woman-v4-1400.webp 1400w" sizes="(max-width: 940px) 100vw, 900px"><img class="sm-vs-img" src="@@/assets/smilodon/smilodon-vs-woman-v4-1400.jpg" width="1400" height="1090" loading="lazy" decoding="async" alt="À l’échelle : la reconstitution de Smilodon fatalis, 100 cm au garrot et environ 175 cm de long plus une queue de 35 cm, à côté d’une femme de 165 cm. Le dos du félin arrive à peu près à la hanche de l’homme."></picture><figcaption>À l’échelle : la reconstitution de Smilodon fatalis, 100 cm au garrot et environ 175 cm de long plus une queue de 35 cm, à côté d’une femme de 165 cm. Le dos du félin arrive à peu près à la hanche de l’homme.<p class="sm-vs-credit">Créé par le Fondateur et SI. Smilodon: <a href="https://commons.wikimedia.org/wiki/File:Smilodon_fatalis_Sergiodlarosa_with_a_white_background.png" rel="noopener noreferrer">Sergio De La Rosa</a>, <a href="https://creativecommons.org/licenses/by-sa/3.0/" rel="noopener noreferrer">CC BY-SA 3.0</a>, via Wikimedia Commons. Femme : créée par le Fondateur et SI, avec sa permission. Image sous licence <a href="https://creativecommons.org/licenses/by-sa/3.0/" rel="noopener noreferrer">CC BY-SA 3.0</a>.</p></figcaption></figure><ul><li><strong>Poids :</strong> <em>S. fatalis</em> pesait environ 160 à 280 kg (350 à 620 lb), soit 2 à 3 hommes adultes. La plus grande espèce, <em>S. populator</em>, pesait environ 220 à 360 kg, jusqu’à environ 4 hommes.</li><li><strong>Hauteur :</strong> son dos arrivait à environ 100 cm au garrot, à peu près à la taille de la plupart des adultes.</li><li><strong>Longueur :</strong> du museau à la croupe, environ 175 cm, un peu plus que la taille de la femme de l’image (165 cm), plus une queue courte d’environ 35 cm.</li><li><strong>Dents :</strong> chaque dent en sabre mesurait jusqu’à 18 cm, à peu près la longueur d’un crayon.</li><li><strong>Morsure :</strong> l’écart entre les pointes des sabres, environ 17 cm, était proche de celui d’un tigre. Ses mâchoires s’ouvraient selon un angle plus large que celles d’un lion.</li><li><strong>La femme :</strong> elle mesure 165 cm.</li></ul><p class="sm-vs-src">Sources de cette comparaison: <a href="https://pubmed.ncbi.nlm.nih.gov/16235255/" rel="noopener noreferrer">Christiansen and Harris, 2005, Journal of Morphology — body size of Smilodon</a> <a href="https://ielc.libguides.com/sdzg/factsheets/extinctsaber-toothedcat/characteristics" rel="noopener noreferrer">San Diego Zoo Wildlife Alliance Library — Extinct saber-toothed cat fact sheet</a> <a href="https://museum.state.il.us/exhibits/larson/smilodon.html" rel="noopener noreferrer">Illinois State Museum — Smilodon</a> <a href="https://anatomypubs.onlinelibrary.wiley.com/doi/10.1002/ar.25529" rel="noopener noreferrer">The Anatomical Record, 2024 — saber-tooth gape</a></p></section>',
    'es': '<section class="sm-vs" lang="es" id="smilodon-vs-you"><h2>Smilodon contra ti</h2><figure><picture><source type="image/webp" srcset="@@/assets/smilodon/smilodon-vs-woman-v4-800.webp 800w, @@/assets/smilodon/smilodon-vs-woman-v4-1400.webp 1400w" sizes="(max-width: 940px) 100vw, 900px"><img class="sm-vs-img" src="@@/assets/smilodon/smilodon-vs-woman-v4-1400.jpg" width="1400" height="1090" loading="lazy" decoding="async" alt="A escala: la reconstrucción de Smilodon fatalis, de 100 cm de alto a la cruz y unos 175 cm de largo más una cola de 35 cm, junto a una mujer de 165 cm. La cruz del felino llega más o menos a la cintura de la mujer."></picture><figcaption>A escala: la reconstrucción de Smilodon fatalis, de 100 cm de alto a la cruz y unos 175 cm de largo más una cola de 35 cm, junto a una mujer de 165 cm. La cruz del felino llega más o menos a la cintura de la mujer.<p class="sm-vs-credit">Creado por el Fundador y SI. Smilodon: <a href="https://commons.wikimedia.org/wiki/File:Smilodon_fatalis_Sergiodlarosa_with_a_white_background.png" rel="noopener noreferrer">Sergio De La Rosa</a>, <a href="https://creativecommons.org/licenses/by-sa/3.0/" rel="noopener noreferrer">CC BY-SA 3.0</a>, vía Wikimedia Commons. Mujer: creada por el Fundador y SI, con su permiso. Imagen con licencia <a href="https://creativecommons.org/licenses/by-sa/3.0/" rel="noopener noreferrer">CC BY-SA 3.0</a>.</p></figcaption></figure><ul><li><strong>Peso:</strong> <em>S. fatalis</em> pesaba unos 160–280 kg (350–620 lb), como 2 o 3 hombres adultos. La especie más grande, <em>S. populator</em>, pesaba unos 220–360 kg, hasta unos 4 hombres.</li><li><strong>Altura:</strong> su lomo medía unos 100 cm a la cruz, más o menos hasta la cadera de un adulto.</li><li><strong>Largo:</strong> del hocico a la grupa medía unos 175 cm, un poco más de lo que mide la mujer de la imagen (165 cm), más una cola corta de unos 35 cm.</li><li><strong>Dientes:</strong> cada diente de sable medía hasta 18 cm, más o menos lo que mide un lápiz.</li><li><strong>Mordida:</strong> la separación entre las puntas de los sables, unos 17 cm, era parecida a la de un tigre. Sus mandíbulas se abrían con un ángulo más amplio que las de un león.</li><li><strong>La mujer:</strong> mide 165 cm.</li></ul><p class="sm-vs-src">Fuentes de esta comparación: <a href="https://pubmed.ncbi.nlm.nih.gov/16235255/" rel="noopener noreferrer">Christiansen and Harris, 2005, Journal of Morphology — body size of Smilodon</a> <a href="https://ielc.libguides.com/sdzg/factsheets/extinctsaber-toothedcat/characteristics" rel="noopener noreferrer">San Diego Zoo Wildlife Alliance Library — Extinct saber-toothed cat fact sheet</a> <a href="https://museum.state.il.us/exhibits/larson/smilodon.html" rel="noopener noreferrer">Illinois State Museum — Smilodon</a> <a href="https://anatomypubs.onlinelibrary.wiley.com/doi/10.1002/ar.25529" rel="noopener noreferrer">The Anatomical Record, 2024 — saber-tooth gape</a></p></section>',
    'ar': '<section class="sm-vs" lang="ar" id="smilodon-vs-you"><h2>سميلودون مقارنةً بك</h2><figure><picture><source type="image/webp" srcset="@@/assets/smilodon/smilodon-vs-woman-v4-800.webp 800w, @@/assets/smilodon/smilodon-vs-woman-v4-1400.webp 1400w" sizes="(max-width: 940px) 100vw, 900px"><img class="sm-vs-img" src="@@/assets/smilodon/smilodon-vs-woman-v4-1400.jpg" width="1400" height="1090" loading="lazy" decoding="async" alt="بمقياس حقيقي: إعادة تصوير سميلودون فاتاليس بارتفاع 100 سم عند الكتف وطول نحو 175 سم مع ذيل 35 سم، بجانب امرأة طولها 165 سم. يصل كتف القط تقريبًا إلى خصرها."></picture><figcaption>بمقياس حقيقي: إعادة تصوير سميلودون فاتاليس بارتفاع 100 سم عند الكتف وطول نحو 175 سم مع ذيل 35 سم، بجانب امرأة طولها 165 سم. يصل كتف القط تقريبًا إلى خصرها.<p class="sm-vs-credit">من إنشاء المؤسس وSI. سميلودون: <a href="https://commons.wikimedia.org/wiki/File:Smilodon_fatalis_Sergiodlarosa_with_a_white_background.png" rel="noopener noreferrer">Sergio De La Rosa</a>, <a href="https://creativecommons.org/licenses/by-sa/3.0/" rel="noopener noreferrer">CC BY-SA 3.0</a>, عبر ويكيميديا كومنز. المرأة: من إنشاء المؤسس وSI، وتُعرض بإذنها. الصورة مرخّصة بموجب <a href="https://creativecommons.org/licenses/by-sa/3.0/" rel="noopener noreferrer">CC BY-SA 3.0</a>.</p></figcaption></figure><ul><li><strong>الوزن:</strong> كان وزن <em>S. fatalis</em> نحو 160–280 كغ (350–620 رطلًا)، أي ما يعادل رجلين إلى ثلاثة رجال بالغين. أما أكبر الأنواع، <em>S. populator</em>، فكان وزنه نحو 220–360 كغ، أي ما يصل إلى نحو أربعة رجال.</li><li><strong>الارتفاع:</strong> كان ارتفاع ظهره نحو 100 سم عند الكتف، أي إلى مستوى الخصر لدى معظم البالغين تقريبًا.</li><li><strong>الطول:</strong> من الأنف إلى المؤخرة نحو 175 سم، أي أطول قليلًا من طول المرأة في الصورة (165 سم)، مع ذيل قصير طوله نحو 35 سم.</li><li><strong>الأسنان:</strong> كان طول كل ناب سيفي يصل إلى 18 سم، أي بطول قلم رصاص تقريبًا.</li><li><strong>العضة:</strong> كانت المسافة بين طرفي النابين نحو 17 سم، وهي قريبة من مسافة النمر. وكان فكّاه ينفتحان بزاوية أوسع من فكّي الأسد.</li><li><strong>المرأة:</strong> طولها 165 سم.</li></ul><p class="sm-vs-src">مصادر هذه المقارنة: <a href="https://pubmed.ncbi.nlm.nih.gov/16235255/" rel="noopener noreferrer">Christiansen and Harris, 2005, Journal of Morphology — body size of Smilodon</a> <a href="https://ielc.libguides.com/sdzg/factsheets/extinctsaber-toothedcat/characteristics" rel="noopener noreferrer">San Diego Zoo Wildlife Alliance Library — Extinct saber-toothed cat fact sheet</a> <a href="https://museum.state.il.us/exhibits/larson/smilodon.html" rel="noopener noreferrer">Illinois State Museum — Smilodon</a> <a href="https://anatomypubs.onlinelibrary.wiley.com/doi/10.1002/ar.25529" rel="noopener noreferrer">The Anatomical Record, 2024 — saber-tooth gape</a></p></section>',
    'it': '<section class="sm-vs" lang="it" id="smilodon-vs-you"><h2>Smilodon contro di te</h2><figure><picture><source type="image/webp" srcset="@@/assets/smilodon/smilodon-vs-woman-v4-800.webp 800w, @@/assets/smilodon/smilodon-vs-woman-v4-1400.webp 1400w" sizes="(max-width: 940px) 100vw, 900px"><img class="sm-vs-img" src="@@/assets/smilodon/smilodon-vs-woman-v4-1400.jpg" width="1400" height="1090" loading="lazy" decoding="async" alt="In scala: la ricostruzione di Smilodon fatalis, alta 100 cm al garrese e lunga circa 175 cm più una coda di 35 cm, accanto a una donna alta 165 cm. Il garrese del felino arriva circa alla sua vita."></picture><figcaption>In scala: la ricostruzione di Smilodon fatalis, alta 100 cm al garrese e lunga circa 175 cm più una coda di 35 cm, accanto a una donna alta 165 cm. Il garrese del felino arriva circa alla sua vita.<p class="sm-vs-credit">Creato dal Fondatore e da SI. Smilodon: <a href="https://commons.wikimedia.org/wiki/File:Smilodon_fatalis_Sergiodlarosa_with_a_white_background.png" rel="noopener noreferrer">Sergio De La Rosa</a>, <a href="https://creativecommons.org/licenses/by-sa/3.0/" rel="noopener noreferrer">CC BY-SA 3.0</a>, tramite Wikimedia Commons. Donna: creata dal Fondatore e SI, con il suo permesso. Immagine con licenza <a href="https://creativecommons.org/licenses/by-sa/3.0/" rel="noopener noreferrer">CC BY-SA 3.0</a>.</p></figcaption></figure><ul><li><strong>Peso:</strong> <em>S. fatalis</em> pesava circa 160–280 kg (350–620 lb), come 2 o 3 uomini adulti. La specie più grande, <em>S. populator</em>, pesava circa 220–360 kg, fino a circa 4 uomini.</li><li><strong>Altezza:</strong> la sua schiena arrivava a circa 100 cm al garrese, più o meno all’altezza della vita della maggior parte degli adulti.</li><li><strong>Lunghezza:</strong> dal muso alla groppa era lungo circa 175 cm, poco più dell’altezza della donna nell’immagine (165 cm), più una coda corta di circa 35 cm.</li><li><strong>Denti:</strong> ogni dente a sciabola era lungo fino a 18 cm, più o meno quanto una matita.</li><li><strong>Morso:</strong> la distanza tra le punte delle sciabole, circa 17 cm, era simile a quella di una tigre. Le sue mascelle si aprivano con un angolo più ampio di quelle di un leone.</li><li><strong>La donna:</strong> è alta 165 cm.</li></ul><p class="sm-vs-src">Fonti di questo confronto: <a href="https://pubmed.ncbi.nlm.nih.gov/16235255/" rel="noopener noreferrer">Christiansen and Harris, 2005, Journal of Morphology — body size of Smilodon</a> <a href="https://ielc.libguides.com/sdzg/factsheets/extinctsaber-toothedcat/characteristics" rel="noopener noreferrer">San Diego Zoo Wildlife Alliance Library — Extinct saber-toothed cat fact sheet</a> <a href="https://museum.state.il.us/exhibits/larson/smilodon.html" rel="noopener noreferrer">Illinois State Museum — Smilodon</a> <a href="https://anatomypubs.onlinelibrary.wiley.com/doi/10.1002/ar.25529" rel="noopener noreferrer">The Anatomical Record, 2024 — saber-tooth gape</a></p></section>',
    'he': '<section class="sm-vs" lang="he" id="smilodon-vs-you"><h2>סמילודון לעומתך</h2><figure><picture><source type="image/webp" srcset="@@/assets/smilodon/smilodon-vs-woman-v4-800.webp 800w, @@/assets/smilodon/smilodon-vs-woman-v4-1400.webp 1400w" sizes="(max-width: 940px) 100vw, 900px"><img class="sm-vs-img" src="@@/assets/smilodon/smilodon-vs-woman-v4-1400.jpg" width="1400" height="1090" loading="lazy" decoding="async" alt="בקנה מידה: שחזור של סמילודון פטליס בגובה 100 ס״מ בכתף ובאורך כ־175 ס״מ ועוד זנב של 35 ס״מ, ליד אישה בגובה 165 ס״מ. כתף החתול מגיעה בערך עד המותניים שלה."></picture><figcaption>בקנה מידה: שחזור של סמילודון פטליס בגובה 100 ס״מ בכתף ובאורך כ־175 ס״מ ועוד זנב של 35 ס״מ, ליד אישה בגובה 165 ס״מ. כתף החתול מגיעה בערך עד המותניים שלה.<p class="sm-vs-credit">נוצר על ידי המייסד ו־SI. סמילודון: <a href="https://commons.wikimedia.org/wiki/File:Smilodon_fatalis_Sergiodlarosa_with_a_white_background.png" rel="noopener noreferrer">Sergio De La Rosa</a>, <a href="https://creativecommons.org/licenses/by-sa/3.0/" rel="noopener noreferrer">CC BY-SA 3.0</a>, דרך ויקימדיה קומונס. אישה: נוצרה על ידי המייסד ו־SI, מוצגת באישורה. התמונה ברישיון <a href="https://creativecommons.org/licenses/by-sa/3.0/" rel="noopener noreferrer">CC BY-SA 3.0</a>.</p></figcaption></figure><ul><li><strong>משקל:</strong> <em>S. fatalis</em> שקל בערך 160–280 ק״ג (350–620 ליברות), כמו 2 עד 3 גברים בוגרים. המין הגדול ביותר, <em>S. populator</em>, שקל בערך 220–360 ק״ג, עד כ-4 גברים.</li><li><strong>גובה:</strong> הגב שלו הגיע לגובה של כ-100 ס״מ בכתף, בערך בגובה המותניים של רוב המבוגרים.</li><li><strong>אורך:</strong> מהאף ועד העכוז כ-175 ס״מ, קצת יותר מגובהה של האישה בתמונה (165 ס״מ), ועוד זנב קצר של כ-35 ס״מ.</li><li><strong>שיניים:</strong> כל שן חרב הייתה באורך של עד 18 ס״מ, בערך כמו עיפרון.</li><li><strong>נשיכה:</strong> המרחק בין קצות שיני החרב, כ-17 ס״מ, היה דומה לזה של נמר. הלסתות שלו נפתחו בזווית רחבה יותר מאלה של אריה.</li><li><strong>האישה:</strong> גובהה 165 ס״מ.</li></ul><p class="sm-vs-src">מקורות להשוואה זו: <a href="https://pubmed.ncbi.nlm.nih.gov/16235255/" rel="noopener noreferrer">Christiansen and Harris, 2005, Journal of Morphology — body size of Smilodon</a> <a href="https://ielc.libguides.com/sdzg/factsheets/extinctsaber-toothedcat/characteristics" rel="noopener noreferrer">San Diego Zoo Wildlife Alliance Library — Extinct saber-toothed cat fact sheet</a> <a href="https://museum.state.il.us/exhibits/larson/smilodon.html" rel="noopener noreferrer">Illinois State Museum — Smilodon</a> <a href="https://anatomypubs.onlinelibrary.wiley.com/doi/10.1002/ar.25529" rel="noopener noreferrer">The Anatomical Record, 2024 — saber-tooth gape</a></p></section>',
}


def _compare(lang, prefix):
    return COMPARE[lang].replace("@@/", prefix)

def page(lang, prefix=""):
    import seo_copy
    fr = lang=="fr"
    L = "fr" if fr else "en"
    note = "" if lang in ("en","fr") else '<p class="sm-note" role="note">TODO machine-draft translation: English for review.</p>'
    la = "" if lang in ("en","fr") else ' lang="en"'
    over = seo_copy.SMILODON.get(lang)
    if over:
        kicker, h1, lead = over["kicker"], over["h1"], over["lead"]
        alt = over["alt"]
        title, desc = over["title"], over["desc"]
    elif fr:
        kicker, h1, lead = "Un félin, pas un tigre", "Le chat à dents de sabre", "Smilodon est un chat. Ce n’est pas un tigre."
        alt = "Squelette monté de Smilodon fatalis dans une salle de musée, avec de longues canines supérieures."
        title, desc = "Le chat à dents de sabre (Smilodon)", "Un félin aux longues canines, pas un tigre. Ce que les fossiles montrent, et ce qui reste ouvert."
    else:
        kicker, h1, lead = "A cat, not a tiger", "Saber-toothed cat", "Smilodon is a cat. It is not a tiger."
        alt = "Mounted skeleton of Smilodon fatalis in a museum hall, with long upper canine teeth."
        title, desc = "Saber-toothed cat (Smilodon)", "A cat with long upper teeth, not a tiger. What the fossils show, and what is still open."
    aria = ("Animation : un squelette de Smilodon prend vie, devient le chat et rugit"
            if fr else
            "Animation: a Smilodon skeleton comes to life, turns into the cat, and roars")
    if fr:
        vcredit = ("Vidéo : <strong>créée par le fondateur et SI</strong>, à partir d’images de la Field Museum Library "
                   "(squelette, pas de droit d’auteur connu, via Wikimedia Commons) et de Sergio De La Rosa "
                   "(dessin, CC BY-SA 3.0, via Wikimedia Commons). La vidéo est partagée sous "
                   f'{_a(CC_BY_SA, "CC BY-SA 3.0")}. Le squelette qui prend vie est une animation, pas un enregistrement du mouvement d’un fossile. '
                   f'{_a(SKEL, "Page du squelette")} · {_a(DRAW, "Page du dessin")}')
    else:
        vcredit = ("Video: <strong>Created by the Founder and SI</strong>, from images by The Field Museum Library "
                   "(skeleton, no known copyright restrictions, via Wikimedia Commons) and Sergio De La Rosa "
                   "(life drawing, CC BY-SA 3.0, via Wikimedia Commons). The video is shared under "
                   f'{_a(CC_BY_SA, "CC BY-SA 3.0")}. The skeleton coming to life is an artist’s animation, not a fossil record of movement. '
                   f'{_a(SKEL, "Skeleton file page")} · {_a(DRAW, "Drawing file page")}')
    hero = (f'<section class="sm-hero"><video class="sm-hero-video" muted playsinline preload="none" '
            f'poster="{prefix}assets/smilodon/hero-video-poster.webp" width="1920" height="1080" '
            f'aria-label="{html.escape(aria)}" data-hd="{prefix}assets/smilodon/hero-1080.mp4" '
            f'data-sd="{prefix}assets/smilodon/hero-720.mp4"></video>'
            f'<script>(function(){{var v=document.currentScript.previousElementSibling;'
            f'if(matchMedia("(prefers-reduced-motion: reduce)").matches)return;'
            f'var big=matchMedia("(min-width: 1100px)").matches;var m=document.createElement("source");'
            f'm.type="video/mp4";m.src=big?v.dataset.hd:v.dataset.sd;v.appendChild(m);v.preload="auto";'
            f'v.autoplay=true;v.load();var p=v.play();if(p&&p.catch)p.catch(function(){{}});}})();</script>'
            f'<div class="sm-hero-shade" aria-hidden="true"></div><div class="sm-hero-copy">'
            f'<p class="sm-kicker">{kicker}</p><h1>{h1}</h1><p class="sm-lead">{lead}</p></div></section>')
    body = _french() if fr else _english()
    body = body.replace("<!--SMVS-->", _compare(lang, prefix))
    pins=[]
    for s in SITES:
        pins.append({"lat":s["lat"],"lng":s["lng"],"species":s["species"],"href":s["href"],"source":s["source"],"name":s["name"][L],"note":s["note"][L]})
    blob=json.dumps(pins, ensure_ascii=False).replace("<","\\u003c")
    aside_h = "Pas sur cette carte" if fr else "Not on this map"
    aside = (_aside_fr() if fr else _aside_en())
    main = f'''<main id="main">{hero}<div class="sm-wrap"{la}>{note}<p class="sm-vcredit">{vcredit}</p>{body}
<section><h2>{"Où sont les fossiles" if fr else "Where the fossils are"}</h2>
<p>{"Chaque épingle est un site cité. L’icône est un dessin de ce site, pas une photo." if fr else "Each pin is a cited site. The icon is a drawing made for this site, not a photograph."}</p>
<div class="sm-map-layout"><div id="sm-map" data-icon="{prefix}assets/smilodon/pin.svg" role="region" aria-label="{html.escape(h1)}"></div>
<aside class="sm-aside"><h3>{aside_h}</h3>{aside}</aside></div>
<script type="application/json" id="sm-sites">{blob}</script></section></div></main>'''
    return title, desc, main

def _english():
    return f'''
{_p(f'Smilodon is in the cat family, Felidae. The saber-toothed cats, Machairodontinae, are an extinct branch of that family. Tigers are a different branch: the living cat <em>Panthera tigris</em>. The nickname “saber-toothed tiger” is easy to say, and it is the wrong animal. The La Brea Tar Pits museum explains why the nickname stuck, and why the museum does not use it. {_a(TIGERS, "La Brea Tar Pits — Smilodon, saber-tooths, and tigers")}')}
<h2>Three species, one timeline</h2>
{_p(f'A 2025 tooth-wear study by Pardo-Judd and DeSantis treats three species as the current set, and it repeats the age and size ranges used in earlier work. {_a(DIET, "Pardo-Judd and DeSantis, 2025")}')}
<ul>
<li><strong><em>Smilodon gracilis</em></strong>, the earliest and the smallest: about 2.5 million to 500,000 years ago, and about 55–100 kg, near the size of a jaguar. In Florida, the same study used teeth from Leisey Shell Pit 1A and Inglis 1A.</li>
<li><strong><em>Smilodon fatalis</em></strong>: about 1.6 million to 10,000 years ago, and about 160–280 kg. This is the cat at La Brea, and the cat at the Talara tar seeps in Peru.</li>
<li><strong><em>Smilodon populator</em></strong>: about 1 million to 10,000 years ago, the largest, and it could pass 400 kg. It lived in South America east of the Andes. Peter Lund named it from caves at Lagoa Santa, Brazil.</li>
</ul>
{_p(f'Kurtén and Werdelin (1990) separate the large eastern South American form, <em>S. populator</em>, from the North American <em>S. fatalis</em>. They place the west coast of South America, Peru and Ecuador, with <em>S. fatalis</em>. {_a(KURTEN, "Kurtén and Werdelin, 1990")}')}
<!--SMVS-->
<h2>What we know</h2>
<ul>
<li>Asphalt at La Brea trapped Ice Age animals and preserved their bones. The Florida Museum of Natural History says more than 2,000 skulls of <em>S. fatalis</em> come from those pits. {_a(FLMNH, "Florida Museum species page")} {_a(TARPITS, "La Brea Tar Pits & Museum")}</li>
<li>The 2025 paper describes <em>S. fatalis</em> as an ambush hunter: heavy shoulders to hold prey larger than itself, and a bite weaker than the bite of cats that did not have saber teeth. That sentence is the paper’s summary of earlier studies, which it cites.</li>
<li>In that same study, tooth wear from Florida and tooth wear from La Brea were not distinguishable. The Florida cats and the La Brea cats seem to have used carcasses in a similar way.</li>
<li>At Talara, Peru, tar seeps trapped animals too. Seymour (2010) counted a minimum of 20 <em>S. fatalis</em> in a collection of more than 27,000 bones at the Royal Ontario Museum. Cruz, Lindsey, and others (2024) publish the map point used here and report dates of about 14,500 to 17,000 years before present for the Talara deposits. {_a(SEYMOUR, "Seymour, 2010")} {_a(TALARA, "Cruz, Lindsey, and others, 2024")}</li>
<li>In the Pampas of Buenos Aires Province, Argentina, <em>S. populator</em> was present around the last glacial maximum. {_a(PAMPA, "Bocherens and others, 2016")}</li>
</ul>
<h2>What we don’t know yet</h2>
<ul>
<li>Whether the huge La Brea sample stands for the species everywhere. The 2025 paper says that is still open, because most fossil sites preserve far fewer carnivores.</li>
<li>Whether these cats hunted in groups. The Florida Museum’s species page points to studies that do not agree. This page does not choose one of them.</li>
<li><em>S. gracilis</em> and <em>S. populator</em> are known from many fewer skeletons than La Brea’s <em>S. fatalis</em>. The 2025 study found the tooth wear of Florida <em>gracilis</em> and Florida <em>fatalis</em> indistinguishable. That went against the simple idea that the smaller species ate softer food.</li>
<li>Fur color and spots are not preserved on these bones. The La Brea essay says early paintings often left the coat plain, and later paintings often added spots. A painting is not a photograph.</li>
</ul>
<h2>Sources (10)</h2>
<ul>
<li>{_a(TIGERS, "La Brea Tar Pits — Smilodon, saber-tooths, and tigers")}</li>
<li>{_a(TARPITS, "La Brea Tar Pits & Museum")}</li>
<li>{_a(FLMNH, "Florida Museum of Natural History — Smilodon fatalis")}. The page lists Florida sites, including Sabertooth Cave and the Ichetucknee River, and it says the Florida records of this species are Rancholabrean. It also says the old name <em>Smilodon floridanus</em> was given to a skull found in 1888 near Ocala, now on display at the Wagner Free Institute of Science in Philadelphia.</li>
<li>{_a(DIET, "Pardo-Judd and DeSantis, 2025, The Anatomical Record")}. Dental wear of <em>S. gracilis</em> and <em>S. fatalis</em> in Florida, compared with La Brea.</li>
<li>{_a(KURTEN, "Kurtén and Werdelin, 1990, Journal of Vertebrate Paleontology")}</li>
<li>{_a(SEYMOUR, "Seymour, 2010, Talara and Corralito")}</li>
<li>{_a(TALARA, "Cruz, Lindsey, and others, 2024, Palaeogeography, Palaeoclimatology, Palaeoecology")}</li>
<li>{_a(PAMPA, "Bocherens and others, 2016, the Pampas")}</li>
<li>{_a(LAGOA, "Lagoa Santa — Peter Lund and the caves")}</li>
<li>{_a(SKEL, "Wikimedia Commons — the skeleton in the hero video")}</li>
</ul>'''

def _french():
    return f'''
{_p(f'Smilodon appartient à la famille des chats, les Félidés. Les chats à dents de sabre, les Machairodontinés, sont une branche éteinte de cette famille. Les tigres sont une autre branche : le chat vivant <em>Panthera tigris</em>. Le surnom « tigre à dents de sabre » est facile à dire, et c’est le mauvais animal. Le musée des puits de bitume de La Brea explique pourquoi ce surnom est resté, et pourquoi le musée ne l’emploie pas. {_a(TIGERS, "La Brea Tar Pits — Smilodon, dents de sabre et tigres")}')}
<h2>Trois espèces, une chronologie</h2>
{_p(f'Une étude de 2025 sur l’usure des dents, par Pardo-Judd et DeSantis, retient trois espèces et reprend les âges et les tailles utilisés dans des travaux plus anciens. {_a(DIET, "Pardo-Judd et DeSantis, 2025")}')}
<ul>
<li><strong><em>Smilodon gracilis</em></strong>, la plus ancienne et la plus petite : d’environ 2,5 millions à 500 000 ans, et environ 55 à 100 kg, proche de la taille d’un jaguar. En Floride, la même étude a utilisé des dents de Leisey Shell Pit 1A et d’Inglis 1A.</li>
<li><strong><em>Smilodon fatalis</em></strong> : d’environ 1,6 million à 10 000 ans, et environ 160 à 280 kg. C’est le chat de La Brea, et le chat des suintements de goudron de Talara, au Pérou.</li>
<li><strong><em>Smilodon populator</em></strong> : d’environ 1 million à 10 000 ans, la plus grande, et elle pouvait dépasser 400 kg. Elle vivait en Amérique du Sud, à l’est des Andes. Peter Lund l’a nommée à partir des grottes de Lagoa Santa, au Brésil.</li>
</ul>
{_p(f'Kurtén et Werdelin (1990) séparent la grande forme de l’est de l’Amérique du Sud, <em>S. populator</em>, du <em>S. fatalis</em> d’Amérique du Nord. Ils placent la côte ouest de l’Amérique du Sud, le Pérou et l’Équateur, avec <em>S. fatalis</em>. {_a(KURTEN, "Kurtén et Werdelin, 1990")}')}
<!--SMVS-->
<h2>Ce que l’on sait</h2>
<ul>
<li>Le bitume de La Brea a piégé des animaux de l’ère glaciaire et conservé leurs os. Le musée de Floride écrit que plus de 2 000 crânes de <em>S. fatalis</em> viennent de ces puits. {_a(FLMNH, "Page de l’espèce, musée de Floride")} {_a(TARPITS, "La Brea Tar Pits & Museum")}</li>
<li>L’article de 2025 décrit <em>S. fatalis</em> comme un chasseur à l’affût : des épaules lourdes pour retenir une proie plus grande que lui, et une morsure plus faible que celle des chats sans dents de sabre. Cette phrase est le résumé que l’article fait d’études plus anciennes, qu’il cite.</li>
<li>Dans la même étude, l’usure des dents de Floride et celle de La Brea ne se distinguaient pas. Les chats de Floride et ceux de La Brea semblent avoir utilisé les carcasses de la même façon.</li>
<li>À Talara, au Pérou, des suintements de goudron ont aussi piégé des animaux. Seymour (2010) a compté au minimum 20 <em>S. fatalis</em> dans une collection de plus de 27 000 os au Musée royal de l’Ontario. Cruz, Lindsey et d’autres (2024) publient le point utilisé sur cette carte et donnent environ 14 500 à 17 000 ans avant le présent pour les dépôts de Talara. {_a(SEYMOUR, "Seymour, 2010")} {_a(TALARA, "Cruz, Lindsey et autres, 2024")}</li>
<li>Dans la Pampa de la province de Buenos Aires, en Argentine, <em>S. populator</em> était présent autour du dernier maximum glaciaire. {_a(PAMPA, "Bocherens et autres, 2016")}</li>
</ul>
<h2>Ce que l’on ne sait pas encore</h2>
<ul>
<li>Si l’immense échantillon de La Brea vaut pour l’espèce partout. L’article de 2025 dit que la question reste ouverte, parce que la plupart des sites gardent beaucoup moins de carnivores.</li>
<li>Si ces chats chassaient en groupe. La page du musée de Floride renvoie à des études qui ne sont pas d’accord. Cette page n’en choisit aucune.</li>
<li><em>S. gracilis</em> et <em>S. populator</em> sont connus par beaucoup moins de squelettes que le <em>S. fatalis</em> de La Brea. L’étude de 2025 a trouvé la même usure dentaire pour le <em>gracilis</em> et le <em>fatalis</em> de Floride. Cela va contre l’idée simple que la plus petite espèce mangeait plus tendre.</li>
<li>La couleur du pelage et les taches ne sont pas conservées sur ces os. Le texte de La Brea dit que les anciennes peintures laissaient souvent le pelage uni, et que les peintures plus récentes ajoutent souvent des taches. Une peinture n’est pas une photographie.</li>
</ul>
<h2>Sources (10)</h2>
<ul>
<li>{_a(TIGERS, "La Brea Tar Pits — Smilodon, dents de sabre et tigres")}</li>
<li>{_a(TARPITS, "La Brea Tar Pits & Museum")}</li>
<li>{_a(FLMNH, "Musée d’histoire naturelle de Floride — Smilodon fatalis")}. La page liste les sites de Floride, dont Sabertooth Cave et la rivière Ichetucknee, et elle dit que les fossiles de Floride de cette espèce sont du Rancholabréen. Elle dit aussi que l’ancien nom <em>Smilodon floridanus</em> a été donné à un crâne trouvé en 1888 près d’Ocala, aujourd’hui exposé au Wagner Free Institute of Science à Philadelphie.</li>
<li>{_a(DIET, "Pardo-Judd et DeSantis, 2025, The Anatomical Record")}. Usure des dents de <em>S. gracilis</em> et de <em>S. fatalis</em> en Floride, comparée à La Brea.</li>
<li>{_a(KURTEN, "Kurtén et Werdelin, 1990, Journal of Vertebrate Paleontology")}</li>
<li>{_a(SEYMOUR, "Seymour, 2010, Talara et Corralito")}</li>
<li>{_a(TALARA, "Cruz, Lindsey et autres, 2024, Palaeogeography, Palaeoclimatology, Palaeoecology")}</li>
<li>{_a(PAMPA, "Bocherens et autres, 2016, la Pampa")}</li>
<li>{_a(LAGOA, "Lagoa Santa — Peter Lund et les grottes")}</li>
<li>{_a(SKEL, "Wikimedia Commons — le squelette de la vidéo")}</li>
</ul>'''

def _aside_en():
    return f'''<p>Florida has many separate records of <em>S. fatalis</em>, and some of <em>S. gracilis</em>. The Florida Museum lists them, including Sabertooth Cave in Citrus County and the Ichetucknee River. This map does not turn that list into one dot.</p>
<p>Buenos Aires Province has <em>S. populator</em> in the Pampas study linked above. That paper describes a region, so there is no cave pin.</p>
<p>No pin is placed in Uruguay. A coordinate and a specimen citation for one Uruguay site were not cleared for this page.</p>
<p><a href="World_Map.html?range=Smilodon">World Map</a></p>'''

def _aside_fr():
    return f'''<p>La Floride a de nombreux sites distincts de <em>S. fatalis</em>, et quelques-uns de <em>S. gracilis</em>. Le musée de Floride les liste, dont Sabertooth Cave dans le comté de Citrus et la rivière Ichetucknee. Cette carte n’en fait pas un seul point.</p>
<p>La province de Buenos Aires a du <em>S. populator</em> dans l’étude de la Pampa citée plus haut. Cet article décrit une région, donc il n’y a pas d’épingle de grotte.</p>
<p>Aucune épingle n’est placée en Uruguay. Un point GPS et une citation de spécimen pour un site d’Uruguay n’ont pas été validés pour cette page.</p>
<p><a href="World_Map.html?range=Smilodon">Carte du monde</a></p>'''
