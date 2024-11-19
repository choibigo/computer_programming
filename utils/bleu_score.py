from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction

def calculate_bleu_score(gts, prediction):
    """
    Calculate the BLEU score for a single prediction against multiple ground truths.

    Args:
        gts (list of str): List of ground truth sentences.
        prediction (str): Predicted sentence.

    Returns:
        float: BLEU score.
    """
    # Convert sentences into lists of words
    reference_list = [gt.split() for gt in gts]
    hypothesis = prediction.split()
    
    # Apply smoothing function to avoid zero scores for short sentences
    smoothing_function = SmoothingFunction().method1
    
    # Calculate BLEU score
    bleu_score = sentence_bleu(reference_list, hypothesis, smoothing_function=smoothing_function)
    
    return bleu_score

if __name__ == "__main__":

    gts = ["Interdisciplinarity: Is there room for It in undergraduate engineering education's futures? Today, let's observe the short agenda as shown on this slide. First, let's speak about our possible futures and how those are shaped by many agents of change. There are pulls of the future caused by agents of change, such as social, technological, environmental, economic, and political. There are pushes of the present like the momentum to go interdisciplinary in addressing complex problems of the world. And there are weights of the past like the tendency to go deeper and deeper into specializations in what looked like academic silos."]
    prediction = "Interdisciplinarity. Is there room for interdisciplinarity in undergraduate engineering education's futures? Today, let's observe the short agenda as shown on this slioderDecoderCache.from_legacy_cache(past_key_values)`de. First, let's speak about our possible futures and how those are shaped by many agents of change. There are pools of the future caused by agents of change such as social, technological, environmental, economic, and political. There are pushes of the present like the momentum to go interdisciplinary in addressing complex problems of the world. And there are weigde. First, let's speak about our possible futures anhts of the past like the tendency to to go deeper and deeper into specializations in what look like academic silo"
    bleu = calculate_bleu_score(gts, prediction)

    print(f"BLEU score: {bleu:.4f}")
