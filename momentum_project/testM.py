from momentum import *
import numpy as np
import unittest

# 구체화한 모멘텀 모듈의 단위 테스트
class TestMomentumClass(unittest.TestCase):

    def setUp(self):
        self.m = Momentum(0, 0, 0.01, 100000, 0.01, 0.5)
        self.dmse = [100,1000]

    def testInit(self):
        self.assertEqual(self.m.getEps(), 0.01)

        self.assertEqual(self.m.getMu(), 0.5)

        self.assertEqual(self.m.getAlpha(), 0.01)

        self.assertEqual(self.m.getSize(), 100000)

        self.assertEqual(self.m.getV()[0], 0)
        self.assertEqual(self.m.getV()[1], 0)

        self.assertEqual(self.m.getW()[0], 0)
        self.assertEqual(self.m.getW()[1], 0)

    def testSetAlpha(self):
        self.m.setAlpha(0.001)
        self.assertEqual(self.m.getAlpha(), 0.001)

    def testSetMu(self):
        self.m.setMu(0.8)
        self.assertEqual(self.m.getMu(), 0.8)

    def testSetEps(self):
        self.m.setEps(0.1)
        self.assertEqual(self.m.getEps(), 0.1)

    def testUpdateV(self):
        self.assertEqual(self.m.getV()[0], 0)
        self.assertEqual(self.m.getV()[1], 0)

        # updateV() 테스트를 위해 두 번 실행
        self.m.updateV(self.dmse)
        self.assertEqual(self.m.getV()[0], -1)
        self.assertEqual(self.m.getV()[1], -10)

        self.m.updateV(self.dmse)
        self.assertEqual(self.m.getV()[0], -1.5)
        self.assertEqual(self.m.getV()[1], -15)

    def testUpdateW(self):
        self.assertEqual(self.m.getW()[0], 0)
        self.assertEqual(self.m.getW()[1], 0)

        # updateW() 테스트를 위해 두 번 실행
        self.m.updateV(self.dmse)
        self.m.updateW()
        self.assertEqual(self.m.getW()[0], -1)
        self.assertEqual(self.m.getW()[1], -10)

        self.m.updateV(self.dmse)
        self.m.updateW()
        self.assertEqual(self.m.getW()[0], -2.5)
        self.assertEqual(self.m.getW()[1], -25)


# 구체화한 경사하강법 모듈의 단위 테스트
class TestGD(unittest.TestCase):
    def setUp(self):
        self.gd = GD(0, 0, 0.01, 100000, 0.01)
        self.dmse = [100,1000]

    def testInit(self):
        self.assertEqual(self.gd.getEps(), 0.01)

        self.assertEqual(self.gd.getAlpha(), 0.01)

        self.assertEqual(self.gd.getSize(), 100000)

        self.assertEqual(self.gd.getW()[0], 0)
        self.assertEqual(self.gd.getW()[1], 0)

    def testSetAlpha(self):
        self.gd.setAlpha(0.0015)
        self.assertEqual(self.gd.getAlpha(), 0.0015)

    def testSetEps(self):
        self.gd.setEps(0.1)
        self.assertEqual(self.gd.getEps(), 0.1)

    def testUpdate(self):
        self.assertEqual(self.gd.getW()[0], 0)
        self.assertEqual(self.gd.getW()[1], 0)

        # update() 테스트를 위해 두 번 실행
        self.gd.update(self.dmse)
        self.assertEqual(self.gd.getW()[0], -1)
        self.assertEqual(self.gd.getW()[1], -10)

        self.gd.update(self.dmse)
        self.assertEqual(self.gd.getW()[0], -2)
        self.assertEqual(self.gd.getW()[1], -20)

if __name__ == "__main__":
    unittest.main()