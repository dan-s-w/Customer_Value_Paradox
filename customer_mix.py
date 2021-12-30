actual_mix = receipt.groupby('customer_type')['customer_id'].nunique()/1000
intended_mix = [customer_probabilities[customer_types.index(c)] for c in actual_mix.index]
pd.DataFrame({'actual_mix': actual_mix, 'intended_mix': intended_mix})
