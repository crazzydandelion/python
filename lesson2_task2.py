
def is_year_leap(x):
    if x % 4 == 0:
        return True
    else: return False
x = 2003
print("Год", x, is_year_leap(x))
