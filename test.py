


# text = ('12 pro max 128 gold 🇯🇵 77000')
# data = text.split('\n')
# print(data)
# phone_data = text.split(' ')
# print(phone_data)
# model = ' '.join(phone_data[:3])
# print(model)
# memory = phone_data[3]
# print(memory)
# color = phone_data[4]
# print(color)

text = ('12 pro max 128 gold 🇯🇵 77000')
data = text.split('\n')
print(data)
#print(data)
for phone in data:
    phone_data = phone.split(' ')
    print(phone_data)
    model = ' '.join(phone_data[:3])
    print(model)
    memory = phone_data[3]
    print(memory)
    color = phone_data[4]
    print(color)
    region = phone_data[5]
    print(region)
    price = phone_data[6]
    print(price)

#print(f'{model}')
    # лучше bulk_create - множественоое создание. но это не критично
    # Data.object.create(
    #     model=model,
    #     memory=memory,
    #     color=color,
    #     price=price,
    #     # тут смайлики, создай dict в котором ключи со смайликами будут ассоцироваться с корректным названием страны
    #     region=region,
    # )