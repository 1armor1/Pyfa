type = "passive"
def handler(fit, src, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Leadership"), "power",
                                  src.getModifiedItemAttr("subsystemCommandBurstFittingReduction"))
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Leadership"), "cpu",
                                  src.getModifiedItemAttr("subsystemCommandBurstFittingReduction"))
