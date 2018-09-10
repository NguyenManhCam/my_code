with open("xa.sql", 'r') as f:
    content = f.readlines()

content = [x.strip() for x in content]
f = open("xa.txt","w+")
for i in content:
    l = len(i)-2
    a1 = i[44:l]
    a2 = (a1.find(","))
    a3 = a1[a2+1:]
    a4 = (a3.find(","))
    a5 = a3[a4+1:]
    a6 = (a5.find(","))
    a7 = a5[a6+3:-1]
    a8 = (a7.find(","))
    a9 = a7[a8:-1]
    code = '"' + a1[1:a2-1].strip() + '"'
    name = '"' + a3[2:a4-1].strip() + '"'
    _type = '"' + a5[2:a6-1].strip() + '"'
    code1 = '"' + a7.strip() + '"'

    str1 = f"INSERT into dbo.Photo(CategoryId,Data,Data_Db,Files)\nvalues (11,\nN'{{\"wardId\":{code},\"name\":{name},\"type\":{_type},\"districtId\":{code1}}}',\nN'{{\"Status\":1,\"CreationTime\":\"2018-09-06T08:28:56.4744264+07:00\",\"CreationBy\":0,\"ModificationTime\":null,\"ModificationBy\":null,\"DelectationTime\":null,\"DelectationBy\":null,\"SortTime\":\"2018-09-06T08:28:56.4744278+07:00\",\"Language\":\"vi\"}}',N'[]')"
    # str1 = f"INSERT into dbo.Photo(CategoryId,Data,Data_Db,Files)\nvalues (10,\nN'{{\"districtId\":{code},\"name\":{name},\"type\":{_type},\"provinceId\":{code1}}}',\nN'{{\"Status\":1,\"CreationTime\":\"2018-09-06T08:28:56.4744264+07:00\",\"CreationBy\":0,\"ModificationTime\":null,\"ModificationBy\":null,\"DelectationTime\":null,\"DelectationBy\":null,\"SortTime\":\"2018-09-06T08:28:56.4744278+07:00\",\"Language\":\"vi\"}}',N'[]')"
    # str1 = f"INSERT into dbo.Photo(CategoryId,Data,Data_Db,Files)\nvalues (9,\nN'{{\"provinceId\":{code},\"name\":{name},\"type\":{_type}}}',\nN'{{\"Status\":1,\"CreationTime\":\"2018-09-06T08:28:56.4744264+07:00\",\"CreationBy\":0,\"ModificationTime\":null,\"ModificationBy\":null,\"DelectationTime\":null,\"DelectationBy\":null,\"SortTime\":\"2018-09-06T08:28:56.4744278+07:00\",\"Language\":\"vi\"}}',N'[]')"
    # print(code1
    f.write(str1 + "\n")
f.close()