from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        current = []
        candidates.sort()

        def checkExistance(arrs: List[List], node: List[int]) -> bool:
            for arr in arrs:
                if len(arr) != len(node): continue
                for i in range(len(arr)):
                    if arr[i] != node[i]:
                        break
                else:
                    print(node, 'Duplicated')
                    return True
            
            return False

        def generate(numbers: List[int], target: int) -> None:
            for index in range(len(numbers)):
                number = numbers[index]
                if number == target:
                    current.append(number)
                    if not checkExistance(ans, current): ans.append(current[:])
                    current.pop()
                    return
                if number < target:
                    current.append(number)
                    _numbers = numbers[index + 1:]
                    generate(_numbers, target - number)
                    current.pop()
                if number > target:
                    return

        generate(candidates, target)
        return ans