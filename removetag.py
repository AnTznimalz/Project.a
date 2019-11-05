"""RemoveTag by ศิษย์เทพปอง#2"""
def remo(text=input(), message=''):
    """Func. remo for remove html tag"""
    state = 'go'
    for i in text:
        if i == '<':
            state = 'wait'
            message += ' '
        if i == '>' and state == 'wait':
            state = 'go'
        if i != '>' and i != '<' and state == 'go':
            message += i
    print(message.split())
remo()
