from school.model import person, instructor, student, employee


people = [student('조규원',28,"물리"), student('조규투',30,"수학"), 
        student('조규삼',23,"만화"),instructor('홍길동', 40, '수학'),
        instructor('홍길금', 40, '파이썬'),instructor('홍길은', 40, '수학'),
        employee('김개똥', 32, 'CS부서'),employee('최개똥', 30, 'CE부서')
]

for data in people:
    print("인물 정보: ")
    data.info()