def count_reps(nums):
    cont = []
    repetidos = 0
    unicos = 0

    for i in nums:
        if nums.count(i) > 1 and i not in cont:
            repetidos += nums.count(i)
            cont.append(i)
        elif i not in cont:
            unicos += 1

    return unicos, repetidos


list1 = [1, 3, 1, 4, 5, 3, 7]
result1 = count_reps(list1)

print(result1)
