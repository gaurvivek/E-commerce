import nltk
import string
import re
import MySQLdb
total1=0
nouns=[]
adj=[]
first_values = []
db = MySQLdb.connect(host="localhost",    # your host, usually localhost
		             user="root",         # your username
		             passwd="root",  # your password
		             db="word")        # name of the data base
cur = db.cursor()
text1=''
'''def input1():
	text1 = ' '.join(input1)
	print text1
	return text1'''
def process():
    punctuations = list(string.punctuation)
    punctuations
    ['/DT','!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
    punctuations.append("''")
    text = "hiiiiiiii"
    #read the text into the variable "text"
    tokens = nltk.word_tokenize(text)
    punct = [i for i in tokens if i not in punctuations]
    tagged=nltk.pos_tag(punct)
    sentance = tagged
    grammar = "NP: {<NN>?<ADJ>?<JJ>?<NN>}"
    grammar = '''N: {<.*>+}
               }<CC|CD|DT|EX|FT|IN|LS|MD|PDT|POS|PRP|RB|RBR|RBS|RP|TO|UH|VB|VBD|VBG|VBI|VBN|VBZ|VDB|VDG|VDI|VDN|VDZ|VHB|VHD|VHG|VHI|VHN|VHZ|VM0|VDD|VBG|VBN|VBP|WP|WRP|VBZ|ADP|ADV|CONJ|DET|NUM|PRTPRON|VERB|IN|NNP|VBG|VBZ|X>{'''
    cp = nltk.RegexpParser(grammar)
    result = cp.parse(sentance)
    p2 = str(result).strip('[]')
    print1 = " ".join(word.split("/")[0] for word in p2.split())
    return print1; 
def overall(o1):
	total1=0
	total=0
	first_value=0
	p = re.findall(r"(\w+)\s+(?=product)", o1)
	p1 = re.findall(r"(\w+)\s+(?=thing)", o1)
	p2 = re.findall(r"(\w+)\s+(?=is|are|am|has|have|was|were)", o1)
	p3 = re.findall(r"(\w+)\s+(?=product)", process())
	p4 = re.findall(r"product(\w+)",process())
	p5 = re.findall(r"(\w+)\s+(?=overall)", o1)
	p6 = re.findall(r"(\w+)\s+(?=all)", o1)
	p7 = re.findall(r"(\w+)\s+(?=display)", o1)
	p8 = re.findall(r"(\w+)\s+(?=per)", o1)
	p9 = re.findall(r"(\w+)\s+(?=performance)", o1)
	p10 = re.findall(r"(\w+)\s+(?=camera)", o1)
	p11 = re.findall(r"(\w+)\s+(?=design)", o1)
	p12 = re.findall(r"(\w+)\s+(?=screen)", o1)
	p13 = re.findall(r"(\w+)\s+(?=battery)", o1)
	p14 = re.findall(r"(\w+)\s+(?=price)", o1)

	args=p+p1+p2+p5+p6+p7+p8+p9+p10+p11+p12+p13+p14
	sql = "SELECT rating FROM r_word where word in (%s)"
	in_p = ', '.join(list(map(lambda x: '%s', args)))
	sql = sql % in_p
	cur.execute(sql,args)
	rows = [item[0] for item in cur.fetchall()]
	for row in rows:
		first_value = float(row)
    		first_values.append(first_value)
		total = sum(first_values)/float(len(first_values))
		total1 = "{0:.2f}".format(round(total,1))
	print "overall",total1
	return str(total1)
def price(p22):
	total1=0
	total=0
	first_value=0
    	p = re.findall(r"(\w+)\s+(?=price)", p22)
    	p2 = re.findall(r"(\w+)\s+(?=rate)", p22)
    	p3 = re.findall(r"(\w+)\s+(?=worth)", p22)
    	if(len(p)==0&len(p2)==0&len(p3)==0):
		return str(total1)
	args=p+p2+p3	
	sql = "SELECT rating FROM r_word where word in (%s)"
	in_p = ', '.join(list(map(lambda x: '%s', args)))
	sql = sql % in_p
	cur.execute(sql,args)
	rows = [item[0] for item in cur.fetchall()]
	for row in rows:
		first_value = float(row)
    		first_values.append(first_value)
		total = sum(first_values)/float(len(first_values))
		total1 = "{0:.2f}".format(round(total,1))
	print "price",total1
	return str(total1)
def display(d11):
	total1=0
	total=0
	first_value=0
    	p = re.findall(r"(\w+)\s+(?=display)", d11)
    	p1 = re.findall(r"(\w+)\s+(?=screen)", d11)
       	p2 = re.findall(r"(\w+)\s+(?=lcd)", d11)
    	p3 = re.findall(r"(\w+)\s+(?=led)", d11)
    	p4 = re.findall(r"(\w+)\s+(?=gorilla)", d11)
    	p5 = re.findall(r"(\w+)\s+(?=picture)", d11)
    	p6 = re.findall(r"(\w+)\s+(?=quality)", d11)
    	if(len(p)==0&len(p1)==0&len(p2)==0&len(p3)==0&len(p4)==0&len(p5)==0&len(p6)==0):
		return str(total1)
	args=p+p1+p2+p3+p4+p5+p6	
	sql = "SELECT rating FROM r_word where word in (%s)"
	in_p = ', '.join(list(map(lambda x: '%s', args)))
	sql = sql % in_p
	cur.execute(sql,args)
	rows = [item[0] for item in cur.fetchall()]	
	for row in rows:
		first_value = float(row)
    		first_values.append(first_value)
		total = sum(first_values)/float(len(first_values))
		total1 = "{0:.2f}".format(round(total,1))
	print "display",total1
	return str(total1)
def camera(c22):
	total1=0
	total=0
	first_value=0
    	p = re.findall(r"(\w+)\s+(?=camera)", c22)
    	if(len(p)==0):
    		return str(total1)
	args=p	
	sql = "SELECT rating FROM r_word where word in (%s)"
	in_p = ', '.join(list(map(lambda x: '%s', args)))
	sql = sql % in_p
	cur.execute(sql,args)
	rows = [item[0] for item in cur.fetchall()]
	for row in rows:
		first_value = float(row)
    		first_values.append(first_value)
		total = sum(first_values)/float(len(first_values))
		total1 = "{0:.2f}".format(round(total,1))
	print "camera",total1
	return str(total1)
def processor(p33):
	total1=0
	total=0
	first_value=0
    	p = re.findall(r"(\w+)\s+(?=memory)", p33)
    	p2 = re.findall(r"(\w+)\s+(?=ram)", p33)
    	p3 = re.findall(r"(\w+)\s+(?=hardware)", p33)
    	p4 = re.findall(r"(\w+)\s+(?=processor)", p33)
    	if(len(p)==0&len(p2)==0&len(p3)==0&len(p4)==0):
		return str(total1)
	args=p+p2+p3+p4
	sql = "SELECT rating FROM r_word where word in (%s)"
	in_p = ', '.join(list(map(lambda x: '%s', args)))
	sql = sql % in_p
	cur.execute(sql,args)
	rows = [item[0] for item in cur.fetchall()]
	for row in rows:
		first_value = float(row)
    		first_values.append(first_value)
		total = sum(first_values)/float(len(first_values))
		total1 = "{0:.2f}".format(round(total,1))
	print "proc",total1
	return str(total1)
def battery(b44):
	total1=0
	total=0
	first_value=0
    	p = re.findall(r"(\w+)\s+(?=battery)", b44)
    	p1 = re.findall(r"(\w+)\s+(?=energy)", b44)
    	p2 = re.findall(r"(\w+)\s+(?=saver)", b44)
    	p3 = re.findall(r"(\w+)\s+(?=cell)", b44)
    	p4 = re.findall(r"(\w+)\s+(?=cells)", b44)
    	if(len(p)==0&len(p1)==0&len(p2)==0&len(p3)==0&len(p4)==0):
		return str(total1)
	args=p+p1+p2+p3+p4	
	sql = "SELECT rating FROM r_word where word in (%s)"
	in_p = ', '.join(list(map(lambda x: '%s', args)))
	sql = sql % in_p
	cur.execute(sql,args)
	rows = [item[0] for item in cur.fetchall()]
	for row in rows:
		first_value = float(row)
    		first_values.append(first_value)
		total = sum(first_values)/float(len(first_values))
		total1 = "{0:.2f}".format(round(total,1))
	print "bat",total1
	return str(total1)
def per(p11):
	total1 =0
	total=0
	first_value=0
	p = re.findall(r"(\w+)\s+(?=performance)", p11)
	p1 = re.findall(r"(\w+)\s+(?=cooling)", p11)
	p2 = re.findall(r"(\w+)\s+(?=washing)", p11)
	p4 = re.findall(r"(\w+)\s+(?=button)", p11)
	p5 = re.findall(r"(\w+)\s+(?=touch)", p11)
	p6 = re.findall(r"(\w+)\s+(?=material)", p11)
	if(len(p)==0&len(p1)==0&len(p2)==0&len(p4)==0&len(p5)==0&len(p6)==0):
		return str(total1)
	args=p+p1+p2+p4+p5+p6
		
	sql = "SELECT rating FROM r_word where word in (%s)"
	in_p = ', '.join(list(map(lambda x: '%s', args)))
	sql = sql % in_p
	cur.execute(sql,args)
	rows = [item[0] for item in cur.fetchall()]
	for row in rows:
		first_value = float(row)
    		first_values.append(first_value)
		total = sum(first_values)/float(len(first_values))
		total1 = "{0:.2f}".format(round(total,1))
	print "per",total1
	return str(total1)
def design(d22):
	total1=0
	total=0
	first_value=0
    	p = re.findall(r"(\w+)\s+(?=design)", d22)
    	if(len(p)==0):
		return str(total1)
	args=p	
	sql = "SELECT rating FROM r_word where word in (%s)"
	in_p = ', '.join(list(map(lambda x: '%s', args)))
	sql = sql % in_p
	cur.execute(sql,args)
	rows = [item[0] for item in cur.fetchall()]
	for row in rows:
		first_value = float(row)
    		first_values.append(first_value)
		total = sum(first_values)/float(len(first_values))
		total1 = "{0:.2f}".format(round(total,1))
	print "des",total1
	return str(total1)
def weight(w11):
	total1=0
	total=0
	first_value=0
	p = re.findall(r"(\w+)\s+(?=weight)", w11)
	if(len(p)==0):
		return str(total1)
	args=p
	sql = "SELECT rating FROM r_word where word in (%s)"
	in_p = ', '.join(list(map(lambda x: '%s', args)))
	sql = sql % in_p
	cur.execute(sql,args)
	rows = [item[0] for item in cur.fetchall()]
	for row in rows:
		first_value = float(row)
    		first_values.append(first_value)
		total = sum(first_values)/float(len(first_values))
		total1 = "{0:.2f}".format(round(total,1))
	print "wei",total1
	return str(total1)
def vibration(v11):
	total1=0
	total=0
	first_value=0
	p = re.findall(r"(\w+)\s+(?=vibration)", v11)
	p2 = re.findall(r"(\w+)\s+(?=vibrate)", v11)
	p3 = re.findall(r"(\w+)\s+(?=vibrations)", v11)
	if(len(p)==0&len(p2)==0&len(p3)==0):
		return str(total1)
	args=p+p2+p3	
	sql = "SELECT rating FROM r_word where word in (%s)"
	in_p = ', '.join(list(map(lambda x: '%s', args)))
	sql = sql % in_p
	cur.execute(sql,args)
	rows = [item[0] for item in cur.fetchall()]
	for row in rows:
		first_value = float(row)

    		first_values.append(first_value)
		total = sum(first_values)/float(len(first_values))
		total1 = "{0:.2f}".format(round(total,1))
	print "vib",total1
	return str(total1)
def cleaning(c11):
	total1=0
	total=0
	first_value=0
	p = re.findall(r"(\w+)\s+(?=cleaning)", c11)
	p2 = re.findall(r"(\w+)\s+(?=clean)", c11)
	p3 = re.findall(r"(\w+)\s+(?=cleans)", c11)
	p4 = re.findall(r"(\w+)\s+(?=wash)", c11)
	p5 = re.findall(r"(\w+)\s+(?=washing)", c11)
	if(len(p)==0&len(p2)==0&len(p3)==0&len(p4)==0&len(p5)==0):
		return str(total1)
	args=p+p2+p3+p4+p5	
	sql = "SELECT rating FROM r_word where word in (%s)"
	in_p = ', '.join(list(map(lambda x: '%s', args)))
	sql = sql % in_p
	cur.execute(sql,args)
	rows = [item[0] for item in cur.fetchall()]
	for row in rows:
		first_value = float(row)

    		first_values.append(first_value)
		total = sum(first_values)/float(len(first_values))
		total1 = "{0:.2f}".format(round(total,1))
	print "clean",total1
	return str(total1)
def sound(s22):
	total1=0
	total=0
	first_value=0
    	p = re.findall(r"(\w+)\s+(?=sound)", s22)
    	p1 = re.findall(r"(\w+)\s+(?=speaker)", s22)
    	p2 = re.findall(r"(\w+)\s+(?=quality)", s22)
    	if(len(p)==0&len(p1)==0&len(p2)==0):
		return str(total1)
	args=p+p1+p2	
	sql = "SELECT rating FROM r_word where word in (%s)"
	in_p = ', '.join(list(map(lambda x: '%s', args)))
	sql = sql % in_p
	cur.execute(sql,args)
	rows = [item[0] for item in cur.fetchall()]
	for row in rows:
		first_value = float(row)
    		first_values.append(first_value)
		total = sum(first_values)/float(len(first_values))
		total1 = "{0:.2f}".format(round(total,1))
	print "des",total1
	return str(total1)
def main1(input1):
	text1 =str(''.join(input1))
	text1=text1.lower()
	return1=''
	return1 = overall(text1),price(text1),battery(text1),per(text1),processor(text1),design(text1),weight(text1),vibration(text1),cleaning(text1),display(text1),camera(text1),sound(text1)
	print return1
	return return1



