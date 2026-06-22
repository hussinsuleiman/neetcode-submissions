from decimal import Decimal

a,b,c = map(int, input().split())
result_decimal = Decimal(a * b) / Decimal(c)

print(result_decimal)