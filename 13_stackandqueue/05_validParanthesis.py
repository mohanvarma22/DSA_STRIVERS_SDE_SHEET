def isValid(s):
    st=[]
    for i in s:
        if i == '(' or i == '{' or i == '[':
            st.append(i)
        else:
            if len(st) == 0:
                return False
            ch=st.pop()
            if (i == ')' and ch =='(') or (i == ']' and ch =='[') or (i == '}' and ch =='{'):
                continue
            else:
                return False
    return len(st) == 0 

if __name__ == '__main__':
    s = "()[{}()]"
    if isValid(s):
        print("True")
    else:
        print("False")