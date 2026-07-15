from app.models.sample import Sample, SampleModel
from app.views.sample_view import SampleView


class SampleController:
    """Wires Model and View together and drives the console loop."""

    def __init__(self, model: SampleModel, view: SampleView):
        self.model = model
        self.view = view

    def run(self) -> None:
        actions = {
            "1": self._register_sample,
            "2": self._list_samples,
            "3": self._search_samples,
        }
        while True:
            choice = self.view.show_menu()
            if choice == "0":
                self.view.show_message("종료합니다.")
                return
            action = actions.get(choice)
            if action is None:
                self.view.show_error("올바른 메뉴를 선택하세요.")
                continue
            action()

    def _register_sample(self) -> None:
        try:
            data = self.view.prompt_new_sample()
            self.model.add(Sample(**data))
            self.view.show_message("등록 완료.")
        except (ValueError, KeyError) as exc:
            self.view.show_error(str(exc))

    def _list_samples(self) -> None:
        self.view.show_samples(self.model.list_all())

    def _search_samples(self) -> None:
        keyword = self.view.prompt_keyword()
        self.view.show_samples(self.model.search_by_name(keyword))
