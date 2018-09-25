
#  过滤敏感字...
passive_str_arr = ("哈", "呵")

user_text = "呵呵呵， 哈哈哈"
for word in passive_str_arr:
    if word in user_text:
        length = len(word)
        user_text = user_text.replace(word, '*'*length)

print(user_text)