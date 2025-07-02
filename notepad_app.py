def save_note(filename, contet):
    with open(filename, 'w', encoding = 'utf-8') as f:
        f.write(contet)

def load_note(filename):
    with open(filename, 'r', encoding = 'utf-8') as f:
        return f.read()
    
filename = input("파일 이름을 저장하세요 : ")
action = input("저장하려면 w, 불러오려면 r 입력 : ")

if action == 'w':
    content = input("저장할 내용을 입력하세요 \n: ")
    save_note(filename, content)
    print("저장 완료!")
elif action == 'r' :
    print("내용:\n", load_note(filename))

    
