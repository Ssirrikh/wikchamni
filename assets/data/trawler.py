
# 13.0 hrs: dev trawler script
# 10.0 hrs: trawl data; record/label unhandled datapoints and inconsistencies
# 2.0 hrs: research mdf format, add mdf formatter
# 4.0 hrs: nameserver/pages/dns/record research
# 6.0 hrs: zoom meeting, powerpoint, email chain
# 1.0 hrs: meetings

#### NOTES ####

# inconsistent treatment of word forms
	# some large single entries with multiple labeled word forms/cases (generally n-theme/v-theme/etc)
	# in other cases, each word form gets its own entry and identifies the form in the "morph" field
	# some do both at once (duplicate data w/ no new info)
	# ex. "blood" has "n-theme" entry with all other forms as labeled paradigms, then each form gets its own separate entry
	# ex. "start" "čʼamna/" is labeled v instead of v-theme and has labeled forms
		# ditto for "bird nest" "čʼapix/"
	# chukchansi database stores all forms in one entry so they're easier to find/compare
# possible inconsistent treatment of literal meanings
	# some eng words translate into a multi-word phrase
		# phrase appears as example sentence w/ "lit." section explaining literal meaning
		# stored in the entry for one of the words in the sentence
		# eng word + wik phrase may or may not have their own entries
		# ex. "automobile" literally translates to "horse without a heart"
			# appears as example sentence in entry "without"
			# neither eng "automobile" or wikchamni phrase "horse without a heart" have their own entry
		# ex. "diarrhea plant" got its own full entry
	# sometimes a wikchamni word with a literal meaning is treated as a second word sense of that literal meaning
		# ex. sense 1 is literal phrase "something to be carried under the arm"
		# and sense 2 is "mountain balm" with literal meaning "something to be carried under the arm", since plant is carried under the arm as a deodorant
# what does "non-singular plural" mean? is it different than "non-singular, plural"?
# inconsistent catg labels and word form labels
	# several entries seem to be "v" instead of "v-theme", etc
	# some morph fields contain things like "nominative, accusative, locative case"
# several word forms are referenced in a n-theme/v-theme entry, but don't have their own entry (or got typoed)

#### TYPOS / MINOR ERRORS ####

# entry #1294 "peaches" has sentence typo "oeaches" -> "peaches"

#### FLAGGED BY SCRIPT ####

# ch.html entry #245 "(into the) bone" has audio from multiple speakers for same word (flagged "no translation")
# ch.html entry #300 "six" has audio from multiple speakers for same word (flagged "no translation")
# h.html entry #760 "mixing thing or place" has multiple word senses
	# sense 1: "mixing thing"/"mixing place"
	# sense 2: "baking soda", literally thing for mixing
# k.html entry #947 "something to be carried under the arm" has multiple word senses
	# sense 1: "something to be carried under the arm"
	# sense 2: "mountain balm (Ceanothus velutinus)", literally thing put under one's arm, because it was put in armpits as deodorant
# k.html entry #954 "enemy, opponent" has multiple word senses
	# sense 1: "enemy, opponent", literally one who does face washing
	# sense 2: "face-washer"
	# entry #954 lists word senses and nominative/accusative cases, but those cases also have full entries (#953/#955 respectively)
# n.html entry #1704 "seven at a time" has floating lpExample with no audio or translation
# s.html entry #2517 "three" has audio from multiple speakers for same word (flagged "no translation")
# t.html entry #3345 "play!" (imperative) has audio of variation which is only explained in phonology note
# t.html entry #3492 "take out!" (causative imperative) has multiple word senses
	# sense 1: "take out!"
	# sense 2: "take off!"
	# sense 3: "fish out!"
# t.html entry #3506 "(to the) cottontail" has audio from multiple speakers for same word (flagged "no translation")
# tr.html entry #3840 "grandmothers" has multiple word senses
	# sense 1: "grandmothers"
	# sense 2: "grandchildren, by daughter"
# y.html entry #4560 "five" has audio from multiple speakers for same word (flagged "no translation")
	# alt audio is captioned "Cecile saying the same word" instead of the word itself like most entries
# ʔ.html entry #5012 "song" has mislabeled audio
	# wikchamni transcription field contains "shooting star song"
	# english translation field is empty



import codecs
import re

FILE = 'pages/t.html'
FILE_STUB = """<p align="center" class="lpTitlePara">L  -  l</p>

<p class="lpLexEntryPara"><span class="lpLexEntryNameNew"></span><span id="e1280" class="lpLexEntryName">lame&middot;sa/</span><span class="lpSpAfterEntryName">&nbsp;&nbsp;&nbsp;</span><span class="lpPartOfSpeech">n-theme. </span><span class="lpGlossEnglish">table.</span> <span class="lpMiniHeading">nominative:&nbsp;</span><span class="lpParadigm">lame&middot;saʔ</span><span class="lpPunctuation">.</span> <span class="lpMiniHeading">locative:&nbsp;</span><span class="lpParadigm">lame&middot;saw</span><span class="lpPunctuation">.</span><span class="lpPunctuation"> </span> <span class="lpMiniHeading">From: </span><span class="lpBorrowedWord">Spanish la mesa</span><span class="lpPunctuation">.</span> <span class="lpMiniHeading">Note: </span><span class="lpNotes_general">Related language Yawelmani lame&middot;saʔ   Chukchansi lame&middot;saʔ  (NAS)</span></p>

<p class="lpLexEntryPara"><span class="lpLexEntryNameNew"></span><audio preload="none" id="table {loc}" src="audio/table {loc}.wav"></audio><a href="#" onclick="document.getElementById('table {loc}').play(); return false"><img border="0" src="images/sound-icon.png" /></a> <span id="e1281" class="lpLexEntryName">lame&middot;saw</span><span class="lpSpAfterEntryName">&nbsp;&nbsp;&nbsp;</span><span class="lpPartOfSpeech">n. </span><span class="lpGlossEnglish">on the table.</span> <audio preload="none" id="The water spilled on the table" src="audio/The water spilled on the table.wav"></audio><a href="#" onclick="document.getElementById('The water spilled on the table').play(); return false"><img border="0" src="images/sound-icon.png" /></a> <span class="lpExample">toxinši ʔitikʼ lame&middot;saw</span> <span class="lpGlossEnglish">The water spilled on the table.</span> <span class="lpMiniHeading">underlying form:&nbsp;</span><span class="lpParadigm">lame&middot;sa/ -w</span><span class="lpPunctuation">.</span><span class="lpPunctuation"> </span><span class="lpMiniHeading">Morph:&nbsp;</span><span class="lpMorph">locative case</span><span class="lpPunctuation">.</span></p>

<p class="lpLexEntryPara"><span class="lpLexEntryNameNew"></span><audio preload="none" id="table" src="audio/table.wav"></audio><a href="#" onclick="document.getElementById('table').play(); return false"><img border="0" src="images/sound-icon.png" /></a> <span id="e1282" class="lpLexEntryName">lame&middot;saʔ</span><span class="lpSpAfterEntryName">&nbsp;&nbsp;&nbsp;</span><span class="lpPartOfSpeech">n. </span><span class="lpGlossEnglish">table.</span> <span class="lpMiniHeading">underlying form:&nbsp;</span><span class="lpParadigm">lame&middot;sa/ -ʔ</span><span class="lpPunctuation">.</span><span class="lpPunctuation"> </span><span class="lpMiniHeading">Morph:&nbsp;</span><span class="lpMorph">absolutive</span><span class="lpPunctuation">.</span></p>

<p class="lpLexEntryPara"><span class="lpLexEntryNameNew"></span><audio preload="none" id="geese" src="audio/geese.wav"></audio><a href="#" onclick="document.getElementById('geese').play(); return false"><img border="0" src="images/sound-icon.png" /></a> <span id="e1283" class="lpLexEntryName">laʔlaʔ</span><span class="lpSpAfterEntryName">&nbsp;&nbsp;&nbsp;</span><span class="lpPartOfSpeech">n. </span><span class="lpGlossEnglish">geese, goose.</span> <span class="lpMiniHeading">Note: </span><span class="lpNotes_general">Related language Yawelmani laʔlaʔ Chankchansi  laʔlaʔ</span></p>

<p class="lpLexEntryPara"><span class="lpLexEntryNameNew"></span><audio preload="none" id="dish" src="audio/dish.wav"></audio><a href="#" onclick="document.getElementById('dish').play(); return false"><img border="0" src="images/sound-icon.png" /></a> <span id="e1284" class="lpLexEntryName">la&middot;tuʔ</span><span class="lpSpAfterEntryName">&nbsp;&nbsp;&nbsp;</span><span class="lpPartOfSpeech">n. </span><span class="lpGlossEnglish">dish.</span> <span class="lpMiniHeading">From: </span><span class="lpBorrowedWord">Spanish plato</span><span class="lpPunctuation">.</span> <span class="lpMiniHeading">Note: </span><span class="lpNotes_general">Related language Chukchansi bila&middot;suʔ  (NAS)</span></p>
"""



#####################################

#### HELPERS ####

def listTags (text, tag='', attributes=''):
	# $1 attribute list
	# $2 innerHTML
	pattern = fr"(?:<{tag}(.*?)>(.*?)<\/{tag}>)+?"
	regex = re.compile(pattern, re.MULTILINE)
	matches = regex.findall(text)
	return matches
def listAttributes (attributes):
	return re.findall(fr"\b(\w+)=\"(.*?)\"", attributes)
def containsClass (c, attributeTuples):
	for k,v in attributeTuples:
		if k == "class" and v == c:
			return True
	return False
def getClasses (attributes):
	classlist = []
	for type,contents in attributes:
		if type == "class":
			classlist.extend( re.split(r"\s+",contents) )
	return classlist
def getId (attributes):
	for type,contents in attributes:
		if type == "id":
			return contents



#### TOKENIZER ####

def tokenize (text):
	# isolate lexicon entries by unique class tag
	entriesRaw = []
	for attributes,contents in listTags(text, "p"):
		if containsClass("lpLexEntryPara",listAttributes(attributes)):
			entriesRaw.append(contents)
	# break entries into data tokens
	entryData = []
	for entry in entriesRaw:
		spans = []
		for attributes,contents in listTags(entry,"span"):
			spans.append( (listAttributes(attributes),contents) )
		entryData.append(spans)
	return entryData

#### tokenize() returns list of tokenstreams
# [
# 	[
# 		([('class', 'lpLexEntryNameNew')], ''), 
# 		([('id', 'e1280'), ('class', 'lpLexEntryName')], 'lame&middot;sa/'), 
# 		([('class', 'lpSpAfterEntryName')], '&nbsp;&nbsp;&nbsp;'), 
# 		([('class', 'lpPartOfSpeech')], 'n-theme. '), 
# 		([('class', 'lpGlossEnglish')], 'table.'), 
# 		([('class', 'lpMiniHeading')], 'nominative:&nbsp;'), 
# 		([('class', 'lpParadigm')], 'lame&middot;saʔ'), 
# 		([('class', 'lpPunctuation')], '.'), 
# 		([('class', 'lpMiniHeading')], 'locative:&nbsp;'), 
# 		([('class', 'lpParadigm')], 'lame&middot;saw'), 
# 		([('class', 'lpPunctuation')], '.'), 
# 		([('class', 'lpPunctuation')], ' '), 
# 		([('class', 'lpMiniHeading')], 'From: '), 
# 		([('class', 'lpBorrowedWord')], 'Spanish la mesa'), 
# 		([('class', 'lpPunctuation')], '.'), 
# 		([('class', 'lpMiniHeading')], 'Note: '), 
# 		([('class', 'lpNotes_general')], 'Related language Yawelmani lame&middot;saʔ   Chukchansi lame&middot;saʔ  (NAS)')
# 	], [
#		...
#	],
#	...
# ]



#### PARSER ####

# capture unrecognized fields
unknownFieldTypes = set() # set off CSS classes used to identify fields (ie "lpLexEntryName")
unknownFieldNames = set() # set of shorthand names for fields (ie "underlying")

# track recognized fields
FIELD_IGNORE = ['lpLexEntryNameNew','lpSpAfterEntryName','lpPunctuation']
FIELD_SINGLETON = ["english","catg","wikchamni", "notes","discourse","grmmar","anthropology","phonology","morphology","borrowed","encyclopediaInfo","scienceInfo","literalMeaning","underlying"]
FIELD_TYPE_NAMES = {
	# base word
	'lpLexEntryName' : 'wikchamni',
	'lpPartOfSpeech' : 'catg',
	'lpGlossEnglish' : 'english',
	# forms and sentences
	'lpMiniHeading' : 'fieldType',
	'lpParadigm' : 'paradigm', # can be word form or underlying form
	'lpExample' : 'exampleSentence',
	'lpCrossRef' : 'linkedWord',
	# notes
	'lpNotes_general' : 'notes',
	'lpNotes_discourse' : 'discourse',
	'lpNotes_grammar' : 'grammar',
	'lpNotes_anthropology' : 'anthropology',
	'lpNotes_phonology' : 'phonology',
	'lpMorph' : 'morphology',
	'lpBorrowedWord' : 'borrowed',
	'lpEncycInfoEnglish' : 'encyclopediaInfo',
	'lpScientific' : 'scienceInfo',
	'lpLiteralMeaningEnglish' : 'literalMeaning',
	'lpMainCrossRef' : 'variant',
}
FIELD_TYPE_ENTRY_LABEL = "lpLexEntryName"
FIELD_TYPE_HEADING = "lpMiniHeading"
FIELD_TYPE_PARADIGM = "lpParadigm"
FIELD_TYPE_EXAMPLE = "lpExample"
FIELD_TYPE_GLOSS = "lpGlossEnglish"
FIELD_TYPE_VARIANT = "lpMainCrossRef"
FIELD_TYPE_LINKED_WORD = "lpCrossRef"
FIELD_TYPE_LITERAL_MEANING = "lpLiteralMeaningEnglish"

class DataEntry:
	def __init__(self):
		# singleton fields: core entry
		self.entryId = -1
		self.english = ""          # \ge english gloss
		self.catg = ""             # \ps part of speech
		self.wikchamni = ""        # \lx primary wikchamni form used to identify entry in lexicon; formname may or may not be stored in morphology field
		# singleton fields: notes and info
		self.notes = ""            # \nt general note
		self.discourse = ""        # \nd discourse note
		self.grammar = ""          # \ng grammar note
		self.anthropology = ""     # \na anthropology note
		self.phonology = ""        # \np phonology note
		self.morphology = ""       # \mr morpheme representation and underlying forms
		self.borrowed = ""         # \bw borrowed word
		self.encyclopediaInfo = "" # \ee encyclopedia entry
		self.scienceInfo = ""      # \sc scientific name
		self.literalMeaning = ""   # \lt literal meaning
		self.underlying = ""       # \pd paradigm
		# collection fields
		self.forms = {}       # \pd paradigms
		self.variants = []    # \va variants
		self.examples = []    # either (\xv \ge \lt) or (\xv \xe \lt) example sentence + eng translation (+ literal meaning)
		self.linkedWords = [] # \mn main entry cross-reference
		self.media = []       # \pc pictures; MDF/shoebox doesn't support audio by default, likely stores them in \pc or custom field
		# debug
		self.flagged = False
		self.log = []
	def addField(self,fieldname,contents):
		if fieldname in FIELD_SINGLETON:
			if getattr(self,fieldname) != "":
				print(f"WARN Found duplicate \"{fieldname}\" field in entry \"{self.english}\"")
			setattr(self,fieldname,contents)
		else:
			unknownFieldNames.add(fieldname)
	def addWordForm(self,formname,form):
		if formname in self.forms:
			print(f"WARN Found duplicate \"{formname}\" form in entry \"{self.english}\"")
		self.forms[formname] = form
	def addWordVariant(self,variant):
		self.variants.append( variant )
	def addExample(self,wikchamni,english,literal):
		self.examples.append( (wikchamni,english,literal) )
	def addLinkedWord(self,word):
		self.linkedWords.append(word)
	def flag(self,msg = "Entry flagged; no reason given"):
		self.flagged = True
		self.log.append(msg)
		print(msg)
	def getMDF(self):
		# mandatory ordered components (\lx \ps), core entry
		mdf = f"\\lx {self.wikchamni}\n"
		mdf = f"{mdf}\\ps {self.catg}\n"
		mdf = f"{mdf}\\ge {self.english}\n"
		mdf = f"{mdf}\\id {self.entryId}\n" # use unsupported field \id for old entry id number
		# notes and info
		if self.notes != "": 			mdf = f"{mdf}\\nt {self.notes}\n"
		if self.discourse != "": 		mdf = f"{mdf}\\nd {self.discourse}\n"
		if self.grammar != "": 			mdf = f"{mdf}\\ng {self.grammar}\n"
		if self.anthropology != "": 	mdf = f"{mdf}\\na {self.anthropology}\n"
		if self.phonology != "": 		mdf = f"{mdf}\\np {self.phonology}\n"
		if self.morphology != "": 		mdf = f"{mdf}\\mr {self.morphology}\n"
		if self.borrowed != "": 		mdf = f"{mdf}\\bw {self.borrowed}\n"
		if self.encyclopediaInfo != "": mdf = f"{mdf}\\ee {self.encyclopediaInfo}\n"
		if self.scienceInfo != "": 		mdf = f"{mdf}\\sc {self.scienceInfo}\n"
		if self.literalMeaning != "": 	mdf = f"{mdf}\\lt {self.literalMeaning}\n"
		if self.underlying != "":
			mdf = f"{mdf}\\pdl underlying\n"
			mdf = f"{mdf}\\pdv {self.underlying}\n"
		# forms and examples
		for variant in self.variants:
			mdf = f"{mdf}\\va {variant}\n"
		for form in self.forms:
			mdf = f"{mdf}\\pdl {form}\n"
			mdf = f"{mdf}\\pdv {self.forms[form]}\n"
		for wikchamni,english,literal in self.examples:
			mdf = f"{mdf}\\xv {wikchamni}\n"
			mdf = f"{mdf}\\ge {english}\n"
			if literal != None: mdf = f"{mdf}\\lt {literal}\n"
		for word in self.linkedWords:
			mdf = f"{mdf}\\mn {word}\n"
		for file in self.media:
			mdf = f"{mdf}\\pc {file}\n"
		return mdf
	def print(self):
		print(f"Entry #{self.entryId}")
		print(f"{self.english} {self.catg} {self.wikchamni}")
		for form in self.forms:
			print(f"    FORM {form} : {self.forms[form]}")
		for variant in self.variants:
			print(f"    VARIANT {variant}")
		for wikchamni,english,literal in self.examples:
			print(f"    SENTENCE {wikchamni} -> {english}")
			if literal != None:
				print(f"        LIT {literal}")
		for word in self.linkedWords:
			print(f"    CROSSREF {word}")
		for file in self.media:
			print(f"    MEDIA {file}")
		if self.notes != "":
			print(f"    Notes: {self.notes}")
		if self.discourse != "":
			print(f"    Discourse Notes: {self.discourse}")
		if self.grammar != "":
			print(f"    Grammar Notes: {self.grammar}")
		if self.anthropology != "":
			print(f"    Anthropology: {self.anthropology}")
		if self.phonology != "":
			print(f"    Phonology: {self.phonology}")
		if self.morphology != "":
			print(f"    Morphology: {self.morphology}")
		if self.borrowed != "":
			print(f"    Borrowed: {self.borrowed}")
		if self.encyclopediaInfo != "":
			print(f"    Encyclopedia Info: {self.encyclopediaInfo}")
		if self.scienceInfo != "":
			print(f"    Scientific Notes: {self.scienceInfo}")
		if self.literalMeaning != "":
			print(f"    Literally: {self.literalMeaning}")
		if self.underlying != "":
			print(f"    Underlying Form: {self.underlying}")

def parse (data):
	entries = []
	for tokenList in data:
		entry = DataEntry()
		i = 0

		def peek():
			return tokenList[i]
		def pop():
			nonlocal i
			i = i + 1
			return tokenList[i-1] if len(tokenList) >= i else ([],None)
		def unpop():
			# backtrack in case parser consumed token of unexpected type (possible missing token)
			nonlocal i
			i = i - 1
			return tokenList[i]

		while i < len(tokenList):
			currAttributes,currContents = pop()
			currClasslist = getClasses(currAttributes)
			for currFieldname in currClasslist:
				# track unknown token types
				if currFieldname not in FIELD_IGNORE and currFieldname not in FIELD_TYPE_NAMES:
					unknownFieldTypes.add(currFieldname)
					entry.flag(f"WARN Unknown field type \"{currFieldname}\"")
				# lpExample tokens is \xv example sentence; try to consume \ge translation for it
				elif currFieldname == FIELD_TYPE_EXAMPLE:
					nextAttributes,nextContents = pop()
					nextClasslist = getClasses(nextAttributes)
					for nextFieldname in nextClasslist:
						if nextFieldname == FIELD_TYPE_GLOSS:
							# if we found a sentence and a translation (\xv \ge), check for a literal meaning (\xv \ge \lt)
							pop() # discard label
							nextNextAttributes,nextNextContents = pop()
							nextNextClasslist = getClasses(nextNextAttributes)
							for nextNextFieldname in nextNextClasslist:
								if nextNextFieldname == FIELD_TYPE_LITERAL_MEANING:
									entry.addExample(currContents, nextContents, nextNextContents)
									entry.flag(f"4T example sentence with literal translation \"{currContents}\" = \"{nextContents}\" (Lit: \"{nextNextContents}\")")
								else:
									unpop()
									unpop()

							entry.addExample(currContents, nextContents, None)
							print(f"2T example sentence \"{currContents}\" = \"{nextContents}\"")
						else:
							entry.flag(f"WARN No translation found for sentence \"{currContents}\"; next field was of type \"{nextFieldname}\"")
							unpop()
				# lpMiniHeading tokens serve as labels for the next token
				elif currFieldname == FIELD_TYPE_HEADING:
					nextAttributes,nextContents = pop()
					nextClasslist = getClasses(nextAttributes)
					formNameClean = re.sub(r"\W", '', re.sub(r"&nbsp", '', currContents)).lower() # remove html spacing, remove non-word chars, lowercase
					for nextFieldname in nextClasslist:
						# track unknown token types
						if nextFieldname not in FIELD_IGNORE and nextFieldname not in FIELD_TYPE_NAMES:
							unknownFieldTypes.add(nextFieldname)
							entry.flag(f"WARN Unknown field type \"{nextFieldname}\" under heading \"{formNameClean}\"")
						# special case: store "underlying form" \pd tokens as singleton field instead of general word form
						elif nextFieldname == FIELD_TYPE_PARADIGM and formNameClean == "underlyingform":
							entry.addField("underlying", nextContents)
							print(f"2T underlying form \"{nextContents}\"")
						# check if next token is \va spelling variation
						elif nextFieldname == FIELD_TYPE_VARIANT:
							entry.addWordVariant(nextContents)
							print(f"2T variant \"{formNameClean}\" = \"{nextContents}\"")
							if formNameClean != "variant":
								entry.flag(f"WARN Detected lpMainCrossRef that was not of type \"variant\"")
						# check if next token is \mn linked word
						elif nextFieldname == FIELD_TYPE_LINKED_WORD:
							entry.addLinkedWord(nextContents)
							print(f"2T linked word \"{nextContents}\"")
							if formNameClean != "see":
								entry.flag(f"WARN Detected lpCrossRef that was not of type \"see (linked word)\"")
						# check if next token is recognized singleton field
						elif FIELD_TYPE_NAMES[nextFieldname] in FIELD_SINGLETON:
							entry.addField(FIELD_TYPE_NAMES[nextFieldname], nextContents)
							print(f"2T singleton field \"{FIELD_TYPE_NAMES[nextFieldname]}\" = \"{nextContents}\"")
						# otherwise treat it as a word form
						else:
							entry.addWordForm(formNameClean, nextContents)
							print(f"2T word form \"{formNameClean}\" = \"{nextContents}\"")
				# check if current token is a recognized singleton field
				elif currFieldname in FIELD_TYPE_NAMES:
					entry.addField(FIELD_TYPE_NAMES[currFieldname],currContents)
					print(f"1T singleton field \"{FIELD_TYPE_NAMES[currFieldname]}\" = \"{currContents}\"")
					# if this token is the \lx main entry label, extract the entry id from it
					if currFieldname == FIELD_TYPE_ENTRY_LABEL:
						currId = int(re.sub(r"[^0-9]+", '', getId(currAttributes)))
						entry.entryId = currId
						print(f"SP entry id \"{currId}\"")
				# else we must be on the ignore list
					# no-op
			if len(currClasslist) > 1:
				entry.flag(f"WARN MULTICLASS {currClasslist}")
		if len(entries) > 0: print("-----")
		entry.print()
		entries.append(entry)
	return entries



######################################

#### MAIN ####

# stub_data = tokenize(FILE_STUB)
# stub_entries = parse(stub_data)
# for entry in stub_entries:
# 	entry.print()
# 	print("-----")

with codecs.open(FILE, encoding='utf-8') as f:
	# parse data (verbose by default)
	print("=== Parsing Data... ===\n")
	data = tokenize( f.read() )
	entries = parse(data)

	# print flagged entries for diagnosis
	print("\n=== Flagged Entries ===\n")
	numEntriesFlagged = 0
	for entry in entries:
		if entry.flagged:
			if numEntriesFlagged > 0: print("-----")
			numEntriesFlagged += 1
			entry.print()
			print(entry.log)

	# print MDF formatter output
	print("\n=== MDF Formatting ===\n")
	mdfTarget = "tuʔ"
	print(f"Printing MDF for entries containing headword \"{mdfTarget}\"...\n")
	for entry in entries:
		# if entry.catg != "v. " and entry.catg != "v-theme. ":
		if entry.wikchamni != "tuʔ":
			continue
		print(entry.getMDF())


	# entries identifying roots
	print("\n=== Word Forms ===\n")
	themes = ["n-theme. ", "v-theme. ", "prn-theme. "]
	themeForms = []
	for entry in entries:
		if entry.catg not in themes:
			if len(entry.forms) > 0:
				print(f"NOTE NON_THEME_FORMS Entry #{entry.entryId} \"{entry.english}\" of catg \"{entry.catg}\" was not labeled as a word-theme entry, but contained forms {entry.forms}")
			continue
		elif len(entry.forms) == 0:
			print(f"NOTE THEME_NO_FORMS Entry #{entry.entryId} \"{entry.english}\" of catg \"{entry.catg}\" was labeled as a word-theme entry, but had no forms.")
		formCollection = []
		for form in entry.forms:
			formCollection.append( (form,entry.forms[form]) )
		themeForms.append( (entry.entryId, entry.catg, formCollection) )
	print("")



	## print statistics

	# counts
	print("\n=== Statistics ===\n")
	print(f"{len(entries)} entries processed, {numEntriesFlagged} of which were flagged for a closer look.\n")
	# unrecognized fields
	if len(unknownFieldTypes) > 0:
		print(f"Encountered {len(unknownFieldTypes)} unsupported fields: {unknownFieldTypes}\n")
	# parts of speech and word forms
	wordforms = {}
	catgCounts = {}
	catgCollectionCounts = {
		'themes' : 0,
		'nouns' : 0,
		'verbs' : 0,
		'misc' : 0
	}
	for entry in entries:
		if entry.catg not in wordforms:
			wordforms[entry.catg] = set()
			catgCounts[entry.catg] = 0
		if entry.morphology != "":
			wordforms[entry.catg].add(entry.morphology)
			catgCounts[entry.catg] += 1
	for catg in wordforms:
		print(f"{len(wordforms[catg])} uniq word forms across {catgCounts[catg]} entries of catg \"{catg}\"")
		for form in wordforms[catg]:
			print(f"    {form}")
	for catg in catgCounts:
		if catg in themes:
			catgCollectionCounts['themes'] += catgCounts[catg]
		elif catg == "n. ":
			catgCollectionCounts['nouns'] += catgCounts[catg]
		elif catg == "v. ":
			catgCollectionCounts['verbs'] += catgCounts[catg]
		else:
			catgCollectionCounts['misc'] += catgCounts[catg]
	print(f"\nDatabase contained {catgCollectionCounts['themes']} word-theme entries, {catgCollectionCounts['nouns']} nouns, {catgCollectionCounts['verbs']} verbs, and {catgCollectionCounts['misc']} misc entries.")

	# word forms
	foundForms = {}
	numFormsFound = 0
	for entryId,catg,forms in themeForms:
		# print(f"Entry #{entryId} of catg \"{catg}\": {forms}")
		for formName,wordForm in forms:
			foundForms[wordForm] = False
	for entry in entries:
		if entry.wikchamni in foundForms:
			foundForms[entry.wikchamni] = True
	print("")
	for form in foundForms:
		if foundForms[form] == True:
			numFormsFound += 1
		else:
			print(f"\"{form}\" was listed in a word-theme entry, but didn't have its own entry.")
	print(f"\n{len(foundForms)-numFormsFound} out of {len(foundForms)} word-forms referenced in a word-theme entry don't have their own entry.\n")



