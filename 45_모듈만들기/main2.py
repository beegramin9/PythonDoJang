from calcpkg import *    # calcpkg 패키지의 모든 변수, 함수, 클래스를 가져옴

print(add(10, 20))    # operation 모듈의 add 함수 사용
print(mul(10, 20))    # operation 모듈의 mul 함수 사용

print(triangle_area(30, 40))    # geometry 모듈의 triangle_area 함수 사용
print(rectangle_area(30, 40))   # geometry 모듈의 rectangle_area 함수 사용

""" __init__ 에서 모듈만 가져왔을 뿐 모듈 안의 함수는 가져오지 않았기 때문임
__init__.py를 수정해야 함 """
