arr = [
    1,
    '0',
    bin(125),
    oct(124),
    hex(124),
    1.43,
    ['1',2,3],
    (1,2,3),
    set('1fsddfgfdgfgfdg121435'),
    frozenset('1fsddfgfdgfgfdg121435'),
    {"name":"Vasy","old":100500},
    True,
    b"text",
    bytearray(b"text"),
    None,
    KeyError
]

[print(type(i))for i in arr]
