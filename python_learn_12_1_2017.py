print("hello world")


i = 4
i += 1;

s = "hello"

print(s, i)


def add(x, y):
    return x + y

print(add(2, 2))

def div(x, y):
    return x / y

def do_it():
    print(div(12, 'three'))

def add_to_model(model, word, successor):
    if word not in model:
        model[word] = []
    model[word].append(successor)

def add_to_model(model, word, successor):
    model.setdefault(word, []).append(successor)

model = {}
words = 'a man a plan a canal a'
word_list = words.split()
for i in range(len(word_list) - 1):
    add_to_model(model, word_list[i], word_list[i + 1])

print(model)

def generate(model, n):
    random.seed(0)
    result = []
    word = random.choice(list(model.keys()))
    for _ in range(n):
        result.append(word)
        word = random.choice(model[word])
    return ' '.join(result)

def add_file_to_model(model, path):
    with open(path) as f:
        data = f.read()
        words = data.split()
        for i in range(len(words) - 1):
            add_to_model(model, words[i], words[i + 1])



model = {}
add_file_to_model(model, '/Users/Administrator/sherlock.txt')
print(generate(model, 100))
