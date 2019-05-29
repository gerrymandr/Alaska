# -*- coding: utf-8 -*-
"""
Created on Sat May 25 22:47:06 2019

@author: daryl
"""

import json
import networkx as nx
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

with open('Ensemble_Permissive_stats.json') as f:
    data = json.load(f)


#ps = [initial_tight, initial_restricted, initial_large]

GOV18ns= sorted((0.5187406297776442, 0.3916434540240218, 0.23378661089760477,
          0.561916167590201, 0.5277943813115976, 0.3967808623758262, 
          0.24347460005648527, 0.2040194040100815, 0.29961685822777134, 
          0.2658227848088675, 0.30213024956718243, 0.2738569188011496, 
          0.3331949346122295, 0.3753434474711785, 0.5018867924316115,
          0.5426127015341067, 0.5913152254553772, 0.6266881029630763,
          0.6404409922858867, 0.6744921745562409, 0.5829798514395329, 
          0.46457747422269396, 0.49254507629009764, 0.45721212122003807, 
          0.5081005584437817, 0.44071841251982957, 0.5078786300489014, 
          0.4823874755528126, 0.3030897498782328, 0.28720868644817754, 
          0.45392418577347565, 0.548494983265805, 0.6961661695141408, 
          0.5386310904517134, 0.5566274613453184, 0.4174338319909295, 
          0.6555631089965965, 0.7312614259593524, 0.7193151212004562, 
          0.61932265686532))
GOV18x=sorted((0.4974431818181818, 0.37424547283702214, 0.20789779326364694, 
        0.5263911254249418, 0.50988230068843, 0.38398798025327324, 
        0.23922875505831945, 0.19625226677412855, 0.28292410714285715, 
        0.2544677544677545, 0.28685985055585933, 0.2606104388658118, 
        0.32402732402732404, 0.3625, 0.47884788478847884, 0.5222623345367028,
        0.5623608017817372, 0.6011283497884344, 0.6125967628430683,
        0.6509209744503862, 0.5640572886011379, 0.45389537071885583, 
        0.4786472475931869, 0.447171453437772, 0.48655110579796773,
        0.42658509454949944, 0.49777777777777776, 0.46891624867001064, 
        0.28942840757025423, 0.27886435331230286, 0.40277539832105536, 
        0.525532969757065, 0.6567947910102919, 0.4908722109533469, 
        0.5396059509449136, 0.4065186962607478, 0.6617647058823529,
        0.7358445297504799, 0.7188718183902775, 0.6151213441194773))
USH18x=sorted((0.5058695058695059, 0.3900736719658782, 0.2543404735062007,
        0.5312662393902651, 0.5138918802498385, 0.37274049449407853, 
        0.2843413033286451, 0.2460960664162878, 0.3040479215828644, 
        0.3051849027830728, 0.32579668862382055, 0.2848743987172635,
        0.35922610453364134, 0.38727149627623564, 0.5108885017421603, 
        0.5274647887323943, 0.5599028602266595, 0.5989611809732094, 
        0.6076079506511309, 0.6491633006347375, 0.5707167497125335,
        0.46821448313985625, 0.4998794309139137, 0.43823479298006474, 
        0.49396417445482865, 0.4271950554444646, 0.49546608632571637, 
        0.467220409374073, 0.33054471091280907, 0.3152729503169086, 
        0.4366804979253112, 0.46370683579985905, 0.6810362274843149,
        0.5284996724175585, 0.5495891458054654, 0.44719662058371734,
        0.4837432852700028, 0.584951998213887, 0.5047358450852452,
        0.4665718349928876))
USH18ns=sorted((0.526629425384675, 0.41081640244677586, 0.2774311777926235, 
         0.5665135137823519, 0.5324396994583951, 0.39077610338199437,
         0.29063095741083556, 0.2520081528281857, 0.3242478870458404,
         0.3145534181033724, 0.3380180359170024, 0.2979472351935256,
         0.36280653131210194, 0.3964223985086792, 0.5198083711638748, 
         0.5483611707902181, 0.5889840870354133, 0.6223695336477948, 
         0.632669752041204, 0.6672778804198621, 0.5931440818852669,
         0.4755756282959946, 0.5105624482537662, 0.4545425262952549,
         0.5164939040837906, 0.4425673222996577, 0.5097079657012924,
         0.4870557891023724, 0.33723477574740685, 0.3260691986801825, 
         0.47925932440512, 0.4839707790207739, 0.7077419247658372, 
         0.5693768081345366, 0.5608357157934066, 0.45216772423949964,
         0.48482656936912155, 0.5846342120988194, 0.5154696428000252,
         0.47246020775337016))
Native=sorted((0.14453345368385423, 0.04791972037433758, 0.04153228088043909,
        0.04711570898459463, 0.09071032124236138, 0.19222777559386758,
        0.0498220640569395, 0.06539540100953449, 0.05580923389142567,
        0.0532899534414091, 0.0553172273650937, 0.04923320694923886, 
        0.03773051250141419, 0.034796273431361546, 0.07209144409234948,
        0.09912389082331799, 0.10816429735348654, 0.1110181311018131, 
        0.1408546235586706, 0.11965233096286262, 0.07601179004648, 
        0.07231765699802872, 0.09871413330338592, 0.05795955259292735, 
        0.08296139254630663, 0.0650539761487594, 0.07099219368706867,
        0.03138710766115423, 0.08620880949739265, 0.06442483768936241,
        0.04401535807690168, 0.16086740056425292, 0.13535582648142896,
        0.09395517319447588, 0.20246844319775595, 0.21248741188318226, 
        0.4281292984869326, 0.8349481363273681, 0.8371329976806019,
        0.6643768400392541))

partisan_w = [data['0'],data['2'],data['4'],data['6']]
partisan_p = [data['1'],data['3'],data['5'],data['7']]
p_types=["GOV18N", "GOV18A", "USH18N", "USH18A"]
p_vecs=[GOV18x, GOV18ns, USH18x, USH18ns]
   
y = 1
plt.figure()
sns.distplot(partisan_w[y],kde=False,color='slateblue',bins=[x for x in range(12,23)],
                                                hist_kws={"rwidth":1,"align":"left"})
plt.axvline(x=sum([val>.5 for val in p_vecs[y]]),color='r',label="Current Plan",linewidth=5)
plt.axvline(x=np.mean(partisan_w[y]),color='g',label="Ensemble Mean",linewidth=5)
plt.legend()
print(p_types[y],"wins: ", np.mean(partisan_w[y]))
plt.savefig("./Outputs/plots/New_Ensemble_Hist_GOV18A.png")
plt.close()
