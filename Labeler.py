
##########
tag = ['대입']

L = [
[],
]
##########

while True:
    msg = f'\n0부터 {len(L) - 1}까지 요소에 부여할 tag의 번호를 선택하시오. 새로운 tag를 추가하려면 "N"을 입력하시오 > '
    
    word = input('\n요소를 입력하시오. 종료하려면 "X"를 입력하시오 > ')
    if word == 'X' or word == 'x' or word == 'ㅌ':
        break
    
    else:
        
        print('')
        for i in range(len(tag)):
            comp = ''
            for j in range(len(L[i])):
                comp += f'{L[i][j]}, '
            print(f'{i} : {tag[i]} : {comp}')
        
        inp = input(msg)
        if inp == '':
            inp = input(msg)
            continue
        
        order = []
        for i in range(len(inp)):
            order.append(ord(inp[i]))
        
        if 48 <= min(order) and max(order) < 58:
            
            if 0 <= int(inp) < len(L):
                tagcode = int(inp)
                if word not in L[tagcode]:
                    L[tagcode].append(word)
            
            else:
                continue
        
        elif inp == 'N' or inp == 'n' or inp == 'ㅜ':
            tagname = input('새로운 tag의 이름을 입력하시오 > ')
            tag.append(tagname)
            L.append([])
            L[-1].append(word)

print(f'\n\n\n<<라벨링 현황>>\n')
for i in range(len(L)):
    comp = ''
    for j in range(len(L[i])):
        comp += f'{L[i][j]}, '
    print(f'{tag[i]} : {comp}')

print(f'\n\n\n▼이 텍스트를 파일 코드의 첫부분에 붙여넣어서 수정하시오\n\n##########\ntag = {tag}\n\nL = [')
for i in range(len(L)):
    print(f'{L[i]},')
print(']\n##########\n\n▲이 텍스트를 파일 코드의 첫부분에 붙여넣어서 수정하시오\n')