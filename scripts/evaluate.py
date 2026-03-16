from jiwer import wer

def evaluate(reference, prediction):
    error = wer(reference, prediction)
    accuracy = max((1 - error) * 100, 0.0)
    return accuracy