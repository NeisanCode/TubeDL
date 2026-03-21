import threading


class Loader:
    def __init__(
        self,
        parent,  # widget CTk parent, pour .after()
        spinner,  # le widget CTkSpinningLabel (ou équivalent)
        loading_label,  # le label "Chargement..."
        on_start=None,  # callback appelé au début (ex: désactiver la search bar)
        on_finish=None,  # callback appelé à la fin avec le résultat
    ):
        self.parent = parent
        self.spinner = spinner
        self.loading_label = loading_label
        self._on_start = on_start
        self._on_finish = on_finish

    def show_spinner(self, task_func, *args, **kwargs):
        if self._on_start:
            self._on_start()

        self.parent.after(50, lambda: self._start_task(task_func, *args, **kwargs))

    def _start_task(self, task_func, *args, **kwargs):
        self.spinner.grid(row=4, column=0, columnspan=2, pady=5)
        self.loading_label.grid(row=2, column=0, columnspan=2, pady=15)
        self.spinner.start()

        def run():
            result = task_func(*args, **kwargs)
            self.parent.after(0, lambda: self._on_task_finished(result))

        threading.Thread(target=run, daemon=True).start()

    def _on_task_finished(self, result):
        self.spinner.stop()
        self.spinner.grid_forget()
        self.loading_label.grid_forget()

        if self._on_finish:
            self._on_finish(result)
