def solution(new_id):
    new_id = new_id.lower()
    
    save_id = ''

    for ch in new_id:
        if ch.isalnum() or ch in '-_.':
            save_id += ch
    
    while save_id and '..' in save_id:
        save_id = save_id.replace('..', '.')
    
    while save_id and '.' in save_id[0]:
        save_id = save_id[1:]
    
    while save_id and '.' in save_id[-1]:
        save_id = save_id[: -1]
    
    if not save_id:
        save_id = 'a'
    
    if len(save_id) > 15:
        save_id = save_id[: 15]
    
    while '.' == save_id[-1]:
        save_id = save_id[: -1]
    
    while len(save_id) <= 2:
        save_id += save_id[-1]

    return save_id


print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution(	"z-+.^."))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))
