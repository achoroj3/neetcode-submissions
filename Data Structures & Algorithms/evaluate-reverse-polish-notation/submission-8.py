class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        i = 0
        numbers = []
        operands = []
        while (i < len(tokens)):
            if tokens[i] not in ['+', '-', '*', '/']:
                numbers.append(int(tokens[i]))
            else:
                operands.append(tokens[i])
            
            if len(numbers) > 1 and len(operands) > 0:
                if operands[-1] == '+':
                    evaluation = numbers[-1] + numbers[-2]
                elif operands[-1] == '-':
                    evaluation = numbers[-2] - numbers[-1]
                elif operands[-1] == '*':
                    evaluation = numbers[-1] * numbers[-2]
                else:
                    evaluation = int(numbers[-2] / numbers[-1])
                del numbers[-1]
                del numbers[-1]
                del operands[-1]
                numbers.append(evaluation)
            i+=1

        return numbers[0]
