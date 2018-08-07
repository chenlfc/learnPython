# 2-3 个性化消息：将用户的姓名存到一个变量中，
# 				 并向该用户显示一条消息。显示的消息应非常简单，
# 				 如"Hello Eric, would you like to learn some
# 				 Python today?"
# 2-4 调整名字的大小写：将一个人名存储到一个变量中，再以小写、大写
# 					  和首字母大写的方式显示这个人名。
import this
# 2-3
name = input("Please enter your name: > ")
print("Hello ", name.title(), ", would you like to learn some Python today?")
# 2-4
print(name.lower())
print(name.upper())
print(name.title())
# 2-5
# 2-6
famous_person = "Albert Einstein"
famous_person_said = "A person who never made a mistake never tried anything new."
message = famous_person + ' once said, ' + famous_person_said
print(message)
# 2-7 剔除人名中的空白: 存储一个人名，并在其开头和末尾都包含一些空白字符。务必至少使用字符组合"\t"和"\n"各一次。
#                      打印这个人名，以显示其开头和末尾的空白。然后分别使用剔除函数lstrip()、rstrip()和strip()
#                      对人名进行处理，并将结果打印出来。
strip_name = "  Oven\n\t Chen "
print(strip_name)
print('>>', strip_name.lstrip(), '<<')
print('>>', strip_name.rstrip(), '<<')
print('>>', strip_name.strip(), '<<')
