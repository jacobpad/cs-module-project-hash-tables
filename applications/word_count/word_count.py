print('-'*75, '\n')


def word_count(s):
    cache = {}
    ignore_punc = '":;,.-+=/\|[]{}()*^&'

    # Chain strip of special characters, including " "
    s = s.lower().replace('\r', ' ').replace('\n', ' ').replace('\t', ' ').split()

    for i in s:
        i = i.strip(ignore_punc)
        if i not in cache and i != "":
            cache[i] = 1
        elif i != "":
          cache[i] += 1
    return cache


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count(
        'This is a test of the emergency broadcast network. This is only a test.'))
