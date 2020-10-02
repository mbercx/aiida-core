# -*- coding: utf-8 -*-
"""Data plugin that models an archived folder on a remote computer."""
import typing

from aiida.common.datastructures import StashMode
from aiida.common.lang import type_check
from ..data import Data

__all__ = ('RemoteStashData',)


class RemoteStashData(Data):
    """Data plugin that models an archived folder on a remote computer.

    A stashed folder is essentially an instance of ``RemoteData`` that has been archived. Archiving in this context can
    simply mean copying the content of the folder to another location on the same or another filesystem as long as it is
    on the same machine. In addition, the folder may have been compressed into a single file for efficiency or even
    written to tape. The ``stash_mode`` attribute will distinguish how the folder was stashed which will allow the
    implementation to also `unstash` it and transform it back into a ``RemoteData`` such that it can be used as an input
    for new ``CalcJobs``.
    """

    def __init__(
        self, stash_mode: StashMode = None, target_basepath: str = None, stash_list: typing.List = None, **kwargs
    ):
        """Construct a new instance

        :param stash_mode: the stashing mode with which the data was stashed on the remote.
        """
        super().__init__(**kwargs)
        self.stash_mode = stash_mode
        self.target_basepath = target_basepath
        self.stash_list = stash_list

    @property
    def stash_mode(self) -> StashMode:
        """Return the mode with which the data was stashed on the remote.

        :return: the stash mode.
        """
        return StashMode(self.get_attribute('stash_mode'))

    @stash_mode.setter
    def stash_mode(self, value: StashMode):
        """Set the mode with which the data was stashed on the remote.

        :param value: the stash mode.
        """
        type_check(value, StashMode)
        self.set_attribute('stash_mode', value.value)

    @property
    def target_basepath(self) -> str:
        """Return the target basepath.

        :return: the target basepath.
        """
        return self.get_attribute('target_basepath')

    @target_basepath.setter
    def target_basepath(self, value: str):
        """Set the target basepath.

        :param value: the target basepath.
        """
        type_check(value, str)
        self.set_attribute('target_basepath', value.value)

    @property
    def source_list(self) -> typing.Union[typing.List, typing.Tuple]:
        """Return the list of source files that were stashed.

        :return: the list of source files.
        """
        return self.get_attribute('source_list')

    @source_list.setter
    def source_list(self, value: typing.Union[typing.List, typing.Tuple]):
        """Set the list of source files that were stashed.

        :param value: the list of source files.
        """
        type_check(value, (list, tuple))
        self.set_attribute('source_list', value)
