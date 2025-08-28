
# 10.0 hrs: dev trawler script
# 6.0 hrs: zoom meeting, powerpoint, email chain
# 1.0 hrs: meetings

# entry 1294 "peaches" has sentence typo "oeaches" -> "peaches"

import codecs
import re

FILE = 'pages/ch.html'
FILE_STUB = """<p align="center" class="lpTitlePara">L  -  l</p>

<p class="lpLexEntryPara"><span class="lpLexEntryNameNew"></span><span id="e1280" class="lpLexEntryName">lame&middot;sa/</span><span class="lpSpAfterEntryName">&nbsp;&nbsp;&nbsp;</span><span class="lpPartOfSpeech">n-theme. </span><span class="lpGlossEnglish">table.</span> <span class="lpMiniHeading">nominative:&nbsp;</span><span class="lpParadigm">lame&middot;saʔ</span><span class="lpPunctuation">.</span> <span class="lpMiniHeading">locative:&nbsp;</span><span class="lpParadigm">lame&middot;saw</span><span class="lpPunctuation">.</span><span class="lpPunctuation"> </span> <span class="lpMiniHeading">From: </span><span class="lpBorrowedWord">Spanish la mesa</span><span class="lpPunctuation">.</span> <span class="lpMiniHeading">Note: </span><span class="lpNotes_general">Related language Yawelmani lame&middot;saʔ   Chukchansi lame&middot;saʔ  (NAS)</span></p>

<p class="lpLexEntryPara"><span class="lpLexEntryNameNew"></span><audio preload="none" id="table {loc}" src="audio/table {loc}.wav"></audio><a href="#" onclick="document.getElementById('table {loc}').play(); return false"><img border="0" src="images/sound-icon.png" /></a> <span id="e1281" class="lpLexEntryName">lame&middot;saw</span><span class="lpSpAfterEntryName">&nbsp;&nbsp;&nbsp;</span><span class="lpPartOfSpeech">n. </span><span class="lpGlossEnglish">on the table.</span> <audio preload="none" id="The water spilled on the table" src="audio/The water spilled on the table.wav"></audio><a href="#" onclick="document.getElementById('The water spilled on the table').play(); return false"><img border="0" src="images/sound-icon.png" /></a> <span class="lpExample">toxinši ʔitikʼ lame&middot;saw</span> <span class="lpGlossEnglish">The water spilled on the table.</span> <span class="lpMiniHeading">underlying form:&nbsp;</span><span class="lpParadigm">lame&middot;sa/ -w</span><span class="lpPunctuation">.</span><span class="lpPunctuation"> </span><span class="lpMiniHeading">Morph:&nbsp;</span><span class="lpMorph">locative case</span><span class="lpPunctuation">.</span></p>

<p class="lpLexEntryPara"><span class="lpLexEntryNameNew"></span><audio preload="none" id="table" src="audio/table.wav"></audio><a href="#" onclick="document.getElementById('table').play(); return false"><img border="0" src="images/sound-icon.png" /></a> <span id="e1282" class="lpLexEntryName">lame&middot;saʔ</span><span class="lpSpAfterEntryName">&nbsp;&nbsp;&nbsp;</span><span class="lpPartOfSpeech">n. </span><span class="lpGlossEnglish">table.</span> <span class="lpMiniHeading">underlying form:&nbsp;</span><span class="lpParadigm">lame&middot;sa/ -ʔ</span><span class="lpPunctuation">.</span><span class="lpPunctuation"> </span><span class="lpMiniHeading">Morph:&nbsp;</span><span class="lpMorph">absolutive</span><span class="lpPunctuation">.</span></p>

<p class="lpLexEntryPara"><span class="lpLexEntryNameNew"></span><audio preload="none" id="geese" src="audio/geese.wav"></audio><a href="#" onclick="document.getElementById('geese').play(); return false"><img border="0" src="images/sound-icon.png" /></a> <span id="e1283" class="lpLexEntryName">laʔlaʔ</span><span class="lpSpAfterEntryName">&nbsp;&nbsp;&nbsp;</span><span class="lpPartOfSpeech">n. </span><span class="lpGlossEnglish">geese, goose.</span> <span class="lpMiniHeading">Note: </span><span class="lpNotes_general">Related language Yawelmani laʔlaʔ Chankchansi  laʔlaʔ</span></p>

<p class="lpLexEntryPara"><span class="lpLexEntryNameNew"></span><audio preload="none" id="dish" src="audio/dish.wav"></audio><a href="#" onclick="document.getElementById('dish').play(); return false"><img border="0" src="images/sound-icon.png" /></a> <span id="e1284" class="lpLexEntryName">la&middot;tuʔ</span><span class="lpSpAfterEntryName">&nbsp;&nbsp;&nbsp;</span><span class="lpPartOfSpeech">n. </span><span class="lpGlossEnglish">dish.</span> <span class="lpMiniHeading">From: </span><span class="lpBorrowedWord">Spanish plato</span><span class="lpPunctuation">.</span> <span class="lpMiniHeading">Note: </span><span class="lpNotes_general">Related language Chukchansi bila&middot;suʔ  (NAS)</span></p>
"""

# tagFinder = /(?:<span(.*?)>(.*?)<\/span>)+?/gm

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

# # isolate lexicon entries by unique class tag
# entriesRaw = []
# for attributes,contents in listTags(FILE_STUB, "p"):
# 	if containsClass("lpLexEntryPara",listAttributes(attributes)):
# 		entriesRaw.append(contents)

# # break entries into data tokens
# entryData = []
# for entry in entriesRaw:
# 	spans = []
# 	for attributes,contents in listTags(entry,"span"):
# 		spans.append( (listAttributes(attributes),contents) )
# 	entryData.append(spans)

#
FIELD_IGNORE = ['lpLexEntryNameNew','lpSpAfterEntryName','lpPunctuation']
FIELD_SINGLETON = ["english","catg","wikchamni","notes","discourse","phonology","morphology","borrowed","underlying"]
FIELD_TYPE_NAMES = {
	'lpLexEntryName' : 'wikchamni',
	'lpPartOfSpeech' : 'catg',
	'lpGlossEnglish' : 'english',
	'lpMiniHeading' : 'fieldType',
	'lpParadigm' : 'paradigm', # can be word form or underlying form
	'lpExample' : 'exampleSentence',
	'lpBorrowedWord' : 'borrowed',
	'lpNotes_general' : 'notes',
	'lpMorph' : 'morphology',

	'lpMainCrossRef' : 'variant',
	'lpNotes_discourse' : 'discourse'
}
FIELD_TYPE_ENTRY_LABEL = "lpLexEntryName"
FIELD_TYPE_HEADING = "lpMiniHeading"
FIELD_TYPE_PARADIGM = "lpParadigm"
FIELD_TYPE_EXAMPLE = "lpExample"
FIELD_TYPE_GLOSS = "lpGlossEnglish"
FIELD_TYPE_VARIANT = "lpMainCrossRef"

unknownFieldTypes = set() # set off CSS classes used to identify fields (ie "lpLexEntryName")
unknownFieldNames = set() # set of 
wordForms = set() # set of word form names (ie "nominative")

class DataEntry:
	def __init__(self):
		# singleton fields
		self.entryId = -1
		self.english = ""
		self.catg = ""
		self.wikchamni = "" # primary wikchamni form used to identify entry in lexicon; formname unknown
		self.notes = ""
		self.discourse = ""
		self.phonology = ""
		self.morphology = ""
		self.borrowed = ""
		self.underlying = ""
		# collection fields
		self.forms = {}
		self.variants = []
		self.examples = []
		# debug
		self.flagged = False
		self.log = []
	def addField(self,fieldname,contents):
		if fieldname in FIELD_SINGLETON:
			# print(getattr(self,fieldname)) # throws error that self is not subscriptable
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
	def addExample(self,wikchamni,english):
		self.examples.append( (wikchamni,english) )
	def flag(self,msg = "Entry flagged; no reason given"):
		self.flagged = True
		self.log.append(msg)
		print(msg)
	def print(self):
		print(f"Entry #{self.entryId}")
		print(f"{self.english} {self.catg} {self.wikchamni}")
		for form in self.forms:
			print(f"    FORM {form} : {self.forms[form]}")
		for variant in self.variants:
			print(f"    VARIANT {variant}")
		for wikchamni,english in self.examples:
			print(f"    SENTENCE {wikchamni} -> {english}")
		if self.notes != "":
			print(f"    Notes: {self.notes}")
		if self.discourse != "":
			print(f"    Discourse Notes: {self.discourse}")
		if self.phonology != "":
			print(f"    Phonology: {self.phonology}")
		if self.morphology != "":
			print(f"    Morphology: {self.morphology}")
		if self.borrowed != "":
			print(f"    Borrowed: {self.borrowed}")
		if self.underlying != "":
			print(f"    Underlying Form: {self.underlying}")

parsedEntries = []
def trawl (data):
	entries = []
	for tokenList in data:
		entry = DataEntry()
		i = 0

		def peek():
			return tokenList[i]
		def pop():
			nonlocal i
			i = i + 1
			return tokenList[i-1]
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
					# print(f"WARN Unknown field type \"{currFieldname}\"")
					entry.flag(f"WARN Unknown field type \"{currFieldname}\"")
				# lpExample tokens is example sentence; try to consume translation for it
				elif currFieldname == FIELD_TYPE_EXAMPLE:
					nextAttributes,nextContents = pop()
					nextClasslist = getClasses(nextAttributes)
					for nextFieldname in nextClasslist:
						if nextFieldname == FIELD_TYPE_GLOSS:
							entry.addExample(currContents, nextContents)
							print(f"2T example sentence \"{currContents}\" = \"{nextContents}\"")
						else:
							# print(f"ERROR No translation found for sentence \"{currContents}\"; next field was of type \"{nextFieldname}\"")
							entry.flag(f"ERROR No translation found for sentence \"{currContents}\"; next field was of type \"{nextFieldname}\"")
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
							# print(f"WARN Unknown field type \"{nextFieldname}\" under heading \"{formNameClean}\"")
							entry.flag(f"WARN Unknown field type \"{nextFieldname}\" under heading \"{formNameClean}\"")
						# special case: convert "underlying form" tokens from general word form to singleton field
						elif nextFieldname == FIELD_TYPE_PARADIGM and formNameClean == "underlyingform":
							entry.addField("underlying", nextContents)
							print(f"2T underlying form \"{nextContents}\"")
						# check if next token is spelling variation
						elif nextFieldname == FIELD_TYPE_VARIANT:
							entry.addWordVariant(nextContents)
							print(f"2T variant \"{formNameClean}\" = \"{nextContents}\"")
							if formNameClean != "variant":
								# print(f"WARN Detected lpMainCrossRef that was not of type \"variant\"")
								entry.flag(f"WARN Detected lpMainCrossRef that was not of type \"variant\"")
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
					# if this token is the main entry label, extract the entry id from it
					if currFieldname == FIELD_TYPE_ENTRY_LABEL:
						currId = int(re.sub(r"[^0-9]+", '', getId(currAttributes)))
						entry.entryId = currId
						print(f"SP entry id \"{currId}\"")
				# else we must be on the ignore list
					# no-op
			if len(currClasslist) > 1:
				# print(f"WARN MULTICLASS {currClasslist}")
				entry.flag(f"WARN MULTICLASS {currClasslist}")
		entry.print()
		print("-----")
		entries.append(entry)
	return entries


# stub_data = tokenize(FILE_STUB)
# stub_entries = trawl(stub_data)
# for entry in stub_entries:
# 	entry.print()
# 	print("-----")

with codecs.open(FILE, encoding='utf-8') as f:
	data = tokenize( f.read() )
	entries = trawl(data)
	print("========")
	numEntriesFlagged = 0
	for entry in entries:
		entry.print()
		print("-----")
		if entry.flagged:
			numEntriesFlagged += 1
	print("========")
	print(f"{len(entries)} entries processed, {numEntriesFlagged} of which were flagged for a closer look.")

#### tokenize() returns parse as list of tokenstreams
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

