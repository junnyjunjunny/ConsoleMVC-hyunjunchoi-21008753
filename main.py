from app.models.sample import SampleModel
from app.views.sample_view import SampleView
from app.controllers.sample_controller import SampleController


def main() -> None:
    controller = SampleController(model=SampleModel(), view=SampleView())
    controller.run()


if __name__ == "__main__":
    main()
