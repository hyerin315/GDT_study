plain_text = "Love will find a way"
encrypted_text = ""
decrypted_text = ""

#암호화
for c in plain_text:
    x = ord(c) #문자의 코드값 : 문자 → 코드화
    x += 2
    cc = chr(x) #코드값에 해당하는 문자 출력 : 코드 → 문자화
    encrypted_text += cc

print(encrypted_text)

#복호화
for c in encrypted_text:
    x = ord(c) #문자의 코드값 : 문자 → 코드화
    x -= 2
    cc = chr(x) #코드값에 해당하는 문자 출력 : 코드 → 문자화
    decrypted_text += cc

print(decrypted_text)
