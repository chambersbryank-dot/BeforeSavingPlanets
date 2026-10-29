# Deep-dive pages linked from Dig Quest hotspots. English first; i18n TODO.
SP="https://www.savingplanets.com/"
CR="Artist’s interpretation — SI render made for Before Saving Planets; science per cited sources (not a photo)."
DEEP={
"Continents":("Continents on the Move","Plate tectonics: how Pangaea broke apart, India built the Himalayas, and Africa is splitting today.","pangaea.webp","About 200 million years ago Pangaea begins to tear apart; a glowing rift will become the Atlantic Ocean.",[
 ("Earth’s skin is broken into plates","Earth’s outer shell (lithosphere) is broken into about a dozen large plates that move a few centimeters a year — about as fast as fingernails grow."),
 ("Pangaea breaks apart","The supercontinent Pangaea began breaking up about 200 million years ago. The South Atlantic opened in the Early Cretaceous, separating Africa and South America — which is why their coastlines fit like puzzle pieces."),
 ("India meets Asia: the Himalayas","India drifted north and collided with Asia about 40–50 million years ago. The crash pushed up the Himalayas and the Tibetan Plateau. Mount Everest sits on the Nepal–China (Tibet) border, and the range is still rising."),
 ("Africa is splitting now","The East African Rift is an active rift where the African Plate is slowly pulling apart into the Nubian and Somali plates. In Ethiopia’s Afar region, the Red Sea, Gulf of Aden and rift meet; one day a new ocean may form there.")],
 [("USGS — This Dynamic Earth","https://pubs.usgs.gov/gip/dynamic/dynamic.html"),("USGS — Historical perspective (Pangaea)","https://pubs.usgs.gov/gip/dynamic/historical.html"),("USGS — The Himalayas","https://pubs.usgs.gov/gip/dynamic/himalaya.html"),("NASA Earth Observatory — The Afar Triangle","https://earthobservatory.nasa.gov/images/91871/the-afar-triangle"),("Yale Peabody Museum — Mineralogy &amp; Meteoritics","https://peabody.yale.edu/explore/collections/mineralogy-meteoritics"),("Harvard Earth &amp; Planetary Sciences","https://eps.harvard.edu/")],
 ("Moving land shapes rivers and forests. See who protects them today.","River solutions",SP+"Rivers.html")),
"Oceans":("Oceans: Earth’s Blue Engine","How the first oceans formed and why they still run our planet.","early-ocean.webp","Early Earth ocean, around 3.8 billion years ago: steaming volcanic islands, a closer Moon, and microbial mats in the shallows.",[
 ("Water arrived early","A 4.4-billion-year-old zircon crystal from Western Australia suggests liquid water existed on Earth very early in its history."),
 ("Life began in the sea","The earliest life was microbial. Ocean microbes made oxygen by photosynthesis, leading to the Great Oxidation Event about 2.4 billion years ago."),
 ("Oceans today","The ocean covers about 71% of Earth’s surface and holds about 97% of Earth’s water. Its average depth is about 3,700 meters (12,100 feet)."),
 ("The deepest place","Challenger Deep in the Mariana Trench is the deepest known point: nearly 11,000 meters (about 36,000 feet).")],
 [("Wilde et al., Nature 409:175 (2001)","https://doi.org/10.1038/35051550"),("NOAA — How much of the ocean have we explored? / ocean percent","https://oceanservice.noaa.gov/facts/ocean-percent.html"),("NOAA — Where is all of the Earth’s water?","https://oceanservice.noaa.gov/facts/oceanwater.html"),("NOAA — How deep is the ocean?","https://oceanservice.noaa.gov/facts/oceandepth.html"),("NOAA — Deepest part of the ocean","https://oceanservice.noaa.gov/facts/deepest.html"),("Harvard Gazette — Knoll: layered ancient seas","https://news.harvard.edu/gazette/story/2003/07/australian-shale-tells-tale-of-layered-seas-2/")],
 ("The same oceans need help today: plastic, warming, overfishing.","Ocean solutions",SP+"Oceans.html")),
"Seas":("Seas: Where Oceans Meet Land","What makes a sea, and how the Mediterranean once dried out and refilled.","zanclean.webp","About 5.33 million years ago the Atlantic broke through at Gibraltar and refilled the dried-out Mediterranean (the Zanclean flood).",[
 ("Ocean or sea?","Seas are smaller than oceans and are usually found where the land and ocean meet, often partly enclosed by land."),
 ("The Mediterranean dried up","About 6 million years ago, during the Messinian Salinity Crisis, the Mediterranean was cut off from the Atlantic and largely evaporated, leaving thick salt layers."),
 ("…and refilled","About 5.33 million years ago, Atlantic water broke through at the Strait of Gibraltar and refilled the basin, possibly within a few years — the Zanclean flood."),
 ("A sea being born","The Red Sea is a young sea forming as Africa and Arabia pull apart — part of the same rift system as the East African Rift.")],
 [("NOAA — What’s the difference between an ocean and a sea?","https://oceanservice.noaa.gov/facts/oceanorsea.html"),("Garcia-Castellanos et al., Nature 462:778 (2009)","https://doi.org/10.1038/nature08555"),("NASA Earth Observatory — The Afar Triangle","https://earthobservatory.nasa.gov/images/91871/the-afar-triangle"),("USGS — This Dynamic Earth","https://pubs.usgs.gov/gip/dynamic/dynamic.html")],
 ("Seas and seagrass meadows are nurseries for life. See who restores them.","Seagrass solutions",SP+"Seagrass.html")),
"DeadSea":("The Dead Sea: Lowest Place on Land","A salty lake in a rift valley, shrinking fast.","deadsea.webp","The Dead Sea at dawn: salt crystals on the shore and the steep walls of the rift valley.",[
 ("Born from a fault","The Dead Sea sits in a basin along the Dead Sea Transform, a fault where the Arabian Plate slides past the African (Sinai) Plate. The pull-apart basin let the land sink."),
 ("Lowest land on Earth","Its shore is the lowest land elevation on Earth, more than 430 meters (1,400 feet) below sea level — and getting lower."),
 ("Almost ten times saltier","With about 34% salt, the water is nearly ten times saltier than the ocean, so people float easily and almost no plants or animals live in it — only hardy microbes."),
 ("Shrinking fast","The water level has fallen more than a meter per year in recent decades as river water is diverted and minerals are extracted. Satellites show the southern part split off into evaporation ponds.")],
 [("NASA Earth Observatory — The Dead Sea (satellite images)","https://earthobservatory.nasa.gov/images/77818/the-dead-sea"),("NASA Earth Observatory — The Dead Sea","https://earthobservatory.nasa.gov/images/40640/the-dead-sea"),("USGS — This Dynamic Earth (transform faults)","https://pubs.usgs.gov/gip/dynamic/dynamic.html")],
 ("Shrinking lakes can come back with smart water use. See lake solutions.","Lake solutions",SP+"Lakes.html")),
}
# which Quest layer gets which hotspot
HOT={0:["Continents"],2:["Oceans","Seas"],4:["Oceans"],5:["Continents"],6:["Seas","DeadSea"],7:["Seas","DeadSea","Continents"]}
