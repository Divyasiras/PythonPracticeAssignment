# 3. Predict the output

#reason: Local variables are accessible only within their function and cannot be used outside it.

def fun():
    X = 10
    print(X)

fun()
print(X)