actual_mix = receipt['category'].value_counts()/receipt.shape[0]
intended_mix = [category_probabilities[categories.index(c)] for c in actual_mix.index]
pd.DataFrame({'actual_mix': actual_mix, 'intended_mix': intended_mix})
