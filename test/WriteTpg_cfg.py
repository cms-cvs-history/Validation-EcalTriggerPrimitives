import FWCore.ParameterSet.Config as cms

process = cms.Process("PROTPGD")
process.load("SimCalorimetry.EcalTrigPrimProducers.ecalTriggerPrimitiveDigis_cff")

process.source = cms.Source("PoolSource",
    maxEvents = cms.untracked.int32(100),
    fileNames = cms.untracked.vstring('rfio:/castor/cern.ch/cms/store/RelVal/2006/12/16/RelVal120SingleEPt35/0000/D41C6AF5-588D-DB11-9E2D-0013D4C3BAFA.root')
)

process.out = cms.OutputModule("PoolOutputModule",
    outputCommands = cms.untracked.vstring('drop *', 
        'keep *_ecalTriggerPrimitiveDigis_*_*'),
    fileName = cms.untracked.string('file:TrigPrim.root')
)

process.Timing = cms.Service("Timing")

process.MessageLogger = cms.Service("MessageLogger")

process.p = cms.Path(process.ecalTriggerPrimitiveDigis)
process.outpath = cms.EndPath(process.out)


