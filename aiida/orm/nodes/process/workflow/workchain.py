# -*- coding: utf-8 -*-
"""Module with `Node` sub class for workchain processes."""
from __future__ import absolute_import

from aiida.common.lang import classproperty

from .workflow import WorkflowNode

__all__ = ('WorkChainNode',)


class WorkChainNode(WorkflowNode):
    """ORM class for all nodes representing the execution of a WorkChain."""

    _cachable = False

    STEPPER_STATE_INFO_KEY = 'stepper_state_info'

    @classproperty
    def _updatable_attributes(cls):
        # pylint: disable=no-self-argument
        return super(WorkChainNode, cls)._updatable_attributes + (cls.STEPPER_STATE_INFO_KEY,)

    @property
    def stepper_state_info(self):
        """
        Return the stepper state info

        :returns: string representation of the stepper state info
        """
        return self.get_attribute(self.STEPPER_STATE_INFO_KEY, None)

    def set_stepper_state_info(self, stepper_state_info):
        """
        Set the stepper state info

        :param state: string representation of the stepper state info
        """
        return self.set_attribute(self.STEPPER_STATE_INFO_KEY, stepper_state_info)
