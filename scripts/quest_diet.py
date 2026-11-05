# Diet lens and Dig Quest homes. Years are written out. No bare time acronym.

def _pack(h, lead, homes_h, homes_lead, carn, herb, omni, homes):
    return dict(h=h, lead=lead, homes_h=homes_h, homes_lead=homes_lead, carn=carn, herb=herb, omni=omni, homes=homes)

def _diet(h, p, land_h, land, sea_h, sea, air_h, air):
    return {"h":h,"p":p,"land_h":land_h,"land":land,"sea_h":sea_h,"sea":sea,"air_h":air_h,"air":air}

DIET = {}

DIET["en"] = _pack(
"Where each diet lived",
"Carnivore, herbivore, and omnivore are a second lens. They cut across land, sea, and air. High-interest dinosaurs, marine hunters, and flyers stay in front. The years are written out.",
"Stories that live on Dig Quest",
"These are long Earth stories. They are not the animal pins on the interest map.",
_diet("Carnivore","Hunters. Meat was the meal.",
"Land","Tyrannosaurus rex hunted in the Hell Creek rocks of east-central Montana in the last few million years before 66 million years ago. Gorgosaurus hunted at Dinosaur Provincial Park 75 to 77 million years ago. Allosaurus hunted at Dinosaur National Monument about 150 million years ago. Sickle-clawed raptors hunted in the Djadokhta rocks of southern Mongolia and in the Cloverly rocks of Montana and Wyoming. This map does not pin those raptor quarries. The movie animal is not those fossils.",
"Sea","Dunkleosteus hunted in the seas of the Cleveland Shale, Ohio, about 360 million years ago. Ichthyosaurus at Lyme Regis falls in bins from 205.7 to 174.7 million years ago on this site’s scale. Mosasaurus runs from 83.6 million years ago through the late Maastrichtian, and not past the end of the Cretaceous. Basilosaurus hunted at Wadi Al-Hitan, Egypt, 40 to 37 million years ago.",
"Air","Archaeopteryx and Pterodactylus lived in the Solnhofen lagoons of Bavaria about 150 million years ago. The Pterodactylus type is 149.2 to 143.1 million years ago, and it is not Archaeopteryx. Sinosauropteryx, a feathered hunter, lived in the Jehol rocks of Liaoning about 125 million years ago."),
_diet("Herbivore","Plant-eaters. Not hunters.",
"Land","Stegosaurus and the long-necked plant-eaters at Dinosaur National Monument lived in the Morrison Formation about 150 million years ago. Centrosaurus lived at Dinosaur Provincial Park 75 to 77 million years ago. Triceratops lived in Hell Creek rocks at the end of the Cretaceous. Borealopelta lived in Alberta in the Early Cretaceous. Nigersaurus lived in Niger in the Early Cretaceous.",
"Sea","This map does not pin a plant-eating swimmer. The sea pins in the top lanes are hunters.",
"Air","This map does not pin a plant-eating flyer. The air pins are hunters with feathers or wing fingers."),
_diet("Omnivore","Mixed eaters. Plants and meat.",
"Land","Ornithomimids at Dinosaur Provincial Park ate a mixed diet 75 to 77 million years ago. They are not the Gorgosaurus skeleton on that coin. Our species at Jebel Irhoud, Morocco, about 300,000 years ago, ate both.",
"Sea","No sea pin on this map is labeled an omnivore.",
"Air","No air pin on this map is labeled an omnivore. Some early birds are still argued over. This page does not pick a stomach for them."),
[
("Deep Earth and first life","Jack Hills zircons, stromatolites, and the Ediacara and Mistaken Point animals sit here, from 4.54 billion years ago to 539 million years ago. They are the Precambrian on this page, not a cluster of animal-diet pins."),
("First forests and stone trees","Rhynie, Gilboa, Joggins, the petrified logs of Arizona, and the Glossopteris forests are stone forests. Their lesson is the trees."),
("Golden spikes","Meishan in China marks the end-Permian boundary, 251.9 million years ago on this site’s scale. Kuhjoch in Austria marks the Triassic–Jurassic boundary, about 201.4 million years ago. The village photo at Kuhjoch is not the spike."),
("Long coasts and landscapes","The Jurassic Coast and the Dolomites are long landscape stories. Ichthyosaurus from Lyme Regis still appears with the marine hunters. The coast itself is the lesson here."),
])

DIET["fr"] = _pack(
"Où vivait chaque régime",
"Carnivore, herbivore et omnivore sont une seconde loupe. Ils traversent la terre, la mer et l’air. Les dinosaures, les chasseurs marins et les animaux volants restent devant. Les années sont écrites en toutes lettres.",
"Récits qui vivent sur Dig Quest",
"Ce sont de longues histoires de la Terre. Ce ne sont pas les repères d’animaux de la carte d’intérêt.",
_diet("Carnivore","Des chasseurs. Le repas était la viande.",
"Terre","Tyrannosaurus rex chassait dans les roches de Hell Creek, dans le centre-est du Montana, dans les derniers millions d’années avant 66 millions d’années. Gorgosaurus chassait à Dinosaur Provincial Park il y a 75 à 77 millions d’années. Allosaurus chassait à Dinosaur National Monument il y a environ 150 millions d’années. Les raptors à griffe en faucille chassaient dans les roches du Djadokhta, dans le sud de la Mongolie, et dans les roches de Cloverly, au Montana et au Wyoming. Cette carte n’épingle pas ces carrières. L’animal du film n’est pas ces fossiles.",
"Mer","Dunkleosteus chassait dans les mers du schiste de Cleveland, dans l’Ohio, il y a environ 360 millions d’années. Ichthyosaurus à Lyme Regis tombe dans des bacs de 205,7 à 174,7 millions d’années sur l’échelle de ce site. Mosasaurus va de 83,6 millions d’années jusqu’au Maastrichtien tardif, et pas au-delà de la fin du Crétacé. Basilosaurus chassait à Wadi Al-Hitan, en Égypte, il y a 40 à 37 millions d’années.",
"Air","Archaeopteryx et Pterodactylus vivaient dans les lagons de Solnhofen, en Bavière, il y a environ 150 millions d’années. Le type de Pterodactylus a 149,2 à 143,1 millions d’années, et ce n’est pas Archaeopteryx. Sinosauropteryx, un chasseur à plumes, vivait dans les roches du Jehol, au Liaoning, il y a environ 125 millions d’années."),
_diet("Herbivore","Mangeurs de plantes. Pas des chasseurs.",
"Terre","Stegosaurus et les mangeurs de plantes à long cou de Dinosaur National Monument vivaient dans la formation de Morrison il y a environ 150 millions d’années. Centrosaurus vivait à Dinosaur Provincial Park il y a 75 à 77 millions d’années. Triceratops vivait dans les roches de Hell Creek à la fin du Crétacé. Borealopelta vivait en Alberta au Crétacé précoce. Nigersaurus vivait au Niger au Crétacé précoce.",
"Mer","Cette carte n’épingle pas un nageur mangeur de plantes. Les repères marins des voies principales sont des chasseurs.",
"Air","Cette carte n’épingle pas un animal volant qui mangeait des plantes. Les repères aériens sont des chasseurs à plumes ou à doigts d’aile."),
_diet("Omnivore","Mangeurs mixtes. Plantes et viande.",
"Terre","Les ornithomimidés de Dinosaur Provincial Park avaient un régime mixte il y a 75 à 77 millions d’années. Ce n’est pas le squelette de Gorgosaurus de cette pièce. Notre espèce à Jebel Irhoud, au Maroc, il y a environ 300 000 ans, mangeait les deux.",
"Mer","Aucun repère marin de cette carte n’est étiqueté omnivore.",
"Air","Aucun repère aérien de cette carte n’est étiqueté omnivore. Certains oiseaux anciens se discutent encore. Cette page ne choisit pas un estomac pour eux."),
[
("Terre profonde et première vie","Les zircons des Jack Hills, les stromatolites, et les animaux d’Ediacara et de Mistaken Point sont ici, de 4,54 milliards d’années à 539 millions d’années. C’est le Précambrien de cette page, pas un groupe de régimes."),
("Premières forêts et arbres de pierre","Rhynie, Gilboa, Joggins, les troncs pétrifiés d’Arizona et les forêts de Glossopteris sont des forêts de pierre. La leçon, ce sont les arbres."),
("Clous d’or","Meishan, en Chine, marque la limite de la fin du Permien, il y a 251,9 millions d’années sur l’échelle de ce site. Kuhjoch, en Autriche, marque la limite Trias–Jurassique, il y a environ 201,4 millions d’années. La photo du village à Kuhjoch n’est pas le clou."),
("Longues côtes et paysages","La côte jurassique et les Dolomites sont de longues histoires de paysage. Ichthyosaurus de Lyme Regis reste avec les chasseurs marins. Ici, la leçon est la côte elle-même."),
])

DIET["es"] = _pack(
"Dónde vivió cada dieta",
"Carnívoro, herbívoro y omnívoro son una segunda lente. Cruzan la tierra, el mar y el aire. Los dinosaurios, los cazadores marinos y los animales que vuelan siguen delante. Los años se escriben con palabras.",
"Historias que viven en Dig Quest",
"Son historias largas de la Tierra. No son las marcas de animales del mapa de interés.",
_diet("Carnívoro","Cazadores. La comida era carne.",
"Tierra","Tyrannosaurus rex cazaba en las rocas de Hell Creek, en el centro-este de Montana, en los últimos millones de años antes de hace 66 millones de años. Gorgosaurus cazaba en Dinosaur Provincial Park hace 75 a 77 millones de años. Allosaurus cazaba en Dinosaur National Monument hace unos 150 millones de años. Los raptores de garra en hoz cazaban en las rocas de Djadokhta, en el sur de Mongolia, y en las rocas de Cloverly, en Montana y Wyoming. Este mapa no clava esas canteras. El animal de la película no es esos fósiles.",
"Mar","Dunkleosteus cazaba en los mares de la lutita de Cleveland, Ohio, hace unos 360 millones de años. Ichthyosaurus en Lyme Regis cae en intervalos de hace 205,7 a 174,7 millones de años en la escala de este sitio. Mosasaurus va desde hace 83,6 millones de años hasta el Maastrichtiense tardío, y no más allá del fin del Cretácico. Basilosaurus cazaba en Wadi Al-Hitan, Egipto, hace 40 a 37 millones de años.",
"Aire","Archaeopteryx y Pterodactylus vivían en las lagunas de Solnhofen, en Baviera, hace unos 150 millones de años. El tipo de Pterodactylus es de hace 149,2 a 143,1 millones de años, y no es Archaeopteryx. Sinosauropteryx, un cazador con plumas, vivía en las rocas de Jehol, en Liaoning, hace unos 125 millones de años."),
_diet("Herbívoro","Comedores de plantas. No cazadores.",
"Tierra","Stegosaurus y los comedores de plantas de cuello largo en Dinosaur National Monument vivían en la Formación Morrison hace unos 150 millones de años. Centrosaurus vivía en Dinosaur Provincial Park hace 75 a 77 millones de años. Triceratops vivía en las rocas de Hell Creek al final del Cretácico. Borealopelta vivía en Alberta en el Cretácico temprano. Nigersaurus vivía en Níger en el Cretácico temprano.",
"Mar","Este mapa no marca un nadador que comiera plantas. Las marcas de mar de las vías principales son cazadores.",
"Aire","Este mapa no marca un volador que comiera plantas. Las marcas de aire son cazadores con plumas o dedos de ala."),
_diet("Omnívoro","Comedores mixtos. Plantas y carne.",
"Tierra","Los ornitomímidos de Dinosaur Provincial Park tenían una dieta mixta hace 75 a 77 millones de años. No son el esqueleto de Gorgosaurus de esa ficha. Nuestra especie en Jebel Irhoud, Marruecos, hace unos 300.000 años, comía las dos cosas.",
"Mar","Ninguna marca de mar en este mapa se etiqueta como omnívora.",
"Aire","Ninguna marca de aire en este mapa se etiqueta como omnívora. Algunas aves antiguas siguen en debate. Esta página no elige un estómago para ellas."),
[
("Tierra profunda y primera vida","Los zircones de Jack Hills, los estromatolitos y los animales de Ediacara y Mistaken Point están aquí, desde hace 4.540 millones de años hasta hace 539 millones de años. Son el Precámbrico de esta página, no un grupo de dietas."),
("Primeros bosques y árboles de piedra","Rhynie, Gilboa, Joggins, los troncos petrificados de Arizona y los bosques de Glossopteris son bosques de piedra. La lección son los árboles."),
("Clavos de oro","Meishan, en China, marca el límite del final del Pérmico, hace 251,9 millones de años en la escala de este sitio. Kuhjoch, en Austria, marca el límite Triásico–Jurásico, hace unos 201,4 millones de años. La foto del pueblo en Kuhjoch no es el clavo."),
("Costas largas y paisajes","La costa jurásica y los Dolomitas son historias largas de paisaje. Ichthyosaurus de Lyme Regis sigue con los cazadores marinos. Aquí la lección es la costa."),
])

DIET["it"] = _pack(
"Dove viveva ogni dieta",
"Carnivoro, erbivoro e onnivoro sono una seconda lente. Attraversano terra, mare e aria. Dinosauri, cacciatori marini e animali volanti restano davanti. Gli anni sono scritti in parole.",
"Storie che vivono su Dig Quest",
"Sono storie lunghe della Terra. Non sono i segnaposto degli animali sulla mappa di interesse.",
_diet("Carnivoro","Cacciatori. Il pasto era carne.",
"Terra","Tyrannosaurus rex cacciava nelle rocce di Hell Creek, nel Montana centro-orientale, negli ultimi milioni di anni prima di 66 milioni di anni fa. Gorgosaurus cacciava a Dinosaur Provincial Park da 75 a 77 milioni di anni fa. Allosaurus cacciava a Dinosaur National Monument circa 150 milioni di anni fa. I raptor con l’artiglio a falce cacciavano nelle rocce del Djadokhta, nel sud della Mongolia, e nelle rocce di Cloverly, in Montana e Wyoming. Questa mappa non punta quelle cave. L’animale del film non è quei fossili.",
"Mare","Dunkleosteus cacciava nei mari dello scisto di Cleveland, in Ohio, circa 360 milioni di anni fa. Ichthyosaurus a Lyme Regis cade in intervalli da 205,7 a 174,7 milioni di anni fa sulla scala di questo sito. Mosasaurus va da 83,6 milioni di anni fa fino al Maastrichtiano tardo, e non oltre la fine del Cretaceo. Basilosaurus cacciava a Wadi Al-Hitan, in Egitto, da 40 a 37 milioni di anni fa.",
"Aria","Archaeopteryx e Pterodactylus vivevano nelle lagune di Solnhofen, in Baviera, circa 150 milioni di anni fa. Il tipo di Pterodactylus è da 149,2 a 143,1 milioni di anni fa, e non è Archaeopteryx. Sinosauropteryx, un cacciatore piumato, viveva nelle rocce di Jehol, nel Liaoning, circa 125 milioni di anni fa."),
_diet("Erbivoro","Mangiatori di piante. Non cacciatori.",
"Terra","Stegosaurus e i mangiatori di piante dal collo lungo a Dinosaur National Monument vivevano nella Formazione Morrison circa 150 milioni di anni fa. Centrosaurus viveva a Dinosaur Provincial Park da 75 a 77 milioni di anni fa. Triceratops viveva nelle rocce di Hell Creek alla fine del Cretaceo. Borealopelta viveva in Alberta nel Cretaceo inferiore. Nigersaurus viveva in Niger nel Cretaceo inferiore.",
"Mare","Questa mappa non segna un nuotatore che mangiava piante. I segnaposto di mare delle corsie principali sono cacciatori.",
"Aria","Questa mappa non segna un volatore che mangiava piante. I segnaposto d’aria sono cacciatori con piume o dita alari."),
_diet("Onnivoro","Mangiatori misti. Piante e carne.",
"Terra","Gli ornitomimidi di Dinosaur Provincial Park avevano una dieta mista da 75 a 77 milioni di anni fa. Non sono lo scheletro di Gorgosaurus di quella scheda. La nostra specie a Jebel Irhoud, in Marocco, circa 300.000 anni fa, mangiava entrambi.",
"Mare","Nessun segnaposto di mare su questa mappa è etichettato onnivoro.",
"Aria","Nessun segnaposto d’aria su questa mappa è etichettato onnivoro. Alcuni uccelli antichi sono ancora discussi. Questa pagina non sceglie uno stomaco per loro."),
[
("Terra profonda e prima vita","Gli zirconi delle Jack Hills, le stromatoliti e gli animali di Ediacara e Mistaken Point stanno qui, da 4,54 miliardi di anni fa a 539 milioni di anni fa. Sono il Precambriano di questa pagina, non un gruppo di diete."),
("Prime foreste e alberi di pietra","Rhynie, Gilboa, Joggins, i tronchi pietrificati dell’Arizona e le foreste di Glossopteris sono foreste di pietra. La lezione sono gli alberi."),
("Chiodi d’oro","Meishan, in Cina, segna il limite della fine del Permiano, 251,9 milioni di anni fa sulla scala di questo sito. Kuhjoch, in Austria, segna il limite Triassico–Giurassico, circa 201,4 milioni di anni fa. La foto del villaggio a Kuhjoch non è il chiodo."),
("Coste lunghe e paesaggi","La costa giurassica e le Dolomiti sono storie lunghe di paesaggio. Ichthyosaurus di Lyme Regis resta con i cacciatori marini. Qui la lezione è la costa."),
])

DIET["ar"] = _pack(
"أين عاش كل غذاء",
"اللاحم والعاشب والقارِت عدسة ثانية. تعبر البر والبحر والهواء. تبقى الديناصورات وصيادو البحر والكائنات الطائرة في المقدمة. السنوات مكتوبة بالكلمات.",
"قصص تعيش في Dig Quest",
"هذه قصص طويلة عن الأرض. ليست دبابيس الحيوانات على خريطة الاهتمام.",
_diet("لاحم","صيادون. الوجبة كانت لحمًا.",
"البر","اصطاد تيرانوصور ركس في صخور هيل كريك في شرق وسط مونتانا في آخر ملايين السنين قبل 66 مليون سنة. اصطاد غورغوصور في منتزه الديناصورات قبل 75 إلى 77 مليون سنة. اصطاد ألوصور في نصب الديناصور قبل نحو 150 مليون سنة. اصطادت الرابتورات ذات المخلب المنجلي في صخور جادوختا في جنوب منغوليا وفي صخور كلوفرلي في مونتانا ووايومنغ. هذه الخريطة لا تضع دبوسًا على تلك المحاجر. حيوان الفيلم ليس هذه الأحافير.",
"البحر","اصطاد دنكليوستيوس في بحار طَفَل كليفلاند في أوهايو قبل نحو 360 مليون سنة. يقع إكثيوصور في لايم ريجيس في فترات من 205.7 إلى 174.7 مليون سنة على مقياس هذا الموقع. يمتد موزاصور من 83.6 مليون سنة حتى الماستريختي المتأخر، وليس بعد نهاية الطباشيري. اصطاد باسيلوصور في وادي الحيتان بمصر قبل 40 إلى 37 مليون سنة.",
"الهواء","عاش أركيوبتركس وبتروداكتيلوس في بحيرات سولنهوفن في بافاريا قبل نحو 150 مليون سنة. نوع بتروداكتيلوس من 149.2 إلى 143.1 مليون سنة، وهو ليس أركيوبتركس. عاش سينوصوروبتركس، وهو صياد ذو ريش، في صخور جيهول في لياونينغ قبل نحو 125 مليون سنة."),
_diet("عاشب","آكلات النبات. ليست صيادين.",
"البر","عاش ستيغوصور وآكلات النبات ذات الرقبة الطويلة في نصب الديناصور في تكوين موريسون قبل نحو 150 مليون سنة. عاش سنتوصور في منتزه الديناصورات قبل 75 إلى 77 مليون سنة. عاش تريسيراتوبس في صخور هيل كريك في نهاية الطباشيري. عاش بوريالوبلتا في ألبرتا في الطباشيري المبكر. عاش نيجرصور في النيجر في الطباشيري المبكر.",
"البحر","هذه الخريطة لا تضع دبوسًا على سبّاح يأكل النبات. دبابيس البحر في المسارات الأولى صيادون.",
"الهواء","هذه الخريطة لا تضع دبوسًا على طائر يأكل النبات. دبابيس الهواء صيادون بريش أو بأصابع جناح."),
_diet("قارِت","آكلات مختلطة. نبات ولحم.",
"البر","كان للأورنيثوميميات في منتزه الديناصورات غذاء مختلط قبل 75 إلى 77 مليون سنة. ليست هيكل غورغوصور في تلك البطاقة. نوعنا في جبل إيغود بالمغرب، قبل نحو 300,000 سنة، أكل الاثنين.",
"البحر","لا دبوس بحري في هذه الخريطة مُسمّى قارِتًا.",
"الهواء","لا دبوس هوائي في هذه الخريطة مُسمّى قارِتًا. بعض الطيور المبكرة ما زالت موضع نقاش. هذه الصفحة لا تختار معدة لها."),
[
("الأرض العميقة والحياة الأولى","زركون جاك هيلز والستروماتوليت وحيوانات إيدياكارا وميستيكن بوينت هنا، من 4.54 مليار سنة إلى 539 مليون سنة. هذا هو ما قبل الكمبري في هذه الصفحة، وليس مجموعة غذاء."),
("الغابات الأولى وأشجار الحجر","رايني وغيلبوا وجوغينز وجذوع أريزونا المتحجرة وغابات غلوسوبتريس غابات من حجر. الدرس هو الأشجار."),
("المسامير الذهبية","ميشان في الصين تعلّم حد نهاية البرمي، قبل 251.9 مليون سنة على مقياس هذا الموقع. كوهيوخ في النمسا تعلّم حد الترياسي والجوراسي، قبل نحو 201.4 مليون سنة. صورة القرية في كوهيوخ ليست المسمار."),
("سواحل طويلة ومشاهد","ساحل الجوراسي والدولوميت قصص مشهد طويلة. يبقى إكثيوصور لايم ريجيس مع صيادي البحر. هنا الدرس هو الساحل نفسه."),
])

DIET["he"] = _pack(
"איפה חיה כל תזונה",
"טורף, אוכל-צמחים ואוכל-כול הם עדשה שנייה. הם חוצים יבשה, ים ואוויר. דינוזאורים, ציידים ימיים ובעלי חיים מעופפים נשארים מקדימה. השנים כתובות במילים.",
"סיפורים שחיים ב-Dig Quest",
"אלה סיפורי ארץ ארוכים. הם לא נעצי החיות במפת העניין.",
_diet("טורף","ציידים. הארוחה הייתה בשר.",
"יבשה","טירנוזאורוס רקס צד בסלעי הל קריק במזרח-מרכז מונטנה במיליוני השנים האחרונות לפני 66 מיליון שנים. גורגוזאורוס צד בפארק הדינוזאורים לפני 75 עד 77 מיליון שנים. אלוזאורוס צד באנדרטת הדינוזאור לפני כ-150 מיליון שנים. רפטורים עם טופר מגל צדו בסלעי הג׳דוחטה בדרום מונגוליה ובסלעי קלוברלי במונטנה ובוויומינג. המפה הזו לא נועצת את המחצבות האלה. חיה מהסרט אינה המאובנים האלה.",
"ים","דנקליאוסטיוס צד בימי פצלי קליבלנד באוהיו לפני כ-360 מיליון שנים. איכתיוזאורוס בליים רג׳יס נופל בטווחים של 205.7 עד 174.7 מיליון שנים בסולם של האתר. מוזאזאורוס נמשך מ-83.6 מיליון שנים עד המאסטריכט המאוחר, ולא מעבר לסוף הקרטיקון. בזילוזאורוס צד בוואדי אל-חיתאן במצרים לפני 40 עד 37 מיליון שנים.",
"אוויר","ארכאופטריקס ופטרודקטילוס חיו בלגונות זולנהופן בבוואריה לפני כ-150 מיליון שנים. הטיפוס של פטרודקטילוס הוא מ-149.2 עד 143.1 מיליון שנים, והוא אינו ארכאופטריקס. סינוזאורופטריקס, צייד עם נוצות, חי בסלעי ג׳הול בליאונינג לפני כ-125 מיליון שנים."),
_diet("אוכל-צמחים","אוכלי צמחים. לא ציידים.",
"יבשה","סטגוזאורוס ואוכלי הצמחים ארוכי-הצוואר באנדרטת הדינוזאור חיו בתצורת מוריסון לפני כ-150 מיליון שנים. צנטרוזאורוס חי בפארק הדינוזאורים לפני 75 עד 77 מיליון שנים. טריצרטופס חי בסלעי הל קריק בסוף הקרטיקון. בוריאלפלטה חי באלברטה בקרטיקון הקדום. ניגרזאורוס חי בניז׳ר בקרטיקון הקדום.",
"ים","המפה הזו לא נועצת שוחה שאכל צמחים. נעצי הים במסלולים הראשיים הם ציידים.",
"אוויר","המפה הזו לא נועצת מעופף שאכל צמחים. נעצי האוויר הם ציידים עם נוצות או אצבעות כנף."),
_diet("אוכל-כול","אוכלים מעורבים. צמחים ובשר.",
"יבשה","לאורניתּומימידים בפארק הדינוזאורים היה תפריט מעורב לפני 75 עד 77 מיליון שנים. הם אינם שלד הגורגוזאורוס בכרטיס ההוא. המין שלנו בג׳בל אירחוד במרוקו, לפני כ-300,000 שנים, אכל גם וגם.",
"ים","אין נעץ ים במפה הזו שמסומן כאוכל-כול.",
"אוויר","אין נעץ אוויר במפה הזו שמסומן כאוכל-כול. כמה עופות קדומים עדיין שנויים במחלוקת. הדף הזה לא בוחר קיבה בשבילם."),
[
("ארץ עמוקה והחיים הראשונים","הזירקונים של ג׳ק הילס, הסטרומטוליטים ובעלי החיים של אדיאקרה ומיסטייקן פוינט נמצאים כאן, מ-4.54 מיליארד שנים עד 539 מיליון שנים. זה הפרקמבריון של הדף, לא קבוצת תפריט."),
("היערות הראשונים ועצי אבן","רייני, גילבואה, ג׳וגינס, גזעי אריזונה המאובנים ויערות גלוסופטריס הם יערות אבן. השיעור הוא העצים."),
("מסמרי זהב","מיישאן בסין מסמנת את גבול סוף הפרם, לפני 251.9 מיליון שנים בסולם של האתר. קוהיוך באוסטריה מסמנת את גבול הטריאס–יורה, לפני כ-201.4 מיליון שנים. תמונת הכפר בקוהיוך אינה המסמר."),
("חופים ארוכים ונופים","חוף היורה והדולומיטים הם סיפורי נוף ארוכים. איכתיוזאורוס מליים רג׳יס נשאר עם הציידים הימיים. כאן השיעור הוא החוף עצמו."),
])
