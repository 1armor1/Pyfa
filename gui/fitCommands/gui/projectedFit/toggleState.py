import wx

import gui.mainFrame
from gui import globalEvents as GE
from gui.fitCommands.calc.projectedFit.toggleState import CalcToggleProjectedFitCommand
from gui.fitCommands.helpers import InternalCommandHistory
from service.fit import Fit


class GuiToggleProjectedFitStateCommand(wx.Command):

    def __init__(self, fitID, projectedFitID):
        wx.Command.__init__(self, True, 'Toggle Projected Fit State')
        self.internalHistory = InternalCommandHistory()
        self.fitID = fitID
        self.projectedFitID = projectedFitID

    def Do(self):
        cmd = CalcToggleProjectedFitCommand(fitID=self.fitID, projectedFitID=self.projectedFitID)
        success = self.internalHistory.submit(cmd)
        Fit.getInstance().recalc(self.fitID)
        wx.PostEvent(gui.mainFrame.MainFrame.getInstance(), GE.FitChanged(fitID=self.fitID))
        return success

    def Undo(self):
        success = self.internalHistory.undoAll()
        Fit.getInstance().recalc(self.fitID)
        wx.PostEvent(gui.mainFrame.MainFrame.getInstance(), GE.FitChanged(fitID=self.fitID))
        return success
