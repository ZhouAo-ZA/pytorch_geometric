from typing import Union, List

import torch

from torch_geometric.data import Data, Dataset


def collate_fn(data_list: List[Data]) -> List[Data]:
    return data_list


class DataListLoader(torch.utils.data.DataLoader):
    r"""A data loader which batches data objects from a
    :class:`torch_geometric.data.dataset` to a Python list.

    .. note::

        This data loader should be used for multi-GPU support via
        :class:`torch_geometric.nn.DataParallel`.

    Args:
        dataset (Dataset): The dataset from which to load the data.
        batch_size (int, optional): How many samples per batch to load.
            (default: :obj:`1`)
        shuffle (bool, optional): If set to :obj:`True`, the data will be
            reshuffled at every epoch. (default: :obj:`False`)
        **kwargs (optional): Additional arguments of
            :class:`torch.utils.data.DataLoader`, such as :obj:`drop_last` or
            :obj:`num_workers`.
    """
    def __init__(self, dataset: Union[Dataset, List[Data]],
                 batch_size: int = 1, shuffle: bool = False, **kwargs):
        if 'collate_fn' in kwargs:
            del kwargs['collate_fn']

        super().__init__(dataset, batch_size=batch_size, shuffle=shuffle,
                         collate_fn=collate_fn, **kwargs)
