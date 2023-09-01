#!/usr/bin/env python3
import sys
nums = sys.argv[1]
nums2 = sys.argv [2]
nums3 = sys.argv[3]
text = sys.argv[4]
try:
    verif1 = int(nums)
    verif2 = int(nums2)
    verif3 = int(nums3)
    verif4 = str(text)
    result = nums, nums2, nums3, text       #to endline, add , "\n" in this construction, but in the file the string will end with ,
    resultStr = ', '.join(map(str, result)) #map convert each tuple element to str bafore joining
    print("Teus números são: ", nums, nums2, nums3, "\ne seu texto é: ", text, "\ne esse conteúdo está em texto2.txt")
    with open('texto2.txt', 'w') as file:
        file.write(resultStr)
except ValueError:
    print("Digite números e texto válidos!")
