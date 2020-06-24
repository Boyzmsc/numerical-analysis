from tensorflow_momentum import TensorflowMomentum

import unittest

# tensorflow로 구현한 모멘텀 모듈의 단위 테스트
class TestTensorflowMomentum(unittest.TestCase):
    def setUp(self):
        self.t_m = TensorflowMomentum(0.01, 0.9)

    def testInit(self):
        self.assertEqual(self.t_m.getM(), 0.9)
        self.assertEqual(self.t_m.getLr(), 0.01)

    def testSetLr(self):
        self.t_m.setLr(0.001)
        self.assertEqual(self.t_m.getLr(), 0.001)

    def testSetM(self):
        self.t_m.setM(0.5)
        self.assertEqual(self.t_m.getM(), 0.5)


if __name__ == "__main__":
    unittest.main()