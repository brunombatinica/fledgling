#Classes in came

#funcitons in this_form

def test(input, *pos, **kw):
    print(input)
    print(pos)
    for i in kw:
        print(i + ":" + kw[i])
  
test("hello","how are you", "its so typical of me","to think of",
     hello = "good song", adele = "artist", "hello" )


