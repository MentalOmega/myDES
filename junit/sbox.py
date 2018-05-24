import unittest


class task1():
    """
    给定某个Sbox的输入差分情况下，计算所有输入对和所有Sbox输出差分的分布情况
    """
    S1 = [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7,
          0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8,
          4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0,
          15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13
          ]



    def Sbox(self, dataInput: str):
        row = int(dataInput[0] + dataInput[5], 2)
        column = int(dataInput[1:5], 2)
        index = row * 16 + column
        dataOutput = self.S1[index]
        return dataOutput

    def int2bin(self, n, count=24):
        """returns the binary of integer n, using count number of digits"""
        return "".join([str((n >> y) & 1) for y in range(count - 1, -1, -1)])

    def run(self, deltaB: str):
        """
            Parameters:
              param1 - this is the first param
              param2 - this is a second param

            Returns:
              This is a description of what is returned

            Raises:
              KeyError - raises an exception
            """
        deltaB = int(deltaB, 2)
        data = dict()
        for i in range(0, 1 << 4):
            data[i] = {"deltaS": self.int2bin(i, 4), "num": 0, "pair": ""}

        unique = set()
        for i in range(0, 1 << 6):
            a = i
            b = i ^ deltaB
            if (a, b) in unique or (b, a) in unique:
                continue
            unique.add((a, b))
            unique.add((b, a))
            # print(bin(a), bin(b), bin(deltaB))
            outputA = self.Sbox(self.int2bin(a, 6))
            outputB = self.Sbox(self.int2bin(b, 6))
            id = outputA ^ outputB
            deltaS = self.int2bin(outputA ^ outputB, 4)
            text: dict = data.get(id)
            if text:
                text["pair"] += " (" + self.int2bin(a, 6) + " " + self.int2bin(b, 6)+")"
                text["num"] += 2
            #else:
            #   text = {"deltaS": deltaS, "num": 2, "pair": self.int2bin(a, 6) + " " + self.int2bin(b, 6)}
            data[id] = text
        return data


class Testf(unittest.TestCase):

    def testRun(self):
        data = {}
        data["ddt"] = {"num": 10, "text": 20}
        print(data.get("ddt"))
        fun = task1()
        print(fun.int2bin(1, 6))
        print(fun.run("000001"))
