while True:
    try:
        n=input().rstrip().replace("&gt;","Z").replace("&lt;",'C').replace("&amp;","V")

        tag=''
        is_tag=0
        valid=1
        cur=''
        tag_stack=[]
        HEX=''
        is_HEX=0
        for i in n:
            if is_tag==1:
                if i=='>':      
                    is_tag=0
                    if len(tag)<1:
                        valid=0
                        break
                    first=1
                    for j in range(len(tag)):
                        if 'a'<=tag[j]<='z' or '0'<=tag[j]<='9':
                            continue
                        elif j==0 or j==len(tag)-1:
                            if tag[j]=='/':
                                continue
                            else:
                                valid=0
                        else:
                            valid=0
                    if tag[0]=='/' and tag[-1]=='/':
                        valid=0
                    elif tag[-1]=='/':
                        pass
                    elif tag[0]=='/':
                        if len(tag_stack) and tag_stack[-1]==tag[1:]:
                            tag_stack.pop()
                        else:
                            valid=0
                    else:
                        tag_stack.append(tag)
                        #print(tag)
                    n=n.replace('<'+tag+'>','X')
                    tag=''
                else:
                    tag+=i
            elif i=='<':
                is_tag=1
            elif i=='>':
                valid=0
            elif i=='&':
                is_HEX=1
            elif is_HEX:
                if i==';':
                    is_HEX=0
                    if len(HEX)%2==0:
                        valid=0
                    if len(HEX)<=1 or HEX[0]!='x':
                        valid=0
                    for j in range(1,len(HEX)):
                        if 'A'<=HEX[j]<='F' or '0'<=HEX[j]<='9' or 'a'<=HEX[j]<='f':
                            continue
                        else:
                            valid=0
                    n=n.replace("&"+HEX+';','N')
                    HEX=''
                else:
                    HEX+=i
            #print(valid,i)
        if '&'in n or '>' in n or '<' in n:
            valid=0
        if len(tag_stack):
            valid=0
        print('in'*(1^valid)+'valid')
    except EOFError:
        break
