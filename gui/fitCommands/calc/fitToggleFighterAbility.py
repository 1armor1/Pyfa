import wx
from logbook import Logger

import eos.db
from service.fit import Fit


pyfalog = Logger(__name__)


class FitToggleFighterAbilityCommand(wx.Command):

    def __init__(self, fitID, position, effectID, isProjected):
        wx.Command.__init__(self, True, "Toggle Fighter Ability")
        self.fitID = fitID
        self.position = position
        self.effectID = effectID
        self.isProjected = isProjected

    def Do(self):
        pyfalog.debug("Toggling fighter ability for fit ID: {0}", self.fitID)
        fit = Fit.getInstance().getFit(self.fitID)
        if self.isProjected:
            fighter = fit.projectedFighters[self.position]
        else:
            fighter = fit.fighters[self.position]

        for fa in fighter.abilities:
            if fa.effectID == self.effectID:
                ability = fa
                break
        else:
            return False

        ability.active = not ability.active
        eos.db.commit()
        return True

    def Undo(self):
        cmd = FitToggleFighterAbilityCommand(self.fitID, self.position, self.effectID, self.isProjected)
        return cmd.Do()