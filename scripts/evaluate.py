from jiwer import wer

def evaluate(reference, prediction):

    error = wer(reference, prediction)

    accuracy = (1 - error) * 100

    return accuracy