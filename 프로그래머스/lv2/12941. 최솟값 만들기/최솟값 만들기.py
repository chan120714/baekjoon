def solution(A,B):
    a=sorted(A)
    b=sorted(B,reverse=True)
    for i in range(min(len(a),len(b))):
        a[i]*=b[i]
    return sum(a)