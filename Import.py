from sys import argv

script, user_name = argv
prompt = 'yabadaba do '

print "hey %s im the %s script" % (user_name, script),
answer = raw_input("what do you want me to print? ")

print answer
