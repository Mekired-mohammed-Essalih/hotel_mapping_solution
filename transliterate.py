import sys
import abc

if sys.version_info >= (3, 4):
	ABC = abc.ABC
else:
	ABC = abc.ABCMeta('ABC', (), {})


class Trans(ABC):

	def __init__(self):
		pass

	def trans(self, word):
		return self.transliterate(word)

	@abc.abstractmethod
	def transliterate(self, word):
		return word

	def untrans(self, word):
		return self.untransliterate(word)

	@abc.abstractmethod
	def untransliterate(self, word):
		return word

class MapTrans(Trans):

	def __init__(self, the_map):
		self.the_map = the_map

	def transliterate(self, word):
		res = ""
		if len(word) < len(self.the_map):
			for char in word:
				res += self.the_map.get(char, char)
		else:
			res = word
			for k,v in self.the_map.items():
				res = res.replace(k, v)

		return res

	def untransliterate(self, word):
		res = word
		for k,v in self.the_map.items():
			res = res.replace(v, k)

		return res


class L2LTrans(Trans):

	def __init__(self, src, dst):
		self.src = src
		self.dst = dst

	def transliterate(self, word):
		res = word
		for i, v in enumerate(self.src):
			res = res.replace(v, self.dst[i])
		return res

	def untransliterate(self, word):
		res = word
		for i, v in enumerate(self.dst):
			res = res.replace(v, self.src[i])
		return res


buckwalter_map =	{
		u"ا": "A", # alif
		u"ب": "b", # ba
		u"ت": "t", # ta
		u"ث": "th", # tha
		u"ج": "j", # jim
		u"ح": "H", # Ḥa
		u"خ": "kh", # kha
		u"د": "d", # dal
		u"ذ": "d", # dhal
		u"ر": "r", # ra
		u"ز": "z", # zin
		u"س": "s", # sin
		u"ش": "ch", # shin
		u"ص": "S", # ṣad
		u"ض": "D", # Ḍad
		u"ط": "T", # Ṭa
		u"ظ": "Z", # Ẓa
		u"ع": "E", # 'Ayn
		u"غ": "gh", # ghayn
		u"ف": "f", # fa
		u"ق": "q", # qaf
		u"ك": "k", # kaf
		u"ل": "l", # lam
		u"م": "m", # mim
		u"ن": "n", # nun
		u"ه": "h", # ha
		u"و": "w", # waw
		u"ي": "y", # ya
		u"٠": "0", # ya
		u"١": "1", # ya
		u"٢": "2", # ya
		u"٣": "3", # ya
		u"٤": "4", # ya
		u"٥": "5", # ya
		u"٦": "6", # ya
		u"٧": "7", # ya
		u"٨": "8", # ya
		u"٩": "9", # ya

		#hamza
		u"ء": "'", # lone hamza
		u"أ": "A", # hamza on alif
		u"إ": "ii", # hamza below alif
		u"ؤ": "u", # hamza on waw
		u"ئ": "y'", # hamza on ya
		#alif
		u"آ": "Ae", # madda on alif
		u"ٱ": "eu", # alif alwasla
		u"\u0670": "`", # dagger alif
		u"ى": "Y", # alif maqsura
		#harakat
		u"\u064E": "a", # fatha
		u"\u064F": "u", # Damma
		u"\u0650": "i", # kasra
		u"\u064B": "F", # fathatayn
		u"\u064C": "N", # dammatayn
		u"\u064D": "K", # kasratayn
		u"\u0651": "~", # shadda
		u"\u0640": "_", # tatwil
		#others
		u"ة": "", # ta marbuta
		u"\u0652": "o", # sukun
}


iso233_map =	{
		u"ا": u"ʾ", # alif
		u"ب": u"b", # ba
		u"ت": u"t", # ta
		u"ث": u"ṯ", # tha
		u"ج": u"ǧ", # jim
		u"ح": u"ḥ", # Ḥa
		u"خ": u"ẖ", # kha
		u"د": u"d", # dal
		u"ذ": u"ḏ", # dhal
		u"ر": u"r", # ra
		u"ز": u"z", # zin
		u"س": u"s", # sin
		u"ش": u"š", # shin
		u"ص": u"ṣ", # ṣad
		u"ض": u"ḍ", # Ḍad
		u"ط": u"ṭ", # Ṭa
		u"ظ": u"ẓ", # Ẓa
		u"ع": u"ʿ", # 'Ayn
		u"غ": u"ġ", # ghayn
		u"ف": u"f", # fa
		u"ق": u"q", # qaf
		u"ك": u"k", # kaf
		u"ل": u"l", # lam
		u"م": u"m", # mim
		u"ن": u"n", # nun
		u"ه": u"h", # ha
		u"و": u"w", # waw
		u"ي": u"y", # ya
		#hamza
		u"ء": u"ˌ", # lone hamza
		u"أ": u"ˈ", # hamza on alif
		u"إ": u"ʾ", # hamza below alif
		u"ؤ": u"ˈ", # hamza on waw
		u"ئ": u"ˈ", # hamza on ya
		#alif
		u"\u0622": u"ʾ", # madda on alif
		u"\u0671": u"ʾ", # alif alwasla
		u"\u0670": u"ʾ", # dagger alif
		u"ى": u"ỳ", # alif maqsura
		u"ة": u"ẗ", # ta marbuta
}

arabic = [
	u"ث", # tha
	u"ح", # Ḥa
	u"خ", # kha
	u"ذ", # dhal
	u"ش", # shin
	u"ص", # ṣad
	u"ض", # Ḍad
	u"ط", # Ṭa
	u"ظ", # Ẓa
	u"غ", # ghayn
	u"ب", # ba
	u"ت", # ta
	u"ج", # jim
	u"د", # dal
	u"ر", # ra
	u"ز", # zin
	u"س", # sin
	u"ع", # 'Ayn
	u"ف", # fa
	u"ق", # qaf
	u"ك", # kaf
	u"ل", # lam
	u"م", # mim
	u"ن", # nun
	u"ه", # ha
	u"و", # waw
	u"ي", # ya
	u"أ", # hamza on alif
	u"إ", # hamza below alif
	u"ؤ", # hamza on waw
	u"ئ", # hamza on ya
	u"آ", # madda on alif
	u"\u0671", # alif alwasla
	u"\u0670", # dagger alif
	u"ى", # alif maqsura
	u"\u064B", # fathatayn
	u"\u064C", # dammatayn
	u"\u064D", # kasratayn
	u"\u064E", # fatha
	u"\u064F", # Damma
	u"\u0650", # kasra
	u"\u0651", # shadda
	u"\u0640", # tatwil
	u"ة", # ta marbuta
	u"\u0652", # sukun
	u"ء", # lone hamza
	u"ا" # alif
]

arabtex_tab = [
	"_t", # tha
	".h", # Ḥa
	"_h", # kha
	"_d", # dhal
	"^s", # shin
	".s", # ṣad
	".d", # Ḍad
	".t", # Ṭa
	".z", # Ẓa
	".g", # ghayn
	"b", # ba
	"t", # ta
	"j", # jim
	"d", # dal
	"r", # ra
	"z", # zin
	"s", # sin
	"`", # 'Ayn
	"f", # fa
	"q", # qaf
	"k", # kaf
	"l", # lam
	"m", # mim
	"n", # nun
	"h", # ha
	"w", # waw or "U"
	"y", # ya or "I"

	"'", # hamza on alif
	"'i", # hamza below alif
	"'", # hamza on waw
	"'", # hamza on ya

	"'A", # madda on alif
	"|", # alif alwasla <<<<<<
	"_a", # dagger alif <<<<<<
	"_A", # alif maqsura

	"aN", # fathatayn
	"uN", # dammatayn
	"iN", # kasratayn
	"a", # fatha
	"u", # Damma
	"i", # kasra
	"xx", # shadda
	"--", # tatwil

	"T", # ta marbuta
	"\"", # sukun

	"'", # lone hamza
	"A" # alif
  ]



class Buckwalter(MapTrans):

	def __init__(self):
		MapTrans.__init__(self, buckwalter_map)

buckwalter = Buckwalter()

class ArabTex(L2LTrans):

	def __init__(self):
		L2LTrans.__init__(self, arabic, arabtex_tab)

arabtex = ArabTex()

class Iso233(MapTrans):

	def __init__(self):
		MapTrans.__init__(self, iso233_map)

	def untransliterate(self, word):
		res = word.replace(u"ˈ", u"أ").replace(u"ʾ", u"ا")
		return MapTrans.untransliterate(self, res)

iso233 = Iso233()

#print(buckwalter.transliterate("Kreuznacher Strasse 37, 60486, فرانكفورت, Germany"))
#print (buckwalter.untransliterate('hdA AlbrnAmj yETynA nTq AlHrwf Alfndq Aldhby'))