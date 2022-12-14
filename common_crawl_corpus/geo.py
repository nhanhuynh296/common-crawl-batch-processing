# Ignore certain countries if there is already enough data

# This list defines what countries to include in the corpus
country_codes = [
    'ad', 'ae', 'af', 'al', 'ao', 'aq', 'ar', 'as', 'at', 'au', 'aw', 'ax', 'az', 'ba', 'bb', 'bd', 'be', 'bf', 'bg',
    'bh', 'bi', 'bj', 'bl', 'bm', 'bn', 'bo', 'bq', 'br', 'bs', 'bt', 'bw', 'by', 'bz', 'ca', 'cd', 'cf', 'cg', 'ch',
    'ci', 'ck', 'cl', 'cm', 'cn', 'co', 'cr', 'cu', 'cv', 'cw', 'cx', 'cy', 'cz', 'de', 'dj', 'dk', 'dm', 'do', 'dz',
    'ec', 'ee', 'eg', 'er', 'es', 'et', 'fi', 'fj', 'fk', 'fm', 'fo', 'fr', 'ga', 'gb', 'gd', 'ge', 'gf', 'gh', 'gi',
    'gl', 'gm', 'gn', 'gp', 'gr', 'gt', 'gu', 'gw', 'gy', 'hk', 'hn', 'hr', 'ht', 'hu', 'id', 'ie', 'il', 'im', 'in',
    'iq', 'ir', 'is', 'it', 'je', 'jm', 'jo', 'jp', 'ke', 'kg', 'kh', 'ki', 'km', 'kn', 'kp', 'kr', 'kw', 'ky', 'kz',
    'lb', 'lc', 'li', 'lk', 'lr', 'ls', 'lt', 'lu', 'lv', 'ma', 'mc', 'md', 'mf', 'mg', 'mh', 'mk', 'ml', 'mm', 'mn',
    'mo', 'mp', 'mq', 'mr', 'mt', 'mu', 'mv', 'mw', 'mx', 'my', 'mz', 'na', 'nc', 'ne', 'nf', 'ng', 'ni', 'nl', 'no',
    'np', 'nr', 'nz', 'om', 'pa', 'pe', 'pf', 'pg', 'ph', 'pk', 'pl', 'pm', 'pr', 'ps', 'pt', 'pw', 'py', 'qa', 're',
    'ro', 'rs', 'ru', 'rw', 'sa', 'sb', 'sc', 'sd', 'se', 'sg', 'si', 'sk', 'sl', 'sm', 'sn', 'so', 'sr', 'ss', 'st',
    'sv', 'sx', 'sy', 'sz', 'tc', 'td', 'tg', 'th', 'tj', 'tl', 'tm', 'tn', 'tp', 'tr', 'tt', 'tw', 'tz', 'ua', 'ug',
    'uk', 'us', 'uy', 'uz', 'va', 'vc', 've', 'vg', 'vi', 'vn', 'vu', 'wf', 'ye', 'yt', 'za', 'zm', 'zw', 'ελ', 'бг',
    'бел', 'мкд', 'рф', 'срб', 'укр', 'қаз', 'հայ', 'الاردن', 'الجزائر', 'السعودية', 'المغرب', 'امارات', 'ایران',
    'بھارت', 'تونس', 'سودان', 'سورية', 'عراق', 'عمان', 'فلسطين', 'قطر', 'مصر', 'مليسيا', 'موريتانيا', 'پاكستان',
    'پاکستان', 'ڀارت', 'भारत', 'বাংলা', 'ভারত', 'ਭਾਰਤ', 'ભારત', 'இந்தியா', 'இலங்கை', 'சிங்கப்பூர்', 'భారత్', 'ಭಾರತ',
    'ഭാരതം', 'ලංකා', 'ไทย', '中国', '中國', '台湾', '台灣', '新加坡', '澳門', '香港', '한국'
]

# This dictionary maps country codes to (English) country names
country_names = {
    "ad": "Andorra", "ae": "United_Arab_Emirates", "af": "Afghanistan", "ag": "Antigua_and_Barbuda", "al": "Albania",
    "am": "Armenia", "ao": "Angola", "aq": "Antarctica", "ar": "Argentina", "as": "American_Samoa", "at": "Austria",
    "au": "Australia", "aw": "Aruba", "ax": "Åland", "az": "Azerbaijan", "ba": "Bosnia and Herzegovina",
    "bb": "Barbados", "bd": "Bangladesh", "be": "Belgium", "bf": "Burkina_Faso", "bg": "Bulgaria", "bh": "Bahrain",
    "bi": "Burundi", "bj": "Benin", "bl": "Saint_Barthélemy", "bm": "Bermuda", "bn": "Brunei ", "bo": "Bolivia",
    "bq": "Caribbean_Netherlands", "br": "Brazil", "bs": "Bahamas", "bt": "Bhutan", "bw": "Botswana", "by": "Belarus",
    "bz": "Belize", "ca": "Canada", "cc": "Cocos", "cd": "Democratic_Republic_Congo", "cf": "Central_African_Republic",
    "cg": "Republic_of_Congo", "ch": "Switzerland", "ci": "Côte_d'Ivoire", "ck": "Cook_Islands", "cl": "Chile",
    "cm": "Cameroon", "cn": "China", "co": "Colombia", "cr": "Costa_Rica", "cu": "Cuba", "cv": "Cabo_Verde",
    "cw": "Curaçao", "cx": "Christmas_Island", "cy": "Cyprus", "cz": "Czechia", "de": "Germany", "dj": "Djibouti",
    "dk": "Denmark", "dm": "Dominica", "do": "Dominican_Republic", "dz": "Algeria", "ec": "Ecuador", "ee": "Estonia",
    "eg": "Egypt", "er": "Eritrea", "es": "Spain", "et": "Ethiopia", "fi": "Finland", "fj": "Fiji",
    "fk": "Falkland_Islands", "fm": "Federated_States_Micronesia", "fo": "Faroe_Islands", "fr": "France", "ga": "Gabon",
    "gb": "United_Kingdom ", "gd": "Grenada",
    "ge": "Georgia", "gf": "French_Guiana", "gg": "Guernsey", "gh": "Ghana", "gi": "Gibraltar", "gl": "Greenland",
    "gm": "Gambia", "gn": "Guinea", "gp": "Guadeloupe", "gq": "Equatorial_Guinea", "gr": "Greece",
    "gs": "South_Georgia", "gt": "Guatemala", "gu": "Guam", "gw": "Guinea-Bissau",
    "gy": "Guyana", "hk": "Hong_Kong", "hm": "Heard_Island", "hn": "Honduras", "hr": "Croatia", "ht": "Haiti",
    "hu": "Hungary", "id": "Indonesia", "ie": "Ireland", "il": "Israel",
    "im": "Isle_of_Man", "in": "India", "iq": "Iraq", "ir": "Iran", "is": "Iceland", "it": "Italy", "je": "Jersey",
    "jm": "Jamaica", "jo": "Jordan", "jp": "Japan", "ke": "Kenya", "kg": "Kyrgyzstan", "kh": "Cambodia",
    "ki": "Kiribati", "km": "Comoros",
    "kn": "Saint_Kitts_Nevis", "kp": "North_Korea", "kr": "South_Korea", "kw": "Kuwait", "ky": "Cayman_Islands",
    "kz": "Kazakhstan", "la": "Lao", "lb": "Lebanon", "lc": "Saint_Lucia", "li": "Liechtenstein", "lk": "Sri_Lanka",
    "lr": "Liberia", "ls": "Lesotho", "lt": "Lithuania", "lu": "Luxembourg",
    "lv": "Latvia", "ly": "Libya", "ma": "Morocco", "mc": "Monaco", "md": "Moldova", "me": "Montenegro",
    "mf": "Saint-Martin", "mg": "Madagascar", "mh": "Marshall_Islands ", "mk": "North_Macedonia",
    "ml": "Mali", "mm": "Myanmar", "mn": "Mongolia", "mo": "Macao", "mp": "Northern_Mariana_Islands",
    "mq": "Martinique", "mr": "Mauritania", "ms": "Montserrat", "mt": "Malta", "mu": "Mauritius",
    "mv": "Maldives", "mw": "Malawi", "mx": "Mexico", "my": "Malaysia", "mz": "Mozambique", "na": "Namibia",
    "nc": "New_Caledonia", "ne": "Niger", "nf": "Norfolk_Island", "ng": "Nigeria",
    "ni": "Nicaragua", "nl": "Netherlands", "no": "Norway", "np": "Nepal", "nr": "Nauru", "nu": "Niue",
    "nz": "New_Zealand", "om": "Oman", "pa": "Panama", "pe": "Peru", "pf": "French_Polynesia", "pg": "Papua_New_Guinea",
    "ph": "Philippines", "pk": "Pakistan", "pl": "Poland",
    "pm": "Saint_Pierre", "pn": "Pitcairn", "pr": "Puerto Rico", "ps": "Palestine", "pt": "Portugal", "pw": "Palau",
    "py": "Paraguay", "qa": "Qatar", "re": "Réunion", "ro": "Romania", "rs": "Serbia", "ru": "Russia", "rw": "Rwanda",
    "sa": "Saudi_Arabia", "sb": "Solomon_Islands",
    "sc": "Seychelles", "sd": "Sudan", "se": "Sweden", "sg": "Singapore", "sh": "Saint_Helena",
    "si": "Slovenia", "sk": "Slovakia", "sl": "Sierra_Leone", "sm": "San_Marino", "sn": "Senegal",
    "so": "Somalia", "sr": "Suriname", "ss": "South_Sudan", "st": "Sao_Tome", "sv": "El_Salvador",
    "sx": "Sint_Maarten", "sy": "Syria", "sz": "Eswatini", "tc": "Caicos_Islands", "td": "Chad",
    "tf": "French_Southern", "tg": "Togo", "th": "Thailand", "tj": "Tajikistan", "tk": "Tokelau",
    "tl": "Timor-Leste", "tm": "Turkmenistan", "tn": "Tunisia", "to": "Tonga", "tp": "East_Timor",
    "tr": "Turkey", "tt": "Trinidad_Tobago", "tv": "Tuvalu", "tw": "China", "tz": "Tanzania",
    "ua": "Ukraine", "ug": "Uganda", "uk": "United_Kingdom", "us": "United_States", "uy": "Uruguay",
    "uz": "Uzbekistan", "va": "The_Vatican", "vc": "Saint_Vincent", "ve": "Venezuela", "vg": "Virgin_Islands",
    "vi": "Virgin_Islands", "vn": "Viet_Nam", "vu": "Vanuatu", "wf": "Wallis_Futuna", "ws": "Samoa",
    "ye": "Yemen", "yt": "Mayotte", "za": "South_Africa", "zm": "Zambia", "zw": "Zimbabwe",
    "ελ": "Greece", "бг": "Bulgaria", "бел": "Bulgaria", "мкд": "North_Macedonia", "рф": "Russia",
    "срб": "Serbia", "укр": "Ukraine", "қаз": "Kazakhstan", "հայ": "Armenia", "الاردن": "Jordan",
    "الجزائر": "Algeria", "السعودية": "Saudi_Arabia", "المغرب": "Morocco", "امارات": "United_Arab_Emirates",
    "ایران": "Iran",
    "بھارت": "India", "تونس": "Tunisia", "سودان": "Sudan", "سورية": "Syria", "عراق": "Iraq",
    "عمان": "Oman", "فلسطين": "Palestine", "قطر": "Qatar", "مصر": "Egypt", "مليسيا": "Malaysia",
    "موريتانيا": "Mauritania", "پاكستان": "Pakistan", "پاکستان": "Pakistan", "ڀارت": "India", "भारत": "India",
    "বাংলা": "Bangladesh", "ভারত": "India", "ਭਾਰਤ": "India", "ભારત": "India", "இந்தியா": "India",
    "இலங்கை": "Sri_Lanka", "சிங்கப்பூர்": "Singapore", "భారత్": "India", "ಭಾರತ": "India", "ഭാരതം": "India",
    "ලංකා": "Thailand", "ไทย": "Thailand", "中国": "China", "中國": "China", "台湾": "Taiwan",
    "台灣": "Taiwan", "新加坡": "Singapore", "澳門": "Macao", "香港": "Hong_Kong", "한국": "South_Korea"
}

# This dictionary maps country names to large regions for organizational purposes
country_regions = {
    "ad": "europe_west", "ae": "middle_east", "af": "asia_central", "al": "europe_west", "ao": "africa_sub",
    "aq": "antarctica", "ar": "america_south", "as": "asia_southeast",
    "at": "europe_west", "au": "oceania", "aw": "america_central", "ax": "europe_west", "az": "asia_central",
    "ba": "europe_east", "bb": "america_central", "bd": "asia_south",
    "be": "europe_west", "bf": "africa_sub", "bg": "europe_east", "bh": "middle_east", "bi": "africa_sub",
    "bj": "africa_sub", "bl": "american_central", "bm": "america_central",
    "bn": "asia_southeast", "bo": "america_south", "bq": "america_central", "br": "america_brazil",
    "bs": "america_central", "bt": "asia_south", "bv": "europe_west", "bw": "africa_southern",
    "by": "europe_east", "bz": "america_central", "ca": "america_north", "cd": "africa_sub", "cf": "africa_sub",
    "cg": "africa_sub", "ch": "europe_west", "ci": "africa_sub",
    "ck": "asia_southeast", "cl": "america_south", "cm": "africa_sub", "cn": "asia_east", "co": "america_south",
    "cr": "america_central", "cu": "america_central", "cv": "africa_sub",
    "cw": "america_central", "cx": "asia_southeast", "cy": "europe_west", "cz": "europe_east", "de": "europe_west",
    "dj": "africa_north", "dk": "europe_west", "dm": "america_central",
    "do": "america_central", "dz": "africa_north", "ec": "america_south", "ee": "europe_east", "eg": "middle_east",
    "er": "africa_north", "es": "europe_west", "et": "africa_north",
    "fi": "europe_west", "fj": "asia_southeast", "fk": "america_south", "fm": "asia_southeast", "fo": "europe_west",
    "fr": "europe_west", "ga": "africa_sub", "gb": "europe_west",
    "gd": "america_central", "ge": "asia_central", "gf": "america_south", "gh": "africa_sub", "gi": "africa_north",
    "gl": "europe_west", "gm": "africa_sub", "gn": "africa_sub",
    "gp": "america_central", "gr": "europe_west", "gt": "america_central", "gu": "oceania", "gw": "africa_sub",
    "gy": "america_south", "hk": "asia_east", "hn": "america_central",
    "hr": "europe_east", "ht": "america_central", "hu": "europe_east", "id": "asia_southeast", "ie": "europe_west",
    "il": "middle_east", "im": "europe_west", "in": "asia_south",
    "iq": "middle_east", "ir": "asia_central", "is": "europe_west", "it": "europe_west", "je": "europe_west",
    "jm": "america_central", "jo": "middle_east", "jp": "asia_east",
    "ke": "africa_sub", "kg": "asia_central", "kh": "asia_southeast", "ki": "asia_southeast", "km": "africa_sub",
    "kn": "america_central", "kp": "asia_east", "kr": "asia_east",
    "kw": "middle_east", "ky": "america_central", "kz": "asia_central", "lb": "middle_east", "lc": "america_central",
    "li": "europe_west", "lk": "asia_south", "lr": "africa_sub",
    "ls": "africa_southern", "lt": "europe_east", "lu": "europe_west", "lv": "europe_east", "ma": "africa_north",
    "mc": "europe_west", "md": "europe_east", "mf": "america_central",
    "mg": "africa_sub", "mh": "oceania", "mk": "europe_east", "ml": "africa_sub", "mm": "asia_southeast",
    "mn": "asia_east", "mo": "asia_east", "mp": "oceania",
    "mq": "america_central", "mr": "africa_sub", "mt": "europe_west", "mu": "asia_southeast", "mv": "europe_west",
    "mw": "africa_sub", "mx": "america_central", "my": "asia_southeast",
    "mz": "africa_sub", "na": "africa_southern", "nc": "oceania", "ne": "africa_sub", "nf": "oceania",
    "ng": "africa_sub", "ni": "america_central", "nl": "europe_west",
    "no": "europe_west", "np": "asia_south", "nr": "asia_southeast", "nz": "oceania", "om": "middle_east",
    "pa": "america_central", "pe": "america_south", "pf": "asia_southeast",
    "pg": "asia_southeast", "ph": "asia_southeast", "pk": "asia_south", "pl": "europe_east", "pm": "america_north",
    "pr": "america_central", "ps": "middle_east", "pt": "europe_west",
    "pw": "asia_southeast", "py": "america_south", "qa": "middle_east", "re": "africa_sub", "ro": "europe_east",
    "rs": "europe_east", "ru": "europe_russia", "rw": "africa_sub",
    "sa": "middle_east", "sb": "asia_southeast", "sc": "asia_south", "sd": "africa_north", "se": "europe_west",
    "sg": "asia_southeast", "si": "europe_east", "sk": "europe_east",
    "sl": "africa_sub", "sm": "asia_southeast", "sn": "africa_sub", "so": "africa_north", "sr": "america_south",
    "ss": "africa_sub", "su": "europe_russia", "sv": "america_central",
    "sx": "america_central", "sy": "middle_east", "sz": "africa_southern", "tc": "america_central", "td": "africa_sub",
    "tg": "africa_sub", "th": "asia_southeast", "tj": "asia_central",
    "tl": "asia_southeast", "tm": "asia_central", "tn": "africa_north", "tp": "asia_southeast", "tr": "middle_east",
    "tt": "america_central", "tw": "asia_east", "tz": "africa_sub",
    "ua": "europe_east", "ug": "africa_sub", "uk": "europe_west", "us": "america_north", "uy": "america_south",
    "uz": "asia_central", "va": "europe_west", "vc": "america_central",
    "ve": "america_south", "vg": "america_central", "vi": "america_central", "vn": "asia_southeast",
    "vu": "asia_southeast", "wf": "asia_southeast", "ye": "middle_east", "yt": "africa_sub",
    "za": "africa_southern", "zm": "africa_sub", "zw": "africa_southern", "ελ": "europe_west", "бг": "europe_east",
    "бел": "europe_east", "мкд": "europe_east", "рф": "europe_russia",
    "срб": "europe_east", "укр": "europe_east", "қаз": "asia_central", "հայ": "asia_central", "الاردن": "middle_east",
    "الجزائر": "africa_north", "السعودية": "middle_east", "المغرب": "middle_east",
    "امارات": "middle_east", "ایران": "middle_east", "بھارت": "asia_south", "تونس": "africa_north",
    "سودان": "africa_sub", "سورية": "middle_east", "عراق": "middle_east", "عمان": "middle_east",
    "فلسطين": "middle_east", "قطر": "middle_east", "مصر": "middle_east", "مليسيا": "asia_southeast",
    "موريتانيا": "africa_north", "پاكستان": "asia_south", "پاکستان": "asia_south", "ڀارت": "asia_south",
    "भारत": "asia_south", "বাংলা": "asia_south", "ভারত": "asia_south", "ਭਾਰਤ": "asia_south", "ભારત": "asia_south",
    "இந்தியா": "asia_south", "இலங்கை": "asia_south", "சிங்கப்பூர்": "asia_southeast",
    "భారత్": "asia_south", "ಭಾರತ": "asia_south", "ഭാരതം": "asia_south", "ලංකා": "asia_southeast",
    "ไทย": "asia_southeast", "中国": "asia_east", "中國": "asia_east", "台湾": "asia_east",
    "台灣": "asia_east", "新加坡": "asia_southeast", "澳門": "asia_east", "香港": "asia_east", "한국": "asia_east",
    "st": "africa_sub"
}
