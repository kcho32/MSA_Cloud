#패키지: 모듈을 디렉토리로 관리하기 위해 사용
#패키지의 모듈을 참조하기 위해서는 패키지 명.패키지2명. ... 모듈 임포트하거나 함수 호출
import game.graphic.render as rd
import game.sound.echo as ec
from game.play.run import run_test

rd.render_test()
ec.echo_test()
run_test()