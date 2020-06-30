import pandas as pd

df = pd.read_csv('scraped_file.csv')
df["nome"] = df["nome"].str.normalize("NFKD")
df = df.dropna()
noMC = df[~df.nome.str.contains("MC")]
noAgR = noMC[~noMC.nome.str.contains("AgR")]
noQO = noAgR[~noAgR.nome.str.contains("QO")]
noED = noQO[~noQO.nome.str.contains("ED")]
noTP = noED[~noED.nome.str.contains("TP")]
noEI = noTP[~noTP.nome.str.contains("EI")]
adis_and = noEI[noEI.nome.str.contains("ADI")]
adis_and["nome"] = adis_and["nome"].str.strip()
adis_and = adis_and.drop_duplicates()
lessthan9 = adis_and.nome.str.len() < 9
adis_only = adis_and[lessthan9]
adis_only.to_csv('adi_links.csv', index=False)
