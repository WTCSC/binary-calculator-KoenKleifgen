def is_bin(bin_str):
    return all(ch in "01" for ch in bin_str)

def binary_calculator(bin1, bin2, operator):
    result = 0 
    dec1 = 0

    if not is_bin(bin1) or not is_bin(bin2):
        return "Error"

    for index, char in enumerate(reversed(bin1)):
        #print(f"Index: {index}, Character: {char}")
        if char == "1":
            dec1 += 2**index
     
    dec2 = 0

    for index, char in enumerate(reversed(bin2)):
        #print(f"Index: {index}, Character: {char}")
        if char == "1":
            dec2 += 2**index
       
    if operator == "*":
        result = dec1 * dec2 

    elif operator == "+":
        result = dec1 + dec2

    elif operator == "-":
        result = dec1 - dec2

    elif operator == "/":
        if dec2 == 0:
            return "NaN"
            
        
        result = dec1 // dec2

    binary_result = format(result, "b")

    if len(binary_result) > 8:
        return "Overflow"
    elif int(binary_result) < 0:
        return "Overflow"
    
    return binary_result.zfill(8)

# print(binary_calculator("1010", "1010", "+"))  # Should return "10100"
# print(binary_calculator("1100", "0011", "-"))  # Should return "1001"
# print(binary_calculator("1010", "0000", "/"))  # Should return "NaN"
# print(binary_calculator("1010", "abc", "+"))   # Should return "Error"
      