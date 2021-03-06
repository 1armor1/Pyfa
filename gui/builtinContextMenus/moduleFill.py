import gui.fitCommands as cmd
import gui.mainFrame
from gui.contextMenu import ContextMenu
from service.fit import Fit
from service.settings import ContextMenuSettings


class FillWithModule(ContextMenu):
    def __init__(self):
        self.mainFrame = gui.mainFrame.MainFrame.getInstance()
        self.settings = ContextMenuSettings.getInstance()

    def display(self, srcContext, selection):
        if not self.settings.get('moduleFill'):
            return False
        return srcContext == "fittingModule"

    def getText(self, itmContext, selection):
        return "Fill With {0}".format(itmContext if itmContext is not None else "Module")

    def activate(self, fullContext, selection, i):

        srcContext = fullContext[0]
        fitID = self.mainFrame.getActiveFit()

        if srcContext == "fittingModule":
            fit = Fit.getInstance().getFit(fitID)
            mod = selection[0]
            if mod in fit.modules:
                position = fit.modules.index(mod)
                self.mainFrame.command.Submit(cmd.GuiFillWithClonedLocalModulesCommand(
                    fitID=fitID, position=position))


FillWithModule.register()
