'''
1. 아이디어 - 인덱스 사이클 고려
'''



# 모음
vowel = ['a', 'i', 'y', 'e', 'o', 'u']
# 자음
consonant = ['b','k','x','z','n','h','d','c','w','g','p','v','j','q','t','s','r','l','m','f']

while True:
  try:
    rot = input()
    answer = ""
    for each in rot:
      if each.isalpha() == False:
        answer += each
      else:
        # 소문자
        if each.islower():
          # 모음
          if each in vowel:
            i = vowel.index(each)
            answer += vowel[(i+3)%6]
          # 자음
          else:
            i = consonant.index(each)
            answer += consonant[(i+10)%20]
    
        # 대문자
        else:
          each = each.lower()
          # 모음
          if each in vowel:
            i = vowel.index(each)
            answer += vowel[(i+3)%6].upper()
          # 자음
          else:
            i = consonant.index(each)
            answer += consonant[(i+10)%20].upper()
    print(answer)
  except:
    break