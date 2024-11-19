import string

text = "Ahoj jak se vede"

jmeno = "Tomas"
vek = 0.256584
mesto = "Praha"

osoba = ["Tomas", 25, "Praha"]

# formatovany_text = "Jmeno: %s, \nvek: %d, \nmesto: %s" % (jmeno, vek, mesto)

# formatovany_text = "Jmeno: {1}, \nvek: {2}, \nmesto: {0}".format(jmeno, vek, mesto)

formatovany_text = f"{jmeno} | {vek:.2%} | {mesto}"  # hratky s f-stringem


# utf-8

cestina = "Přecitlivělý text"
print(cestina)

print(string.ascii_letters)
print(string.digits)
print(string.punctuation)
print(string.whitespace)

if "=" in string.punctuation:
    print("ano")