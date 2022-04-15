T = 2
for t in range(T):
    n, m = [2,2] # Expected Output: 2
    n, m = [1,4] # Expected Output: 1
    if m == 1:
        print(2)
    else:
        if n % 2 == 1:
            print(1)
        else:
            print(2)

# T = 2
# for t in range(T):
#     n, m = [1,7] # Expected Output: 1
#     n, m = [3,7] # Expected Output: 1
#     if m == 1:
#         print(2)
#     else:
#         if n % 2 == 1:
#             print(1)
#         else:
#             print(2)