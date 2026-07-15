# ConsoleMVC-hyunjunchoi-21008753

반도체 시료 생산주문관리 시스템 - PoC 1: MVC 스켈레톤 코드

## 목적
Model / Controller / View 패키지 구조와 역할 분리를 검증하기 위한 콘솔 기반 MVC 스켈레톤 PoC.

## 구조
```
app/
  models/sample.py        # Sample 엔티티 + 인메모리 저장/조회 (Model)
  views/sample_view.py    # 콘솔 입출력 전담 (View)
  controllers/sample_controller.py  # Model-View 연결, 흐름 제어 (Controller)
main.py                   # 진입점: 의존성 조립 후 컨트롤러 실행
tests/                    # unittest 기반 단위 테스트
```

## 실행 방법
```
python main.py
```

## 테스트
```
python -m unittest discover tests
```

## 담당자
- 이름: hyunjunchoi
- 사번: 21008753
