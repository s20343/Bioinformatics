from Bio import Entrez


Entrez.email = "s19806@pjwstk.edu.pl"


query = "colon cancer"


max_records = 10


handle = Entrez.esearch(db="pubmed", term=query, retmax=max_records)
record = Entrez.read(handle)
handle.close()


for pub_id in record["IdList"]:
    handle = Entrez.esummary(db="pubmed", id=pub_id, retmode="xml")
    summary = Entrez.read(handle)[0]
    handle.close()
    

    title = summary["Title"]
    authors = ", ".join(summary["AuthorList"])
    pub_date = summary["PubDate"]

    print("Title:", title)
    print("Authors:", authors)
    print("Publication Date:", pub_date)
    print("-" * 50)


# Title: Effect of High-Versus Low-Frequency of Abdominopelvic Computed Tomography Follow-Up Testing on Overall Survival in Patients With Stage II Or III Colon Cancer.
# Authors: Jeon J, Lee DB, Shin SJ, Han DH, Chang JS, Han YD, Kim H, Lim JS, Kim HS, Ahn JB
# Publication Date: 2023 May 11
# --------------------------------------------------
# Title: Syntheses and Antitumor Activities of Neorautenol and Shinpterocarpin Analogs.
# Authors: Huang G, Hoang VH, Min HY, Lee HY, Ann J, Lee J
# Publication Date: 2023 Jun 2
# --------------------------------------------------
# Title: Hypusination Maintains Intestinal Homeostasis and Prevents Colitis and Carcinogenesis by Enhancing Aldehyde Detoxification.
# Authors: Gobert AP, Smith TM, Latour YL, Asim M, Barry DP, Allaman MM, Williams KJ, McNamara KM, Delgado AG, Short SP, Mirmira RG, Rose KL, Schey KL, Zagol-Ikapitte I, Coleman JS, Boutaud O, Zhao S, Piazuelo MB, Washington MK, Coburn LA, Wilson KT
# Publication Date: 2023 Jun 2
# --------------------------------------------------
# Title: Atomic vacancies-engineered ultrathin trimetallic nanozyme with anti-inflammation and antitumor performances for intestinal disease treatment.
# Authors: Wang Y, Dai X, Wu L, Xiang H, Chen Y, Zhang R
# Publication Date: 2023 May 27
# --------------------------------------------------
# Title: Patient-Reported Outcomes During and After Treatment for Locally Advanced Rectal Cancer in the PROSPECT Trial (Alliance N1048).
# Authors: Basch E, Dueck AC, Mitchell SA, Mamon H, Weiser M, Saltz L, Gollub M, Rogak L, Ginos B, Mazza GL, Colgrove B, Chang G, Minasian L, Denicoff A, Thanarajasingam G, Musher B, George T, Venook A, Farma J, O'Reilly E, Meyerhardt JA, Shi Q, Schrag D
# Publication Date: 2023 Jun 4
# --------------------------------------------------
# Title: Young adults with colon cancer: clinical features and surgical outcomes.
# Authors: Wang C, Gan L, Gao Z, Shen Z, Jiang K, Ye Y
# Publication Date: 2023 Jun 3
# --------------------------------------------------
# Title: ASO Author Reflections: Potentially Avoidable and Prolonged Hospitalizations for Suspected Colon Cancer-Hospital Impact.
# Authors: Tagerman DL, In H
# Publication Date: 2023 Jun 3
# --------------------------------------------------
# Title: Differential Efficacy of Targeted Monoclonal Antibodies in Left-Sided Colon and Rectal Metastatic Cancers.
# Authors: Kodama H, Masuishi T, Wakabayashi M, Nakata A, Kumanishi R, Nakazawa T, Ogata T, Matsubara Y, Honda K, Narita Y, Taniguchi H, Kadowaki S, Ando M, Muro K
# Publication Date: 2023 May 11
# --------------------------------------------------
# Title: Global application of National Comprehensive Cancer Network resource-stratified guidelines for systemic treatment of colon cancer: a population-based, customisable model for cost, demand, and procurement.
# Authors: Wilson BE, Booth CM, Sullivan R, Aggarwal A, Sengar M, Jacob S, Bray F, Barton MB, Pearson SA
# Publication Date: 2023 Jun
# --------------------------------------------------
# Title: Enhancing colon cancer care in restricted-resource settings.
# Authors: Von Wallwitz Freitas L, Stefani S
# Publication Date: 2023 Jun
# --------------------------------------------------