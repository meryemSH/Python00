def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))

    def helper(n):
        if n > days:
            return
        print("Day", n)
        helper(n + 1)
    helper(1)
    print("Harvest time!")
