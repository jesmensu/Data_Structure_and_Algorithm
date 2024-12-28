def decodeString(s: str) -> str:
        stack = []
        
        temp_digit = ""
        result = ""

        for ch in s:
            if ch != "]":
                stack.append(ch)
            else:
                temp_string = ""
                while stack[-1] != "[":
                    temp_string = stack.pop() + temp_string
                stack.pop()
                temp_digit = ""
                while stack and stack[-1].isdigit() == True:
                    temp_digit = stack.pop() + temp_digit
                stack.append(temp_string*int(temp_digit))
        return "".join(stack)


                      


print(decodeString("3[a2[c]]"))


def decodeString1(s: str) -> str:
        stack=[]

        for c in s:
            if c!=']':
                stack.append(c)
            else:
                res=''
                while stack[-1]!='[':
                    res+=stack.pop()
                stack.pop()
                n=''
                while len(stack)!=0 and stack[-1].isdigit()==True:
                    n+=stack.pop()
                stack.append(res*int(n[::-1]))

        return ''.join([word[::-1] for word in stack])

# print(decodeString1("3[a2[c]]"))