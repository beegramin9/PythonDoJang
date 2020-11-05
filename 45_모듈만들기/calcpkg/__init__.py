from .operation import *
from .geometry import *
# 패키지를 만들 때 관례적으로 빈 파일을 하나 만들어 놓는다.

# import 패키지.모듈이 아니라
# import 패키지 형식으로 패키지만 가져오고 싶다면?
# 밑에 코드를 써줘야 함

""" 패키지 가져오고 패키지.모듈 이런식으로 쓸 때 """
# from . import operation    # 현재 패키지에서 operation 모듈을 가져옴
# from . import geometry     # 현재 패키지에서 geometry 모듈을 가져옴

""" 패키지를 부를 때 모듈 안 부르고 가져오고 싶을 때
main2.py 에서 모듈 안의 함수까지 가져와야 할 때 """
