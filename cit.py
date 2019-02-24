import kkdata

#Exercise 1 ############################################
def get_citizen_dist_age(countries):
    year = 2015
    citizenship_dist = {}
    for area in kkdata.STATISTICS[year].keys():
        for age in kkdata.STATISTICS[year][area]:
            for citizen_code in kkdata.STATISTICS[year][area][age]:
                for country in countries:
                    if country == citizen_code:
                        citizenship_dist.setdefault(country, {})
                        citizenship_dist[country][age] = citizenship_dist[country].get(age, 0)+kkdata.STATISTICS[year][area][age][country]
    return citizenship_dist


#Exercise 2 ############################################
#Part 1
def get_citizen_dist_total(countries):
    year = 2015
    citizenship_dist = {}
    for area in kkdata.STATISTICS[year].keys():
        for age in kkdata.STATISTICS[year][area]:
            for citizen_code in kkdata.STATISTICS[year][area][age]:
                for country in countries:
                    if country == citizen_code:
                        citizenship_dist[country] = citizenship_dist.get(country, 0)+kkdata.STATISTICS[year][area][age][country]
    return citizenship_dist

#Part 2
def get_citizen_dist_area(countries):
    year = 2015
    citizenship_dist = {}
    for area in kkdata.STATISTICS[year].keys():
        for age in kkdata.STATISTICS[year][area]:
            for citizen_code in kkdata.STATISTICS[year][area][age]:
                for country in countries:
                    if country == citizen_code:
                        citizenship_dist.setdefault(country, {})
                        citizenship_dist[country][area] = citizenship_dist[country].get(area, 0)+kkdata.STATISTICS[year][area][age][country]
    return citizenship_dist


#Exercise 3 ############################################
def get_top_5():
    year = 2015
    citizenship_dist = {}
    for area in kkdata.STATISTICS[year].keys():
        for age in kkdata.STATISTICS[year][area]:
            if 20 <= age <= 65:
                for citizen_code in kkdata.STATISTICS[year][area][age]:
                    citizenship_dist[citizen_code] = citizenship_dist.get(citizen_code, 0)+kkdata.STATISTICS[year][area][age][citizen_code]
    so = sorted(citizenship_dist.items(), key=lambda x: x[1], reverse=True)
    so5 = so[:5]
    return {tup[0]:tup[1] for tup in so5}