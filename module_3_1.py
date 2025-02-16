def count_calls():
    global calls
    calls += 1

def string_info(s):
    count_calls()
    return (len(s), s.upper(), s.lower())

def is_contains(w, l):
    count_calls()
    for i in l:
        if i.lower() == w.lower():
            return True
    return False

calls = 0

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)