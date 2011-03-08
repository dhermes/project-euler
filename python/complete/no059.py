def translate(message, key):
    len_key = len(key)
    result = message[:]

    for i in range(len_key):
        for j in range(i, len(result), len_key):
            result[j] = result[j] ^ key[i]

    result = "".join([ chr(xx) for xx in result ])
    return result

with open('/Users/dan/Documents/sandbox/euler_project'
          '/problem_data/no059.txt', 'r') as fh:
    message = fh.read()[:-2].split(",")

message = [ int(xx) for xx in message ]

possible_keys = []
for xx in range(97,123):
    for yy in range(97,123):
        for zz in range(97,123):
            possible_keys += [ [xx,yy,zz] ]

for key in possible_keys:
    curr = translate(message, key)
    if ( curr.upper().find("THE") != -1
         and curr.upper().find("IS") != -1
         and curr.upper().find("AND") != -1
         and curr.upper().find("OF") != -1
         and curr.upper().find("ARE") != -1 ):
       break

print "Acual Message:"
print curr

print "\nThe key is: %s or" % "".join([ chr(xx) for xx in key ]), key

print "\nThe sum of the values is: %s" % sum([ ord(xx) for xx in curr ])
