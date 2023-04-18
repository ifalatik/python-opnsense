from .interface_diagnostics_controller import InterfaceDiagnosticsController as Interface
from .netflow_diagnostics_controller import NetflowDiagnosticsController as Netflow
from .system_diagnostics_controller import SystemDiagnosticsController as System


class Diagnostics(object):

    def __init__(self, device):
        self._device = device

    @property
    def system_diagnostics(self) -> System:
        """

        :return: SystemDiagnosticsController
        """
        return System(self._device)

    @property
    def interface_diagnostics(self) -> Interface:
        """

        :return: InterfaceDiagnosticsController
        """
        return Interface(self._device)

    @property
    def netflow_diagnostics(self) -> Netflow:
        """

        :return: NetflowDiagnosticsController
        """
        return Netflow(self._device)
