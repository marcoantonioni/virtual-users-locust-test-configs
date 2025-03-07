# ==================================
# Python code for assert manager
# Application [VirtualUsersSandbox] Acronym [VUS] Snapshot [] Tip [true]
# ==================================

"""
https://opensource.org/license/mit/
MIT License

Author: Antonioni Marco

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

import logging, json

# ignore warning on 'bawsys', will be resolved at runtime
from bawsys import bawUniTestScenarioAsserter as scenAssert

#=========================================================================
# Edit this function to add your asserts
# Params:
#   asserter: scenAssert.ScenarioAsserter, is an object that offers a set of prebuilt assertions
#   listOfInstances, is a list of object representing process instances included into the U.T. scenario 
def executeAsserts(asserter: scenAssert.ScenarioAsserter, listOfInstances):

    """
    # Usage sample
    logging.info("======> executeAsserts, tot instances: %d %s", len(listOfInstances), json.dumps(listOfInstances, indent=2))

    asserter.assertItemsCountEquals(listOfInstances, 1)
    asserter.assertItemsCountNotEquals(listOfInstances, 2)
    
    asserter.assertEqual(listOfInstances, "variables.promoteRequest", "true")
    asserter.assertNotEqual(listOfInstances, "variables.promoteRequest", "false")
    
    asserter.assertTrue(listOfInstances, "variables.promoteRequest")
    asserter.assertFalse(listOfInstances, "variables.reviewForm")

    asserter.assertEqual(listOfInstances, "variables.evaluationForm.vote", 6)
    asserter.assertNotEqual(listOfInstances, "variables.evaluationForm.vote", 60)

    asserter.assertLesserThan(listOfInstances, "variables.evaluationForm.vote", 10)
    asserter.assertLesserEqualThan(listOfInstances, "variables.evaluationForm.vote", 10)
    
    asserter.assertGreaterThan(listOfInstances, "variables.evaluationForm.vote", 0)
    asserter.assertGreaterEqualThan(listOfInstances, "variables.evaluationForm.vote", 0)

    asserter.assertNull(listOfInstances, "variables.NONEXISTENTVAR")
    asserter.assertNotNull(listOfInstances, "variables.promoteRequest")
    """
    
    return
