"""
https://opensource.org/license/mit/
MIT License

Copyright 2023 Antonioni Marco

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

# ==================================
# Python code for data model objects
# Application [VirtualUsersSandbox] Acronym [VUS] Snapshot [] Tip [True]
# ==================================

#==========================
# Create AuthorizationData json object
def newAuthorizationData():
    return {"authorized": False, "comments": "", "review": False}


#==========================
# Create CCTRData json object
def newCCTRData():
    return {"newCounter": 0, "requestId": ""}


#==========================
# Create ExampleOfComplexTypesReferences json object
# 'authorizationData' of type AuthorizationData
# 'cctrData' of type CCTRData
def newExampleOfComplexTypesReferences():
    return {"authorizationData": {}, "cctrData": {}}


#==========================
# Create ExampleOfTypes json object
def newExampleOfTypes():
    return {"attrBool": False, "attrDate": None, "attrDecimal": 0.0, "attrInt": 0, "attrListBool": [], "attrListDate": [], "attrListDecimal": [], "attrListInt": [], "attrListText": [], "attrListTime": [], "attrText": "", "attrTime": None}


#==========================
# Create UTExample1Data json object
# 'data' of type UTExample1StartData
def newUTExample1Data():
    return {"data": {}, "vote": 0}


#==========================
# Create UTExample1StartData json object
def newUTExample1StartData():
    return {"counter": 0, "name": ""}


