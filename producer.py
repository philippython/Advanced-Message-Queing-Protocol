import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue="hello")

channel.basic_publish(exchange="", routing_key="hello", body="hello_world msg #2")
print("[x] Sent Hello World")

connection.close()

# import inspect
# def reversed_args(f):
    
#     def g(*args):
#         if f.__name__ == "pow":
#             return args[1] ** args[0]
#         elif "separator" in str(inspect.signature(f)):
#             print(True)
#         else:
#             if args[1] > args[0] :
#                 return 1
#             elif args[1] < args[0] :
#                 return -1
#             else : 
#                 return 0
#     return g
    
# # int_func_map = {
#     'pow': pow,
#     'cmp': lambda a, b: 0 if a == b else [1, -1][a < b],
# }

# string_func_map = {
#     'join_with': lambda separator, *args: separator.join(args),
#     'capitalize_first_and_join': lambda first, *args: ''.join([first.upper()] + list(args)),
# }

# queries = int(input())
# for _ in range(queries):
#     line = input().split()
#     func_name, args = line[0], line[1:]
#     if func_name in int_func_map:
#         args = list(map(int, args))
#         print(reversed_args(int_func_map[func_name])(*args))
#     else:
#         print(reversed_args(string_func_map[func_name])(*args))
