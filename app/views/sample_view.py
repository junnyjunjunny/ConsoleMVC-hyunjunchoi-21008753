class SampleView:
    """Handles all console input/output. Owns no business logic."""

    def show_menu(self) -> str:
        print("\n===== 반도체 시료 관리 (MVC PoC) =====")
        print("[1] 시료 등록  [2] 시료 목록  [3] 시료 검색  [0] 종료")
        return input("선택 > ").strip()

    def prompt_new_sample(self) -> dict:
        sample_id = input("시료 ID > ").strip()
        name = input("이름 > ").strip()
        avg_time = float(input("평균 생산시간(min/ea) > ").strip())
        yield_rate = float(input("수율(0~1) > ").strip())
        return {
            "sample_id": sample_id,
            "name": name,
            "avg_production_time": avg_time,
            "yield_rate": yield_rate,
        }

    def prompt_keyword(self) -> str:
        return input("검색어 > ").strip()

    def show_samples(self, samples) -> None:
        if not samples:
            print("등록된 시료가 없습니다.")
            return
        print(f"{'ID':<8}{'이름':<20}{'평균생산시간':<14}{'수율':<8}{'재고':<8}")
        for s in samples:
            print(f"{s.sample_id:<8}{s.name:<20}{s.avg_production_time:<14}{s.yield_rate:<8}{s.stock:<8}")

    def show_message(self, message: str) -> None:
        print(message)

    def show_error(self, message: str) -> None:
        print(f"[오류] {message}")
