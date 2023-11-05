from view import View
from view_model import ViewModel
from model import Model
from Web import WebPage
import json

def main(view: View) -> None:
    view.mainloop()

if __name__ == "__main__":
    with open('appsettings.json','r') as config_file:
        config = json.load(config_file)
    main(
        view = View(
            view_model= ViewModel(
                model=Model(),
            ),
            web=WebPage(config['Api']['BaseUrl'], config['Api']['Endpoint'])
        )
    )