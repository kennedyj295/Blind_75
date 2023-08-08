
def groupAnagrams(strs):
        groups = {}
        output = []

        for str in strs:
            sorted_string = "".join(sorted(str))

            if (sorted_string in groups):
                groups[sorted_string].append(str)
            else:
                groups[sorted_string] = [str]

        for value in groups.values():
            output.append(value)

        return output
