# ==================================
# Python code for assert manager
# Application [VirtualUsersSandbox] Acronym [VUS] Snapshot [] Tip [true]
# ==================================


import logging, json

# ignore warning on 'bawsys', will be resolved at runtime
from bawsys import bawUniTestScenarioAsserter as scenAssert

#=========================================================================
# Edit this function to add your asserts
# Params:
#   asserter: scenAssert.ScenarioAsserter, is an object that offers a set of prebuilt assertions
#   listOfInstances, is a list of object representing process instances included into the U.T. scenario 
def executeAsserts(asserter: scenAssert.ScenarioAsserter, listOfInstances):

    # logging.info("======> executeAsserts, tot instances: %d %s", len(listOfInstances), json.dumps(listOfInstances, indent=2))

    asserter.assertItemsCountEquals(listOfInstances, 1)
    asserter.assertItemsCountNotEquals(listOfInstances, 2)
    
    asserter.assertEqual(listOfInstances, "variables.promoteRequest", "true")
    asserter.assertNotEqual(listOfInstances, "variables.promoteRequest", "false")
    
    asserter.assertTrue(listOfInstances, "variables.promoteRequest")
    asserter.assertFalse(listOfInstances, "variables.reviewForm")

    asserter.assertEqual(listOfInstances, "variables.evaluationForm.vote", 6)
    asserter.assertNotEqual(listOfInstances, "variables.evaluationForm.vote", 60)

    asserter.assertLesserThan(listOfInstances, "variables.evaluationForm.vote", 11)
    asserter.assertLesserEqualThan(listOfInstances, "variables.evaluationForm.vote", 10)
    
    asserter.assertGreaterThan(listOfInstances, "variables.evaluationForm.vote", 0)
    asserter.assertGreaterEqualThan(listOfInstances, "variables.evaluationForm.vote", 0)

    asserter.assertNull(listOfInstances, "variables.NONEXISTENTVAR")
    asserter.assertNotNull(listOfInstances, "variables.promoteRequest")


