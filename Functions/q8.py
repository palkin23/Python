def print_kwargs(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")
print_kwargs(Name="P",Enemy="S")
print_kwargs(Name="P")
print_kwargs(Name="S",power="hi",enemy="S")