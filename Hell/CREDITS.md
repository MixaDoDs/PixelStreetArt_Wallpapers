# Hell — pixel hell for angelOS's demon

16-colour pixel-art wallpapers (1920×1080, and 1080×1920 for portrait screens) made from
public-domain paintings: cropped, reduced to 1/4, pushed into a hell palette with 4×4 Bayer
dithering and scaled back up without smoothing. angelOS puts them up while the demon rules
(Settings → Y2K → Angel or demon).

Seven of them share one hell palette (`tools/hell-pixelate.py`). The nine circles of angelOS's
hell have a pair each — a landscape and a portrait picture in the circle's own colours, made
the same way from Gustave Doré's engravings for Dante's *Inferno*, one scene of that circle
(`tools/circle-pixelate.py`: the 16 colours are sampled from the circle's palette in angelOS,
`story/circles.json`; the engravings' paper sinks into the circle's dark with a gamma).

| File | Painting | Source (Wikimedia Commons, public domain) |
|---|---|---|
| `hell-pandemonium.png` | John Martin, *Pandemonium*, 1841 | [John_Martin_-_Pandemonium_-_WGA14149.jpg](https://commons.wikimedia.org/wiki/File:John_Martin_-_Pandemonium_-_WGA14149.jpg) |
| `hell-fallen-city.png` | John Martin, c. 1841 | [John_Martin_002.jpg](https://commons.wikimedia.org/wiki/File:John_Martin_002.jpg) |
| `hell-great-day.png` | John Martin, *The Great Day of His Wrath*, c. 1851 | [John_Martin_-_The_Great_Day_of_His_Wrath_-_Google_Art_Project.jpg](https://commons.wikimedia.org/wiki/File:John_Martin_-_The_Great_Day_of_His_Wrath_-_Google_Art_Project.jpg) |
| `hell-ash-and-fire.png` | John Martin, *The Destruction of Pompeii and Herculaneum*, 1822 | [Destruction_of_Pompeii_and_Herculaneum.jpg](https://commons.wikimedia.org/wiki/File:Destruction_of_Pompeii_and_Herculaneum.jpg) |
| `hell-lucifer.png`, `hell-lucifer-portrait.png` | Gustave Doré, *Lucifer* (Inferno, canto 34), 1861 | [Dore_Lucifer.jpg](https://commons.wikimedia.org/wiki/File:Dore_Lucifer.jpg) |
| `hell-bosch-portrait.png` | Hieronymus Bosch, *The Garden of Earthly Delights*, hell panel, 1490–1510 | [Hieronymus_Bosch_-_The_Garden_of_Earthly_Delights_-_Hell.jpg](https://commons.wikimedia.org/wiki/File:Hieronymus_Bosch_-_The_Garden_of_Earthly_Delights_-_Hell.jpg) |

### The nine circles

| File | Circle | Engraving | Source (Wikimedia Commons, public domain) |
|---|---|---|---|
| `hell-limbo.png` | Лимб (Limbo) | Gustave Doré, *Canto IV — Limbo, the virtuous pagans*, Inferno, 1861 | [Gustave Doré - Dante Alighieri - Inferno - Plate 11 (Canto IV - Limbo, the Viruous Pagans).jpg](https://commons.wikimedia.org/wiki/File:Gustave_Dor%C3%A9_-_Dante_Alighieri_-_Inferno_-_Plate_11_(Canto_IV_-_Limbo,_the_Viruous_Pagans).jpg) |
| `hell-limbo-portrait.png` | Лимб (Limbo) | Gustave Doré, *Canto IV — Homer and the classical poets*, Inferno, 1861 | [DVinfernoHomerClassicPoets m.jpg](https://commons.wikimedia.org/wiki/File:DVinfernoHomerClassicPoets_m.jpg) |
| `hell-lust.png` | Похоть (Lust) | Gustave Doré, *Canto V — the hurricane of souls*, Inferno, 1861 | [Gustave Doré - Dante Alighieri - Inferno - Plate 14 (Canto V - The hurricane of souls).jpg](https://commons.wikimedia.org/wiki/File:Gustave_Dor%C3%A9_-_Dante_Alighieri_-_Inferno_-_Plate_14_(Canto_V_-_The_hurricane_of_souls).jpg) |
| `hell-lust-portrait.png` | Похоть (Lust) | Gustave Doré, *Canto V — Paolo and Francesca*, Inferno, 1861 | [DVinfernoPaoloFrancesca m.jpg](https://commons.wikimedia.org/wiki/File:DVinfernoPaoloFrancesca_m.jpg) |
| `hell-gluttony.png` | Чревоугодие (Gluttony) | Gustave Doré, *Canto VI — Cerberus*, Inferno, 1861 | [Inferno Canto 6 - Cerberus (148618330).jpg](https://commons.wikimedia.org/wiki/File:Inferno_Canto_6_-_Cerberus_(148618330).jpg) |
| `hell-gluttony-portrait.png` | Чревоугодие (Gluttony) | Gustave Doré, *Canto VI — Cerberus*, Inferno, 1861 | [Inferno Canto 6 - Cerberus (148618330).jpg](https://commons.wikimedia.org/wiki/File:Inferno_Canto_6_-_Cerberus_(148618330).jpg) |
| `hell-greed.png` | Жадность (Greed) | Gustave Doré, *Canto VII — the hoarders and wasters*, Inferno, 1861 | [Gustave Doré - Dante Alighieri - Inferno - Plate 22 (Canto VII - Hoarders and Wasters).jpg](https://commons.wikimedia.org/wiki/File:Gustave_Dor%C3%A9_-_Dante_Alighieri_-_Inferno_-_Plate_22_(Canto_VII_-_Hoarders_and_Wasters).jpg) |
| `hell-greed-portrait.png` | Жадность (Greed) | Gustave Doré, *Canto VII — the hoarders and wasters*, Inferno, 1861 | [Gustave Doré - Dante Alighieri - Inferno - Plate 22 (Canto VII - Hoarders and Wasters).jpg](https://commons.wikimedia.org/wiki/File:Gustave_Dor%C3%A9_-_Dante_Alighieri_-_Inferno_-_Plate_22_(Canto_VII_-_Hoarders_and_Wasters).jpg) |
| `hell-wrath.png` | Гнев (Wrath) | Gustave Doré, *Canto VII — Virgil shows the souls of the wrathful*, Inferno, 1861 | [DVinfernoVirgilShowSoulsOfWrathful m.jpg](https://commons.wikimedia.org/wiki/File:DVinfernoVirgilShowSoulsOfWrathful_m.jpg) |
| `hell-wrath-portrait.png` | Гнев (Wrath) | Gustave Doré, *Canto VIII — the ferry across the Styx*, Inferno, 1861 | [DVinfernoFerryAcrossTheStyx m.jpg](https://commons.wikimedia.org/wiki/File:DVinfernoFerryAcrossTheStyx_m.jpg) |
| `hell-heresy.png` | Ересь (Heresy) | Gustave Doré, *Canto IX — Megaera, Tisiphone and Alecto on the walls of Dis*, Inferno, 1861 | [DVinfernoMegaeraTisifphoneAlecto m.jpg](https://commons.wikimedia.org/wiki/File:DVinfernoMegaeraTisifphoneAlecto_m.jpg) |
| `hell-heresy-portrait.png` | Ересь (Heresy) | Gustave Doré, *Canto X — Farinata degli Uberti in his tomb*, Inferno, 1861 | [DVinfernoUbertiAddressesDante m.jpg](https://commons.wikimedia.org/wiki/File:DVinfernoUbertiAddressesDante_m.jpg) |
| `hell-violence.png` | Насилие (Violence) | Gustave Doré, *Canto XIV — the violent in the rain of fire*, Inferno, 1861 | [DVinfernoViolentInRainOfFire m.jpg](https://commons.wikimedia.org/wiki/File:DVinfernoViolentInRainOfFire_m.jpg) |
| `hell-violence-portrait.png` | Насилие (Violence) | Gustave Doré, *Canto XIII — the forest of the suicides*, Inferno, 1861 | [DVinfernoForestOfSuicides m.jpg](https://commons.wikimedia.org/wiki/File:DVinfernoForestOfSuicides_m.jpg) |
| `hell-fraud.png` | Обман (Fraud) | Gustave Doré, *Canto XXII — Ciampolo and the demon Alichino over the pitch*, Inferno, 1861 | [DVinfernoCiampoloDemonAlichino m.jpg](https://commons.wikimedia.org/wiki/File:DVinfernoCiampoloDemonAlichino_m.jpg) |
| `hell-fraud-portrait.png` | Обман (Fraud) | Gustave Doré, *Canto XXVI — the flaming spirits of the evil counsellors*, Inferno, 1861 | [DVinfernoFlamingSpiritsOfEvilCounsellors m.jpg](https://commons.wikimedia.org/wiki/File:DVinfernoFlamingSpiritsOfEvilCounsellors_m.jpg) |
| `hell-treachery.png` | Предательство (Treachery) | Gustave Doré, *Canto XXXIII — Ugolino gnawing Ruggieri's head*, Inferno, 1861 | [DVinfernoUgolinoGnawingHeadOfRuggieari m.jpg](https://commons.wikimedia.org/wiki/File:DVinfernoUgolinoGnawingHeadOfRuggieari_m.jpg) |
| `hell-treachery-portrait.png` | Предательство (Treachery) | Gustave Doré, *Canto XXXI — the giant Antaeus lowers Dante and Virgil to Cocytus*, Inferno, 1861 | [DVinfernoGiantAntaeusLoweringDanteAndVirgil m.jpg](https://commons.wikimedia.org/wiki/File:DVinfernoGiantAntaeusLoweringDanteAndVirgil_m.jpg) |

The paintings are in the public domain (their authors died more than 100 years ago — Doré in 1883);
the pixel versions are released the same way.
