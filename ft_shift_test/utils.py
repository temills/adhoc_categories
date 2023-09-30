import json
import string

#adapted from preprocessing script in wctm repo
def code_response(cat, res):
    res = res.lower().strip().translate(str.maketrans('', '', string.punctuation))
    with open('../wctm_data/study3/ratings.json') as f:
        temp = json.load(f)[cat]
    ok_res_list = temp[list(temp.keys())[0]].keys()
    if cat == "zoo animals":
        if res in ["chimpanzee", "ape chimp etc"]: res = "chimp"
        elif res in ["orangutang", "orangutange", "orangatan", "orangutans", "haranatang"]: res = "orangutan"
        elif res in ["snakes"]: res = "snake"
        elif res in ["meercat"]: res = "meerkat"
        elif res in ["raccoons"]: res = "raccoon"
        elif res in ["sea otter", "sea otters", "otters"]: res = "otter"
        elif res in ["hippopotamus", "hippopatamus", "hippos"]: res = "hippo"
        elif res in ["aligator", "alligators"]: res = "alligator"
        elif res in ["other lizards", "some sort of lizard"]: res = "lizard"
        elif res in ["cheeta", "african cheetah", "cheetahs"]: res = "cheetah"
        elif res in ["anteaters"]: res = "anteater"
        elif res in ["giraffes", "girraffe", "girrafe", "jiraffe", "griraffe", "giraffee", "giraff"]: res = "giraffe"
        elif res in ["elephants", "elphant", "elephan", "elepehant", "asian elephants", "elepahnt", "indian elephant", "african elephant"]: res = "elephant"
        elif res in ["coati"]: res = "coyote"
        elif res in ["manitee"]: res = "manatee" 
        elif res in ["camal", "camals", "camels"]: res = "camel"
        elif res in ["panda bear", "pandas"]: res = "panda"
        elif res in ["crocks", "croc", "crocodiles"]: res = "crocodile"
        elif res in ["gorrila", "gorillas"]: res = "gorilla"
        elif res in ["whales", "killer whale", "blue whale"]: res = "whale"
        elif res in ["spider monkey", "ape/monkeys", "monkeys"]: res = "monkey"
        elif res in ["bats"]: res = "bat"
        elif res in ["most baby animals are harmless  i will choose a deer", "a deer"]: res = "deer"
        elif res in ["bald eagle"]: res = "eagle"
        elif res in ["rhinos", "rhinoceros", "rino"]: res = "rhino"
        elif res in ["penguins", "penguine"]: res = "penguin"
        elif res in ["owls"]: res = "owl"
        elif res in ["sloths"]: res = "sloth"
        elif res in ["turtles", "sea turtle"]: res = "turtle"
        elif res in ["sting rayy"]: res = "stingray"
        elif res in ["butterflies"]: res = "butterfly"
        elif res in ["sharks", "tiger shark"]: res = "shark"
        elif res in ["bob cat"]: res = "bobcat"
        elif res in ["goats"]: res = "goat"
        elif res in ["sea lions"]: res = "sea lion"
        elif res in ["birds", "chicken", "wild birds", "various birds", "turkey", "hummingbird", "common bird", "condor", "tucan"]: res = "bird"
        elif res in ["ostritch", "ostriches"]: res = "ostrich"
        elif res in ["flamingoes", "flamingos"]: res = "flamingo"
        elif res in ["zebras", "zeebra"]: res = "zebra"
        elif res in ["wolves"]: res = "wolf"
        elif res in ["beare", "bears", "brown bear", "other bear", "cub"]: res = "bear"
        elif res in ["antelopes"]: res = "antelope"
        elif res in ["hyenas"]: res = "hyena"
        elif res in ["polar bears"]: res = "polar bear"
        elif res in ["seals"]: res = "seal"
        elif res in ["lemurs"]: res = "lemur"
        elif res in ["opkapi"]: res = "okapi"
        elif res in ["a fish"]: res = "fish"
        elif res in ["lions"]: res = "lion"
        elif res in ["dolphins"]: res = "dolphin"
        elif res in ["parrots"]: res = "parrot"
        elif res in ["kangroo"]: res = "kangaroo"
        elif res in ["tigers", "tigert", "tiger cub"]: res = "tiger"
        elif res in ["cappabara"]: res = "capybara"
        elif res in ["rams"]: res = "ram"
        elif res in ["water buffalo"]: res = "buffalo"
    if cat == "holidays":
        if res in ["4th of july", "4th july", "4ths of july", "forth of july", "july 4", "july 4th", "independence day", "independence day.", "emancipation day", "independance day", "4 of july"]: res = "fourth of july"
        elif res in ["st pattys day", "st patricks", "st pattys", "st patrciks",  "st patricks day", "saint patricks", "st patrick day", "the holiday that i think about the least is st patricks day", "saint patricks day"]: res = "st. patricks day"
        elif res in ["new years eve", "new year's", "new year", "NYE", "new years day ", "new years day", "new years eve and day", "new yearseve", "new years eveday", "new years day because its the only day we have a tradition for watching the parade"]: res = "new years"
        elif res in ["mlk", "mlk day", "martin luther king day", "martin luther kings birthday", "martin luther king, jr. day", "martin luther king", "martin luther king jr day", "martin luther king jr. birthday", "birthday of martin luther", "martin luther king, jr", "mlk jr"]: res = "martin luther king jr. day"
        elif res in ["columbus", "columbus day", "columbus day." "columbus day ", "indigenous peoples day", "columbus day", "colombus day"]: res = "christopher columbus day"
        elif res in ["christmas eve", "chirstmas", "christmas day", "christmasq", "christman", "christmans", "probably christmas"]: res = "christmas"
        elif res in ["memorial", "memorial day."]: res = "memorial day"
        elif res in ["ressurrection dayeaster", "eastern", "probably easter its way more of a holiday for kids theres not much romance to be had"]: res = "easter"
        elif res in ["kwansa", "kwanzaa", "kwanaaaza"]: res = "kwanza"
        elif res in ["june 19th"]: res == "juneteenth"
        elif res in ["veterens day", "veterons day", "veteran day", "veterensday", "veterans"]: res = "veterans day"
        elif res in ["st. valentines day", "valetines day", "valentine", "valentines", "velentines day", "st valentines day", "valentines days", "valentines  day"]: res = "valentines day"
        elif res in ["washingtons birthday", "president day"]: res = "presidents day"
        elif res in ["thanksgiving day", "thanks giving", "thanksgivng"]: res = "thanksgiving"
        elif res in ["honaka", "chanukah", "hanukah", "hanakah", "hanuakah", "hannukkah", "hauneca", "chananaukah", "hannukah", "channukah"]: res = "hanukkah"
        elif res in ["chinese new years", "lunar new year"]: res = "chinese new year"
        elif res in ["my birthday", "bithdays", "birthday", "birth day", "birthday"]: res = "birthdays"
        elif res in ["holloween", "haloween", "all hallows eve", "hallowen"]: res = "halloween"
        elif res in ["labor day.", "labor dy"]: res = "labor day"
        elif res in ["diwahli"]: res = "diwali"
        
    elif cat == "chain restaurants":
        if res in ["kfc", "kentucky friend chicken"]: res = "kentucky fried chicken"
        elif res in ["chiles", "chillis", "chilles", "chilies"]: res = "chilis"
        elif res in ["tgif", "fridays", "tgifridays", "tgi friday", "t g i fridays"]: res = "tgi fridays"
        elif res in ["outback"]: res = "outback steakhouse"
        elif res in ["burgerking", "burga king", "burker king", "burger kings"]: res = "burger king"
        elif res in ["chic fil a", "chick fi a", "chicfila", "chicfale", "chick fil e", "chickfila", "chickfilet", "chick-fil-a", "chicfila", "chic-fil-a", "chick fila", "chick fila" "chik-fil-a", "chikafila", "chick filette", "chikfila", "chik fil a", "chick filet"]: res = "chick fil a"
        elif res in ["mcd", "mcdonald" "macdonalds", "mcdonald", "mcdoanlds", "mconalds", "mcdonals", "mc donalds", "mc ds"]: res = "mcdonalds"
        elif res in ["five guys burgers", "5 guys", "five guys and fries", "four guys"]: res = "five guys"
        elif res in ["panera bread", "pananera", "panera or wolfgang puck"]: res = "panera"
        elif res in ["olive garen"]: res = "olive garden"
        elif res in ["papa johns pizza"]: res = "papa johns"
        elif res in ["red loster"]: res = "red lobster"
        elif res in ["windys", "wendy"]: res = "wendys"
        elif res in ["chopotle", "chipolte", "chipoltle"]: res = "chipotle"
        elif res in ["pizzahut", "pozza hut", "pizza hutt"]: res = "pizza hut"
        elif res in ["lil ceasars", "little ceasars", "little ceasars", "little ceasar", "little cesars"]: res = "little caesars"
        elif res in ["applebee", "apple bees", "apple bes" "applebys", "applebees grill  bar"]: res = "applebees"
        elif res in ["macaronni grill"]: res = "macaroni grill"
        elif res in ["ruby tuesday", "ruby tusdays"]: res = "ruby tuesdays"
        elif res in ["bonefish", "bone fish grill"]: res = "bonefish grill"
        elif res in ["taco ball", "taco  bell", "taco bells", "taobell", "tacobell"]: res = "taco bell"
        elif res in ["cracker barrell", "crackerbarrel"]: res = "cracker barrel"
        elif res in ["jack and box"]: res = "jack in the box"
        elif res in ["p.f. changs", "p.f. changes", "pf chang"]: res = "pf changs"
        elif res in ["domino", "domminos", "dominoes"]: res = "dominos"
        elif res in ["arby", "abrys"]: res = "arbys"
        elif res in ["popeye"]: res = "popeyes"
        elif res in ["hardys"]: res = "hardees"
        elif res in ["panda"]: res = "panda express"
        elif res in ["texas road house"]: res = "texas roadhouse"
        elif res in ["sonic drive in"]: res = "sonic"
        elif res in ["dunkin"]: res = "dunkin donuts"
    
    if res not in ok_res_list:
        return None
    else:
        return res