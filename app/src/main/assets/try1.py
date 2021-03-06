from pyspark import SparkContext, SparkConf
import os
import csv
import time
import urllib2


#proxy_support = urllib2.ProxyHandler({'http':r'http://142191005:kithu123@172.18.61.10:3128'})
#auth = urllib2.HTTPBasicAuthHandler()
#opener = urllib2.build_opener(proxy_support, auth, urllib2.HTTPHandler)
#urllib2.install_opener(opener)
#response = urllib2.urlopen('http://www.nseindia.com')
#html = response.read()


proxy_support = urllib2.ProxyHandler({})
opener = urllib2.build_opener(proxy_support)
urllib2.install_opener(opener)


os.environ['http_proxy']=''
os.environ['https_proxy']=''
conf = SparkConf().setAppName('appName3').setMaster('spark://172.18.109.68:7077')
sc = SparkContext(conf=conf)

def myfuc(s):
    from nsetools import Nse
    nse=Nse()
    #list1=[]
    #for x in file:
    q=nse.get_quote(s)
    k=(q['buyPrice1'])
     #list1.append(k)
    return(k)

def prifun(s):
    return('a')

if __name__ == '__main__':
    start_time = time.time()
    data = ["20MICRONS",
"3IINFOTECH",
"3MINDIA",
"8KMILES",
"A2ZINFRA",
"A2ZINFRA",
"AARTIDRUGS",
"AARTIIND",
"AARVEEDEN",
"ABAN",
"ABB",
"ABBOTINDIA",
"ABGSHIP",
"ABIRLANUVO",
"ACC",
"ACCELYA",
"ACE",
"ACROPETAL",
"ADANIENT",
"ADANIPORTS",
"ADANIPOWER",
"ADANITRANS",
"ADFFOODS",
"ADHUNIK",
"ADI",
"ADLABS",
"ADORWELD",
"ADSL",
"ADVANIHOTR",
"ADVANTA",
"AEGISCHEM",
"AFL",
"AGARIND",
"AGCNET",
"AGRODUTCH",
"AHLEAST",
"AHLUCONT",
"AHLWEST",
"AIAENG",
"AIL",
"AJANTPHARM",
"AJMERA",
"AKSHOPTFBR",
"AKZOINDIA",
"ALANKIT",
"ALBK",
"ALCHEM",
"ALEMBICLTD",
"ALICON",
"ALKALI",
"ALKYLAMINE",
"ALLCARGO",
"ALLSEC",
"ALMONDZ",
"ALOKTEXT",
"ALPA",
"ALPHAGEO",
"ALPSINDUS",
"ALSTOMT&D",
"AMARAJABAT",
"AMBIKCO",
"AMBUJACEM",
"AMDIND",
"AMRUTANJAN",
"AMTEKAUTO",
"AMTL",
"ANANTRAJ",
"ANDHRABANK",
"ANDHRACEMT",
"ANDHRSUGAR",
"ANGIND",
"ANIKINDS",
"ANKITMETAL",
"ANSALAPI",
"ANSALHSG",
"ANTGRAPHIC",
"APARINDS",
"APCOTEXIND",
"APLAPOLLO",
"APLLTD",
"APOLLOHOSP",
"APOLLOTYRE",
"APOLSINHOT",
"APTECHT",
"ARCHIDPLY",
"ARCHIES",
"ARCOTECH",
"ARIES",
"ARIHANT",
"AROGRANITE",
"ARROWCOAT",
"ARROWTEX",
"ARSHIYA",
"ARSSINFRA",
"ARVIND",
"ARVINFRA",
"ASAHIINDIA",
"ASAHISONG",
"ASAL",
"ASHAPURMIN",
"ASHIANA",
"ASHIMASYN",
"ASHOKA",
"ASHOKLEY",
"ASIANHOTNR",
"ASIANPAINT",
"ASIANTILES",
"ASSAMCO",
"ASTEC",
"ASTRAL",
"ASTRAMICRO",
"ASTRAZEN",
"ATFL",
"ATLANTA",
"ATLASCYCLE",
"ATUL",
"ATULAUTO",
"AURIONPRO",
"AUROPHARMA",
"AUSOMENT",
"AUSTRAL",
"BAFNAPHARM",
"BAGFILMS",
"BAJAJ-AUTO",
"BAJAJCORP",
"BAJAJELEC",
"BAJAJFINSV",
"BAJAJHIND",
"BAJAJHLDNG",
"BAJFINANCE",
"BALAJITELE",
"BALAMINES",
"BALKRISIND",
"BALLARPUR",
"BALMLAWRIE",
"BALPHARMA",
"BALRAMCHIN",
"BANARBEADS",
"BANARISUG",
"BANCOINDIA",
"BANG",
"BANKBARODA",
"BANKINDIA",
"BANSWRAS",
"BARTRONICS",
"BASF",
"BASML",
"BATAINDIA",
"BAYERCROP",
"BBL",
"BBTC",
"BEDMUTHA",
"BEL",
"BEML",
"BEPL",
"BERGEPAINT",
"BFINVEST",
"BFUTILITIE",
"BGRENERGY",
"BHAGYNAGAR",
"BHARATFORG",
"BHARATGEAR",
"BHARATRAS",
"BHARTIARTL",
"BHEL",
"BHUSANSTL",
"BIL",
"BINANIIND",
"BINDALAGRO",
"BIOCON",
"BIRLACORPN",
"BIRLACOT",
"BIRLAERIC",
"BIRLAMONEY",
"BLBLIMITED",
"BLISSGVS",
"BLKASHYAP",
"BLUESTARCO",
"BLUESTINFO",
"BODALCHEM",
"BOMDYEING",
"BOSCHLTD",
"BPCL",
"BPL",
"BRFL",
"BRIGADE",
"BRITANNIA",
"BROOKS",
"BSELINFRA",
"BSL",
"BSLIMITED",
"BUTTERFLY",
"BVCL",
"BYKE",
"CANDC",
"CADILAHC",
"CAIRN",
"CTE",
"CAMLINFINE",
"CANFINHOME",
"CANBK",
"CANTABIL",
"CAPF",
"CAPLIPOINT",
"CGCL",
"CARBORUNIV",
"CAREERP",
"CASTEXTECH",
"CASTROLIND",
"CCL",
"CEATLTD",
"CELEBRITY",
"CELESTIAL",
"CENTRALBK",
"CENTUM",
"CENTENKA",
"CENTEXT",
"CENTURYPLY",
"CENTURYTEX",
"CERA",
"CEREBRAINT",
"CESC",
"CHAMBLFERT",
"CHEMFALKAL",
"CHENNPETRO",
"CHOLAFIN",
"CHROMATIC",
"CIGNITITEC",
"CNOVAPETRO",
"CIMMCO",
"CINELINE",
"CINEVISTA",
"CIPLA",
"CUB",
"CLNINDIA",
"COALINDIA",
"COLPAL",
"CEBBCO",
"COMPUSOFT",
"CCCL",
"CONSOFINVT",
"CONCOR",
"CORDSCABLE",
"COROMANDEL",
"CORPBANK",
"COSMOFILMS",
"CCHHL",
"COUNCODOS",
"CREATIVEYE",
"CARERATING",
"CREST",
"CRISIL",
"CROMPGREAV",
"CUMMINSIND",
"CYBERTECH",
"CYIENT",
"DAAWAT",
"DABUR",
"DALMIABHA",
"DALMIASUG",
"DATAMATICS",
"DBCORP",
"DBREALTY",
"DBSTOCKBRO",
"DCBBANK",
"DCM",
"DCMSHRIRAM",
"DCW",
"DECCANCE",
"DEEPAKFERT",
"DEEPAKNTR",
"DEEPIND",
"DELTACORP",
"DELTAMAGNT",
"DEN",
"DENABANK",
"DENORA",
"DHAMPURSUG",
"DHANBANK",
"DHANUKA",
"DHARSUGAR",
"DHFL",
"DHUNINV",
"DIAPOWER",
"DICIND",
"DISHMAN",
"DISHTV",
"DIVISLAB",
"DLF",
"DLINKINDIA",
"DOLPHINOFF",
"DONEAR",
"DPL",
"DPSCLTD",
"DQE",
"DREDGECORP",
"DRREDDY",
"DSKULKARNI",
"DTIL",
"DWARKESH",
"DYNAMATECH",
"DYNATECH",
"EASTSILK",
"EASUNREYRL",
"ECEIND",
"ECLERX",
"EDELWEISS",
"EDL",
"EDUCOMP",
"EICHERMOT",
"EIDPARRY",
"EIHAHOTELS",
"EIHOTEL",
"EIMCOELECO",
"EKC",
"ELAND",
"ELECON",
"ELECTCAST",
"ELECTHERM",
"ELGIEQUIP",
"ELGIRUBCO",
"EMAMIINFRA",
"EMAMILTD",
"EMCO",
"EMKAY",
"EMMBI",
"ENERGYDEV",
"ENGINERSIN",
"ENIL",
"ENTEGRA",
"EON",
"EROSMEDIA",
"ESABINDIA",
"ESCORTS",
"ESL",
"ESSARSHPNG",
"ESSDEE",
"ESSELPACK",
"ESTER",
"EUROCERA",
"EVEREADY",
"EVERESTIND",
"EVERONN",
"EXCEL",
"EXCELCROP",
"EXCELINDUS",
"EXIDEIND",
"FACT",
"FAGBEARING",
"FARMAXIND",
"FCEL",
"FCL",
"FCSSOFT",
"FDC",
"FEDDERLOYD",
"FEDERALBNK",
"FIEMIND",
"FINANTECH",
"FINCABLES",
"FINPIPE",
"FLEXITUFF",
"FLFL",
"FMGOETZE",
"FMNL",
"FORTIS",
"FOSECOIND",
"FRL",
"FRLDVR",
"FSL",
"GABRIEL",
"GAEL",
"GAIL",
"GAL",
"GALLANTT",
"GALLISPAT",
"GAMMNINFRA",
"GAMMONIND",
"GANDHITUBE",
"GANECOS",
"GANESHHOUC",
"GARDENSILK",
"GARWALLROP",
"GATI",
"GAYAPROJ",
"GDL",
"GEECEE",
"GEMINI",
"GENESYS",
"GENUSPAPER",
"GENUSPOWER",
"GEOJITBNPP",
"GEOMETRIC",
"GESHIP",
"GHCL",
"GICHSGFIN",
"GILLANDERS",
"GILLETTE",
"GINNIFILA",
"GIPCL",
"GITANJALI",
"GKWLIMITED",
"GLAXO",
"GLENMARK",
"GLOBALVECT",
"GLOBOFFS",
"GLOBUSSPR",
"GMBREW",
"GMDCLTD",
"GMRINFRA",
"GNFC",
"GOACARBON",
"GOCLCORP",
"GODFRYPHLP",
"GODREJCP",
"GODREJIND",
"GODREJPROP",
"GOENKA",
"GOKEX",
"GOKUL",
"GOKULAGRO",
"GOLDENTOBC",
"GOLDIAM",
"GOLDINFRA",
"GOODLUCK",
"GPIL",
"GPPL",
"GRANULES",
"GRAPHITE",
"GRASIM",
"GRAVITA",
"GREAVESCOT",
"GREENFIRE",
"GREENLAM",
"GREENPLY",
"GREENPOWER",
"GRINDWELL",
"GRPLTD",
"GRUH",
"GSCLCEMENT",
"GSFC",
"GSKCONS",
"GSPL",
"GSS",
"GTL",
"GTLINFRA",
"GTNTEX",
"GTOFFSHORE",
"GUFICBIO",
"GUJALKALI",
"GUJAPOLLO",
"GUJFLUORO",
"GUJGASLTD",
"GUJNRECOKE",
"GUJNREDVR",
"GULFOILLUB",
"GULFPETRO",
"GULPOLY",
"GVKPIL",
"HANUNG",
"HARITASEAT",
"HARRMALAYA",
"HATHWAY",
"HATSUN",
"HAVELLS",
"HBLPOWER",
"HBSTOCK",
"HCC",
"HCG",
"HCIL",
"HCL-INSYS",
"HCLTECH",
"HDFC",
"HDFCBANK",
"HDIL",
"HEG",
"HEIDELBERG",
"HERCULES",
"HERITGFOOD",
"HEROMOTOCO",
"HESTERBIO",
"HEXATRADEX",
"HEXAWARE",
"HFCL",
"HGS",
"HIKAL",
"HIL",
"HILTON",
"HIMATSEIDE",
"HINDALCO",
"HINDCOMPOS",
"HINDCOPPER",
"HINDDORROL",
"HINDMOTORS",
"HINDNATGLS",
"HINDOILEXP",
"HINDPETRO",
"HINDSYNTEX",
"HINDUJAFO",
"HINDUJAVEN",
"HINDUNILVR",
"HINDZINC",
"HIRECT",
"HITACHIHOM",
"HITECHGEAR",
"HITECHPLAS",
"HMT",
"HMVL",
"HOCL",
"HONAUT",
"HONDAPOWER",
"HOTELEELA",
"HOVS",
"HSIL",
"HTMEDIA",
"HUBTOWN",
"IBREALEST",
"IBULHSGFIN",
"IBVENTURES",
"IBWSL",
"ICICIBANK",
"ICIL",
"ICRA",
"ICSA",
"IDBI",
"IDEA",
"IDFC",
"IDFCBANK",
"IFBAGRO",
"IFBIND",
"IFCI",
"IFGLREFRAC",
"IGARASHI",
"IGL",
"IGPL",
"IIFL",
"IL&FSENGG",
"IL&FSTRANS",
"IMFA",
"IMPAL",
"IMPEXFERRO",
"INDBANK",
"INDHOTEL",
"INDIACEM",
"INDIAGLYCO",
"INDIANB",
"INDIANCARD",
"INDIANHUME",
"INDIGO",
"INDLMETER",
"INDNIPPON",
"INDOCO",
"INDORAMA",
"INDOSOLAR",
"INDOTECH",
"INDOTHAI",
"INDOWIND",
"INDRAMEDCO",
"INDSWFTLAB",
"INDSWFTLTD",
"INDTERRAIN",
"INDUSINDBK",
"INFINITE",
"INFOMEDIA",
"INFRATEL",
"INFY",
"INGERRAND",
"INOXLEISUR",
"INOXWIND",
"INSECTICID",
"INTELLECT",
"INVENTURE",
"IOB",
"IOC",
"IOLCP",
"IPAPPM",
"IPCALAB",
"IRB",
"ISFT",
"ISMTLTD",
"ITC",
"ITDCEM",
"ITI",
"IVC",
"IVP",
"IVRCLINFRA",
"IZMO",
"J&KBANK",
"JAGRAN",
"JAGSNPHARM",
"JAIBALAJI",
"JAICORPLTD",
"JAINSTUDIO",
"JAMNAAUTO",
"JAYAGROGN",
"JAYBARMARU",
"JAYNECOIND",
"JAYSREETEA",
"JBCHEPHARM",
"JBFIND",
"JBMA",
"JCTEL",
"JENSONICOL",
"JETAIRWAYS",
"JHS",
"JINDALPHOT",
"JINDALPOLY",
"JINDALSAW",
"JINDALSTEL",
"JINDCOT",
"JINDRILL",
"JINDWORLD",
"JISLDVREQS",
"JISLJALEQS",
"JKCEMENT",
"JKIL",
"JKLAKSHMI",
"JKPAPER",
"JKTYRE",
"JMA",
"JMCPROJECT",
"JMFINANCIL",
"JMTAUTOLTD",
"JOCIL",
"JPASSOCIAT",
"JPINFRATEC",
"JPOLYINVST",
"JPPOWER",
"JSL",
"JSLHISAR",
"JSWENERGY",
"JSWHL",
"JSWSTEEL",
"JSWSTEEL",
"JUBILANT",
"JUBLFOOD",
"JUBLINDS",
"JUSTDIAL",
"JVLAGRO",
"JYOTHYLAB",
"J&KBANK",
"JAGRAN",
"JAGSNPHARM",
"JAIBALAJI",
"JAICORPLTD",
"JAINSTUDIO",
"JAMNAAUTO",
"JAYAGROGN",
"JAYBARMARU",
"JAYNECOIND",
"JAYSREETEA",
"JBCHEPHARM",
"JBFIND",
"JBMA",
"JCTEL",
"JENSONICOL",
"JETAIRWAYS",
"JHS",
"JINDALPHOT",
"JINDALPOLY",
"JINDALSAW",
"JINDALSTEL",
"JINDCOT",
"JINDRILL",
"JINDWORLD",
"JISLDVREQS",
"JISLJALEQS",
"JKCEMENT",
"JKIL",
"JKLAKSHMI",
"JKPAPER",
"JKTYRE",
"JMA",
"JMCPROJECT",
"JMFINANCIL",
"JMTAUTOLTD",
"JOCIL",
"JPASSOCIAT",
"JPINFRATEC",
"JPOLYINVST",
"JPPOWER",
"JSL",
"JSLHISAR",
"JSWENERGY",
"JSWHL",
"JSWSTEEL",
"JSWSTEEL",
"JUBILANT",
"JUBLFOOD",
"JUBLINDS",
"JUSTDIAL",
"JVLAGRO",
"JYOTHYLAB",
"JYOTISTRUC",
"KABRAEXTRU",
"KAJARIACER",
"KAKATCEM",
"KALINDEE",
"KALPATPOWR",
"KALYANIFRG",
"KAMATHOTEL",
"KANANIIND",
"KANORICHEM",
"KANSAINER",
"KARMAENG",
"KARURVYSYA",
"KAUSHALYA",
"KAVVERITEL",
"KAYA",
"KCP",
"KCPSUGIND",
"KEC",
"KECL",
"KEI",
"KELLTONTEC",
"KEMROCK",
"KERNEX",
"KESARENT",
"KESORAMIND",
"KGL",
"KHAITANELE",
"KHANDSE",
"KICL",
"KILITCH",
"KIRIINDUS",
"KIRLOSBROS",
"KIRLOSENG",
"KIRLOSIND",
"KITEX",
"KKCL",
"KMSUGAR",
"KNRCON",
"KOHINOOR",
"KOKUYOCMLN",
"KOLTEPATIL",
"KOPRAN",
"KOTAKBANK",
"KOTARISUG",
"KOTHARIPET",
"KOTHARIPRO",
"KPIT",
"KPRMILL",
"KRBL",
"KRIDHANINF",
"KSBPUMPS",
"KSCL",
"KSERASERA",
"KSK",
"KSL",
"KTIL",
"KTKBANK",
"KWALITY",
"L&TFH",
"LAKPRE",
"LAKSHMIEFL",
"LAKSHVILAS",
"LALPATHLAB",
"LAMBODHARA",
"LAOPALA",
"LAXMIMACH",
"LGBBROSLTD",
"LGBFORGE",
"LIBERTSHOE",
"LICHSGFIN",
"LINCOLN",
"LINCPEN",
"LINDEINDIA",
"LITL",
"LLOYDELENG",
"LML",
"LOKESHMACH",
"LOTUSEYE",
"LOVABLE",
"LPDC",
"LT",
"LUMAXAUTO",
"LUMAXIND",
"LUMAXTECH",
"LUPIN",
"LUXIND",
"LYCOS",
"LYKALABS",
"LYPSAGEMS",
"M&M",
"M&MFIN",
"MAANALU",
"MADHAV",
"MADHUCON",
"MADRASFERT",
"MAGMA",
"MAGNUM",
"MAHABANK",
"MAHINDCIE",
"MAHLIFE",
"MAHSCOOTER",
"MAHSEAMLES",
"MAITHANALL",
"MAJESCO",
"MALUPAPER",
"MANAKALUCO",
"MANAKCOAT",
"MANAKINDST",
"MANAKSIA",
"MANAKSTEEL",
"MANALIPETC",
"MANAPPURAM",
"MANAPPURAM",
"MANDHANA",
"MANGALAM",
"MANGCHEFER",
"MANGLMCEM",
"MANGTIMBER",
"MANINDS",
"MANINFRA",
"MANPASAND",
"MANUGRAPH",
"MARALOVER",
"MARICO",
"MARKSANS",
"MARUTI",
"MASTEK",
"MAWANASUG",
"MAXWELL",
"MAYURUNIQ",
"MBECL",
"MBLINFRA",
"MCDHOLDING",
"MCDOWELL-N",
"MCLEODRUSS",
"MCX",
"MEGASOFT",
"MEGH",
"MENONBE",
"MEP",
"MERCATOR",
"MERCK",
"METALFORGE",
"METKORE",
"MFSL",
"MHRIL",
"MIC",
"MICROSEC",
"MINDACORP",
"MINDAIND",
"MINDTREE",
"MIRCELECTR",
"MIRZAINT",
"MMFL",
"MMTC",
"MOHITIND",
"MOIL",
"MOLDTKPAC",
"MONNETISPA",
"MONSANTO",
"MONTECARLO",
"MORARJEE",
"MOREPENLAB",
"MOSERBAER",
"MOTHERSUMI",
"MOTILALOFS",
"MOTOGENFIN",
"MPHASIS",
"MPSLTD",
"MRF",
"MRO-TEK",
"MRPL",
"MSPL",
"MTEDUCARE",
"MTNL",
"MUKANDENGG",
"MUKANDLTD",
"MUKANDLTD",
"MUKTAARTS",
"MUNJALAU",
"MUNJALSHOW",
"MURUDCERA",
"MUTHOOTCAP",
"MUTHOOTFIN",
"MVL",
"MYSOREBANK",
"NAGAROIL",
"NAGREEKEXP",
"NAHARCAP",
"NAHARINDUS",
"NAHARPOLY",
"NAHARSPING",
"NAKODA",
"NATCOPHARM",
"NATHBIOGEN",
"NATIONALUM",
"NATNLSTEEL",
"NAUKRI",
"NAVINFLUOR",
"NAVKARCORP",
"NAVNETEDUL",
"NBCC",
"NBVENTURES",
"NCC",
"NCLIND",
"NDL",
"NDTV",
"NECCLTD",
"NECLIFE",
"NELCAST",
"NELCO",
"NEPCMICON",
"NESCO",
"NESTLEIND",
"NETWORK18",
"NEULANDLAB",
"NEXTMEDIA",
"NEYVELILIG",
"NFL",
"NH",
"NHPC",
"NIBL",
"NIITLTD",
"NIITTECH",
"NILAINFRA",
"NILKAMAL",
"NIPPOBATRY",
"NIRVIKARA",
"NITCO",
"NITESHEST",
"NITINFIRE",
"NITINSPIN",
"NMDC",
"NOCIL",
"NOESISIND",
"NOIDATOLL",
"NRBBEARING",
"NSIL",
"NTPC",
"NUCLEUS",
"NUTEK",
"OBEROIRLTY",
"OCCL",
"OCL",
"OFSS",
"OIL",
"OILCOUNTUB",
"OISL",
"OMAXAUTO",
"OMAXE",
"OMKARCHEM",
"OMMETALS",
"OMNITECH",
"ONELIFECAP",
"ONGC",
"ONMOBILE",
"ONWARDTEC",
"OPTOCIRCUI",
"ORBITCORP",
"ORBTEXP",
"ORCHIDPHAR",
"ORICONENT",
"ORIENTABRA",
"ORIENTBANK",
"ORIENTBELL",
"ORIENTCEM",
"ORIENTHOT",
"ORIENTLTD",
"ORIENTPPR",
"ORIENTREF",
"ORISSAMINE",
"ORTEL",
"ORTINLABSS",
"OUDHSUG",
"PAEL",
"PAGEIND",
"PALREDTECH",
"PANACEABIO",
"PANAMAPET",
"PANORAMUNI",
"PAPERPROD",
"PARABDRUGS",
"PARACABLES",
"PARAPRINT",
"PARASPETRO",
"PARRYSUGAR",
"PARSVNATH",
"PATELENG",
"PATINTLOG",
"PATSPINLTD",
"PBAINFRA",
"PCJEWELLER",
"PDPL",
"PDSMFL",
"PDUMJEIND",
"PDUMJEPULP",
"PEARLPOLY",
"PEL",
"PENIND",
"PENINLAND",
"PENPEBS",
"PERSISTENT",
"PETRONENGG",
"PETRONET",
"PFC",
"PFIZER",
"PFOCUS",
"PFS",
"PGEL",
"PGHH",
"PGIL",
"PHILIPCARB",
"PHOENIXLL",
"PHOENIXLTD",
"PIDILITIND",
"PIIND",
"PILANIINVS",
"PILITA",
"PIONDIST",
"PIONEEREMB",
"PIRPHYTO",
"PITTILAM",
"PKTEA",
"PLASTIBLEN",
"PNB",
"PNBGILTS",
"PNC",
"PNCINFRA",
"PNEUMATIC",
"POCHIRAJU",
"POLARIS",
"POLYMED",
"POLYPLEX",
"PONNIERODE",
"POWERGRID",
"POWERMECH",
"PPAP",
"PRABHAT",
"PRAENG",
"PRAJIND",
"PRAKASH",
"PRAKASHCON",
"PRAKASHSTL",
"PRATIBHA",
"PRECAM",
"PRECOT",
"PRECWIRE",
"PREMIER",
"PRESSMN",
"PRESTIGE",
"PRICOL",
"PRIMESECU",
"PRISMCEM",
"PROVOGE",
"PROZONINTU",
"PSB",
"PSL",
"PTC",
"PTL",
"PUNJABCHEM",
"PUNJLLOYD",
"PURVA",
"PVP",
"PVR",
"QUICKHEAL",
"RADICO",
"RAIN",
"RAINBOWPAP",
"RAIREKMOH",
"RAJESHEXPO",
"RAJOIL",
"RAJRAYON",
"RAJSREESUG",
"RAJTV",
"RALLIS",
"RAMANEWS",
"RAMASTEEL",
"RAMCOCEM",
"RAMCOIND",
"RAMCOSYS",
"RAMKY",
"RAMSARUP",
"RANASUG",
"RANEENGINE",
"RANEHOLDIN",
"RASOYPR",
"RATNAMANI",
"RAYMOND",
"RBL",
"RCF",
"RCOM",
"RECLTD",
"REDINGTON",
"REFEX",
"REIAGROLTD",
"RELAXO",
"RELCAPITAL",
"RELIANCE",
"RELIGARE",
"RELINFRA",
"REMSONSIND",
"RENUKA",
"REPCOHOME",
"REPRO",
"RESPONIND",
"REVATHI",
"RICOAUTO",
"RIIL",
"RJL",
"RKDL",
"RKFORGE",
"RMCL",
"RML",
"RMMIL",
"ROHITFERRO",
"ROHLTD",
"ROLTA",
"ROSSELLIND",
"RPGLIFE",
"RPOWER",
"RPPINFRA",
"RSSOFTWARE",
"RSWM",
"RSYSTEMS",
"RTNINFRA",
"RTNPOWER",
"RUBYMILLS",
"RUCHINFRA",
"RUCHIRA",
"RUCHISOYA",
"RUPA",
"RUSHIL"]
    distData = sc.parallelize(data).cache()
    newdist=distData.map(lambda x: myfuc(x)).collect()
    #rows=zip(newdist)
    #with open("MYFILE.csv", "a+") as to_file:
		#writer = csv.writer(to_file, delimiter=",")
		#for new_row in rows:
			#writer.writerow(new_row)
    c = csv.writer(open("/home/hduser/work/spark-1.4.1-bin-hadoop2.4/18_4_Myfile.csv", "a+"))
    #rows=zip(newdist)
    #for row in rows:
    c.writerow([start_time]+newdist)
    #c.writerow(newdist)
    print(newdist)
    
