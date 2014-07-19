# -*- coding: utf-8 -*-

"""
This layer is the Test class base.

Check out all tests on this package:

./bin/test -s ploneconf2014.contenttypes --list-tests
"""

from plone.testing.z2 import ZSERVER_FIXTURE, installProduct, uninstallProduct

from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting
from plone.testing import Layer
from zope.configuration import xmlconfig

class Fixture(Layer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):

        # Load ZCML
        import ploneconf2014.contenttypes
        self.loadZCML(package=ploneconf2014.contenttypes)
        xmlconfig.file(
            'configure.zcml',
            ploneconf2014.contenttypes,
            context=configurationContext
        )

        # Install products that use an old-style initialize() function
        installProduct(app, 'ploneconf2014.contenttypes')

    def tearDownZope(self, app):
        # Uninstall products installed above
        uninstallProduct(app, 'ploneconf2014.contenttypes')

    def setUpPloneSite(self, portal):
        # Install into Plone site using portal_setup
        applyProfile(portal, 'ploneconf2014.contenttypes:default')

FIXTURE = Fixture()

"""
We use this base for all the tests in this package. If necessary,
we can put common utility or setup code in here. This applies to unit 
test cases.
"""
INTEGRATION_TESTING = IntegrationTesting(
    bases=(FIXTURE,),
    name="ploneconf2014.contenttypes:Integration"
)

"""
We use this for functional integration tests. Again, we can put basic 
common utility or setup code in here.
"""
ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(FIXTURE, ZSERVER_FIXTURE),
    name="ploneconf2014.contenttypes:Acceptance"
)
