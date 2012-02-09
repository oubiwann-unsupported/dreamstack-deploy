from unittest import TestCase

from dreamstack import persona


class PersonaTestCase(TestCase):
    """
    """
    def setUp(self):
        self.persona = persona.Persona()

    def test_creation(self):
        self.assertEqual(self.persona._main_package.uri, "git://uri")
        self.assertEqual(self.persona._main_package.install_path, "./")
        self.assertEqual(self.persona._main_package.upstream.uri, "ro+git://uri")
