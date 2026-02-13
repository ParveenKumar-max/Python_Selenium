#Fixtures -- another powerful feature what this pytest has is fixtures.
#So this is core concept in the whole pytest world.
#So basically fixed fixtures "provide a way to create reusable setup code so that we can share that reusable
#code across multiple test cases."



def test_initialCheck(preWork):
    print("First Playwright Test")

def test_BasicCheck(preWork):
    print("Second Playwright Test")