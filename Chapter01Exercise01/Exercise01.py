prompt_text = "Enter a number: "
user_in = input(prompt_text)
user_num = int(user_in)

for i in range(1, 11):
    print(i, "times", user_num, "is", i*user_num)

even = (user_num % 2) == 0

if even:
    print(user_num, "is even")
else:
    print(user_num, "is odd")

print("prompt_text is of type", type(prompt_text))
print("user_in is of type", type(user_in))
print("user_num_text is of type", type(user_num))
print("i is of type", type(i))
print("even is of type", type(even))
