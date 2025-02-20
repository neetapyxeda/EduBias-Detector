BIAS_ANALYSER = """
You are very good at analysing bias and you are tasked with analyzing a text to identify potential biases.

Here is the text input : {text}

Please focus on identifying biases related to race, profession, gender, and value. If no biases are detected, categorize the text as "no-bias." 

For each document, provide the analysis in the format outlined below. 

Bias Status: Indicate the type of bias detected, which could be one of the following: race, profession, gender, value,cultural or no-bias.

Reason: Offer a concise explanation for why the text was categorized with a particular bias status, citing specific examples or language from the text.

Instructions:

1. Thoroughly review the text provided.

2. Pay attention to the language and content that might suggest biases.

3. Deliver a justification grounded in specific evidence from the text.

4. Keep the analysis clear, objective, and succinct.
"