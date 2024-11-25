
from factorplots import *
Rdp = 2500 #lt Angabe[Miles]
Rctg = Rdp*0.05 #5% of Rdp[Miles]
Rdiv = 100 #lt Angabe[Miles]
Rhld = 100 #0.5 hours with 200 Miles[Miles]


Rphys = [Rdp + Rctg + Rdiv + Rhld] #Physische Reichweite [Miles,km]
Rphys.append(round(Rphys[0]*1.852,2)) # List in der im ersten eintrag die Range in NM steht und im zweiten die Range in km

def getmPpayload(pax):
    mCargo = 5000 #[kg]
    mPax = 83 #[kg]
    mPaxBag	= 12 #[kg]
    mPaxGross = pax*mPax #[kg]
    mPaxBagGross = mPaxBag*pax #[kg]
    mPaxOverall	= mPaxGross+mPaxBagGross#[kg]
    mPayload = mPaxOverall + mCargo#[kg]
    return(mPayload)

mPayload = getmPpayload(226)


#payloadFactor = Rphys[1]**2*(-1e-9) + Rphys[1]*7e-6 + 0.2626 # polynom von excel
payloadFactor = getfactor('airplane_list.csv','Payload factor',Rphys[1])# payload factor from numpy

mTO = mPayload/payloadFactor

fuelFactor = getfactor('airplane_list.csv','Fuel factor',Rphys[1])# fuel factor from numpy
#fuelFactor = -3e-9*Rphys[1]**2 + 5e-5*Rphys[1] + 0.0384  # polynom von excel

mF = fuelFactor*mTO

#mTO = mOE + mP + mF
mOE = mTO-mPayload-mF #empty operation weight

#Technolocical Corrections
payloadFactor *= 1.01#tech correction
fuelFactor *= 0.9#tech correction


mZF = mOE+mPayload

mF_LHE = mTO-mPayload
mC = mTO
mB = mOE+mF

dmfdR = (mTO-mOE-mPayload)/Rphys[1]
RB = Rphys[1]+(mOE+mPayload-mZF)/dmfdR

print ("Physical Range B: ", RB)
print ("Physical Range C: ", Rphys[1])
print ("mass B: ", mB)
print ("mass C: ", mC)




mOE_LHE = mOE * 1.3# Correction for weight of Hydrogen Drivetrain
#Corrections
dragCorrection = 1.07; fuelEvaporationCorrection = 1.02; driveEfficiencyCorrection = 0.833; energyContentCorrection = 0.357
Corrections = dragCorrection * fuelEvaporationCorrection * driveEfficiencyCorrection * energyContentCorrection

fuelFactor_LHE = fuelFactor * Corrections


#mTO_LHE*(1-fuelFactor_LHE)=mOE_LHE+mPayload

mTO_LHE = (mOE_LHE+mPayload)/(1-fuelFactor_LHE)

print ("Physical Range: ", Rphys)
print ("Operation Empty weight LHE: ", round(mOE_LHE,2))
print ("Maximum take off mass LHE[NM,km]: ", round(mTO_LHE,2))
rangepayloadplot(RB,mB,Rphys[1],mC)
plotfactor('airplane_list.csv','Payload factor')
plotfactor('airplane_list.csv','Fuel factor')
###Range Payload plot
##Compute R_B


