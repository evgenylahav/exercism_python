def hey(speech: str) -> str:
    speech = ''.join(speech.split())
    if 'please' in speech.lower():
        return 'mmm... OK'
    elif speech.isupper() and speech.endswith('?'):
        return "Calm down, I know what I'm doing!"
    elif speech.isupper():
        return 'Whoa, chill out!'
    elif 'bob' in speech.lower():
        return "that's me"
    elif speech.endswith('?'):
        return 'Sure.'
    elif speech.strip() == '':
        return 'Fine. Be that way!'
    else:
        return 'Whatever.'
