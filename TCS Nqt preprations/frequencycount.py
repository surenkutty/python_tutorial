def frequency_count(arr):
    unique=[]
    count=[]
    for i in range(len(arr)):
        found=False
        for j in range(len(unique)):
            if arr[i]==unique[j]:
                found=True
                count[j]+=1
                break
        if not found:
            unique.append(arr[i])
            count.append(1)

    for i in range(len(unique)):
        print(f"{unique[i]} occurs {count[i]} times")

arr = [1, 2, 2, 3, 1, 4, 2]
print(frequency_count(arr))