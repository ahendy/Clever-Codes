def reverse_string(s):
    s = list(s)  # strings are immutable
    n = len(s)

    for i in range(n / 2):
        s[i], s[n - i - 1] = s[n - i - 1], s[i]  # 1 line pythonic magic

    return ''.join(s)  # back to string

if __name__ == '__main__':
    assert (reverse_string('hello') == 'olleh'), 'Test1 Failed'
    print 'Test1 Passed'
