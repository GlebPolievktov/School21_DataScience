
def func():
    list_of_tuples = [
        ('Russia', '25'),
        ('France', '132'),
        ('Germany', '132'),
        ('Spain', '178'),
        ('Italy', '162'),
        ('Portugal', '17'),
        ('Finland', '3'),
        ('Hungary', '2'),
        ('The Netherlands', '28'),
        ('The USA', '610'),
        ('The United Kingdom', '95'),
        ('China', '83'),
        ('Iran', '76'),
        ('Turkey', '65'),
        ('Belgium', '34'),
        ('Canada', '28'),
        ('Switzerland', '26'),
        ('Brazil', '25'),
        ('Austria', '14'),
        ('Israel', '12')
    ]
    main_dict = dict()
    country = []
    for item, key in list_of_tuples:
        if key not in main_dict:
            main_dict[key] = []
        main_dict[key].append(item)
    sorted_dict = dict(sorted(main_dict.items(), key=lambda k: int(k[0]), reverse=True))
    for i in sorted_dict.values():
        country.append(i)
    for item in country:
        if len(item) > 1:
            item.sort()
    mass = [i for s in country for i in s]
    for k in mass:
        print(k)


if __name__ == "__main__":
    func()