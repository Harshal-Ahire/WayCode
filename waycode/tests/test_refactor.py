import unittest
from waycode.refactor_agent import RefactorAgent

class TestRefactorAgent(unittest.TestCase):
    def setUp(self):
        self.agent = RefactorAgent()
    
    def test_agent_initialization(self):
        self.assertIsNotNone(self.agent)
        self.assertIsNotNone(self.agent.memory)
    
    # Add more tests here

if __name__ == '__main__':
    unittest.main()