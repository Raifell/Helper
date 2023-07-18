s = '\\xed\\xe5 \\xff?xb\\xff\\xe5\\xf2\\xf1\\xff \\xef\\xf0\\xe8\\xeb\\xee\\xe6\\xe5\\xed\\xe8\\xe5\\xec'
res = s.encode('latin1').decode('unicode_escape').encode('latin1')
print(res.decode('cp1251'))
