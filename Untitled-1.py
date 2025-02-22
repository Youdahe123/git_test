def is_prime(n):
    if n < 2:
        return True
    else:
        for i in range(2,int(n * 0.5)+1):
            if n/i == n//i:
                return False
    return True
            

print(is_prime(47))
                