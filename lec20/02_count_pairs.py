def count_pairs(nums: list[int], target: int) -> int:
    """
    Counts adjacent pairs of target number.
    """
    num_pairs = 0
    for i in range(1, len(nums)):
        if nums[i] == target and nums[i-1] == target:
            num_pairs += 1
    
    return num_pairs

def main() -> None:
    some_nums = [0, 2, 0, 0, 3, 4, 0, 0, 1, 0, 2, 5, 0, 0]
    print(f"Pairs of 0s: {count_pairs(some_nums, 0)}")

main()