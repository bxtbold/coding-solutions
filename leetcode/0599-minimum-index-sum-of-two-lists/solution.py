class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        """
        RUNTIME: 271 ms (79.87%)
        MEMORY: 14.5 MB (40.48%)
        """
        least = len(list1) + len(list2)
        list_dict1, list_dict2 = {}, {}
        if len(list1) > len(list2):  # for tweaking running time
            list1, list2 = list2, list1
        for i, string in enumerate(list2):
            list_dict2[string] = i
        for i, string in enumerate(list1):
            if string in list_dict2:  # for tweaking running time
                list_dict1[string] = i

        for string in list_dict1:
            if string in list_dict2:
                min_sum = list_dict1[string] + list_dict2[string]
                if least > min_sum:
                    least_dict = {min_sum: [string]}
                    least = min_sum
                elif least == min_sum:
                    least_dict[min_sum].append(string)
        return least_dict[least]
