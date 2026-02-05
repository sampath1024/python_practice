marks = {
    "maths": 35,
    "science": 75,
    "english": 28
}

filtered = dict(filter(lambda item: item[1] >= 35, marks.items()))
print(filtered)


