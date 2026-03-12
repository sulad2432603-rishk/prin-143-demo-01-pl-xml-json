from models.bank import Bank
from models.entertainment import Entertainment
from models.management import Management
from models.politician import Politician
from models.retail import Retail
from models.student import Student
from models.subject import Subject
from utilities.utilities import write_to_json, write_to_xml

subject = Subject(code = "PRIN143", students=[
    Student(lastName="ADVINCULA", firstName="ZOFIA ELIONOR", address="City of Malolos, Bulacan", reason="Versatile course.", expectation="No idea yet.")
    , Student(lastName="BALMES", firstName="ERYN ARABELLA", address="Calumpit, Bulacan", reason="In demand & versatile.", expectation="Architeture based on subject title.")
    , Student(lastName="CATABAS", firstName="MARYHALEIN YSHABELA", address="City of Malolos, Bulacan", reason="Gusto madaming pera.", expectation="Makakatulong sa career.")
    , Student(lastName="HAKOJIMA", firstName="FUMIE JOY", address="City of Malolos, Bulacan", reason="Sabi ni mommy", expectation="Sana Pumasa.")
    , Student(lastName="MANALASTAS", firstName="KIRSTEN EMELIZA", address="San Ildefonso, Bulacan", reason="Wala choice.", expectation="Mahirap daw ang subject.")
    , Student(lastName="MANANSALA", firstName="JEANNE DESSIEREI", address="City of Malolos, Bulacan", reason="In demand at madaming pera.", expectation="No clue.")
    , Student(lastName="MARTINEZ", firstName="JULIANA MARIE", address="Guiguinto, Bulacan", reason="Sabi ng kuya and no choice.", expectation="Madami matutunan and mahirap yung subject.")
    , Student(lastName="PINGOL", firstName="MA. ALEXANDRIA", address="City of Malolos, Bulacan", reason="Suggestion ng parents", expectation="Mahirap subject")
    , Student(lastName="REYES", firstName="TEHYA SHAYE", address="Calumpit, Bulacan", reason="In demand.", expectation="Explore system architecture and design.")
    , Student(lastName="RODRIGUEZ", firstName="MA. ARABELLA", address="Plaridel, Bulacan", reason="Mataas sahod", expectation="Expect the unexpected based from the subject.")
    , Student(lastName="SULAD", firstName="IRISH KRISTEL", address="Baliwag, Bulacan", reason="Recommended as scholarship.", expectation="Same with Ms. Manalastas.")
    , Student(lastName="UNTALAN", firstName="FRANCHESCA", address="Guiguinto, Bulacan", reason="Sabi ng nanay na nagbabayad ng tuition.", expectation="Designing systems.")
    , Student(lastName="AGNAS", firstName="RONNE JUSTIN", address="Plaridel, Bulacan", reason="Flexible industry.", expectation="Mahirap at nakakabaliw.")
    , Student(lastName="ALEJO", firstName="LENNARD CHEZTER", address="Baliwag, Bulacan", reason="Flexible course.", expectation="Maraming matututunan.")
    , Student(lastName="AURE", firstName="IVAN NIKOLAI", address="City of Malolos, Bulacan", reason="Loves PC and Flexible Subject", expectation="Masaya madami matututnan.")
    , Student(lastName="BARON", firstName="RICHARD CARLO", address="Calumpit, Bulacan", reason="Noong araw marunong magcode.", expectation="Create a feasible and scalable systems.")
    , Student(lastName="BATAC", firstName="FRANCIS ALBERT", address="Sta. Maria, Bulacan", reason="Pursue AI and CyberSec", expectation="Connectivity ng Hardware and Software")
    , Student(lastName="BAUTISTA", firstName="TRISTAN JACOB", address="", reason="", expectation="")
    , Student(lastName="CALIWAG", firstName="DANIEL JOSEF", address="City of Malolos, Bulacan", reason="In demand at maraming option pag graduate.", expectation="Designing and integration concepts.")
    , Student(lastName="CENTENO", firstName="BRENT", address="Hagonoy, Bulacan", reason="Madami opportunity.", expectation="Mahirap na masarap.")
    , Student(lastName="CORTEZ", firstName="JAIRUZ JERIEL", address="Apalit, Pampanga", reason="Computer boy since child.", expectation="Hardware and software integration to create a system.")
    , Student(lastName="CULLAMCO", firstName="ALJO MIGUEL", address="Calumpit, Bulacan", reason="Maraming job opportunity.", expectation="Magaaral")
    , Student(lastName="DE LUNA", firstName="CHARLES ANGELO", address="City of Malolos, Bulacan", reason="Likes to code.", expectation="Middleware and Microservices.")
    , Student(lastName="DELA ROCA", firstName="KERR ANDRESS", address="Pulilan , Bulacan", reason="Coding is interesting.", expectation="No idea.")
    , Student(lastName="EVANGELISTA", firstName="JURAY", address="Plaridel, Bulacan", reason="Interest in IT and easy to branch out in multiple fields.", expectation="Mapapalaban lalo na sa exam.")
    , Student(lastName="GALANG", firstName="MARK JR", address="", reason="", expectation="")
    , Student(lastName="GATBUNTON", firstName="JIRO YVANN", address="Calumpit, Bulacan", reason="Find it enjoyable since HS and into games", expectation="Hone skills ion computer programming and integration.")
    , Student(lastName="JACINTO", firstName="GABRIELLE", address="Sta. Maria, Bulacan", reason="Di alam pa.", expectation="Mahirap daw.")
    , Student(lastName="MANUEL", firstName="VICTOR EION", address="Plaridel, Bulacan", reason="Ayaw mag nursing.", expectation="50-50 madali at mahirap.")
    , Student(lastName="MERCADO", firstName="OUIM CARL", address="Pulilan, Bulacan", reason="Influence ni kuya.", expectation="Maraming Matututunan.")
    , Student(lastName="NAKAGAWA", firstName="DAISHI", address="Calumpit, Bulacan", reason="In demand for opportunites and inspired from collegues.", expectation="Designing different kinds of systems.")
    , Student(lastName="OCAMPO", firstName="MANUEL JOAQUIN", address="City of Malolos, Bulacan", reason="Kala ko petiks lang.", expectation="Sana fun kahit mahirap.")
    , Student(lastName="RAMOS", firstName="DART JHACOB", address="City of Malolos, Bulacan", reason="Enhance coding skills.", expectation="Build ng systems and makapasa sa course.")
    , Student(lastName="SAGANA", firstName="MARK LAUREN", address="Sta. Maria, Bulacan", reason="Enjoyable course.", expectation="Lot to learn to be used in future work.")
    , Student(lastName="STO. DOMINGO", firstName="FARYEL FRENZ", address="Calumpit, Bulacan", reason="Likes computers.", expectation="Coding complex systems.")
    , Student(lastName="TADEO", firstName="KENT HERMIN", address="City of Malolos, Bulacan", reason="Nasimulang subject course", expectation="Mahirap kasi ako yung prof.")
    , Student(lastName="TRAYFALGAR", firstName="JETHRO GABRIEL", address="Apalit, Pampanga", reason="In demand in today's world.", expectation="May pagkain.")
    , Student(lastName="VALE", firstName="JAZREL", address="City of Malolos, Bulacan", reason="Basic lang daw ang IT.", expectation="Gumawa ng bagay na mapapadali ang buhay.")
    , Student(lastName="VILLANUEVA", firstName="NICHO SEBASTIAN", address="Apalit, Pampanga", reason="Ayaw mag medicine related course.", expectation="Too many to mention.")
])
fileName = subject.__class__.__name__.lower()

retail = Retail(product_id="M7364", product_category= "Coffee", coffee_flavor= "Salted Caramel", price= 120, size= "Medium")
fileName = retail.__class__.__name__.lower()

entertainment = Entertainment(movie_id=74859, movie_title= "City of Angels", genre= "Romance", language= "English", release_year= 1998)
fileName = entertainment.__class__.__name__.lower()

politician = Politician(candidate_name="Lando T. Gaspuso", position_running_for= "Senator", political_party= "Green Future Party", election_year= 2026, platform= "Improve Urban Green Spaces")
fileName = politician.__class__.__name__.lower()

management = Management(student_id="28647", student_name= "Kristel Frisnedi", course= "BSIT", section= "A", year_level= "2nd")
fileName = management.__class__.__name__.lower()

bank = Bank(bank_name="Security Bank", account_id= "A9402", account_name= "Kristel D. Magiba", account_status= "Active", balance= "Php 70,000", last_transaction= "02-19-2026")
fileName = bank.__class__.__name__.lower()

#write_to_xml(subject.as_xml(), fileName)
#write_to_json(subject.as_json(), fileName)

write_to_xml(retail.as_xml(), fileName)
write_to_json(retail.as_json(), fileName)

write_to_xml(entertainment.as_xml(), fileName)
write_to_json(entertainment.as_json(), fileName)

write_to_xml(politician.as_xml(), fileName)
write_to_json(politician.as_json(), fileName)

write_to_xml(management.as_xml(), fileName)
write_to_json(management.as_json(), fileName)

write_to_xml(bank.as_xml(), fileName)
write_to_json(bank.as_json(), fileName)
