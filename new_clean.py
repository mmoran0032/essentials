

from pathlib import Path


class Cleaner:
    extensions = ('aux', 'bbl', 'blg', 'fdb_latexmk', 'fls',
                  'lis', 'lof', 'log', 'lot', 'nav', 'out',
                  'snm', 'spl', 'syn', 'toc')

    def __init__(self, directory='.'):
        self.directory = Path(directory)
        self.files_to_delete = None
        # self.dirs_to_delete = None

    def remove_files(self, extension):
        for file_name in self.directory.rglob(extension):
            file_name.unlink()
