# Program to perform run-length encoding (RLE) by counting consecutive character repetitions in a string
# Example: input "aaaaabbcc" -> output "a5b2c2"

string = input("Enter the String: ")

result = ""
count = 1  

for i in range(1, len(string)):
    if string[i] == string[i - 1]:
        count += 1
    else:
        result += string[i - 1] + str(count)
        count = 1

result += string[-1] + str(count)

print(result)
