read n
i = 1
numerator = 1
denominator = 1
halfpi = 0
while n - i
    fraction = numerator / denominator
    halfpi = halfpi + fraction
    numerator = numerator * i
    x = 2 * i
    x = x + 1
    denominator = denominator * x
    i = i + 1
    n = n - 1
end
print halfpi * 2