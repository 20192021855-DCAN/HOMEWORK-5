from functools import reduce


class UDPChecksum(object):

    __slots__ = ['word_size', 'history']

    def __init__(self, word_size: int=16):
        self.word_size = word_size
        self.history = None

    def _check_word_size(self, word):
        assert len(word) == self.word_size, "期望字长为{}, 但输入字的长度为{}".format(self.word_size, len(word))

    def __call__(self, words: [str]) -> str:

        for w in words:
            self._check_word_size(w)

        self.history = []
        
        def single_step(word0: str, word1: str) -> str:

            num0 = eval("0b{}".format(word0))
            num1 = eval("0b{}".format(word1))
            result = num0 + num1

            mask = eval("0b{}".format("1" * self.word_size))
            result = (result & mask) + (result // (mask + 1))

            result = bin(result).split('b')[-1] # 去除二进制标识'0b'
            result = "{}{}".format('0' * (self.word_size - len(result)), result) # 补齐位宽
            self.history.append(result)

            return result

        return "".join(map(lambda x:'0' if x=='1' else '1', reduce(single_step, words))) # 最终结果取反


def main():
    
    sum_checker = UDPChecksum()
    words = ["0110011001100000",
             "0101010101010101",
             "1000111100001100"]
    print("Answer: {}".format(sum_checker(words)))
    print("Intermediate Results: {}".format(", ".join(sum_checker.history)))

if __name__ == "__main__":
    main()
