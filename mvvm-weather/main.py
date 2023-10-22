from view import View
from view_model import ViewModel
from model import Model

def main(view: View) -> None:
    view.mainloop()

if __name__ == "__main__":
    main(
        view = View(
            view_model= ViewModel(
                model=Model()
            )
        )
    )