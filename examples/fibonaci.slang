read n
if n - 2
    print 1
end
if n - 3
    print 1
end
i = 3
n = n - 3
a = 1
b = 1
while n
    temp = a + b
    print temp
    a = b
    b = temp
    n = n - 1
end