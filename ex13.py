# Did she say hallo?
# Option 1
def validate_hello(greetings):
    return any(x in greetings.lower() for x in ['hello','ciao','salut','hallo','hola','ahoj','czesc'])

# Option 2
def validate_hello(greetings):
    g = ['hello', 'ciao', 'salut', 'hallo', 'hola', 'ahoj', 'czesc']
    for s in g:
        if s in greetings.lower():
            return True
    return False