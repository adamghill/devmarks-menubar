import rumps


class DevmarksBarApp(rumps.App):
    @rumps.clicked("Login")
    def login(self, sender):
        window = rumps.Window(
            "Devmarks API Key (https://devmarks.io/account/api-key)",
            title="Devmarks API Key",
            default_text="",
            ok="Save",
            cancel="Cancel",
        )
        response = window.run()

    @rumps.clicked("Add Bookmark")
    def search(self, sender):
        window = rumps.Window(
            "URL",
            title="Add Bookmark",
            default_text="",
            ok="Save",
            cancel="Cancel",
        )
        response = window.run()

    @rumps.clicked("ℹ️ About")
    def about(self, _):
        rumps.alert(
            title="Devmarks",
            message="Version 0.1.0 - 2022 by @adamghill\nhttps://github.com/adamghill/devmarks-menubar\n\nLicensed under MIT.\n\nrumps licensed under BSD 3-Clause.",
            ok=None,
            cancel=None,
            # icon_path=ICON_PATH,
        )


def cli():
    DevmarksBarApp("🔖").run()


if __name__ == "__main__":
    cli()
