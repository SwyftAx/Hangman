# head, eyes, spine, legs, arms

template = """|------
|     |
|
|
|
|
|
--------"""
template1 = """|------
|     |
|   (   )
|   
|
|
|
--------"""
template2 = """|------
|     |
|   (° °)
|   
|
|
|
--------"""
template3 = """|------
|     |
|   (° °)
|     |
|     |
|
|
--------"""
template4 = """|------
|     |
|   (° °)
|     |
|     |
|    / \
|
--------"""
template_failed = """|------
|     |
|   (° °)
|   __|__
|     |
|    / \
|
--------"""
topic = input("""Player one, what is the topic?
""")
word = input("""What is the word?
""")
print("""












""")
tries = 1
while tries < 6:
    print(f"The topic is: {topic}")
    attempt = input(f"What is guess #{tries}? ")
    if attempt.lower() == word:
        print("That is correct!")
        break
    elif tries < 5:
        if tries == 1:
            print(template1)
        if tries == 2:
            print(template2)
        if tries == 3:
            print(template3)
        if tries == 4:
            print(template4)
    else:
        print(template_failed)
        print(f"Failed. The correct word was {word}. Try again next time!")
    tries += 1
