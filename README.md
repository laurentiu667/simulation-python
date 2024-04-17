# PROJET_GENIE
## Donnée pour Environnement de base selon Montréal

**Source :** OpenAI ChatGPT

### Ensoleillement:
- Pourcentage: 60%
- Heures: 2 077 heures #stat non use pour l'instant

### Précipitations:
- Total: 978 mm
- Pluie: 742 mm #stat non use pour l'instant
- Neige: 236 mm #stat non use pour l'instant

### Humidité:
- Moyenne: 73%

### Température de Base :
La température moyenne annuelle à Montréal est d'environ 6°C. Cette valeur sera notre base

### Impact humidité (comment l'humidité impacte la temperature)

### Impact ensoleillement
5% 

### Liason mois saison :
- Hiver (Décembre à Février)
- Printemps (Mars à Mai)
- Été (Juin à Août)
- Automne (Septembre à Novembre)
	
### Calcule Température:
calcule humidité (moyenne humidité biome et humidité moyenne)
calcule ensoleillement

- impactHumidite = humiditeActuel * moyenne (impacteHumidite de la saison et du biome)
- impactEnsoleillement = ensoleillement Actuel * impactEnsoleillement (5)

- temperature actuel  = temperature de base + variation saisoniere + variation du biome + impactHumidite + impactEnsoleillement
	
### Calcule Ensoleillement
ensoleillement Max  = moyenne(ensolleillement moyen et du biome)
	
- #ajuste la position du soleil en fonction de l'heure actuelle 
  #si l'heure actuelle est entre le lever et l'apogée du soleil
  etatDuSoleil = (heureCible / difference apogée et lever) # a quelle pourcentage il est levée

  #si l'heure actuelle est entre le coucher et l'apogée du soleil
  etatDuSoleil = (heureCible / difference apogée et couche) # a quelle pourcentage il est couché

  #adapte l'etat du soleil pour qu'il soit relatif a l'environnement max
  ensoleillement Actuel = etatDuSoleil* ensoleillement Max

  si l'ensoleillement Actuel > 0 alors soleil levé
  sinon il est couché

### Ajuster heure de lever, de coucher et d'apoger du soleil
diffParNbjours =((difference tranche d'heure)/ nb jours dans la saison) * jours actuel
heure du lerver au debut de la saison += diffParNbjours
#permet au lever et coucher du soleil de s'ajuster selon les jours durant la saison
	
## Saison :
Variation de Température Saisonnière:  par rapport à la moyenne annuelle.
- Hiver : -15°C 
- Printemps : +5°C
- Été : +15°C
- Automne : +5°C
		
### Hiver (Décembre à Février)
Lever du soleil : Entre 7:15 et 7:30 AM en décembre, progressivement avançant vers environ 6:45 AM à la fin de février.
Coucher du soleil : Entre 4:00 PM en décembre et s'étendant jusqu'à environ 5:45 PM à la fin de février.
Apogée solaire : Entre 11:45 AM et 12:30 PM.

### Printemps (Mars à Mai)
Lever du soleil : Entre environ 6:00 AM au début de mars, avançant vers 5:05 AM à la fin de mai.
Coucher du soleil : À partir d'environ 5:35 PM au début de mars, s'étendant jusqu'à environ 8:35 PM à la fin de mai.
Apogée solaire : Entre 12:00 PM au début de mars et environ 1:20 PM à la fin de mai.

### Été (Juin à Août)
Lever du soleil : Entre 5:00 AM au début de juin, reculant légèrement vers 5:35 AM à la fin d'août.
Coucher du soleil : Entre 8:45 PM au début de juin, diminuant à environ 7:45 PM à la fin d'août.
Apogée solaire : Autour de 1:00 PM au début de juin, se déplaçant vers 1:15 PM à la fin d'août.

### Automne (Septembre à Novembre)
Lever du soleil : Entre environ 6:15 AM au début de septembre, reculant vers 7:15 AM à la fin de novembre.
Coucher du soleil : De 7:30 PM au début de septembre à environ 4:15 PM à la fin de novembre.
Apogée solaire : Entre environ 12:45 PM au début de septembre et 11:45 AM à la fin de novembre.
	
### Impact Humidité (Les valeurs sont *100 .Pour s'adapter la realité de notre simulation et ainsi avoir des saisin plus significative )
- Hiver: L'effet de l'humidité sur la température pourrait être moins perceptible en hiver en raison du froid; par exemple, -0,02°C par % d'humidité au-dessus de la norme.
- Printemps: -0,04°C par % d'humidité au-dessus de la norme, car le temps commence à se réchauffer et l'humidité peut affecter plus la température.
- Été: -0,07°C par % d'humidité au-dessus de la norme, car l'effet de l'humidité peut être plus prononcé avec la chaleur.
- Automne: -0,03°C par % d'humidité au-dessus de la norme, similaire au printemps mais avec un effet potentiellement moindre à mesure que la température diminue
		
## Biome :

### Variation de Température par Biome :
- Forêts Boréales : -5°C. Ces forêts sont caractérisées par des hivers longs et froids et des étés courts. Leur emplacement plus au nord contribue à des températures plus basses.
- Toundra : -8°C. La toundra est encore plus froide, avec un sol souvent gelé (pergélisol) et une végétation clairsemée, ce qui réduit la capacité du sol à absorber la chaleur.
- Rivières et Lacs : 0°C. Les grands plans d'eau ont tendance à modérer les températures locales, les rendant plus constants tout au long de l'année.
- Montagnes et Plateaux : -4°C 
- Prairies et Savanes : +2°C. L'absence d'ombre et la végétation basse peuvent conduire à des températures légèrement plus élevées, surtout en plein soleil. 	

### Pourcentage d'Ensoleillement par Biome :
- Forêts Boréales: 30-50%
- Toundra : 40-60% (Peut être plus élevé en été avec des jours de 24 heures dans certaines régions.)
- Rivières et Lacs : 50-70%
- Montagnes et Plateaux : 60-80% (L'ensoleillement peut être plus élevé en altitude.)
- Prairies et Savanes : 70-90% (Ces biomes sont généralement plus ouverts et reçoivent plus de soleil.)

### Pourcentage d'Humidité
- Forêts Boréales: 60-80%
- Toundra : 50-70% (L'humidité peut être faible en raison du froid, mais le sol peut rester humide.)
- Rivières et Lacs : 70-90%
- Montagnes et Plateaux : 40-60% (L'humidité diminue généralement avec l'augmentation de l'altitude.)
- Prairies et Savanes : 40-60% (L'humidité peut être plus élevée pendant la saison des pluies.)
		
### Impact Humidité:(Les valeurs sont *10 .Pour s'adapter la realité de notre simulation )
- Forêts Boréales : -0,05°C par % d'humidité au-dessus de la norme, supposant une humidité de référence de 75%.
- Toundra: -0,04°C par % d'humidité au-dessus de la norme, avec une humidité de référence de 70%.
- Rivières et Lacs: -0,03°C par % d'humidité au-dessus de la norme, avec une humidité de référence de 80%.
- Montagnes et Plateaux: Varie significativement avec l'altitude, mais pourrait être -0,06°C par % d'humidité au-dessus de la norme à des altitudes moyennes, avec une humidité de référence de 65%.
- Prairies et Savanes: -0,05°C par % d'humidité au-dessus de la norme, supposant une humidité de référence de 60% pour refléter leur climat généralement plus sec.
