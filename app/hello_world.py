def greetings(name="World"):
    return f"Hello {name}"


import hashlib


def sha256(message):
    return hashlib.sha256(message.encode("ascii")).hexdigest()


def code_exc():
    difficulty = 1
    message = "helloworld"
    assert difficulty >= 1
    prefix = "1" * difficulty
    for i in range(1000):
        digest = sha256(str(hash(message)) + str(i))
        if digest.startswith(prefix):
            print("after " + str(i) + " iterations found nonce: " + digest)
        print(digest)