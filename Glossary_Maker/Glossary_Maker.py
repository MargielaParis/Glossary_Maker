import os
import sys
with open(f"{os.path.join(os.path.expanduser('~'),'Desktop')}/eng.txt", 'w', encoding="utf8") as f:
    f.write('')
with open(f"{os.path.join(os.path.expanduser('~'),'Desktop')}/kor.txt", 'w', encoding="utf8") as f:
    f.write('')

print('')
print('********************************************')
print("*                                          *")
print("*            <<< HOW TO USE >>>            *")
print("*                                          *")
print("* Insert Glossary Sets or Insert 1 to Quit *")
print("*                                          *")
print("*                 Example:                 *")
print("*                                          *")
print("*                Break 깨다                *")
print("*                Run 뛰다                  *")
print("*                make 만들다               *")
print("*                                          *")
print("*     처럼 영단어와 한글 사이 띄어쓰기!    *")
print("*                                          *")
print("*              <<< Notice >>>              *")
print("*                                          *")
print("*  !   This is not a Perfect Program    !  *")
print("*  !  Please Check After Making Sheets  !  *")
print("*                                          *")
print("*      종료 하기 위해서 1 + 엔터키 입력    *")
print("*                                          *")
print('********************************************')
print('')


while (1):
    eng = []
    kor = []
    words = sys.stdin.readline().split()
    if words == ['1']:
        break
    if words == ['Reading', '2'] or words == ['Reading', '1']:
        continue
    
    for i in words:
        if (i >= 'a' and i<= 'z') or (i >= 'A' and i <= 'Z'):
            eng.append(i)
        else:
            kor.append(i)
    with open(f"{os.path.join(os.path.expanduser('~'),'Desktop')}/eng.txt", 'a', encoding="utf8") as f:
        for j in eng:
            f.write(j)
            f.write(' ')
        f.write('\n')
    
    with open(f"{os.path.join(os.path.expanduser('~'),'Desktop')}/kor.txt", 'a', encoding="utf8") as f:
        for j in kor:
            f.write(j)
            f.write(' ')
        f.write('\n')
