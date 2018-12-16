# -*- coding: utf-8 -*-
frase = input("Frase: \n")
path = input("Directorio del archivo encriptado: \n")
#path = "/home/jaimeale/Documents/tutorials/Python/Encrypt/CKinput02.txt"
#frase = 'el veloz murciélago hindú comía feliz cardillo y kiwi cuando la cigüeña tocaba el saxofón detrás del palenque de paja'
#frase = "la invasión fue planeada para el día de la toma de gobierno en puebla de los ángeles con autorización del mariscal con el fin de recuperar la plaza de los niños"
#encrypted = "cx kuyxnkfu úrj hcxujxqx hxlx jc qbx qj cx pdáx qj odókjlud ju hrjócx jc yjcdü árlskacxod mkuqt sdábx újckü sxlqkccd z ikík srxuqd cx skovjex pdsxóx jc nxñdúfu qjplwn qjc hxcjuérj qj hxgx qj cdn wuojcjn sdu xrpdlküxskfu qjc jgjlskpd qj cx uxskfu sdu jc úku qj ljsrhjlxl cx hcxüx qj cdn ukedn"
#encrypted = "úhwod wáleófóe xdá iweádá ymá ñeóáñwá wáñü kdlqw wáleófóe úde wvwyúxd xü kdlqw wáñm wáñewxxüoü  g ñóeóñük üuhxwá xdá üáñedá ü xd xwvdá wx iówkñd ow xü kdlqw íóeü wk wx lówxd g lükñü úhwod wáleófóe xdá iweádá ymá ñeóáñwá wáñü kdlqw  gd xü jhóáw g ü iwlwá wxxü ñüyfóak yw jhóád wk xüá kdlqwá wx iwxdu yhelóaxüíd qókop ldysü rwxóu lüeoóxxd g bóéó lhükod xü lóítwnü ñdlüfü wx áüzdrck owñemá owx úüxwkjhw ow úüvü ldyd aáñü xü ñhiw wkñew yóá feüudá xü fwáa ñükñüá iwlwá füvd wx lówxd ókrókóñd wxxü yw jhóád ü iwlwá gd ñüyfóak xü jhwesü lcyd kd qüfwe üyüod áhá íeükowá dvdá róvdá"
# print ("Tamano de la frase: " + str(len(frase)))
# print ("Tamaño de la encriptación: " + str(len(encrypted)))
f = open(path, "r")

tmpString = ""
for line in f.readlines():
    tmpString += line
tmpString = tmpString.replace("\n", " ")
tmpString =  tmpString[3:]

encrypted = tmpString

chars    = []
dicc     = {}

for char in frase:
    dicc [char] = []

index = 0
for char in frase:
    dicc [char].append(index)
    chars.append(char)
    index += 1

diccEnc  = {}
charsEnc = []

for char in encrypted:
    diccEnc [char] = []

# index = 0
# for char in encrypted:
#     diccEnc[char].append(index)
#     charsEnc.append(char)
#     index += 1

# print (dicc)
# print(chars)

keys = list(dicc)

startLine = 0
start = 0
checking = True
while (checking):
    fail = 0
    for key in keys:
        diff = []
        for place in dicc[key]:
            newPlace = place + start
            if newPlace == len(encrypted):
                newPlace -= 1
                checking = False
            if start == 70:
                #print ("Key: " + key)
                #print ("Place: " + str(newPlace))
                #print("Chars: " + encrypted[newPlace])
                pass
            diff.append(encrypted[newPlace])
            #print ("Place: " + str(place) + " Key: " + key + " CharEnc: " + encrypted[newPlace])

        if (len(diff) > 1):
                for val in range(0, len(diff)):
                    if val < (len(diff)):
                        val2 = 1 + val
                        if (val2 == len(diff)):
                            val2 -= val2

                    if (diff[val] != diff[val2]):
                        fail += 1
                
        if fail == 0:
            startLine = start
            checking = False

        if checking == False:
            #print (diff)
            pass

        #diccEnc[encrypted[newPlace]].append(key)

    start += 1

    # print ("\nWhile: " + str(start))
    # print ("Number of erros: " str(fail))

start -= 1
for key in keys:
    diff = []
    for place in dicc[key]:
        newPlace = place + start
        if newPlace == len(encrypted):
            newPlace -= 1
        # print ("Key: " + key)
        # print ("newPlace: " + str(newPlace))
        # print ("CharEnc: " + encrypted[newPlace])

        diccEnc[encrypted[newPlace]].append(key)
        #diff.append(encrypted[newPlace])

    diccEnc[encrypted[newPlace]] = diccEnc[encrypted[newPlace]][0]

#print (diccEnc)

newString = ""
for char in encrypted:
    newString += diccEnc[char]

firstString =  newString[:start]
secondString = newString[start + len(frase):]

print (firstString + secondString)
# indice 70 es el bueno
#print ("Start line: " + str(startLine))
#print ("Tamano de la frase: " + str(len(frase)))
#print ("Tamaño de la encriptación: " + str(len(encrypted)))

#encrypted = encrypted[startLine:]
#print (encrypted)