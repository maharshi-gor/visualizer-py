from loader.file import NiftiFile
from concurrent.futures import ThreadPoolExecutor


class Reader:

    images = []

    def __init__(self, file_paths):

        self._files = []

        for path in file_paths:
            file = NiftiFile(path)
            self._files.append(file)

        self._start_reading()

    def _read_files(self, file):
        return file.load()

    def _process_results(self, results):
        for result in results:
            if result.meta_data['type'] == 'Nifti':
                Reader.images.append(result)

    def _start_reading(self):
        with ThreadPoolExecutor(max_workers=5) as executor:
            results = list(
                executor.map(self._read_files, self._files)
            )
            self._process_results(results)
