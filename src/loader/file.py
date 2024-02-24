from abc import abstractmethod
from pathlib import Path
import nibabel as nib
from dataclasses import dataclass


@dataclass
class LoadResult:
    data: any
    meta_data: dict


class File:

    def __init__(self, path):
        self._path = path
        self._name = Path(path).name

    @abstractmethod
    def load(self):
        pass

    @property
    def name(self):
        return self._name

    @property
    def path(self):
        return self._path


class NiftiFile(File):

    def __init__(self, path):
        self._meta_data = {'type': 'Nifti'}
        super().__init__(path)

    def load(self):
        return self._read_nifti_file()

    def _read_nifti_file(self):
        print("Started Reading:", self._name)
        img = nib.load(self._path)
        v_img = (img.get_fdata().astype("float32"), img.header.get_sform())
        print("Loaded File:", self._name)
        return LoadResult(v_img, self._meta_data)
