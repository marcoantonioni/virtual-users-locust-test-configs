# ==================================
# Python code for payload manager
# Application [VirtualUsersSandbox] Acronym [VUS] Snapshot [] Tip [true]
# Application data model generated in file: ../virtual-users-locust-test-configs/configurations/payloadManager_VirtualUsersSandbox_VUS_tip_DataModel.py
# ==================================

"""
https://opensource.org/license/mit/
MIT License

Author: Antonioni Marco

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

#=============================
# import section, add what you need
#=============================
import random, json

# !!! import your-data-model, example: 
# from configurations import payloadManager_VirtualUsersSandbox_VUS_tip_DataModel as myDataModel

#=============================
# the function 'buildPayloadForSubject' must be present in any payload manager
# it must return a Boolean, True when taskSubjectText match the subjext in a dictionary
# the default logic is: search as substring
# reimplement isMatchingTaskSubject as from your needs
#=============================

def isMatchingTaskSubject(taskSubjectText, subjectFromUserDictionary):
    return taskSubjectText.find(subjectFromUserDictionary) != -1

#=============================
# the function 'buildPayloadForSubject' must be present in any payload manager
# input parameters:
#   text: str (subject text from Task)
#   preExistPayload: dict = None (optional: data of Task)
#   unitTestCreateIndex: int = None (used only in unit test scenario for "Start-" subjects: process instance counter, from zero to BAW_PROCESS_INSTANCES_MAX)
# it must return a dict() object with keys
#   jsonObject = your payload in json format
#   thinkTime = your ad hoc think thime for the subject in input; if the returned value is -1 the global think thime will be used
#
# reimplement buildPayloadForSubject as from your needs
#=============================

def buildPayloadForSubject(text: str , preExistPayload: dict = None, unitTestCreateIndex: int = None):
    retObject = dict()
    retObject["jsonObject"] = {}
    retObject["thinkTime"] = -1

    # The following code is an example from demo apps, remove it if not needed

    """
    Process: VUSLoanRequest
    key: 
    task key: 'Evaluate Loan Request Data'
    task key: 'Validate Loan Request Data'

    if text.find('Start-VUSLoanRequest') != -1:
        rndVal : int = random.randint(0, 100) + 1
        retObject["jsonObject"] = {
            'loanRequest': {
                'userName': 'customer'+str(rndVal), 
                'amountRequested': 100000, 
                'loanDurationMonths': 36, 
                'requestorAnnualNetIncome': 300000,
                'activeLoans': 0,
                'badPayer': False,
                'challengeYourLuck': False
            }
        }
        retObject["thinkTime"] = random.randint(0, 5)

    if text.find('Evaluate Loan Request Data') != -1:
        rndVal : int = random.randint(0, 1)
        if preExistPayload != None:
            loanRequest = preExistPayload["loanRequest"]
            installmentAmount = preExistPayload["installmentAmount"]
            requestorMonthlyNetIncome = preExistPayload["requestorMonthlyNetIncome"]
            riskLevel = preExistPayload["riskLevel"]
            print(json.dumps(loanRequest, indent=2))
            print("installmentAmount", installmentAmount)
            print("requestorMonthlyNetIncome", requestorMonthlyNetIncome)
            print("riskLevel", riskLevel)
        rejected = False
        if rndVal == 1:
            rejected = True
        retObject["jsonObject"] = {'rejected': rejected} 
        retObject["thinkTime"] = random.randint(0, 5)

    if text.find('Validate Loan Request Data') != -1:
        rndVal : int = random.randint(0, 1)
        if preExistPayload != None:
            loanRequest = preExistPayload["loanRequest"]
            installmentAmount = preExistPayload["installmentAmount"]
            requestorMonthlyNetIncome = preExistPayload["requestorMonthlyNetIncome"]
            riskLevel = preExistPayload["riskLevel"]
            print(json.dumps(loanRequest, indent=2))
            print("installmentAmount", installmentAmount)
            print("requestorMonthlyNetIncome", requestorMonthlyNetIncome)
            print("riskLevel", riskLevel)
        loanAccepted = False
        if rndVal == 1:
            loanAccepted = True
        retObject["jsonObject"] =  {'loanAccepted': loanAccepted}
        retObject["thinkTime"] = random.randint(0, 5)
    """

    """
    Process: VUSClaimCompleteTwoRoles 
    key: [CCTR]
    task key: 'Compile Request [CCTR]'
    task key: 'Authorize Request [CCTR]'

    if text.find('Start-VUSClaimCompleteTwoRoles') != -1:
        rndVal : int = random.randint(0, 100) + 1
        retObject["jsonObject"] = {'inputData': {'requestId': 'req'+str(rndVal), 'newCounter': rndVal}}

    if text.find('Compile Data [CCTR]') != -1:
        rndVal : int = random.randint(0, 100) + 1
        retObject["jsonObject"] = {'inputData': {'requestId': 'reqCompiled', 'newCounter': rndVal}}

    if text.find('Validate Data [CCTR]') != -1:
        rndVal : int = random.randint(50, 150) + 1

        if preExistPayload != None:
            # update prev values
            inputData = preExistPayload["inputData"]
            inputData["newCounter"] = rndVal
            retObject["jsonObject"] = {'inputData': inputData} 
        else:
            # new values
            retObject["jsonObject"] =  {'inputData': {'requestId': 'reqValidated', 'newCounter': rndVal}}

        retObject["thinkTime"] = random.randint(0, 5)
    """

    """
    Process: VUSClaimCompleteAuthorize
    key: [CCA]
    task key: 'Compile Request [CCA]'
    task key: 'Authorize Request [CCA]'

    if text.find('Start-VUSClaimCompleteAuthorize') != -1:
        rndVal : int = random.randint(0, 100) + 1
        retObject["jsonObject"] = {'inputData': {'requestId': 'req'+str(rndVal), 'newCounter': rndVal}}

    if text.find('Compile Data [CCA]') != -1:
        rndVal : int = random.randint(0, 100) + 1
        retObject["jsonObject"] = {'inputData': {'requestId': 'reqCompiled', 'newCounter': rndVal}}

    if text.find('Validate Data [CCA]') != -1:
        authorize = False
        review = False

        rndReview : int = random.randint(0, 1) + 1
        if rndReview != 0:
            review = True
        if review == False:
            rndAuth : int = random.randint(0, 1) + 1
            if rndAuth != 0:
                authorize = True

        rndVal : int = random.randint(50, 150) + 1

        if preExistPayload != None:
            # update prev values
            inputData = preExistPayload["inputData"]
            inputData["newCounter"] = rndVal
            authorizationData = preExistPayload["authorizationData"]
            authorizationData["authorized"] = authorize
            authorizationData["review"] = review
            retObject["jsonObject"] =  {'inputData': inputData, 'authorizationData': authorizationData}
        else:
            retObject["jsonObject"] =  {'inputData': {'requestId': 'reqValidated', 'newCounter': rndVal},
                                        'authorizationData': {'authorized': authorize, 'comments': '', 'review': review}}

        retObject["thinkTime"] = random.randint(0, 5)
    """

    return retObject
